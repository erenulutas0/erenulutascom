"""23 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-23"

INTRO = "Günün kapağı cache üzerine ve backend mühendisliğinin en temel meselelerinden birine dokunuyor: yanlış bir HTTP başlığı yüzünden cache’e girmesi gereken içeriğin her seferinde origin'e gitmesi. Yazı sıkıcı görünüyor ama okuduktan sonra kendi API'nin başlıklarına bir daha bakacaksın."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/introducing-cache-response-rules/",
        "slot": "cover",
        "title_tr": "Bir Set-Cookie başlığı cache’ini nasıl mahveder",
        "difficulty": "orta",
        "tags": [
            "caching",
            "HTTP",
            "performance",
            "CDN"
        ],
        "summary": "Cloudflare yeni bir kural tipi duyuruyor: origin sunucusu cevap verdikten **sonra**, ama Cloudflare içeriği cache’e almadan **önce** çalışan kurallar. Ürün duyurusu ama içindeki HTTP cache anlatımı başlı başına iyi bir ders.\n\nFoundation model şu: CDN cache’i ile origin sunucu bir çift olarak çalışır. Amaç mümkün olan her yerde cache’ten cevap vermek ve yalnızca uç (edge) cevap veremediğinde origin'e gitmek. Cache hit ratio’daki (**cache hit ratio**) her puan, bu iş bölümünü doğru kurmaktan geliyor. Gereksiz yere cache’e bakarsan zaten ıskalayacak bir arama boşa gider; çok az bakarsan uç katmanın emmesi gereken trafiği origin karşılar ve performans kazancı buharlaşır.\n\nKritik nokta: **origin, cache’i yönlendirir.** Önbelleklenebilir bir varlık döndürdüğünde, cevap başlıkları Cloudflare'e ne kadar süre sunabileceğini, ne zaman ve nasıl yeniden doğrulayacağını, hatta cache’e alınıp alınmayacağını söyler. Cache ancak origin'i kadar verimlidir.\n\nYazının çözdüğü problem tam da burada: çoğu cache uygunluk sorunu istek anında değil, **origin cevap verdikten sonra** ortaya çıkar. Klasik senaryo: ziyaretçi `/static/app.js` ister, cache ıskalar, istek origin'e gider ve origin dosyayı döndürürken cevap başlıklarının arasına sessizce bir `Set-Cookie` sıkışır. Her uç noktada cache’lenmesi gereken varlık, artık cache’lenemez hâle gelir.",
        "key_points": [
            "Aynı problemin varyasyonları çok: origin güvenle cache’lenebilecek varlıklara `Cache-Control: no-cache` gönderir, ya da tarayıcı için doğru olan direktifleri CDN'e de yollar.",
            "Bu başlıkları origin'in kendisinde temizlemek çoğu zaman zor, bazen imkânsız — araya giren bir katman gerekiyor.",
            "Yeni kurallar tam doğru anda çalışıyor: origin cevabından sonra, cache’e yazmadan önce."
        ],
        "why_it_matters": "Cache hit ratio, bir web sisteminin en yüksek kaldıraçlı metriklerinden biri: %70'ten %90'a çıkmak origin trafiğini üçte birine indirir. Ve bu oranı bozan şey genelde büyük bir mimari hata değil, yanlışlıkla eklenmiş tek bir başlıktır. Küçük detayların büyük sistemleri belirlemesine iyi bir örnek.",
        "for_you": "Bunu bugün kendi projende kontrol edebilirsin. Session yönetimi açıksa, statik kaynak isteklerine bile `Set-Cookie` eklenmesi çok yaygın bir hatadır. Sonuç: CDN hiçbir şeyi cache’lemez ve sebebini aylarca bulamazsın. Kontrol basit: `curl -I https://siten/static/app.js` çalıştır ve cevap header’larına bak. `Set-Cookie` görüyorsan sorun var. API’nde de aynısını yap: `Cache-Control` header’larını bilinçli ayarla; değişmeyen varlıklara uzun `max-age`, kullanıcıya özel cevaplara `private, no-store`. Bu ayrımı yapmamak ya performans ya da güvenlik kaybettirir.",
        "terms": [
            {
                "en": "cache hit ratio",
                "tr": "cache hit ratio",
                "definition": "Toplam isteklerin yüzde kaçının cache’ten karşılandığı; CDN verimliliğinin ana ölçüsü."
            },
            {
                "en": "origin server",
                "tr": "origin server",
                "definition": "İçeriğin asıl üretildiği sunucu; CDN cache’leyemediğinde isteği buraya iletir."
            },
            {
                "en": "Cache-Control",
                "tr": "Cache-Control",
                "definition": "Bir cevabın ne kadar süre, kim tarafından ve nasıl cache’lenebileceğini belirten HTTP başlığı."
            },
            {
                "en": "revalidation",
                "tr": "revalidation",
                "definition": "Cache’teki kopyanın hâlâ güncel olup olmadığını origin'e sorup, güncelse tam içeriği indirmeden kullanma."
            }
        ]
    },
    {
        "url": "https://openai.com/index/health-in-chatgpt",
        "slot": "brief",
        "title_tr": "Sağlık verisini bir LLM'e bağlamak: izin, kapsam ve sınırlar",
        "difficulty": "başlangıç",
        "tags": [
            "privacy",
            "LLM",
            "product",
            "data governance"
        ],
        "summary": "ChatGPT'ye ABD'de sağlık özelliği geliyor: kullanıcı isterse Apple Health'i ve desteklenen tıbbi kayıtları güvenli biçimde bağlayabiliyor. OpenAI'ın verdiği rakama göre haftada 300 milyondan fazla kişi ChatGPT'ye sağlıkla ilgili soru soruyor — ama o soruların arkasındaki bağlam hasta portalları, tıbbi kayıtlar, uygulamalar ve giyilebilir cihazlar arasına dağılmış durumda.\n\nMühendislik açısından ilgi çekici kısım gizlilik tasarımı. Bağlanan tıbbi kayıtlar, Apple Health bilgileri ve bunları kullanan konuşmalar **foundation model’leri eğitmek için kullanılmıyor** ve reklam hedeflemede yer almıyor. Kullanıcı neyi bağlayacağına ve ChatGPT'nin bunu ne zaman kullanabileceğine kendisi karar veriyor.",
        "key_points": [
            "Hassas veriyi bir ürüne bağlarken üç ayrı karar var: ne toplanır, ne zaman kullanılır, ve eğitimde kullanılır mı. Üçü birbirinden bağımsız.",
            "Model tarafında hedef, karmaşık detaylar arasında daha dikkatli akıl yürütmek ve **eksik bağlamı sormak** — belirsizliği fark edip soru sormak, uydurmaktan iyidir."
        ],
        "for_you": "Kullanıcı ses kaydı ya da kişisel veri tutan bir uygulamada hassaslık derecesi farklı ama sorular aynı. Bu yazıyı bir kontrol listesi olarak kullan: **(1)** Kullanıcı hangi verinin tutulduğunu açıkça biliyor mu? **(2)** Veriyi model iyileştirmesi için kullanıyorsan bu ayrı bir izin mi? **(3)** Kullanıcı sildiğinde gerçekten siliniyor mu, yoksa backup’larda kalıyor mu? Bunlar hukuk sorusu gibi görünür ama aslında mimari sorulardır; sonradan eklemek baştan tasarlamaktan kat kat pahalıdır.",
        "terms": [
            {
                "en": "data governance",
                "tr": "data governance",
                "definition": "Verinin kim tarafından, hangi amaçla, ne kadar süre kullanılabileceğini belirleyen kurallar bütünü."
            },
            {
                "en": "opt-in",
                "tr": "opt-in",
                "definition": "Bir özelliğin varsayılan olarak kapalı olması ve ancak kullanıcı açıkça izin verdiğinde çalışması."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
