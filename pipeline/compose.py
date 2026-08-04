"""Taslak özetleri tam `Edition` nesnesine çevirir.

İki kullanım yolu var:
  1. Otomatik  — summarize.py modelden taslak üretir, buraya verir.
  2. Editöryel — özet elle yazılır, teknik meta veriler (başlık, tarih, yazar,
     okuma süresi, id) makale önbelleğinden otomatik doldurulur.

Her iki yolda da tek doğrulama noktası burasıdır: eksik alan varsa yüksek sesle
hata verir, sessizce boş içerik üretmez.
"""

from __future__ import annotations

from pathlib import Path

from .config import CONTENT_DIR, ROOT
from .fetch import Article, load_index
from .models import Edition, Summary, Term

WORDS_PER_MINUTE = 220
_ARTICLE_CACHE: dict[str, Article] | None = None

_ALLOWED_KEYS = {
    "url", "slot", "title_tr", "summary", "key_points",
    "why_it_matters", "for_you", "terms", "tags", "difficulty",
}


def _norm(url: str) -> str:
    return url.split("?")[0].split("#")[0].rstrip("/")


def article_cache(path: Path | None = None) -> dict[str, Article]:
    """Çekilmiş makaleleri URL -> Article olarak indeksler."""
    global _ARTICLE_CACHE
    if _ARTICLE_CACHE is None or path is not None:
        source = path or (ROOT / ".cache" / "enriched.json")
        if not source.exists():
            raise FileNotFoundError(
                f"makale önbelleği yok: {source}\n"
                "Önce `python -m pipeline.cli fetch` çalıştır."
            )
        _ARTICLE_CACHE = {_norm(a.url): a for a in load_index(source)}
    return _ARTICLE_CACHE


def read_minutes(words: int) -> int:
    return max(1, round(words / WORDS_PER_MINUTE))


def compose_summary(draft: dict) -> Summary:
    """Tek bir taslağı doğrulayıp Summary'ye çevirir.

    draft: {url, slot, title_tr, summary, key_points, why_it_matters,
            for_you, terms, tags, difficulty}
    """
    url = draft["url"]
    art = article_cache().get(_norm(url))
    if art is None:
        raise KeyError(f"önbellekte yok: {url}")

    # Anahtar adındaki bir yazım hatası içeriği sessizce düşürmesin
    unknown = set(draft) - _ALLOWED_KEYS
    if unknown:
        raise ValueError(f"{url}: tanınmayan alan(lar): {', '.join(sorted(unknown))}")

    for required in ("title_tr", "summary", "slot"):
        if not draft.get(required):
            raise ValueError(f"{url}: '{required}' boş olamaz")

    return Summary(
        id=art.id,
        slot=draft["slot"],
        source_key=art.source_key,
        source_name=art.source_name,
        title=art.title,
        title_tr=draft["title_tr"],
        url=art.url,
        published=art.date,
        summary=draft["summary"].strip(),
        key_points=draft.get("key_points", []),
        why_it_matters=draft.get("why_it_matters", "").strip(),
        for_you=draft.get("for_you", "").strip(),
        terms=[Term(**t) for t in draft.get("terms", [])],
        tags=draft.get("tags", []),
        difficulty=draft.get("difficulty", "orta"),
        read_minutes=read_minutes(art.word_count),
        authors=art.authors[:2],
    )


def compose_edition(date: str, intro: str, drafts: list[dict]) -> Edition:
    articles = [compose_summary(d) for d in drafts]

    covers = [a for a in articles if a.slot == "cover"]
    if len(covers) != 1:
        raise ValueError(f"{date}: tam olarak 1 kapak olmalı, {len(covers)} var")

    # Kapak her zaman ilk sırada dursun
    articles.sort(key=lambda a: {"cover": 0, "brief": 1, "archive": 2}[a.slot])
    return Edition(date=date, intro=intro.strip(), articles=articles)


def save_edition(date: str, intro: str, drafts: list[dict], *, quiet: bool = False) -> Path:
    edition = compose_edition(date, intro, drafts)
    path = edition.save(CONTENT_DIR)
    if not quiet:
        slots = ", ".join(f"{a.slot}:{a.source_key}" for a in edition.articles)
        print(f"  yazıldı {path.name}  ({len(edition.articles)} yazı — {slots})")
    return path
