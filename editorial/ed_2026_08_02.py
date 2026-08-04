"""2 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-02"

INTRO = (
    "Bugün tek yayın çıktı — Cloudflare'in \"Agents Week\" açılışı. Yazının kendisi "
    "kısa ama sorduğu soru iyi: bulut insanlar için tasarlandı, peki yazılım "
    "ajanları için tasarlansaydı neye benzerdi? Bu soruyu ciddiye almak için "
    "arşivden iki yazı ekledim: biri agent mimarisinin temel desenleri, diğeri "
    "de \"ölçekte ne kırılır\" sorusunun çok somut bir cevabı."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/agents-week-welcome/",
        "slot": "cover",
        "title_tr": "\"Agent Cloud\" nedir? Cloudflare'in sorduğu soru",
        "difficulty": "başlangıç",
        "tags": ["agent", "bulut", "mimari"],
        "summary": (
            "Cloudflare bir haftalık duyuru serisi açıyor ve açılış yazısı teknik "
            "değil, kavramsal. Sordukları soru şu: bugünkü bulut ve üstündeki web, "
            "**insanlar** için tasarlandı. Her katman ekranın başında bir insan "
            "olduğunu varsayıyor — dikkat çekmek için tasarlanmış sayfalar, "
            "tıklanacak panolar, insan okuma hızına göre ayarlanmış arayüzler.\n\n"
            "Yazılım ajanları böyle çalışmıyor. Dikkatleri dağılmıyor, yorulmuyor; "
            "buna karşılık hız, yapı ve erişim konusunda kendi ihtiyaçları var. "
            "Cloudflare'in iddiası bir \"Agent Cloud\"un iki işi aynı anda yapması "
            "gerektiği: ajanlar için sıfırdan tasarlanmış temel yapıtaşları sunmak, "
            "ve bu arada bugünkü insan-şekilli web ile ajan-şekilli web arasında "
            "bir **çeviri katmanı** olarak durmak."
        ),
        "key_points": [
            "Bugünkü web'in her katmanı \"karşıda bir insan var\" varsayımıyla tasarlandı; "
            "ajanlar bu varsayımı bozuyor.",
            "İki ayrı ihtiyaç var: ajan-yerel (agent-native) yeni yapıtaşları, ve mevcut "
            "web'i ajanlara çevirecek bir ara katman.",
            "Yazının kendisi bir duyuru değil, çerçeve kurma denemesi — asıl teknik "
            "içerik haftanın geri kalanında geliyor.",
        ],
        "why_it_matters": (
            "Bu tür \"çerçeve kurma\" yazıları genelde pazarlama olur, ama buradaki "
            "gözlem gerçek bir mühendislik sorusuna işaret ediyor: bir API'yi insan "
            "geliştiriciler mi yoksa bir LLM mi tüketecek, tasarımı değiştirir. "
            "Hata mesajları, sayfalama, kimlik doğrulama akışları, dokümantasyon "
            "biçimi — hepsi tüketicinin insan olup olmamasına göre farklılaşır."
        ),
        "for_you": (
            "Bunu somut bir tasarım kontrolüne çevir: Mobit'teki doküman arama "
            "API'sini bir LLM çağıracaksa, dönen hata mesajı \"400 Bad Request\" "
            "değil \"tarih formatı YYYY-MM-DD olmalı, sen 12/03/2026 gönderdin\" "
            "olmalı — çünkü modelin kendini düzeltmesi için okunabilir bir sinyal "
            "gerekiyor. Aynı şekilde sayfalama: insan \"sonraki sayfa\" düğmesine "
            "basar, ajan ise toplam sayıyı ve kalanı bilmek ister. Bu küçük "
            "kararlar, LLM tabanlı bir istemcinin çalışıp çalışmamasını belirliyor."
        ),
        "terms": [
            {
                "en": "agent",
                "tr": "yazılım ajanı",
                "definition": "Bir hedefi verilen, hangi araçları hangi sırayla çağıracağına kendisi karar veren LLM tabanlı program.",
            },
            {
                "en": "primitive",
                "tr": "temel yapıtaşı",
                "definition": "Bir platformun sunduğu en küçük yapı birimi (kuyruk, nesne deposu, çalıştırma birimi gibi).",
            },
        ],
    },
    {
        "url": "https://www.anthropic.com/engineering/building-effective-agents",
        "slot": "archive",
        "title_tr": "Etkili agent kurmanın sırrı: framework değil, basit desenler",
        "difficulty": "orta",
        "tags": ["agent", "LLM", "mimari", "tasarım"],
        "summary": (
            "Anthropic onlarca ekiple LLM tabanlı agent kuruldu ve şu sonuca varmış: "
            "en başarılı uygulamalar karmaşık framework'ler kullanmıyordu, basit ve "
            "birleştirilebilir desenler kullanıyordu.\n\n"
            "Yazının en değerli kısmı bir ayrım: **workflow** (iş akışı) ile **agent** "
            "aynı şey değil. Workflow'da adımlar önceden kodla tanımlanır; agent'ta "
            "hangi aracı ne zaman kullanacağına modelin kendisi karar verir. "
            "Workflow öngörülebilir ve tutarlıdır, iyi tanımlanmış görevler için "
            "doğru seçimdir. Agent ise esneklik ve ölçekte model-güdümlü karar "
            "gerektiğinde kazanır. Anthropic'in tavsiyesi net: en basit çözümle "
            "başla, ancak gerektiğinde karmaşıklığı artır — çoğu uygulama için "
            "tek bir LLM çağrısını retrieval ve örneklerle güçlendirmek zaten yeterli."
        ),
        "key_points": [
            "Agent sistemleri gecikme ve maliyeti, görev başarısıyla takas eder. "
            "Bu takasın ne zaman mantıklı olduğunu bilerek karar ver.",
            "Framework'ler başlangıcı kolaylaştırır ama araya soyutlama katmanı koyar; "
            "altındaki prompt'u ve çağrıları göremezsen hata ayıklamak zorlaşır.",
            "Tavsiye: doğrudan LLM API'siyle başla. Çoğu desen birkaç satır kod.",
            "Temel yapıtaşı \"güçlendirilmiş LLM\": retrieval + araçlar + hafıza eklenmiş bir model.",
        ],
        "why_it_matters": (
            "Sektörde agent framework'leri hızla çoğalıyor ve varsayılan refleks "
            "\"önce bir framework seç\" oluyor. Bu yazı tersini söylüyor: "
            "karmaşıklık ancak kazandırdığında eklenmeli. Bu, sadece agent'lar için "
            "değil genel mühendislik disiplini için de doğru bir refleks."
        ),
        "for_you": (
            "Sen zaten 10.000+ kaydı işleyen bir LLM kategorizasyon pipeline'ı "
            "yazdın — bu yazının tanımıyla o bir *workflow*, agent değil, ve doğrusu "
            "da o. Bunu mülakatta böyle anlatabilmen değerli: \"kategorizasyon "
            "adımları sabit olduğu için agent kurmadım, deterministik bir pipeline "
            "yazdım; model kararı sadece sınıflandırma noktasında devreye giriyor.\" "
            "Mobit'teki doküman aramada ise agent mantıklı olabilir, çünkü "
            "hangi belgeye bakılacağı sorudan soruya değişiyor. Ayrımı bilerek "
            "seçmek, ikisini de körlemesine kullanmaktan iyi."
        ),
        "terms": [
            {
                "en": "workflow",
                "tr": "iş akışı",
                "definition": "Adımların ve sıralarının önceden kodla belirlendiği sistem; model sadece belirli noktalarda karar verir.",
            },
            {
                "en": "agentic system",
                "tr": "ajanik sistem",
                "definition": "Modelin araç seçimini ve sırasını kendi belirlediği sistem; esnek ama daha az öngörülebilir.",
            },
            {
                "en": "augmented LLM",
                "tr": "güçlendirilmiş LLM",
                "definition": "Retrieval, araç kullanımı ve hafıza yetenekleriyle desteklenmiş dil modeli — agent mimarilerinin temel birimi.",
            },
        ],
    },
    {
        "url": "https://www.uber.com/blog/from-static-rate-limiting-to-intelligent-load-management/",
        "slot": "archive",
        "title_tr": "Uber veritabanı çökmesini nasıl durdurdu: sabit kotadan akıllı yük yönetimine",
        "difficulty": "ileri",
        "tags": ["veritabanı", "dağıtık sistemler", "rate limiting", "dayanıklılık"],
        "summary": (
            "Uber'in binlerce mikroservisi 170 milyondan fazla aylık aktif kullanıcıya "
            "hizmet veriyor. Altta Docstore ve Schemaless var: MySQL üzerine kurulmuş, "
            "binlerce küme, onlarca petabyte veri, saniyede on milyonlarca istek.\n\n"
            "Bu ölçekte küçük aşırı yüklenmeler izole kalmıyor, **çığ etkisi** "
            "yaratıyor: bir yerdeki kısa ani yük aşağı akıştaki servislerin zaman "
            "aşımına uğramasına, yeniden denemelerin (retry) birikmesine ve bozulmanın "
            "büyüyerek genel bir arızaya dönüşmesine yol açıyor.\n\n"
            "İlk denedikleri çözüm klasik: sorgu motoru katmanında kota tabanlı "
            "rate limiting. Her isteğe işlenen bayta göre bir maliyet ver, kullanıcılara "
            "sabit kota tanı, aşınca 429 dön. Ama işe yaramamış. Sebebi öğretici: "
            "her istek için Redis'e gitmek gerekiyordu — yani yeni bir hata noktası "
            "ve fazladan bir ağ turu. Yükü korumak için eklenen mekanizmanın kendisi "
            "yük ve kırılganlık üretiyordu."
        ),
        "key_points": [
            "Çok kiracılı (multitenant) bir sistemde tek bir kiracının tüm kaynağı "
            "yutmasını engellemek, korumanın yarısı kadar önemli.",
            "Statik kota işe yaramıyor çünkü iş yükleri trafik şekli, gecikme profili "
            "ve sistem etkisi bakımından birbirine benzemiyor.",
            "Mimari üç katman: durumsuz sorgu motoru (yönlendirme, şema, yetkilendirme), "
            "durumlu depolama motoru (işlem, replikasyon), ve Raft ile koordine edilen "
            "1 lider + 2 takipçi bölümler.",
            "Çözüm tek bir sinyale değil, birden fazla sinyalden aşırı yükü tespit eden "
            "bir yük yöneticisine dayanıyor.",
        ],
        "why_it_matters": (
            "\"Korumak için eklediğin mekanizma yeni bir kırılma noktası yaratıyor mu?\" "
            "sorusu, dağıtık sistemlerin en tekrarlayan tuzağı. Redis'e giden bir "
            "rate limiter, Redis düştüğünde tüm trafiği durdurur — koruduğu şeyden "
            "daha kırılgandır. Bu yazı o dersi çok net bir vakayla veriyor."
        ),
        "for_you": (
            "Tradebot'ta piyasa verisi çekerken rate limit mantığını mutlaka "
            "kurmuşsundur; oradaki tasarımı bu gözle bir daha bak. Redis'i "
            "sayaç olarak kullanıyorsan Redis düştüğünde ne oluyor — istekler "
            "geçiyor mu (fail-open) yoksa duruyor mu (fail-closed)? İkisi de "
            "geçerli bir karar ama **bilinçli** verilmiş olmalı. Ayrıca yerel "
            "bir token bucket (in-process) ile merkezî sayacı birleştirmek, "
            "her istekte ağ turu ödemekten çok daha ucuz — Uber'in tam da "
            "kaçındığı maliyet bu."
        ),
        "terms": [
            {
                "en": "cascading failure",
                "tr": "çığ etkisiyle arıza",
                "definition": "Bir bileşendeki küçük bir sorunun, yeniden denemeler ve zaman aşımlarıyla büyüyerek tüm sistemi düşürmesi.",
            },
            {
                "en": "multitenant",
                "tr": "çok kiracılı",
                "definition": "Aynı altyapıyı birden fazla bağımsız kullanıcının/servisin paylaşması; adil kaynak paylaşımı gerektirir.",
            },
            {
                "en": "Raft",
                "tr": "Raft uzlaşı algoritması",
                "definition": "Bir lider ve takipçiler arasında verinin tutarlı kopyalanmasını sağlayan uzlaşı (consensus) protokolü.",
            },
            {
                "en": "rate limiting",
                "tr": "istek hız sınırlama",
                "definition": "Belirli bir sürede kabul edilecek istek sayısını sınırlayarak sistemi aşırı yüklenmeden koruma tekniği.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
