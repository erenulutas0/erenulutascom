"""Kaynak tanımları ve genel ayarlar.

Her kaynağın nasıl okunacağı `kind` alanıyla belirlenir:
  - "rss"      : standart RSS/Atom feed
  - "sitemap"  : sitemap.xml + liste sayfasından tarih eşleme (Anthropic)
  - "html"     : liste sayfasından slug kazıma (Uber)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# --- Yollar ---------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"          # günlük JSON arşivi (kaynak-of-truth)
RAW_DIR = ROOT / ".cache" / "raw"       # indirilen ham HTML (tekrar indirmemek için)
OUTPUT_DIR = ROOT / "docs"              # GitHub Pages çıktısı
TEMPLATE_DIR = ROOT / "templates"
STATIC_DIR = ROOT / "static"

# --- Site kimliği ---------------------------------------------------------
SITE = {
    "domain": "erenulutas.com",
    "base_url": "https://erenulutas.com",
    "title": "Eren'in Mühendislik Gazetesi",
    "tagline": "Dünyanın en iyi mühendislik ekipleri bugün ne yazdı?",
    "author": "Eren Ulutaş",
    "author_url": "https://github.com/erenulutas0",
    "linkedin": "https://linkedin.com/in/eren-u-55918a2a0",
    "email": "eerenulutass@gmail.com",
    "lang": "tr",
    "timezone": "Europe/Istanbul",
}

# --- HTTP -----------------------------------------------------------------
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)
BROWSER_HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
}
REQUEST_TIMEOUT = 30
REQUEST_DELAY = 0.7          # aynı host'a ardışık istekler arası bekleme (saniye)


@dataclass(frozen=True)
class Source:
    key: str                  # dosya/URL güvenli kimlik
    name: str                 # ekranda görünen ad
    kind: str                 # rss | sitemap | html
    url: str                  # feed ya da liste sayfası
    site: str                 # kaynağın ana sayfası
    color: str                # marka rengi (arayüzdeki rozet)
    # Konu etiketi: özetlerken "bu kaynak neyle ilgilenir" ipucu olarak kullanılır
    focus: str = ""
    # Sadece bu yol öneki altındaki yazılar alınır (RSS'i geniş olan kaynaklar için)
    path_filter: tuple[str, ...] = field(default_factory=tuple)
    # Başlık/özet bu kelimeleri içeriyorsa ele: pazarlama/duyuru gürültüsünü kes
    exclude_keywords: tuple[str, ...] = field(default_factory=tuple)


# Pazarlama içeriğini elemek için ortak sözlük.
_MARKETING_NOISE = (
    "webinar", "join us at", "register now", "is now generally available in",
    "partner spotlight", "customer story", "case study:", "award",
    "gartner", "magic quadrant", "forrester wave", "summit recap",
    "now hiring", "we're hiring", "job opening",
)

SOURCES: tuple[Source, ...] = (
    Source(
        key="uber",
        name="Uber Engineering",
        kind="html",
        url="https://www.uber.com/blog/engineering/",
        site="https://www.uber.com/blog/engineering/",
        color="#000000",
        focus="dağıtık sistemler, veri altyapısı, mikroservis ölçeklendirme, ML platformları",
    ),
    Source(
        key="netflix",
        name="Netflix Tech Blog",
        kind="rss",
        url="https://netflixtechblog.com/feed",
        site="https://netflixtechblog.com",
        color="#E50914",
        focus="dayanıklılık (resilience), video altyapısı, veri platformu, öneri sistemleri",
    ),
    Source(
        key="aws-architecture",
        name="AWS Architecture Blog",
        kind="rss",
        url="https://aws.amazon.com/blogs/architecture/feed/",
        site="https://aws.amazon.com/blogs/architecture/",
        color="#FF9900",
        focus="bulut mimarisi desenleri, well-architected, serverless, çok-bölgeli dayanıklılık",
    ),
    Source(
        key="cloudflare",
        name="Cloudflare Blog",
        kind="rss",
        url="https://blog.cloudflare.com/rss/",
        site="https://blog.cloudflare.com",
        color="#F6821F",
        focus="ağ, edge computing, güvenlik, performans, internet altyapısı",
        exclude_keywords=_MARKETING_NOISE,
    ),
    Source(
        key="stripe",
        name="Stripe Engineering",
        kind="rss",
        url="https://stripe.com/blog/feed.rss",
        site="https://stripe.com/blog",
        color="#635BFF",
        focus="ödeme altyapısı, API tasarımı, idempotency, finansal sistemlerde tutarlılık",
        exclude_keywords=_MARKETING_NOISE + ("trends from", "what we learned at"),
    ),
    Source(
        key="databricks",
        name="Databricks Engineering",
        kind="rss",
        url="https://www.databricks.com/feed",
        site="https://www.databricks.com/blog",
        color="#FF3621",
        focus="veri mühendisliği, Spark, lakehouse, ETL, veri kalitesi, ML pipeline",
        exclude_keywords=_MARKETING_NOISE,
    ),
    Source(
        key="meta",
        name="Meta Engineering",
        kind="rss",
        url="https://engineering.fb.com/feed/",
        site="https://engineering.fb.com",
        color="#0866FF",
        focus="ölçek, performans optimizasyonu, altyapı, büyük ölçekli ML eğitimi",
    ),
    Source(
        key="openai",
        name="OpenAI Research",
        kind="rss",
        url="https://openai.com/news/rss.xml",
        site="https://openai.com/news/",
        color="#000000",
        focus="LLM araştırmaları, model yetenekleri, güvenlik, uygulama mimarileri",
        exclude_keywords=_MARKETING_NOISE + (
            "partnership", "we're bringing", "announcing our", "policy",
        ),
    ),
    Source(
        key="anthropic",
        name="Anthropic Engineering",
        kind="sitemap",
        url="https://www.anthropic.com/sitemap.xml",
        site="https://www.anthropic.com/engineering",
        color="#D97757",
        focus="LLM uygulama mühendisliği, agent tasarımı, tool use, context engineering, RAG",
        path_filter=("/engineering/",),
    ),
    Source(
        key="google-research",
        name="Google Research",
        kind="rss",
        url="https://research.google/blog/rss/",
        site="https://research.google/blog/",
        color="#4285F4",
        focus="temel araştırma, ML/algoritma, sistemler, sağlık ve bilim uygulamaları",
    ),
    Source(
        key="google-cloud",
        name="Google Cloud Blog",
        kind="rss",
        url="https://cloudblog.withgoogle.com/rss/",
        site="https://cloud.google.com/blog/",
        color="#34A853",
        focus="bulut altyapısı, veritabanları, Kubernetes, veri analitiği, AI platformu",
        exclude_keywords=_MARKETING_NOISE,
    ),
    Source(
        key="microsoft",
        name="Microsoft Engineering",
        kind="rss",
        url="https://devblogs.microsoft.com/engineering-at-microsoft/feed/",
        site="https://devblogs.microsoft.com/engineering-at-microsoft/",
        color="#0078D4",
        focus="geliştirici araçları, developer experience, iç mühendislik pratikleri",
    ),
)

SOURCE_BY_KEY = {s.key: s for s in SOURCES}


# --- Küratörlük ------------------------------------------------------------
# Bir günde en fazla kaç makale yayınlanacak. Fazlası "ayrıca bugün" listesine düşer.
MAX_ARTICLES_PER_DAY = 6

# Okuyucu profili: özetlerin "Pratikte" kısmını kalibre eder. Kişisel proje adı yok.
READER_PROFILE = """
Okuyucu: yeni mezun, junior bir yazılım mühendisi.
Güçlü olduğu yerler: Java/Spring Boot, Python, PostgreSQL, Redis, Docker, Linux,
CI/CD, LLM API'leri, RAG, embeddings, SQL.
Geliştirmek istediği yerler: büyük ölçekte distributed systems, production observability,
maliyet mühendisliği, kıdemli seviye sistem tasarımı.
Hedefi: iyi bir mühendislik ekibinde backend / data / uygulamalı AI rolü.
""".strip()
