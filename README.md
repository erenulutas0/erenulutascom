# erenulutas.com — Mühendislik Gazetesi

Dünyanın en iyi mühendislik ekiplerinin blog yazılarını her gün derleyip
Türkçe özetleyen kişisel bir gazete. Özetler yeni mezun bir mühendisin
anlayacağı dilde yazılır; teknik terimlerin İngilizcesi korunur.

**Yayın:** https://erenulutas.com

---

## Ne yapıyor?

```
11 kaynak  →  tara  →  gövde metnini çıkar  →  küratörlük  →  özetle  →  statik site
   RSS/HTML     fetch      trafilatura          puanlama      Claude      Jinja2
```

1. **Toplama** — 11 mühendislik blogu taranır. Çoğu RSS veriyor; Uber'in RSS'i yok
   (blog sayfası kazınıyor), Anthropic için `sitemap.xml` kullanılıyor.
2. **Ayıklama** — makalenin gövde metni navigasyon ve footer gürültüsünden temizlenir.
3. **Küratörlük** — her yazı konu sinyalleri ve kaynak ağırlığına göre puanlanır;
   duyuru ve pazarlama yazıları elenir. Günde en fazla 6 yazı sayıya girer.
4. **Özetleme** — seçilenler Türkçeye özetlenir. Her özette *Öne çıkanlar*,
   *Neden önemli?*, *Sende karşılığı* ve bir terim sözlüğü bulunur.
5. **Yayın** — sonuç statik HTML olarak `docs/` altına üretilir, GitHub Pages yayınlar.

### Kaynaklar

| Kaynak | Yöntem |
|---|---|
| Netflix Tech Blog, AWS Architecture, Cloudflare, Stripe, Databricks, Meta, OpenAI, Google Research, Google Cloud, Microsoft Engineering | RSS |
| Anthropic Engineering | `sitemap.xml` (RSS yok) |
| Uber Engineering | HTML kazıma (RSS yok, bot koruması var) |

> Microsoft Engineering ve Anthropic Engineering seyrek yazıyor. Bir gün az yayın
> çıktığında sayı **"Arşivden Seçmeler"** ile takviye edilir; bu yazıların gerçek
> yayın tarihi başlığın üstünde açıkça görünür.

---

## Kurulum

```bash
python -m venv .venv && .venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

Özetleme için API anahtarı gerekir (`build`, `check` ve `serve` için gerekmez):

```bash
setx ANTHROPIC_API_KEY "sk-ant-..."
```

## Komutlar

```bash
python -m pipeline.cli fetch                 # kaynakları tara, metinleri çıkar
python -m pipeline.cli candidates            # günün adaylarını puanı ve metniyle bas
python -m pipeline.cli build                 # docs/ statik sitesini üret
python -m pipeline.cli check                 # içerik tutarlılık denetimi
python -m pipeline.cli serve                 # http://localhost:4173 önizleme
```

Otomatik özetleme (yalnızca bunlar `ANTHROPIC_API_KEY` ister):

```bash
python -m pipeline.cli daily                 # bugünün sayısını Claude ile üret
python -m pipeline.cli backfill --days 30    # geçmişi doldur (Batch API, yarı fiyat)
```

### Günlük akış (editöryel mod — şu an kullanılan)

```bash
python -m pipeline.cli fetch                        # 1. yeni yazıları çek
python -m pipeline.cli candidates                   # 2. adayları oku, kapak/kısa seç
#    3. editorial/ed_YYYY_MM_DD.py dosyasını yaz
python -m editorial.apply                           # 4. content/ altına yaz
python -m pipeline.cli check                        # 5. doğrula
git add content/ editorial/ && git commit -m "içerik: <tarih> sayısı" && git push
#    6. push → "Siteyi yayınla" workflow'u devreye girer, site birkaç dakikada güncellenir
```

`docs/` klasörünü elle commit'lemene gerek yok — GitHub Actions siteyi kendisi
üretiyor. Yerelde bakmak istersen `build` + `serve`.

### Model seçimi ve maliyet

Varsayılan model `claude-opus-5`. Ortam değişkeniyle değiştirilebilir:

```bash
set GAZETE_MODEL=claude-sonnet-5
```

Sistem promptu sabittir ve **prompt cache**'lenir, yani her makalede yeniden tam
ücret ödenmez. Toplu üretimde `--batch` bayrağı **Batch API**'yi kullanır: yarı
fiyat, karşılığında sonuç saatler içinde gelir.

---

## Yeni gün nasıl eklenir?

İki yol var.

**Otomatik (pipeline):** `python -m pipeline.cli daily` — küratörlük ve özetleme
Claude tarafından yapılır, sonuç doğrudan `content/YYYY-MM-DD.json` olur.

**Editöryel (elle):** `editorial/ed_YYYY_MM_DD.py` dosyası açılır, `DRAFTS`
listesine makale URL'leri ve Türkçe özetler yazılır, sonra:

```bash
python -m editorial.apply
```

Teknik meta veriler (başlık, tarih, yazar, okuma süresi, id) makale önbelleğinden
otomatik doldurulur. Arşivdeki 22 sayı bu yolla üretildi.

---

## Yayına alma (GitHub Pages + `erenulutas.com`)

### 1. Depoyu oluştur ve gönder

```bash
git init -b main
git add -A
git commit -m "gazete: ilk sürüm"
git remote add origin https://github.com/erenulutas0/erenulutas.com.git
git push -u origin main
```

### 2. Pages'i aç

Depo → **Settings → Pages → Build and deployment → Source: GitHub Actions**

`deploy.yml` her `content/` değişikliğinde siteyi üretip yayınlar.

### 3. Alan adını bağla

`docs/CNAME` dosyası `erenulutas.com` içeriyor (build her seferinde korur).
Alan adı sağlayıcında şu DNS kayıtlarını gir:

| Tip | Ad | Değer |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `erenulutas0.github.io` |

DNS yayılması 10 dakika–24 saat sürebilir. Sonra Settings → Pages → Custom domain
alanına `erenulutas.com` yaz ve **Enforce HTTPS**'i işaretle.

### 4. Günlük otomasyon (şu an kapalı — bilinçli tercih)

Sayılar **elle** yazılıyor (yukarıdaki editöryel akış). `daily.yml` otomatik
üretimi de destekliyor ama cron'u kapalı ve API anahtarı tanımlı değil.

Bir gün otomatiğe almak istersen:

1. **Settings → Secrets and variables → Actions** → `ANTHROPIC_API_KEY` ekle
   (ya da `gh secret set ANTHROPIC_API_KEY --repo erenulutas0/erenulutascom`)
2. `.github/workflows/daily.yml` içindeki `schedule` bloğunun `#`'lerini kaldır
3. Önce elle dene: **Actions → Günlük sayı → Run workflow**

Otomasyon kapalıyken de workflow zararsız duruyor; hiçbir şey çalıştırmıyor.

---

## Proje yapısı

```
pipeline/
  config.py       kaynak tanımları, site kimliği, okuyucu profili
  fetch.py        RSS / sitemap / HTML adaptörleri
  extract.py      gövde metni ve gerçek başlık çıkarımı
  curate.py       puanlama ve günlük seçim
  summarize.py    Claude ile özetleme (şema zorlamalı, cache'li, Batch destekli)
  compose.py      taslak → doğrulanmış Edition
  models.py       içerik şeması (content/*.json sözleşmesi)
  build.py        Jinja2 → docs/
  cli.py          komut satırı
editorial/        elle yazılmış sayılar (ed_YYYY_MM_DD.py)
templates/        Jinja2 şablonları
static/           CSS ve JS
content/          günlük JSON arşivi ← tek doğruluk kaynağı
docs/             üretilen statik site ← GitHub Pages buradan yayınlar
```

`content/` tek doğruluk kaynağıdır. `docs/` her zaman ondan yeniden üretilebilir;
`docs/` içindeki bir dosyayı elle düzenlemek anlamsızdır, bir sonraki build siler.

---

## Notlar

- Her özetin altında orijinal makalenin linki var; amaç kaynağın yerine geçmek
  değil, ona yönlendirmek.
- Yayın tarihleri gerçektir. "Arşivden Seçmeler" bölümündeki yazılar o güne ait
  değildir ve tarihleri açıkça yazılıdır.
- `pipeline.cli check` her sayıda tam olarak bir kapak olduğunu, zorunlu alanların
  dolu olduğunu, aynı URL'nin iki kez kullanılmadığını ve hiçbir yazının
  bulunduğu sayıdan yeni tarihli olmadığını doğrular. CI'da build'den önce koşar.

## Lisans

Kod MIT. Özetlenen makalelerin telifi orijinal yazarlara aittir.
