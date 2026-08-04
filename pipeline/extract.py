"""Makale sayfasından tam metin ve gerçek başlık çıkarma.

trafilatura ana araç; bulamazsa elle yazılmış yedek bir çıkarıcı devreye girer.
Amaç: özetleyiciye navigasyon/footer gürültüsü olmadan temiz gövde metni vermek.
"""

from __future__ import annotations

import html as html_mod
import re

import trafilatura

from .fetch import Article, http_get, parse_date, strip_html

MIN_WORDS = 120          # bunun altı muhtemelen paywall/JS duvarı; özetlemeye değmez
MAX_CHARS = 60_000       # özetleyiciye gidecek metin tavanı


def _meta(html: str, *patterns: str) -> str:
    for pattern in patterns:
        m = re.search(pattern, html, re.I)
        if m:
            return html_mod.unescape(m.group(1)).strip()
    return ""


def real_title(html: str, fallback: str = "") -> str:
    title = _meta(
        html,
        r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"',
        r'<meta[^>]+name="twitter:title"[^>]+content="([^"]+)"',
        r'"headline"\s*:\s*"((?:[^"\\]|\\.)+)"',
        r"<h1[^>]*>(.*?)</h1>",
        r"<title[^>]*>(.*?)</title>",
    )
    title = strip_html(title)
    # Site adı ekleri: "Başlık | Uber Blog", "Başlık - Cloudflare"
    title = re.sub(
        r"\s*[|–—-]\s*(Uber Blog|Uber|Cloudflare|Databricks|Anthropic|"
        r"Google Research|Google Cloud Blog|Netflix TechBlog|Engineering at Meta|"
        r"Stripe|OpenAI|Amazon Web Services|AWS)\s*$",
        "",
        title,
    ).strip()
    return title or fallback


def _fallback_text(html: str) -> str:
    """trafilatura boş dönerse: en çok <p> içeren kabı seç."""
    html = re.sub(r"(?is)<(script|style|nav|header|footer|aside|form)[^>]*>.*?</\1>", " ", html)
    candidates = re.findall(r"(?is)<(?:article|main)[^>]*>(.*?)</(?:article|main)>", html)
    if not candidates:
        candidates = re.findall(r"(?is)<div[^>]*>(.*?)</div>", html)
    best, best_score = "", 0
    for chunk in candidates:
        score = len(re.findall(r"(?i)<p[ >]", chunk))
        if score > best_score:
            best, best_score = chunk, score
    paragraphs = re.findall(r"(?is)<p[^>]*>(.*?)</p>", best or html)
    text = "\n\n".join(strip_html(p) for p in paragraphs)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def extract(article: Article, *, verbose: bool = False) -> Article:
    """Makalenin gövdesini indirir ve `article` üzerine yazar."""
    try:
        html = http_get(article.url)
    except RuntimeError as exc:
        if verbose:
            print(f"    ! indirilemedi {article.url}: {exc}")
        return article

    text = trafilatura.extract(
        html,
        include_comments=False,
        include_tables=True,
        include_formatting=False,
        favor_precision=True,
        url=article.url,
    ) or ""

    if len(text.split()) < MIN_WORDS:
        alt = _fallback_text(html)
        if len(alt.split()) > len(text.split()):
            text = alt

    text = re.sub(r"\n{3,}", "\n\n", text).strip()[:MAX_CHARS]
    article.text = text
    article.word_count = len(text.split())

    # Slug'dan türetilmiş başlıkları gerçek başlıkla değiştir (Anthropic, Uber)
    better = real_title(html, article.title)
    if better and len(better) > 8:
        article.title = better

    if not article.feed_summary:
        article.feed_summary = _meta(
            html,
            r'<meta[^>]+name="description"[^>]+content="([^"]+)"',
            r'<meta[^>]+property="og:description"[^>]+content="([^"]+)"',
        )[:1200]

    if not article.authors:
        author = _meta(
            html,
            r'"author"\s*:\s*\{\s*"@type"\s*:\s*"Person"\s*,\s*"name"\s*:\s*"([^"]+)"',
            r'<meta[^>]+name="author"[^>]+content="([^"]+)"',
        )
        if author and len(author) < 80:
            article.authors = [author]

    # Tarihi feed'den alamadıysak sayfadan dene
    if not article.published:
        found = _meta(
            html,
            r'<meta[^>]+property="article:published_time"[^>]+content="([^"]+)"',
            r'"datePublished"\s*:\s*"([^"]+)"',
        )
        dt = parse_date(found)
        if dt:
            article.published = dt.isoformat()

    if verbose:
        print(f"    · {article.word_count:5d} kelime  {article.title[:64]}")
    return article


def extract_many(articles: list[Article], *, verbose: bool = True) -> list[Article]:
    out = []
    for i, article in enumerate(articles, 1):
        if verbose:
            print(f"  [{i}/{len(articles)}] {article.source_name}")
        out.append(extract(article, verbose=verbose))
    return out
