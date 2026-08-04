"""Küratörlük: ham makale havuzundan günün sayısını seçme.

Bir günde 15 makale yayımlanabiliyor ve bunların yarısı pazarlama. Amaç:
Eren'in profiline (backend / veri / uygulamalı AI) en çok öğreten 3-5 tanesini
yukarı çıkarmak. Puanlama kaba ama şeffaf; her makalenin neden seçildiği loglanır.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass

from .fetch import Article

# --- Kaynak ağırlıkları ----------------------------------------------------
# Derin mühendislik yazısı çıkaran kaynaklar daha yüksek taban puan alır.
SOURCE_WEIGHT: dict[str, float] = {
    "uber": 3.0,
    "netflix": 3.0,
    "meta": 2.8,
    "anthropic": 2.8,
    "stripe": 2.5,
    "cloudflare": 2.2,
    "databricks": 2.0,
    "microsoft": 2.0,
    "aws-architecture": 1.8,
    "google-research": 1.6,
    "openai": 1.3,
    "google-cloud": 1.0,
}

# --- Konu sinyalleri -------------------------------------------------------
# Eren'in stack'ine ve büyümek istediği alanlara doğrudan dokunanlar.
STRONG_SIGNALS = {
    # dağıtık sistemler / backend
    "latency": 3, "throughput": 3, "scalab": 3, "distributed": 3, "consistency": 3,
    "replication": 3, "sharding": 3, "partition": 2, "consensus": 3, "raft": 3,
    "idempoten": 3, "backpressure": 3, "rate limit": 3, "circuit breaker": 3,
    "load balanc": 2, "queue": 2, "kafka": 3, "event-driven": 2, "microservice": 2,
    "failover": 3, "outage": 3, "postmortem": 4, "incident": 3, "reliability": 3,
    "observability": 3, "tracing": 3, "profiling": 3, "benchmark": 2,
    # veri
    "postgres": 4, "redis": 4, "database": 3, "query optim": 3, "index": 2,
    "cache": 3, "etl": 2, "data pipeline": 3, "spark": 2, "lakehouse": 2,
    "streaming": 2, "olap": 2, "oltp": 2, "sql": 2, "schema migration": 3,
    # uygulamalı AI
    "rag": 4, "retrieval": 3, "embedding": 3, "vector": 3, "agent": 3,
    "tool use": 3, "context window": 3, "fine-tun": 2, "inference": 3,
    "prompt": 2, "evaluation": 3, "hallucinat": 2, "llm": 2, "quantiz": 2,
    # diller / araçlar
    "python": 2, "java": 2, "golang": 2, " go ": 1, "rust": 3, "jvm": 2,
    "docker": 2, "kubernetes": 2, "ci/cd": 2, "github actions": 3,
    "grpc": 3, "api design": 3, "rest api": 2, "testing": 2, "migration": 2,
    # mühendislik kültürü
    "how we built": 4, "lessons learned": 3, "we migrated": 3, "deep dive": 3,
    "under the hood": 4, "architecture": 2, "trade-off": 3, "cost": 2,
}

# Pazarlama / duyuru sinyalleri: puanı aşağı çeker.
WEAK_SIGNALS = {
    "generally available": -4, "now available": -3, "announcing": -3,
    "introducing": -2, "partnership": -5, "customer": -2, "webinar": -6,
    "summit": -4, "keynote": -4, "award": -5, "leader in": -5,
    "transform your business": -6, "empower": -3, "unlock the power": -5,
    "policy": -4, "governance framework": -3, "economic": -3, "hiring": -5,
    "pricing update": -3, "roadmap": -2, "recap": -3, "q&a with": -2,
}

MIN_SCORE = 2.0            # bunun altındakiler sayıya girmez


@dataclass
class Scored:
    article: Article
    score: float
    reasons: list[str]


def _signal_score(text: str, table: dict[str, int]) -> tuple[float, list[str]]:
    total, hits = 0.0, []
    for phrase, weight in table.items():
        if phrase in text:
            total += weight
            hits.append(phrase)
    return total, hits


def score(article: Article) -> Scored:
    haystack = f" {article.title.lower()} {article.feed_summary.lower()} "
    body_head = article.text[:4000].lower() if article.text else ""

    base = SOURCE_WEIGHT.get(article.source_key, 1.0)
    reasons = [f"kaynak:{article.source_key}(+{base})"]

    strong, strong_hits = _signal_score(haystack, STRONG_SIGNALS)
    # gövdedeki sinyaller daha zayıf sayılır (başlıkta geçmesi daha anlamlı)
    body_strong, body_hits = _signal_score(body_head, STRONG_SIGNALS)
    weak, weak_hits = _signal_score(haystack, WEAK_SIGNALS)

    total = base + strong + (body_strong * 0.25) + weak

    # Uzun yazı = derin yazı (belli bir noktaya kadar)
    if article.word_count:
        if article.word_count >= 2500:
            total += 3
            reasons.append("uzun-derin(+3)")
        elif article.word_count >= 1200:
            total += 2
            reasons.append("orta-uzun(+2)")
        elif article.word_count < 400:
            total -= 3
            reasons.append("çok-kısa(-3)")

    # Başlıkta soru ya da sayı → çoğunlukla somut vaka çalışması
    if re.search(r"\b\d+(x|%|\s*(ms|gb|tb|qps|rps))\b", article.title.lower()):
        total += 2
        reasons.append("somut-metrik(+2)")

    if strong_hits:
        reasons.append("konu:" + ",".join(strong_hits[:6]))
    if body_hits and not strong_hits:
        reasons.append("gövde:" + ",".join(body_hits[:4]))
    if weak_hits:
        reasons.append("pazarlama:" + ",".join(weak_hits[:4]))

    return Scored(article=article, score=round(total, 2), reasons=reasons)


def rank(articles: list[Article]) -> list[Scored]:
    return sorted((score(a) for a in articles), key=lambda s: s.score, reverse=True)


def pick_for_day(
    articles: list[Article],
    *,
    limit: int = 5,
    max_per_source: int = 2,
    min_score: float = MIN_SCORE,
) -> tuple[list[Scored], list[Scored]]:
    """Bir günün makalelerinden sayıyı seçer.

    Döner: (seçilenler, elenenler). Tek kaynağın günü domine etmesini engeller.
    """
    ranked = rank(articles)
    chosen: list[Scored] = []
    per_source: defaultdict[str, int] = defaultdict(int)
    rejected: list[Scored] = []

    for item in ranked:
        key = item.article.source_key
        if len(chosen) >= limit:
            rejected.append(item)
        elif item.score < min_score:
            rejected.append(item)
        elif per_source[key] >= max_per_source:
            rejected.append(item)
        else:
            chosen.append(item)
            per_source[key] += 1

    return chosen, rejected


def group_by_day(articles: list[Article]) -> dict[str, list[Article]]:
    days: defaultdict[str, list[Article]] = defaultdict(list)
    for a in articles:
        days[a.date].append(a)
    return dict(sorted(days.items(), reverse=True))
