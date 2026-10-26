"""22 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-22"

INTRO = "İki yazı da aynı tema: tekrar eden işi bir kez yap ve sakla. Uber, modelin eğitimde gördüğü özelliklerle üretimde gördüklerinin farklı çıktığı sinsi hatayı, özellikleri inference anında loglayarak çözüyor. OpenAI ise prompt cache’i için pratik bir kullanım kılavuzu yayımlamış."

DRAFTS = [
    {
        "url": "https://www.uber.com/blog/taming-ml-firehose/",
        "slot": "cover",
        "title_tr": "Eğitimde gördüğünü üretimde görmemek: Uber’in özellik loglama çerçevesi",
        "difficulty": "ileri",
        "tags": [
            "ML infrastructure",
            "data engineering",
            "Flink",
            "training-serving skew"
        ],
        "summary": "Uber'in hedefi net: **inference anında kullanılan özellikler, bir sonraki model yinelemesini eğitirken kullanılan özelliklerle aynı olsun.** Tek doğruluk kaynağı, daha güçlü model performansı ve sorunların daha hızlı tespiti demek.\n\nProblem sinsi: çevrimiçi ve çevrimdışı hatlar özellikleri farklı hesaplayıp tüketebiliyor. Model eğitimde sabit bir sözlükten öğreniyor (örneğin dil kodları `en-US`, `fr-FR`), ama servis anında aynı özellik `en` olarak gelebiliyor. Çevrimdışı hat da biçim farkı üretebiliyor (`jp_JA` ile `jp-JA`). Sonuç: model, servis sırasında hiç görünmeyen kategorilerden öğrenmiş oluyor ve güçlü sinyaller **sessizce** bozuluyor. Dağılımlar kayıyor, tahmin kararlılığı düşüyor ve görünür hiçbir hata yok. Ek sorunlar: birbirine bağımlı ETL işlerinden oluşan kırılgan veri hatları (eksik bölümler, sessizce bozulan eğitim verisi), çok günlük tazelik gecikmeleri ve geliştiricilerin sorunları anlamak için haftalar harcaması.\n\nÇözüm **özellik loglama**: inference anında modele giden gerçek özellikleri kaydedip eğitimde onları kullanmak. Ölçek ise başlı başına sorun. Transformer tabanlı öneri sistemleri saniyede 8 milyon sorguya ulaşıyor; her tahminin özelliklerini loglamak günde yüz milyarlarca kayıt, ayda 5 trilyon satır ve günde yaklaşık 1,7 PB demek. Restoran öneri modeli için tüm özellikleri yollamak saniyede yaklaşık 9,3 GiB ve mevcut Kafka kümelerinin çok üstünde.\n\nÇevrimiçi mimarideki çözümler: **özellik allowlist** (modelin kullanmadığı özellikleri loglamamak) yük boyutunu 4-5 kat düşürüyor; **özellik adı takma adları**: uzun adlar (`store_unique_identifier_operational_meal_period_context_key`) serileştirmede kompakt tamsayı kimliklere çevriliyor; **gösterim filtreleme**: sıralamaya giren adayların yalnızca yaklaşık %40'ı filtre sonrası kalıyor ve onların da yalnızca %5'i gerçekten gösterime dönüşüyor, o yüzden Flink'te tahminler istemci olaylarıyla zaman pencereli olarak birleştirilip yalnızca gerçekten gösterilenler tutuluyor.\n\nFlink işini ölçeklemek de öğreticiydi. Paralelliği körü körüne artırmak işe yaramadı: her operatör ayrı profillendi ve birleştirme öncesi operatörlere 512, birleştirmeye 768 paralellik (Uber'in en büyük Flink dağıtımı) verildi. Varsayılan RocksDB kontrol noktası saatte 12 TB'ı aşarak bulut yazmalarını başarısız kıldı; çözüm özel durum yönetimi: yalnızca gerekli metadata'yı tutmak, birleştirmeden hemen sonra kayıtları atmak ve tekrarları silmek. Nesne yeniden kullanımı, tipli yükler, yapılandırma cache’i ve daha az serileştirme gibi küçük iyileştirmeler tepe consumer gecikmesini yaklaşık %70 düşürdü.",
        "key_points": [
            "Training-serving skew hata vermez, sessizce kaliteyi düşürür; bu yüzden en tehlikeli ML hatalarından.",
            "Tek doğruluk kaynağı: eğitimde, servisin gördüğü özellikleri kullan.",
            "Her veriyi loglama: modelin kullandığı özellikler ve gerçekten gösterilen adaylar yeterli.",
            "Uzun metin adları yerine tamsayı kimlik: milyarlarca kez gönderilen şeyde bayt başına maliyet çarpılır.",
            "Paralellik artırmak yetmez; her operatörü ayrı profillendir. Varsayılan kontrol noktası stratejisi ölçekte patlayabilir."
        ],
        "why_it_matters": "ML sistemlerinin üretimde en sık kırıldığı yer model değil, modelin besleme hattıdır. Hata genelde ‘kod çalışıyor ama değerler farklı’ biçiminde gelir ve aylarca fark edilmez. Çözüm, eğitim verisini servisten elde etmek: iki ayrı hesaplamayı birbirine denk tutmaya çalışmak yerine tek hesaplamayı iki yerde kullanmak.",
        "for_you": "Bu, ML sistemlerinin en kritik sorusu: **backtest ya da eğitimde kullandığın feature’lar canlıda hesapladıklarınla birebir aynı mı?** Eğitim için toplu (Pandas) bir kod, canlı için ayrı bir stream kodu yazdıysan, iki kodun farklı yuvarlama, farklı zaman penceresi ya da farklı eksik veri davranışı vardır. Paper/shadow execution’ın değeri de burada: canlıda karar anında hesaplanan feature’ları **logla** ve sonraki eğitimi o log’larla yap. Aynısı kategori kodlayan her LLM hattında geçerli: eğitimde gördüğün `'Fuel'` ile production’da gelen `'fuel '` farklı kategoridir; girdileri normalize edip şemayla doğrula.",
        "terms": [
            {
                "en": "training-serving skew",
                "tr": "training-serving skew",
                "definition": "Modelin eğitimde gördüğü özelliklerle üretimde gördüklerinin farklı hesaplanması; sessiz kalite kaybına yol açar."
            },
            {
                "en": "feature store",
                "tr": "feature store",
                "definition": "Model özelliklerinin tutarlı biçimde saklandığı ve hem eğitime hem servise sunulduğu merkezî katman."
            },
            {
                "en": "allow list",
                "tr": "allow list",
                "definition": "Yalnızca açıkça listelenen öğelerin kabul edildiği filtreleme yaklaşımı."
            },
            {
                "en": "windowed join",
                "tr": "windowed join",
                "definition": "Akış verilerini, belirli bir zaman penceresi içinde gelen karşılıklarıyla eşleştirme."
            }
        ]
    },
    {
        "url": "https://openai.com/index/better-prompt-caching-for-gpt-6",
        "slot": "brief",
        "title_tr": "Cache’i bozmadan reasoning effort’u değiştirmek: GPT-6 için prompt cache kılavuzu",
        "difficulty": "orta",
        "tags": [
            "prompt caching",
            "cost",
            "agent",
            "LLM"
        ],
        "summary": "Kalıcı agent'lar saatlerce çalışırken art arda API istekleri atıyor ve her istek öncekilerin talimatını, araç tanımlarını ve bağlamını taşıyor. OpenAI bu ortak bağlamı cache’e alıp hesabı yeniden kullanıyor: yanıt süresi düşüyor, cache’ten gelen girdi token'larında **%90'a kadar indirim** var. GPT-6 ailesiyle birlikte cache sistemi iyileştirildi: uygun ortak önekler **30 dakikalık pencerede** yeniden kullanıldığında indirim veriliyor.\n\nYeni araçlar pratik: bir **kontrol paneli** cache’ten gelen girdi oranını zaman içinde gösteriyor, bir **teşhis aracı** beklenmedik bir kaçırmada isteği son yanıtla karşılaştırıp model, araç, ayar ya da girdideki hangi değişikliğin yeniden kullanımı engellediğini söylüyor. Ayrıca açık **cache kesme noktaları**, cache’e alınacak öneki sen seçiyorsun.\n\nİlginç kısım cache’i korumak için verilen kurallar: (1) reasoning effort’u yanıtlar arasında **`configuration_update` ekleyerek** değiştir, istek düzeyindeki ayarı değil; (2) araç tanımlarını ve sıralarını sabit tut, araç kaldırmak yerine `allowed_tools` ile yalnızca ilgilileri çağrılabilir yap ya da araç gerekmiyorsa `tool_choice: none` kullan; (3) yeni talimatları bağlamın sonuna yeni geliştirici mesajı olarak ekle; (4) bilinen bağlamı açılışta **önceden ısıt** (prewarm), böylece işlem kullanıcının bekleme süresinin dışına çıkar.",
        "key_points": [
            "Cache bir önek eşleşmesidir: önekte olan her değişiklik sonrasındaki her şeyi geçersiz kılar.",
            "Sabit olması gerekenler: araç tanımları, şemalar, sıralama. Değişken olanlar sona eklenir.",
            "Değişimi ‘kaldır’ yerine ‘gizle’ ile yap (`allowed_tools`): tanım yerinde kalır.",
            "Cache kaçırmalarını görünür kılmak (panel, teşhis) optimizasyonun ön koşulu."
        ],
        "for_you": "Bu, Anthropic ve OpenAI için ortak bir kural olduğundan öğrenmeye değer: system prompt’u ve tool listesini **sabit tut**, tarih ya da kullanıcı adı gibi değişkenleri prompt’un başına koyma, sona koy. Kullanıcı adını system prompt’un içine enjekte ediyorsan, her kullanıcı için ayrı bir cache girdisi yaratıyorsun; adı kullanıcı mesajına taşırsan ortak prefix tüm kullanıcılar için paylaşılır. API cevabındaki `cache_read_input_tokens` gibi alanlara bak: sıfırsa cache’in çalışmıyor.",
        "terms": [
            {
                "en": "prompt caching",
                "tr": "prompt caching",
                "definition": "Tekrar eden prompt önekini yeniden işlemek yerine cache’ten okuyarak maliyet ve gecikmeyi düşürme."
            },
            {
                "en": "cache breakpoint",
                "tr": "cache breakpoint",
                "definition": "Promptun hangi noktaya kadarının cache’e alınacağını belirten işaret."
            },
            {
                "en": "prewarming",
                "tr": "prewarming",
                "definition": "Bilinen bağlamı kullanıcı isteği gelmeden önce işleyip cache’e koyma."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
