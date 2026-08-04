"""23 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-23"

INTRO = (
    "Günün kapağı önbellek üzerine ve backend mühendisliğinin en temel "
    "meselelerinden birine dokunuyor: yanlış bir HTTP başlığı yüzünden "
    "önbelleğe girmesi gereken içeriğin her seferinde origin'e gitmesi. "
    "Yazı sıkıcı görünüyor ama okuduktan sonra kendi API'nin başlıklarına "
    "bir daha bakacaksın."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/introducing-cache-response-rules/",
        "slot": "cover",
        "title_tr": "Bir Set-Cookie başlığı önbelleğini nasıl mahveder",
        "difficulty": "orta",
        "tags": ["önbellek", "HTTP", "performans", "CDN"],
        "summary": (
            "Cloudflare yeni bir kural tipi duyuruyor: origin sunucusu cevap "
            "verdikten **sonra**, ama Cloudflare içeriği önbelleğe almadan **önce** "
            "çalışan kurallar. Ürün duyurusu ama içindeki HTTP önbellek anlatımı "
            "başlı başına iyi bir ders.\n\n"
            "Temel model şu: CDN önbelleği ile origin sunucu bir çift olarak "
            "çalışır. Amaç mümkün olan her yerde önbellekten cevap vermek ve "
            "yalnızca uç (edge) cevap veremediğinde origin'e gitmek. Önbellek "
            "isabet oranındaki (**cache hit ratio**) her puan, bu iş bölümünü "
            "doğru kurmaktan geliyor. Gereksiz yere önbelleğe bakarsan zaten "
            "ıskalayacak bir arama boşa gider; çok az bakarsan uç katmanın "
            "emmesi gereken trafiği origin karşılar ve performans kazancı buharlaşır.\n\n"
            "Kritik nokta: **origin, önbelleği yönlendirir.** Önbelleklenebilir "
            "bir varlık döndürdüğünde, cevap başlıkları Cloudflare'e ne kadar süre "
            "sunabileceğini, ne zaman ve nasıl yeniden doğrulayacağını, hatta "
            "önbelleğe alınıp alınmayacağını söyler. Önbellek ancak origin'i kadar "
            "verimlidir.\n\n"
            "Yazının çözdüğü problem tam da burada: çoğu önbellek uygunluk sorunu "
            "istek anında değil, **origin cevap verdikten sonra** ortaya çıkar. "
            "Klasik senaryo: ziyaretçi `/static/app.js` ister, önbellek ıskalar, "
            "istek origin'e gider ve origin dosyayı döndürürken cevap başlıklarının "
            "arasına sessizce bir `Set-Cookie` sıkışır. Her uç noktada "
            "önbelleklenmesi gereken varlık, artık önbelleklenemez hâle gelir."
        ),
        "key_points": [
            "Aynı problemin varyasyonları çok: origin güvenle önbelleklenebilecek "
            "varlıklara `Cache-Control: no-cache` gönderir, ya da tarayıcı için "
            "doğru olan direktifleri CDN'e de yollar.",
            "Bu başlıkları origin'in kendisinde temizlemek çoğu zaman zor, bazen "
            "imkânsız — araya giren bir katman gerekiyor.",
            "Yeni kurallar tam doğru anda çalışıyor: origin cevabından sonra, "
            "önbelleğe yazmadan önce.",
        ],
        "why_it_matters": (
            "Önbellek isabet oranı, bir web sisteminin en yüksek kaldıraçlı "
            "metriklerinden biri: %70'ten %90'a çıkmak origin trafiğini üçte birine "
            "indirir. Ve bu oranı bozan şey genelde büyük bir mimari hata değil, "
            "yanlışlıkla eklenmiş tek bir başlıktır. Küçük detayların büyük "
            "sistemleri belirlemesine iyi bir örnek."
        ),
        "for_you": (
            "Bunu bugün kendi projende kontrol edebilirsin. Spring Boot'ta "
            "session yönetimi açıksa, statik kaynak isteklerine bile `Set-Cookie` "
            "eklenmesi çok yaygın bir hatadır — sonuç: CDN hiçbir şeyi "
            "önbelleklemez ve sen sebebini aylarca bulamazsın. Kontrolü basit: "
            "`curl -I https://siten/static/app.js` çalıştır ve cevap başlıklarına "
            "bak. `Set-Cookie` görüyorsan sorun var. KlioAI'nın API'sinde de "
            "aynısını yap: `Cache-Control` başlıklarını bilinçli ayarla — "
            "değişmeyen varlıklara uzun `max-age`, kullanıcıya özel cevaplara "
            "`private, no-store`. Bu ayrımı yapmamak, ya performans ya da "
            "güvenlik kaybettirir."
        ),
        "terms": [
            {
                "en": "cache hit ratio",
                "tr": "önbellek isabet oranı",
                "definition": "Toplam isteklerin yüzde kaçının önbellekten karşılandığı; CDN verimliliğinin ana ölçüsü.",
            },
            {
                "en": "origin server",
                "tr": "kaynak sunucu",
                "definition": "İçeriğin asıl üretildiği sunucu; CDN önbellekleyemediğinde isteği buraya iletir.",
            },
            {
                "en": "Cache-Control",
                "tr": "Cache-Control başlığı",
                "definition": "Bir cevabın ne kadar süre, kim tarafından ve nasıl önbelleklenebileceğini belirten HTTP başlığı.",
            },
            {
                "en": "revalidation",
                "tr": "yeniden doğrulama",
                "definition": "Önbellekteki kopyanın hâlâ güncel olup olmadığını origin'e sorup, güncelse tam içeriği indirmeden kullanma.",
            },
        ],
    },
    {
        "url": "https://openai.com/index/health-in-chatgpt",
        "slot": "brief",
        "title_tr": "Sağlık verisini bir LLM'e bağlamak: izin, kapsam ve sınırlar",
        "difficulty": "başlangıç",
        "tags": ["gizlilik", "LLM", "ürün", "veri yönetişimi"],
        "summary": (
            "ChatGPT'ye ABD'de sağlık özelliği geliyor: kullanıcı isterse Apple "
            "Health'i ve desteklenen tıbbi kayıtları güvenli biçimde bağlayabiliyor. "
            "OpenAI'ın verdiği rakama göre haftada 300 milyondan fazla kişi "
            "ChatGPT'ye sağlıkla ilgili soru soruyor — ama o soruların arkasındaki "
            "bağlam hasta portalları, tıbbi kayıtlar, uygulamalar ve giyilebilir "
            "cihazlar arasına dağılmış durumda.\n\n"
            "Mühendislik açısından ilgi çekici kısım gizlilik tasarımı. Bağlanan "
            "tıbbi kayıtlar, Apple Health bilgileri ve bunları kullanan konuşmalar "
            "**temel modelleri eğitmek için kullanılmıyor** ve reklam hedeflemede "
            "yer almıyor. Kullanıcı neyi bağlayacağına ve ChatGPT'nin bunu ne zaman "
            "kullanabileceğine kendisi karar veriyor."
        ),
        "key_points": [
            "Hassas veriyi bir ürüne bağlarken üç ayrı karar var: ne toplanır, "
            "ne zaman kullanılır, ve eğitimde kullanılır mı. Üçü birbirinden bağımsız.",
            "Model tarafında hedef, karmaşık detaylar arasında daha dikkatli akıl "
            "yürütmek ve **eksik bağlamı sormak** — belirsizliği fark edip soru "
            "sormak, uydurmaktan iyidir.",
        ],
        "for_you": (
            "KlioAI'da kullanıcı ses kayıtları tutuyorsun — hassaslık derecesi "
            "farklı ama sorular aynı. Bu yazıyı bir kontrol listesi olarak kullan: "
            "(1) Kullanıcı hangi verinin tutulduğunu açıkça biliyor mu? "
            "(2) Veriyi model iyileştirmesi için kullanıyorsan bu ayrı bir izin mi? "
            "(3) Kullanıcı sildiğinde gerçekten siliniyor mu, yoksa yedeklerde "
            "kalıyor mu? Bunlar hukuk sorusu gibi görünür ama aslında mimari "
            "sorulardır — sonradan eklemek, baştan tasarlamaktan kat kat pahalıdır."
        ),
        "terms": [
            {
                "en": "data governance",
                "tr": "veri yönetişimi",
                "definition": "Verinin kim tarafından, hangi amaçla, ne kadar süre kullanılabileceğini belirleyen kurallar bütünü.",
            },
            {
                "en": "opt-in",
                "tr": "açık rıza",
                "definition": "Bir özelliğin varsayılan olarak kapalı olması ve ancak kullanıcı açıkça izin verdiğinde çalışması.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
