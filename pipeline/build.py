"""content/*.json -> docs/ statik site üretimi.

Çıktı tamamen statik: GitHub Pages doğrudan `docs/` klasörünü yayınlar.
Arama istemci tarafında `search-index.json` üzerinden çalışır (sunucu gerekmez).
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import Counter, defaultdict
from datetime import datetime, timezone
from email.utils import format_datetime
from html import escape
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

from .config import CONTENT_DIR, OUTPUT_DIR, SITE, SOURCE_BY_KEY, SOURCES, STATIC_DIR, TEMPLATE_DIR
from .models import Edition, Summary, load_all, slugify, tr_date


# --------------------------------------------------------------------------
# Jinja ortamı
# --------------------------------------------------------------------------
def _paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", (text or "").strip()) if p.strip()]


def _inline_md(text: str) -> Markup:
    """Özet metninde sadece `kod` ve **kalın** desteklenir; gerisi düz metin.

    Girdi önce kaçırılır (escape), sonra bu iki desen HTML'e çevrilir. Sonuç
    Markup olarak döndüğü için Jinja tekrar kaçırmaz — XSS riski yok.
    """
    out = escape(text or "")
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    return Markup(out)


def rich(text: str) -> Markup:
    return Markup("".join(f"<p>{_inline_md(p)}</p>" for p in _paragraphs(text)))


def _asset_version() -> str:
    digest = hashlib.sha1()
    for f in sorted(STATIC_DIR.glob("*")):
        if f.is_file():
            digest.update(f.read_bytes())
    return digest.hexdigest()[:8]


def make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["rich"] = rich
    env.filters["inline"] = _inline_md
    env.filters["plain"] = _plain
    env.filters["tr_date"] = tr_date
    env.filters["slugify"] = slugify
    env.globals["site"] = SITE
    env.globals["sources"] = SOURCES
    env.globals["source_by_key"] = SOURCE_BY_KEY
    env.globals["now"] = datetime.now(timezone.utc)
    # Statik dosyalar değişince tarayıcı önbelleği kendiliğinden kırılsın
    env.globals["asset_version"] = _asset_version()
    return env


# --------------------------------------------------------------------------
# Yazma yardımcıları
# --------------------------------------------------------------------------
def write_page(out_root: Path, url_path: str, html: str) -> None:
    """'/arsiv/' -> docs/arsiv/index.html"""
    rel = url_path.strip("/")
    target = out_root / rel / "index.html" if rel else out_root / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def write_file(out_root: Path, name: str, content: str) -> None:
    target = out_root / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


# --------------------------------------------------------------------------
# Toplu veri
# --------------------------------------------------------------------------
def collect_stats(editions: list[Edition]) -> dict:
    articles = [a for e in editions for a in e.articles]
    per_source = Counter(a.source_key for a in articles)
    tags = Counter(t for a in articles for t in a.tags)
    return {
        "edition_count": len(editions),
        "article_count": len(articles),
        "source_count": len({a.source_key for a in articles}),
        "term_count": sum(len(a.terms) for a in articles),
        "per_source": per_source,
        "top_tags": tags.most_common(24),
        "first_date": editions[-1].date if editions else "",
        "last_date": editions[0].date if editions else "",
    }


def _plain(text: str) -> str:
    """Arama parçacığı için: `kod` ve **kalın** işaretlerini kaldır."""
    out = re.sub(r"`([^`]+)`", r"\1", text or "")
    out = re.sub(r"\*\*([^*]+)\*\*", r"\1", out)
    return re.sub(r"\s+", " ", out).strip()


def build_search_index(editions: list[Edition]) -> str:
    rows = []
    for e in editions:
        for a in e.articles:
            rows.append({
                "d": e.date,
                "t": a.title_tr,
                "o": a.title,
                "s": a.source_name,
                "k": a.source_key,
                "g": a.tags,
                "x": a.difficulty,
                "b": _plain(a.summary)[:320],
                "u": f"/sayi/{e.date}/#{a.id}",
            })
    return json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


def build_feed(editions: list[Edition]) -> str:
    items = []
    for e in editions[:20]:
        for a in e.articles:
            link = f"{SITE['base_url']}/sayi/{e.date}/#{a.id}"
            pub = datetime.fromisoformat(f"{e.date}T08:00:00+00:00")
            desc = escape(_plain(a.summary)[:600])
            items.append(
                "    <item>\n"
                f"      <title>{escape(a.title_tr)}</title>\n"
                f"      <link>{escape(link)}</link>\n"
                f"      <guid isPermaLink=\"false\">{a.id}</guid>\n"
                f"      <pubDate>{format_datetime(pub)}</pubDate>\n"
                f"      <category>{escape(a.source_name)}</category>\n"
                f"      <description>{desc}</description>\n"
                "    </item>"
            )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0">\n  <channel>\n'
        f"    <title>{escape(SITE['title'])}</title>\n"
        f"    <link>{SITE['base_url']}</link>\n"
        f"    <description>{escape(SITE['tagline'])}</description>\n"
        f"    <language>tr</language>\n"
        + "\n".join(items)
        + "\n  </channel>\n</rss>\n"
    )


def build_sitemap(editions: list[Edition], extra: list[str]) -> str:
    urls = ["/", "/arsiv/", "/hakkinda/", "/ara/"] + [e.path for e in editions] + extra
    body = "\n".join(
        f"  <url><loc>{SITE['base_url']}{u}</loc></url>" for u in dict.fromkeys(urls)
    )
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n"
    )


# --------------------------------------------------------------------------
# Ana akış
# --------------------------------------------------------------------------
def build(content_dir: Path = CONTENT_DIR, out_root: Path = OUTPUT_DIR) -> dict:
    editions = load_all(content_dir)
    if not editions:
        raise SystemExit(
            f"content/ boş ({content_dir}). Önce `python -m pipeline.cli daily` çalıştır."
        )

    env = make_env()
    stats = collect_stats(editions)
    # Sayı numarası: en eski sayı 1
    env.globals["edition_no"] = {e.date: n for n, e in enumerate(reversed(editions), 1)}

    # Temiz çıktı (CNAME'i koru)
    cname = (out_root / "CNAME").read_text(encoding="utf-8").strip() if (out_root / "CNAME").exists() else SITE["domain"]
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    # Statik dosyalar
    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, out_root / "static")

    # --- Ana sayfa: en son sayı ---
    latest = editions[0]
    write_page(out_root, "/", env.get_template("index.html").render(
        edition=latest,
        recent=editions[1:9],
        stats=stats,
        is_home=True,
    ))

    # --- Günlük sayılar ---
    day_tpl = env.get_template("day.html")
    for i, edition in enumerate(editions):
        newer = editions[i - 1] if i > 0 else None      # listeyi tersten geziyoruz
        older = editions[i + 1] if i + 1 < len(editions) else None
        write_page(out_root, edition.path, day_tpl.render(
            edition=edition,
            newer=newer,
            older=older,
            stats=stats,
        ))

    # --- Arşiv ---
    by_month: defaultdict[str, list[Edition]] = defaultdict(list)
    for e in editions:
        by_month[e.date[:7]].append(e)
    write_page(out_root, "/arsiv/", env.get_template("archive.html").render(
        editions=editions,
        by_month=sorted(by_month.items(), reverse=True),
        stats=stats,
    ))

    # --- Kaynak sayfaları ---
    src_tpl = env.get_template("source.html")
    source_paths = []
    for source in SOURCES:
        rows = [
            (e, a) for e in editions for a in e.articles if a.source_key == source.key
        ]
        if not rows:
            continue
        path = f"/kaynak/{source.key}/"
        source_paths.append(path)
        write_page(out_root, path, src_tpl.render(
            source=source, rows=rows, stats=stats,
        ))

    # --- Etiket sayfaları ---
    tag_tpl = env.get_template("tag.html")
    tag_rows: defaultdict[str, list] = defaultdict(list)
    tag_label: dict[str, str] = {}
    for e in editions:
        for a in e.articles:
            for t in a.tags:
                key = slugify(t)
                tag_label[key] = t
                tag_rows[key].append((e, a))
    tag_paths = []
    # Her etiket için sayfa üretilir: kartlardaki #etiket linkleri hep canlı olmalı,
    # tek yazılık bir etiket bile 404 vermemeli.
    for key, rows in tag_rows.items():
        path = f"/etiket/{key}/"
        tag_paths.append(path)
        write_page(out_root, path, tag_tpl.render(
            tag=tag_label[key], rows=rows, stats=stats,
        ))

    # --- Sabit sayfalar ---
    write_page(out_root, "/hakkinda/", env.get_template("about.html").render(stats=stats))
    write_page(out_root, "/ara/", env.get_template("search.html").render(stats=stats))

    # --- Veri dosyaları ---
    write_file(out_root, "search-index.json", build_search_index(editions))
    write_file(out_root, "feed.xml", build_feed(editions))
    write_file(out_root, "sitemap.xml", build_sitemap(editions, source_paths + tag_paths))
    write_file(out_root, "robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE['base_url']}/sitemap.xml\n")
    write_file(out_root, "CNAME", cname + "\n")
    write_file(out_root, ".nojekyll", "")

    stats["pages"] = 4 + len(editions) + len(source_paths) + len(tag_paths)
    return stats


if __name__ == "__main__":
    result = build()
    print(
        f"OK  {result['pages']} sayfa | {result['edition_count']} sayı | "
        f"{result['article_count']} özet | {result['source_count']} kaynak"
    )
