"""5 Kasım 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-11-05"

INTRO = (
    "Uber’in yazısı bir ölçek hatırlatması: günde 100 PB okuyup yazan bir Spark filosunda "
    "yüzde birkaçlık verim bile gerçek para demek. Yanında, web siteleri için agent’ların "
    "‘insan mı, makine mi?’ ikilemini kimlik, itibar ve hesap verebilirlik üzerinden ele alan "
    "bir Cloudflare tartışması."
)

DRAFTS = [
    {
        "url": "https://www.uber.com/blog/uber-benchmarking-quanton/",
        "slot": "cover",
        "title_tr": "Her çekirdek işe yarasın: Uber’de Spark’ı Gluten/Velox ve storage-aware engine ile hızlandırmak",
        "difficulty": "ileri",
        "tags": ["Spark", "data engineering", "performance", "cost"],
        "summary": (
            "Uber dünyanın en büyük Apache Spark filolarından birini işletiyor: yalnızca data lake "
            "ingestion 200.000’den fazla CPU çekirdeği tüketiyor, üzerindeki ETL daha da fazlasını. "
            "Spark altyapısı günde 100 PB’tan fazla veri okuyup yazıyor, 80 PB’tan fazla shuffle "
            "verisi taşıyor, günde 500.000’den fazla uygulama ve bir milyondan fazla çekirdek "
            "çalıştırıyor. Bu ölçekte yüzde birkaçlık verim bile gerçek etki; bu yüzden Spark’ı "
            "ucuzlatmak tek seferlik bir proje değil sürekli bir program. İşin büyük kısmı, her "
            "Spark uygulamasının nasıl gönderildiğini, yapılandırıldığını ve yayınlandığını "
            "kontrol eden Spark-as-a-Service platformu **Drogon** üzerinden yürüyor; bu da "
            "filo çapında engine değişikliklerini mümkün kılıyor.\n\n"
            "**Birinci adım: Gluten ve Velox.** Apache Gluten, JVM tabanlı SQL engine’lerinin "
            "çalıştırılmasını Velox gibi native engine’lere devreden bir ara katman; native "
            "yürütme SIMD gibi yetenekleri açıyor. Uber’in bildirdiği sonuçlar: taşınan iş "
            "yüklerinde yaklaşık 3,5 kat daha hızlı sorgu ve 3,4 kat daha düşük CPU maliyeti, "
            "kullanıcı kodunda değişiklik olmadan ve ortalama yüzde 79’a varan runtime "
            "iyileşmesi. TPC-DS benchmark’ında 64 executor ile en iyi durumda 4 kat, 32 "
            "executor ile en kötü durumda 2,7 kat, genel ortalamada yaklaşık 3,4 kat iyileşme "
            "görülmüş. İlginç bir bulgu: native shuffle’da columnar-to-row dönüşümü ek "
            "yük yaratıyor ve shuffle ağırlıklı sorgularda Gluten geriye düşebiliyor (bir "
            "sorguda Spark 10 saniyede, Gluten 1 dakikada bitmiş). Celeborn’un columnar sort "
            "shuffle’ı ile bu dönüşüm ortadan kalkınca ortalama iyileşme yaklaşık 3,65 kata "
            "çıkmış. Production’da seçili iş yüklerinde runtime’da yüzde 79’a, kritik "
            "pipeline’larda maliyette yüzde 98’e kadar azalma görülmüş (örneğin bir iş 1 saat "
            "7 dakikadan 16 dakikaya inmiş). Üretime hazırlık için Uber upstream’e 30’dan fazla "
            "yama (50’den fazla commit) göndermiş: row-to-column dönüşümünden doğan maliyet "
            "artışlarını azaltan fallback mekanizmaları ve bellek ayarları (Velox için off-heap, "
            "diğer işlemler için on-heap bellek ayrımı), native C++ Parquet okuyucu ve "
            "yazıcılarda şifreleme desteği ve eksik operatör ve fonksiyonlar.\n\n"
            "**İkinci adım: storage-aware engine değerlendirmesi.** Gluten kazanımlarının üstüne "
            "Uber, Spark hesaplamasının en büyük payını oluşturan ingestion ve tablo bakımı "
            "iş akışlarına baktı: bunlar yalnızca SQL operatörleri değil, mevcut veriyi "
            "okuyup güncelleme uygulayan, dosya yazan ve tablo metadata’sını güncel tutan "
            "işler. Data lake’teki tabloların çoğu düz Parquet; yaklaşık 17.200 tablo Apache "
            "Hudi ile yönetiliyor ve Hudi iş yükleri ingestion hesaplamasının önemli bir "
            "kısmı. Uber, Onehouse’un ticari Spark engine’i **Quanton**’ı benchmark etti. "
            "Production iş yüklerinden modellenmiş sentetik veriyle, kontrollü bir "
            "ortamda: 60 milyar kayıtlı, insert ağırlıklı bir fact tablosunda 1.080 vCPU ile "
            "write-round başına medyan **5,5 kat** hızlanma; 10 milyar kayıtlı, update ağırlıklı "
            "bir dimension tablosunda 3.300 vCPU ile **4,7 kat**. Her karşılaştırmada Quanton ve "
            "açık kaynak Spark/Hudi baseline’ı aynı executor tahsisini kullanmış; sonuçlar "
            "metadata-compaction turlarını içermiyor. Bu rakamlar bir tedarikçinin ürünü, "
            "sentetik veri ve kontrollü ortam için; Uber production sonucu değil, bir "
            "değerlendirme olarak sunuyor."
        ),
        "key_points": [
            "Bu ölçekte yüzde birkaçlık verim bile gerçek bir kazançtır; optimizasyon sürekli bir programdır.",
            "Platform katmanı (Drogon) tüm Spark uygulamalarının gönderimini kontrol ettiği için filo çapında engine değişikliği mümkündür.",
            "Native engine’e geçince shuffle ile row/column dönüşümü darboğaz olabilir; ortalama iyileşme tek tek sorgularda ters düşebilir.",
            "Vendor benchmark’ını sentetik veriyle ve aynı kaynakla yaptığın baseline ile karşılaştır; production sonucu olarak okuma.",
        ],
        "why_it_matters": (
            "Çoğu Spark optimizasyonu SQL operatörlerine odaklanır; ama yazının gösterdiği gibi "
            "ingestion ve tablo bakımı gibi okuma, güncelleme ve yazma yollarını içeren iş "
            "yükleri, hesaplamanın büyük kısmını yer. Optimizasyonu büyük harcama kalemine "
            "yönlendirmek, önce ölçmekle başlar."
        ),
        "for_you": (
            "Kendi Spark ya da Pandas işlerinde üç hızlı kontrol: **(1)** Shuffle’ı ölç; Spark UI’da "
            "‘Shuffle Read/Write’ boyutuna bak, büyükse join stratejini (broadcast join) ya da "
            "partition sayısını gözden geçir. **(2)** Düz CSV yerine Parquet kullan ve gereksiz "
            "kolonları okuma (column pruning). **(3)** Bir performans iddiasını (‘5 kat hızlı’) "
            "kendi verinle, aynı kaynakla, birkaç kez tekrarlayarak ölç. Vendor sayıları "
            "yalnızca hipotez."
        ),
        "terms": [
            {"en": "shuffle", "tr": "shuffle", "definition": "Dağıtık işlemede verinin düğümler arasında yeniden dağıtılması; genelde en pahalı adımlardan biridir."},
            {"en": "vectorized execution", "tr": "vectorized execution", "definition": "Veriyi satır satır değil toplu bloklar hâlinde, SIMD gibi donanım yetenekleriyle işleme."},
            {"en": "Apache Hudi", "tr": "Apache Hudi", "definition": "Data lake’te güncelleme ve silmeyi destekleyen açık kaynak tablo formatı."},
            {"en": "fallback", "tr": "fallback", "definition": "Hızlı yol çalışmadığında sistemin yavaş ama güvenli yola düşmesi."},
            {"en": "column pruning", "tr": "column pruning", "definition": "Bir sorgunun yalnızca ihtiyaç duyduğu kolonları diskten okuması."},
        ],
    },
    {
        "url": "https://blog.cloudflare.com/trusted-agent-delegation/",
        "slot": "brief",
        "title_tr": "Kapıdaki kişi kimin adına geldi? Agent’lar insan değil ama insan gibi davranıyor",
        "difficulty": "orta",
        "tags": ["agent", "identity", "web", "security"],
        "summary": (
            "Agent’lar artık milyonlarca insan adına web’de eylem yapıyor. Bir siteye göre bir "
            "agent çoğu zaman bir insan kullanıcıdan ayırt edilemez ya da tek bir ziyaretçi "
            "gibi görünüp birçok kullanıcıyı temsil edebilir. Bu, sitenin arkadaki kullanıcıyı "
            "tanıma, ona hizmet verme ve sorumlu tutma yeteneğini ortadan kaldırıyor ve bir şey "
            "ters gidince maliyeti site üstleniyor. Cloudflare’in tezi: siteler agent’lara "
            "erişimi artırmak istiyorsa, site ile kullanıcı arasındaki ilişkiyi koruyan yeni "
            "mekanizmalar gerekiyor. Güvenlik ve dolandırıcılık önlemede bu üç şey demek: "
            "**kimlik** (eylemi yapan kişi kim olduğu konusunda dürüst mü?), **itibar** (bu kişi "
            "güvenilir mi?) ve **hesap verebilirlik** (kim sorumlu?).\n\n"
            "Yazının merkezindeki ilke **Intermediation Principle**: kullanıcılar ve siteler "
            "arasındaki iş ilişkisi ve her tarafın güvenlik sorumlulukları, araya bir aracı "
            "girse de korunmalı. Agent ve arkasındaki operatör de tanınabilir ve hesap "
            "verebilir olmalı; çünkü bir agent insanın yapamayacağı şeyleri yapabilir (yorulmaz, "
            "gece gündüz çalışır, paralel eylem yapar ve hiçbir insanın katlanmayacağı "
            "sürtünmeye katlanır). Yazının benzetmesi: bir şehirde dört kişinin işlerini "
            "yapan bir asistanı düşün; bakkal artık yalnızca asistanı görüyor ve kimin "
            "tercihinin hangisi olduğunu bilemiyor. Müşterilerden biri asistana bir telefon "
            "aldırıp haftalar sonra ‘onay vermedim’ derse mağaza, kimsenin onay verdiğini "
            "kanıtlayamaz. Yazı yalnızca uzak bir yerde barındırılan agent’ları kapsıyor; "
            "kullanıcının kendi cihazında ya da tarayıcısında çalışan yerel agent’lar "
            "kapsam dışı."
        ),
        "key_points": [
            "Bir agent bir aracıdır; site, arkasındaki kullanıcıyı ve sorumluyu ayırt edebilmelidir.",
            "Kimlik, itibar ve hesap verebilirlik, klasik fraud önlemenin üç ayağıdır ve agent’lar için de gereklidir.",
            "İnsan gibi davranan ama insan limitlerine uymayan agent’lar, sitenin kapasite ve gelir varsayımlarını bozar.",
        ],
        "for_you": (
            "Bir API ya da web uygulaması yazıyorsan şu soruyu şimdiden sor: bir istek bir insandan "
            "mı, bir agent’tan mı geliyor ve hangi kullanıcı adına? Pratik bir adım: her isteğe bir "
            "`on_behalf_of` kullanıcı kimliği ve istemci kimliği (API key ya da OAuth client) "
            "iste, bunları logla ve agent’lar için ayrı bir rate limit uygula. Böylece bir şey "
            "ters gidince ‘kim, kimin adına’ sorusuna cevabın olur."
        ),
        "terms": [
            {"en": "intermediary", "tr": "intermediary", "definition": "Kullanıcı ile site arasında duran, siteye kullanıcının yerine görünen aracı."},
            {"en": "accountability", "tr": "accountability", "definition": "Bir eylemin sorumlusunun belli olması ve sonuçlarını üstlenmesi."},
            {"en": "operator", "tr": "operator", "definition": "Bir agent’ı barındıran ve işleten şirket ya da servis."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
