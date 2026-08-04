"""Kaynaklardan makale listesi çekme katmanı.

Üç adaptör var: RSS/Atom, sitemap (Anthropic), HTML kazıma (Uber).
Hepsi ortak `Article` yapısına indirger; üst katman kaynağın türünü bilmez.
"""

from __future__ import annotations

import gzip
import hashlib
import html as html_mod
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from .config import (
    BROWSER_HEADERS,
    RAW_DIR,
    REQUEST_DELAY,
    REQUEST_TIMEOUT,
    SOURCES,
    Source,
)

_last_request_at: dict[str, float] = {}


@dataclass
class Article:
    source_key: str
    source_name: str
    title: str
    url: str
    published: str                      # ISO 8601, UTC
    feed_summary: str = ""              # feed'den gelen kısa açıklama (varsa)
    authors: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    text: str = ""                      # extract.py doldurur
    word_count: int = 0

    @property
    def date(self) -> str:
        return self.published[:10]

    @property
    def id(self) -> str:
        return hashlib.sha1(self.url.encode("utf-8")).hexdigest()[:12]

    def to_dict(self) -> dict:
        d = asdict(self)
        d["id"] = self.id
        d["date"] = self.date
        return d


# --------------------------------------------------------------------------
# HTTP
# --------------------------------------------------------------------------
def _throttle(url: str) -> None:
    """Aynı host'a çok hızlı ardışık istek atmamak için basit gecikme."""
    host = urllib.parse.urlsplit(url).netloc
    now = time.monotonic()
    prev = _last_request_at.get(host, 0.0)
    wait = REQUEST_DELAY - (now - prev)
    if wait > 0:
        time.sleep(wait)
    _last_request_at[host] = time.monotonic()


def http_get(url: str, *, cache: bool = True, retries: int = 3) -> str:
    """URL'yi indirir. `cache=True` ise diske yazar; aynı URL bir daha indirilmez."""
    cache_path = RAW_DIR / f"{hashlib.sha1(url.encode()).hexdigest()}.html"
    if cache and cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")

    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            _throttle(url)
            req = urllib.request.Request(url, headers=BROWSER_HEADERS)
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                raw = resp.read()
                if resp.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                body = raw.decode("utf-8", errors="ignore")
            if cache:
                cache_path.parent.mkdir(parents=True, exist_ok=True)
                cache_path.write_text(body, encoding="utf-8")
            return body
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"indirilemedi: {url} ({last_error})")


# --------------------------------------------------------------------------
# Ortak yardımcılar
# --------------------------------------------------------------------------
_TAG_RE = re.compile(r"<[^>]+>")
_WS_RE = re.compile(r"[ \t\r\f\v]+")


def strip_html(fragment: str) -> str:
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", fragment or "")
    text = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>", "\n", text)
    text = _TAG_RE.sub(" ", text)
    text = html_mod.unescape(text)
    text = _WS_RE.sub(" ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def _cdata(value: str) -> str:
    value = value.strip()
    if value.startswith("<![CDATA[") and value.endswith("]]>"):
        value = value[9:-3]
    return html_mod.unescape(value).strip()


def parse_date(value: str) -> datetime | None:
    """RFC 822, ISO 8601 ve Atom biçimlerini tek noktadan çözer."""
    value = (value or "").strip()
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
        if dt is not None:
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        pass
    cleaned = value.replace("Z", "+00:00")
    for candidate in (cleaned, cleaned[:19], cleaned[:10]):
        try:
            dt = datetime.fromisoformat(candidate)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue

    # "June 23, 2026" / "Jun 23 2026" — Uber ve Anthropic sayfalarındaki görünen tarih
    normalized = value.replace(",", " ").strip()
    normalized = _WS_RE.sub(" ", normalized)
    for fmt in ("%B %d %Y", "%b %d %Y", "%d %B %Y", "%d %b %Y"):
        try:
            return datetime.strptime(normalized, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def _blocks(xml: str, tag: str) -> list[str]:
    return re.findall(rf"<{tag}[ >].*?</{tag}>", xml, re.S) or re.findall(
        rf"<{tag}>.*?</{tag}>", xml, re.S
    )


def _field(block: str, *names: str) -> str:
    for name in names:
        m = re.search(rf"<{name}(?:\s[^>]*)?>(.*?)</{name}>", block, re.S)
        if m:
            return _cdata(m.group(1))
    return ""


# --------------------------------------------------------------------------
# Adaptör: RSS / Atom
# --------------------------------------------------------------------------
def _fetch_rss(source: Source) -> list[Article]:
    xml = http_get(source.url, cache=False)
    entries = _blocks(xml, "item") or _blocks(xml, "entry")
    articles: list[Article] = []

    for block in entries:
        title = _field(block, "title")
        if not title:
            continue

        link = _field(block, "link")
        if not link:  # Atom: <link href="..."/>
            m = re.search(r'<link[^>]+rel="alternate"[^>]+href="([^"]+)"', block) or re.search(
                r'<link[^>]+href="([^"]+)"', block
            )
            link = html_mod.unescape(m.group(1)) if m else ""
        if not link:
            continue

        dt = parse_date(_field(block, "pubDate", "published", "updated", "dc:date"))
        if dt is None:
            continue

        summary = strip_html(_field(block, "description", "summary", "content:encoded"))
        authors = [
            _cdata(a) for a in re.findall(r"<(?:dc:creator|author)>(.*?)</(?:dc:creator|author)>", block, re.S)
        ]
        authors = [strip_html(a) for a in authors if a and "@" not in a][:3]
        tags = [_cdata(c) for c in re.findall(r"<category[^>]*>(.*?)</category>", block, re.S)][:6]

        articles.append(
            Article(
                source_key=source.key,
                source_name=source.name,
                title=strip_html(title),
                url=link.strip(),
                published=_iso(dt),
                feed_summary=summary[:1200],
                authors=authors,
                tags=tags,
            )
        )
    return articles


# --------------------------------------------------------------------------
# Adaptör: sitemap + liste sayfası (Anthropic)
# --------------------------------------------------------------------------
def _fetch_sitemap(source: Source) -> list[Article]:
    xml = http_get(source.url, cache=False)
    articles: list[Article] = []

    for block in _blocks(xml, "url"):
        loc = _field(block, "loc")
        if not loc or not any(p in loc for p in source.path_filter):
            continue
        # Liste sayfasının kendisi değil, tekil yazılar
        if loc.rstrip("/").endswith(tuple(p.strip("/") for p in source.path_filter)):
            continue

        dt = parse_date(_field(block, "lastmod"))
        if dt is None:
            continue

        slug = loc.rstrip("/").rsplit("/", 1)[-1]
        title = slug.replace("-", " ").strip()
        articles.append(
            Article(
                source_key=source.key,
                source_name=source.name,
                title=title[:1].upper() + title[1:],  # gerçek başlık extract'te düzeltilir
                url=loc,
                published=_iso(dt),
            )
        )
    return articles


# --------------------------------------------------------------------------
# Adaptör: HTML liste kazıma (Uber)
# --------------------------------------------------------------------------
_UBER_SKIP = {
    "engineering", "business", "community-support", "earn", "eat", "freight",
    "health", "higher-education", "merchants", "ride", "advertising", "transit",
    "autonomous-mobility-delivery", "product", "safety", "en", "tr",
}


def _fetch_html_uber(source: Source, max_pages: int = 4) -> list[Article]:
    """Uber blog'unda RSS yok; liste sayfalarından slug toplayıp yazıya gidiyoruz."""
    slugs: list[str] = []
    seen: set[str] = set()

    for page in range(1, max_pages + 1):
        url = source.url if page == 1 else f"{source.url}page/{page}/"
        try:
            page_html = http_get(url, cache=False)
        except RuntimeError:
            break
        found = re.findall(r"blog/([a-z0-9][a-z0-9\-]{10,})", page_html)
        fresh = [s for s in found if s not in _UBER_SKIP and s not in seen]
        if not fresh:
            break
        for s in fresh:
            seen.add(s)
            slugs.append(s)

    articles: list[Article] = []
    for slug in slugs:
        url = f"https://www.uber.com/blog/{slug}/"
        try:
            page_html = http_get(url)
        except RuntimeError:
            continue

        dt = None
        # 1) JSON-LD  2) <meta property="article:published_time">  3) görünen tarih
        m = re.search(r'"datePublished"\s*:\s*"([^"]+)"', page_html)
        if not m:
            m = re.search(r'<meta[^>]+article:published_time"[^>]+content="([^"]+)"', page_html)
        if m:
            dt = parse_date(m.group(1))
        if dt is None:
            m = re.search(
                r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(20\d\d)",
                page_html,
            )
            if m:
                dt = parse_date(f"{m.group(1)} {m.group(2)} {m.group(3)}")
        if dt is None:
            continue

        title = ""
        tm = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', page_html) or re.search(
            r"<title[^>]*>(.*?)</title>", page_html, re.S
        )
        if tm:
            title = html_mod.unescape(tm.group(1)).replace(" | Uber Blog", "").strip()
        if not title:
            title = slug.replace("-", " ").capitalize()

        desc = ""
        dm = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', page_html)
        if dm:
            desc = html_mod.unescape(dm.group(1)).strip()

        articles.append(
            Article(
                source_key=source.key,
                source_name=source.name,
                title=title,
                url=url,
                published=_iso(dt),
                feed_summary=desc[:1200],
            )
        )
    return articles


# --------------------------------------------------------------------------
# Üst katman
# --------------------------------------------------------------------------
_ADAPTERS = {
    "rss": _fetch_rss,
    "sitemap": _fetch_sitemap,
    "html": _fetch_html_uber,
}


def _is_noise(article: Article, source: Source) -> bool:
    haystack = f"{article.title} {article.feed_summary}".lower()
    return any(kw in haystack for kw in source.exclude_keywords)


def fetch_source(source: Source) -> list[Article]:
    adapter = _ADAPTERS[source.kind]
    articles = adapter(source)
    # Aynı URL'nin farklı varyantlarını tekilleştir
    unique: dict[str, Article] = {}
    for a in articles:
        if _is_noise(a, source):
            continue
        key = a.url.split("?")[0].rstrip("/")
        if key not in unique:
            unique[key] = a
    return sorted(unique.values(), key=lambda a: a.published, reverse=True)


def fetch_all(
    *,
    since: datetime | None = None,
    until: datetime | None = None,
    sources: tuple[Source, ...] = SOURCES,
    verbose: bool = True,
) -> list[Article]:
    collected: list[Article] = []
    for source in sources:
        try:
            found = fetch_source(source)
        except Exception as exc:  # bir kaynağın çökmesi tüm koşuyu düşürmesin
            if verbose:
                print(f"  ! {source.name}: {type(exc).__name__}: {exc}")
            continue

        if since or until:
            kept = []
            for a in found:
                dt = parse_date(a.published)
                if dt is None:
                    continue
                if since and dt < since:
                    continue
                if until and dt > until:
                    continue
                kept.append(a)
            found = kept

        if verbose:
            print(f"  + {source.name}: {len(found)} makale")
        collected.extend(found)

    return sorted(collected, key=lambda a: a.published, reverse=True)


def save_index(articles: list[Article], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": _iso(datetime.now(timezone.utc)),
        "count": len(articles),
        "articles": [a.to_dict() for a in articles],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def load_index(path: Path) -> list[Article]:
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for d in data["articles"]:
        d.pop("id", None)
        d.pop("date", None)
        out.append(Article(**d))
    return out
