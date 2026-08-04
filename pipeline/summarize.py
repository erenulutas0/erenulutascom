"""Makaleyi Claude ile Türkçe özete çevirir.

Tasarım notları:
  * Çıktı şeması Pydantic ile zorlanır (`messages.parse`) — modelden serbest
    metin beklemiyoruz, doğrulanmış nesne alıyoruz.
  * Sistem promptu sabittir ve prompt cache'lenir; her makalede yeniden
    ücretlendirilmez (kaynak: yalnızca değişen kısım makale metni).
  * Toplu iş için Batch API var: yarı fiyat, saatler içinde döner.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

from pydantic import BaseModel, Field

from .config import READER_PROFILE, ROOT, SOURCE_BY_KEY
from .fetch import Article
from .models import DIFFICULTIES

# claude-opus-5 en iyi özeti çıkarır. Maliyeti düşürmek istersen ortam
# değişkeniyle claude-sonnet-5 ya da claude-haiku-4-5 verebilirsin.
MODEL = os.environ.get("GAZETE_MODEL", "claude-opus-5")
MAX_TOKENS = 8000
MAX_ARTICLE_CHARS = 40_000     # promptta makale metni tavanı


# --------------------------------------------------------------------------
# Çıktı şeması
# --------------------------------------------------------------------------
class TermOut(BaseModel):
    en: str = Field(description="Teknik terimin İngilizce hâli")
    tr: str = Field(description="Türkçe karşılığı")
    definition: str = Field(description="Tek cümlelik, jargonsuz tanım")


class SummaryDraft(BaseModel):
    title_tr: str = Field(description="Türkçe başlık; merak uyandırsın, tıklama tuzağı olmasın")
    summary: str = Field(
        description=(
            "Ana özet. Kapak yazısı için 3-4 paragraf (~300 kelime), "
            "kısa yazı için 2 paragraf (~130 kelime). Paragraflar boş satırla ayrılır. "
            "`kod` ve **kalın** kullanılabilir."
        )
    )
    key_points: list[str] = Field(description="2-5 madde; her biri tek cümle, somut")
    why_it_matters: str = Field(description="Bu tekniğin sektörde neden önemli olduğu, 2-3 cümle")
    for_you: str = Field(
        description=(
            "Okuyucunun kendi projelerine ve stack'ine somut bağlantı. "
            "Genel geçer tavsiye değil; hangi projesinde neyi değiştirmesi gerektiği."
        )
    )
    terms: list[TermOut] = Field(description="Özette geçen 2-4 teknik terim")
    tags: list[str] = Field(description="2-4 Türkçe konu etiketi, örn. 'dağıtık sistemler'")
    difficulty: str = Field(description="başlangıç, orta veya ileri")


# --------------------------------------------------------------------------
# Prompt
# --------------------------------------------------------------------------
SYSTEM_PROMPT = f"""\
Sen bir mühendislik gazetesinin editörüsün. İngilizce mühendislik blog
yazılarını Türkçeye özetliyorsun. Tek bir okuyucun var:

{READER_PROFILE}

Kuralların:

1. TERİMLER. Teknik terimlerin İngilizcesini koru, ilk geçtiğinde Türkçesini
   parantez içinde ver: "kuyruk gecikmesi (tail latency)". Uydurma Türkçe
   karşılık icat etme; yerleşmiş bir karşılığı yoksa İngilizcesini bırak.

2. SOMUTLUK. "Performansı iyileştirdiler" yazma; "padding yüzünden hesabın
   %50'si boşa gidiyordu, jagged attention ile bunu kapattılar" yaz. Yazıdaki
   sayıları, isimleri ve takasları (trade-off) koru.

3. DÜRÜSTLÜK. Yazıda olmayan bir şey ekleme. Bir nokta belirsizse belirsiz
   olduğunu söyle. Pazarlama dilini ("devrim niteliğinde", "sorunsuz")
   tekrar etme; ne yaptıklarını sade dille anlat.

4. ÖĞRETME. Okuyucu kod yazmayı biliyor ama büyük ölçek görmedi. Bir kavram
   ilk kez geçiyorsa bir cümlede açıkla, sonra devam et. Ders verme tonu kurma.

5. "SENDE KARŞILIĞI" alanı en önemli kısım. Okuyucunun gerçek projelerine
   (KlioAI mobil uygulaması, Tradebot piyasa verisi platformu, Mobit'teki ERP
   ve doküman arama sistemi, LLM kategorizasyon pipeline'ı) somut bağlantı kur.
   Bağlantı zorlama olmasın; ilgisizse genel bir mühendislik dersi çıkar ama
   yine de uygulanabilir olsun.

6. TON. Kısa cümleler. Gereksiz sıfat yok. Türkçe yazım kurallarına uy.
   Okuyucuya "sen" diye hitap et.

7. UZUNLUK. Sana verilen bölüm tipine ("kapak" veya "kısa") uy.
"""


def _user_prompt(article: Article, slot: str) -> str:
    source = SOURCE_BY_KEY.get(article.source_key)
    focus = source.focus if source else ""
    length = (
        "KAPAK YAZISI — özet 3-4 paragraf olacak (~300 kelime), 4-5 öne çıkan madde."
        if slot == "cover"
        else "KISA YAZI — özet 2 paragraf olacak (~130 kelime), 2-3 öne çıkan madde."
    )
    return (
        f"Bölüm tipi: {length}\n\n"
        f"Kaynak: {article.source_name} ({focus})\n"
        f"Yayın tarihi: {article.date}\n"
        f"Orijinal başlık: {article.title}\n"
        f"URL: {article.url}\n"
        f"Uzunluk: {article.word_count} kelime\n\n"
        "--- MAKALE METNİ ---\n"
        f"{article.text[:MAX_ARTICLE_CHARS]}"
    )


def _client():
    import anthropic

    return anthropic.Anthropic()


def _system_blocks() -> list[dict]:
    # Sistem promptu her istekte aynı — cache'lenir, tekrar tam ücret ödenmez.
    return [
        {
            "type": "text",
            "text": SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }
    ]


# --------------------------------------------------------------------------
# Tek tek özetleme (az sayıda makale / günlük koşu)
# --------------------------------------------------------------------------
def summarize(article: Article, slot: str = "brief", *, client=None) -> dict:
    """Bir makaleyi özetler ve compose.py'nin beklediği taslak sözlüğü döner."""
    if not article.text or article.word_count < 120:
        raise ValueError(f"metin çok kısa, özetlenemez: {article.url}")

    client = client or _client()
    response = client.messages.parse(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=_system_blocks(),
        messages=[{"role": "user", "content": _user_prompt(article, slot)}],
        output_format=SummaryDraft,
    )

    if response.stop_reason == "refusal":
        raise RuntimeError(f"model yanıtı reddetti: {article.url}")

    draft = response.parsed_output
    if draft is None:
        raise RuntimeError(f"şema doğrulanamadı: {article.url}")

    return _to_dict(draft, article, slot)


def _to_dict(draft: SummaryDraft, article: Article, slot: str) -> dict:
    difficulty = draft.difficulty.strip().lower()
    return {
        "url": article.url,
        "slot": slot,
        "title_tr": draft.title_tr.strip(),
        "summary": draft.summary.strip(),
        "key_points": [p.strip() for p in draft.key_points if p.strip()],
        "why_it_matters": draft.why_it_matters.strip(),
        "for_you": draft.for_you.strip(),
        "terms": [t.model_dump() for t in draft.terms],
        "tags": [t.strip() for t in draft.tags if t.strip()],
        "difficulty": difficulty if difficulty in DIFFICULTIES else "orta",
    }


def summarize_many(pairs: list[tuple[Article, str]], *, verbose: bool = True) -> list[dict]:
    """(makale, slot) çiftlerini sırayla özetler. Bir hata tüm koşuyu düşürmez."""
    client = _client()
    out: list[dict] = []
    for i, (article, slot) in enumerate(pairs, 1):
        try:
            out.append(summarize(article, slot, client=client))
            if verbose:
                print(f"  [{i}/{len(pairs)}] ok   {article.title[:60]}")
        except Exception as exc:
            if verbose:
                print(f"  [{i}/{len(pairs)}] HATA {type(exc).__name__}: {exc}")
    return out


# --------------------------------------------------------------------------
# Toplu özetleme (Batch API) — yarı fiyat, saatler içinde döner
# --------------------------------------------------------------------------
def submit_batch(pairs: list[tuple[Article, str]]) -> str:
    """Batch işi açar ve batch id döner. Arşiv doldurmak için ideal."""
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    client = _client()
    requests = [
        Request(
            custom_id=f"{article.id}-{slot}",
            params=MessageCreateParamsNonStreaming(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                system=_system_blocks(),
                messages=[{"role": "user", "content": _user_prompt(article, slot)}],
                output_config={
                    "format": {
                        "type": "json_schema",
                        "schema": SummaryDraft.model_json_schema(),
                    }
                },
            ),
        )
        for article, slot in pairs
    ]
    batch = client.messages.batches.create(requests=requests)
    print(f"batch açıldı: {batch.id} ({len(requests)} istek) — durum: {batch.processing_status}")
    return batch.id


def collect_batch(batch_id: str, pairs: list[tuple[Article, str]], *, poll: int = 60) -> list[dict]:
    """Batch bitene kadar bekler, sonuçları taslak sözlüklerine çevirir."""
    client = _client()
    index = {f"{a.id}-{s}": (a, s) for a, s in pairs}

    while True:
        batch = client.messages.batches.retrieve(batch_id)
        if batch.processing_status == "ended":
            break
        print(f"  bekleniyor… {batch.request_counts.processing} işlemde")
        time.sleep(poll)

    out: list[dict] = []
    for result in client.messages.batches.results(batch_id):
        if result.result.type != "succeeded":
            print(f"  ! {result.custom_id}: {result.result.type}")
            continue
        article, slot = index[result.custom_id]
        text = next(b.text for b in result.result.message.content if b.type == "text")
        out.append(_to_dict(SummaryDraft(**json.loads(text)), article, slot))
    return out


def save_drafts(drafts: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(drafts, ensure_ascii=False, indent=2), encoding="utf-8")


DRAFTS_PATH = ROOT / ".cache" / "drafts.json"
