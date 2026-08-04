"""Komut satırı arayüzü.

    python -m pipeline.cli fetch              # kaynakları tara, metinleri çıkar
    python -m pipeline.cli candidates         # günün adaylarını metinleriyle bas
    python -m pipeline.cli build              # docs/ üret
    python -m pipeline.cli check              # içerik tutarlılık denetimi
    python -m pipeline.cli serve              # yerel önizleme

Otomatik özetleme (ANTHROPIC_API_KEY gerekir):

    python -m pipeline.cli daily              # bugünün sayısını üret
    python -m pipeline.cli backfill --days 30 # geçmişi doldur (Batch API)
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

from .config import CONTENT_DIR, MAX_ARTICLES_PER_DAY, ROOT, SITE
from .curate import group_by_day, pick_for_day, rank
from .extract import extract
from .fetch import Article, fetch_all, load_index, save_index

CACHE = ROOT / ".cache"
POOL = CACHE / "pool.json"
ENRICHED = CACHE / "enriched.json"

# Kaç günlük geçmişi her koşuda tarayalım (feed'ler geriye dönük yazı da ekleyebiliyor)
LOOKBACK_DAYS = 10
# "Arşivden" doldurmak için ne kadar geriye bakalım
ARCHIVE_POOL_DAYS = 150


def _today() -> str:
    return datetime.now(ZoneInfo(SITE["timezone"])).date().isoformat()


# --------------------------------------------------------------------------
def cmd_fetch(args: argparse.Namespace) -> int:
    until = datetime.now(timezone.utc)
    since = until - timedelta(days=args.days)
    print(f"Kaynaklar taranıyor: {since.date()} .. {until.date()}")

    articles = fetch_all(since=since, until=until)
    print(f"\n{len(articles)} makale bulundu. Metinler çıkarılıyor…")

    # Sadece küratörlüğü geçenlerin tam metnini indir — gereksiz trafik olmasın
    shortlist: list[Article] = []
    for day, items in group_by_day(articles).items():
        chosen, _ = pick_for_day(items, limit=MAX_ARTICLES_PER_DAY + 2, min_score=0.0)
        shortlist.extend(s.article for s in chosen)

    for i, article in enumerate(shortlist, 1):
        extract(article)
        flag = "ok " if article.word_count >= 200 else "zayıf"
        print(f"  [{i}/{len(shortlist)}] {flag} {article.word_count:5d}w  {article.title[:58]}")

    save_index(articles, POOL)
    save_index(shortlist, ENRICHED)
    print(f"\nYazıldı: {POOL.name}, {ENRICHED.name}")
    return 0


# --------------------------------------------------------------------------
def _build_edition(date: str, enriched: list[Article], *, use_batch: bool) -> bool:
    """Bir gün için sayıyı üretir. İçerik yoksa False döner."""
    from .compose import save_edition
    from .summarize import summarize_many

    todays = [a for a in enriched if a.date == date and a.word_count >= 200]
    chosen, _ = pick_for_day(todays, limit=MAX_ARTICLES_PER_DAY)

    pairs: list[tuple[Article, str]] = []
    if chosen:
        pairs.append((chosen[0].article, "cover"))
        pairs.extend((s.article, "brief") for s in chosen[1:])

    # Gün zayıfsa arşivden takviye et
    if len(pairs) < 3:
        used = {a.url for a, _ in pairs}
        pool = [
            a for a in enriched
            if a.date < date and a.url not in used and a.word_count >= 400
        ]
        need = 3 - len(pairs)
        fillers = [s.article for s in rank(pool)[: need * 3]][:need]
        if not pairs and fillers:
            pairs.append((fillers.pop(0), "cover"))
        pairs.extend((a, "archive") for a in fillers)

    if not pairs:
        print(f"  {date}: içerik yok, atlanıyor")
        return False

    print(f"  {date}: {len(pairs)} yazı özetleniyor…")
    if use_batch:
        from .summarize import collect_batch, submit_batch

        drafts = collect_batch(submit_batch(pairs), pairs)
    else:
        drafts = summarize_many(pairs, verbose=False)

    if not drafts:
        print(f"  {date}: özet üretilemedi")
        return False
    if not any(d["slot"] == "cover" for d in drafts):
        drafts[0]["slot"] = "cover"

    intro = (
        f"{len(drafts)} yazı: "
        + ", ".join(dict.fromkeys(d["tags"][0] for d in drafts if d["tags"]))
        + "."
    )
    save_edition(date, intro, drafts)
    return True


def _condense(text: str, budget: int) -> str:
    """Uzun metni kırpar: baş kısmı tam, gerisinden paragraf başları."""
    if len(text) <= budget:
        return text
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    head, used = [], 0
    for p in paragraphs:
        # İlk paragraf bütçeyi aşsa bile alınır — giriş olmadan özet yazılamaz.
        if head and used + len(p) > budget * 0.62:
            break
        head.append(p)
        used += len(p)

    tail, remaining = [], budget - used
    for p in paragraphs[len(head):]:
        chunk = p if len(p) < 110 else p[:260] + " …"
        if remaining - len(chunk) < 0:
            break
        tail.append(chunk)
        remaining -= len(chunk)
    return "\n".join(head) + "\n\n[…ARADAN ATLANDI…]\n\n" + "\n".join(tail)


def cmd_candidates(args: argparse.Namespace) -> int:
    """Bir günün adaylarını puanlarıyla ve metinleriyle basar.

    Sayıyı elle yazarken kullanılır: çıktıyı okuyup hangi yazının kapak,
    hangisinin kısa olacağına karar verirsin.
    """
    if not ENRICHED.exists():
        print("Önce `fetch` çalıştır.", file=sys.stderr)
        return 1

    enriched = load_index(ENRICHED)
    date = args.date or _today()
    todays = [a for a in enriched if a.date == date]

    if not todays:
        print(f"{date}: bu güne ait yazı yok.\n")
        print("Arşivden takviye için en iyi adaylar:")
        pool = [a for a in enriched if a.date < date and a.word_count >= 400]
        for s in rank(pool)[: args.limit]:
            print(f"  {s.score:6.1f} [{s.article.source_key:16s}] {s.article.date}  {s.article.title[:66]}")
        return 0

    chosen, rejected = pick_for_day(todays, limit=args.limit, min_score=0.0)

    print(f"\n{'=' * 100}\n{date} — {len(todays)} yayın, {len(chosen)} aday\n{'=' * 100}")
    for s in chosen:
        a = s.article
        print(f"\n{'─' * 100}")
        print(f"PUAN   : {s.score}   ({', '.join(s.reasons[:3])})")
        print(f"KAYNAK : {a.source_name}")
        print(f"BAŞLIK : {a.title}")
        print(f"URL    : {a.url}")
        print(f"BOYUT  : {a.word_count} kelime (~{max(1, round(a.word_count / 220))} dk)")
        print(f"{'─' * 100}")
        print(_condense(a.text, args.chars))

    if rejected:
        print(f"\n{'=' * 100}\nELENENLER ({len(rejected)})\n{'=' * 100}")
        for r in rejected:
            print(f"  {r.score:6.1f} [{r.article.source_key:16s}] {r.article.title[:70]}")
    return 0


def cmd_daily(args: argparse.Namespace) -> int:
    date = args.date or _today()
    if not ENRICHED.exists():
        print("Önce `fetch` çalıştır.", file=sys.stderr)
        return 1
    enriched = load_index(ENRICHED)
    ok = _build_edition(date, enriched, use_batch=args.batch)
    return 0 if ok else 1


def cmd_backfill(args: argparse.Namespace) -> int:
    if not ENRICHED.exists():
        print("Önce `fetch` çalıştır.", file=sys.stderr)
        return 1
    enriched = load_index(ENRICHED)
    end = datetime.fromisoformat(args.until) if args.until else datetime.now(timezone.utc)
    dates = [(end - timedelta(days=i)).date().isoformat() for i in range(args.days)]

    made = 0
    for date in sorted(dates):
        if (CONTENT_DIR / f"{date}.json").exists() and not args.force:
            print(f"  {date}: zaten var, atlanıyor")
            continue
        if _build_edition(date, enriched, use_batch=args.batch):
            made += 1
    print(f"\n{made} sayı üretildi.")
    return 0


# --------------------------------------------------------------------------
def cmd_build(_: argparse.Namespace) -> int:
    from .build import build

    result = build()
    print(
        f"OK  {result['pages']} sayfa | {result['edition_count']} sayı | "
        f"{result['article_count']} özet | {result['source_count']} kaynak"
    )
    return 0


def cmd_serve(args: argparse.Namespace) -> int:
    import http.server
    import socketserver
    from functools import partial

    from .config import OUTPUT_DIR

    if not OUTPUT_DIR.exists():
        print("docs/ yok — önce `build` çalıştır.", file=sys.stderr)
        return 1
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(OUTPUT_DIR))
    with socketserver.TCPServer(("", args.port), handler) as httpd:
        print(f"http://localhost:{args.port}  (Ctrl+C ile durdur)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\ndurduruldu")
    return 0


def cmd_check(_: argparse.Namespace) -> int:
    """İçerik dosyalarını doğrular: eksik alan, bozuk slot, tekrar eden URL."""
    from .models import load_all

    editions = load_all(CONTENT_DIR)
    problems: list[str] = []
    seen_urls: dict[str, str] = {}

    for e in editions:
        covers = [a for a in e.articles if a.slot == "cover"]
        if len(covers) != 1:
            problems.append(f"{e.date}: {len(covers)} kapak (1 olmalı)")
        for a in e.articles:
            if not a.summary.strip():
                problems.append(f"{e.date}/{a.id}: özet boş")
            if not a.for_you.strip():
                problems.append(f"{e.date}/{a.id}: 'sende karşılığı' boş")
            if a.published > e.date:
                problems.append(f"{e.date}/{a.id}: yayın tarihi sayıdan yeni ({a.published})")
            if a.url in seen_urls:
                problems.append(f"{e.date}/{a.id}: URL tekrarı ({seen_urls[a.url]} sayısında da var)")
            else:
                seen_urls[a.url] = e.date

    total = sum(len(e.articles) for e in editions)
    if problems:
        print(f"{len(problems)} sorun bulundu:\n")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"OK  {len(editions)} sayı, {total} özet, tekrar yok, tüm alanlar dolu.")
    return 0


# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pipeline", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("fetch", help="kaynakları tara ve metinleri çıkar")
    p.add_argument("--days", type=int, default=LOOKBACK_DAYS)
    p.set_defaults(func=cmd_fetch)

    p = sub.add_parser("candidates", help="bir günün adaylarını metinleriyle bas (elle yazmak için)")
    p.add_argument("--date", help="YYYY-MM-DD (varsayılan: bugün)")
    p.add_argument("--limit", type=int, default=6, help="kaç aday gösterilsin")
    p.add_argument("--chars", type=int, default=2200, help="makale başına karakter bütçesi")
    p.set_defaults(func=cmd_candidates)

    p = sub.add_parser("daily", help="bir günün sayısını üret (Claude API ile, otomatik)")
    p.add_argument("--date", help="YYYY-MM-DD (varsayılan: bugün)")
    p.add_argument("--batch", action="store_true", help="Batch API kullan (yarı fiyat, yavaş)")
    p.set_defaults(func=cmd_daily)

    p = sub.add_parser("backfill", help="geçmiş günleri doldur")
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--until", help="YYYY-MM-DD (varsayılan: bugün)")
    p.add_argument("--batch", action="store_true", default=True)
    p.add_argument("--force", action="store_true", help="var olan sayıları da yeniden üret")
    p.set_defaults(func=cmd_backfill)

    p = sub.add_parser("build", help="docs/ statik sitesini üret")
    p.set_defaults(func=cmd_build)

    p = sub.add_parser("serve", help="yerel önizleme sunucusu")
    p.add_argument("--port", type=int, default=4173)
    p.set_defaults(func=cmd_serve)

    p = sub.add_parser("check", help="içerik tutarlılık denetimi")
    p.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
