"""content/*.json içindeki veri sözleşmesi.

Bu dosya sitenin tek gerçek kaynağıdır: pipeline buraya yazar, build buradan okur.
Şema değişirse `SCHEMA_VERSION` artırılır ve build eski dosyaları da okuyabilir.
"""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from datetime import date as _date
from pathlib import Path

SCHEMA_VERSION = 1

# Yazının sayfadaki yeri
SLOT_COVER = "cover"       # günün kapağı: uzun özet
SLOT_BRIEF = "brief"       # kısa kısa
SLOT_ARCHIVE = "archive"   # arşivden seçme (gün zayıfsa)

DIFFICULTIES = ("başlangıç", "orta", "ileri")

TR_MONTHS = (
    "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
    "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık",
)
TR_DAYS = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar")


def tr_date(iso: str, *, with_weekday: bool = False) -> str:
    """'2026-08-03' -> '3 Ağustos 2026' (istenirse '· Pazartesi' ekli)."""
    y, m, d = (int(x) for x in iso[:10].split("-"))
    out = f"{d} {TR_MONTHS[m - 1]} {y}"
    if with_weekday:
        out += f", {TR_DAYS[_date(y, m, d).weekday()]}"
    return out


def slugify(value: str) -> str:
    table = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosucgiosu")
    value = value.translate(table).lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:80]


@dataclass
class Term:
    """Özette geçen teknik terimin Türkçe/İngilizce karşılığı ve tek cümlelik tanımı."""
    en: str
    tr: str
    definition: str


@dataclass
class Summary:
    id: str
    slot: str
    source_key: str
    source_name: str
    title: str                       # orijinal (İngilizce) başlık
    title_tr: str                    # Türkçe başlık
    url: str
    published: str                   # ISO tarih (gerçek yayın tarihi)
    summary: str                     # 1-3 paragraf ana özet
    key_points: list[str] = field(default_factory=list)
    why_it_matters: str = ""         # neden önemli / sektörel bağlam
    for_you: str = ""                # Eren'in stack'ine somut bağlantı
    terms: list[Term] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    difficulty: str = "orta"
    read_minutes: int = 0            # orijinal makalenin tahmini okuma süresi
    authors: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.terms = [Term(**t) if isinstance(t, dict) else t for t in self.terms]
        if self.difficulty not in DIFFICULTIES:
            self.difficulty = "orta"

    @property
    def is_archive(self) -> bool:
        return self.slot == SLOT_ARCHIVE

    @property
    def published_tr(self) -> str:
        return tr_date(self.published)

    @property
    def slug(self) -> str:
        return slugify(self.title_tr or self.title)


@dataclass
class Edition:
    """Bir günün sayısı."""
    date: str                        # YYYY-MM-DD
    intro: str = ""                  # editör notu, 1-2 cümle
    articles: list[Summary] = field(default_factory=list)
    schema: int = SCHEMA_VERSION

    def __post_init__(self) -> None:
        self.articles = [
            Summary(**a) if isinstance(a, dict) else a for a in self.articles
        ]

    # --- türetilmiş -------------------------------------------------------
    @property
    def cover(self) -> Summary | None:
        for a in self.articles:
            if a.slot == SLOT_COVER:
                return a
        return self.articles[0] if self.articles else None

    @property
    def briefs(self) -> list[Summary]:
        return [a for a in self.articles if a.slot == SLOT_BRIEF]

    @property
    def archive_picks(self) -> list[Summary]:
        return [a for a in self.articles if a.slot == SLOT_ARCHIVE]

    @property
    def date_tr(self) -> str:
        return tr_date(self.date, with_weekday=True)

    @property
    def date_short(self) -> str:
        return tr_date(self.date)

    @property
    def path(self) -> str:
        return f"/sayi/{self.date}/"

    @property
    def sources(self) -> list[str]:
        seen: list[str] = []
        for a in self.articles:
            if a.source_name not in seen:
                seen.append(a.source_name)
        return seen

    @property
    def all_tags(self) -> list[str]:
        seen: list[str] = []
        for a in self.articles:
            for t in a.tags:
                if t not in seen:
                    seen.append(t)
        return seen

    # --- G/Ç --------------------------------------------------------------
    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False, indent=2)

    def save(self, directory: Path) -> Path:
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{self.date}.json"
        path.write_text(self.to_json(), encoding="utf-8")
        return path

    @classmethod
    def load(cls, path: Path) -> "Edition":
        return cls(**json.loads(path.read_text(encoding="utf-8")))


def load_all(directory: Path) -> list[Edition]:
    """content/ içindeki tüm sayıları yeniden-eskiye sıralı döner."""
    editions = [Edition.load(p) for p in sorted(directory.glob("20*.json"))]
    return sorted(editions, key=lambda e: e.date, reverse=True)
