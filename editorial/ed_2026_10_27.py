"""27 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-27"

INTRO = (
    "Gizlilik kuralını her sisteme ayrı ayrı kodlamak aylar sürer. Meta, kuralı veriye "
    "erişim anına, tek bir ortak kütüphaneye taşıdı. Yanında Uber Freight’ın onlarca "
    "servisin verisini tek bir arama index’inde birleştirme yöntemi ve ‘bu kod gerçekten "
    "çalıştı mı?’ sorusuna kriptografik bir cevap var."
)

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/10/27/security/privacylib/",
        "slot": "cover",
        "title_tr": "Gizlilik kuralını bir kez entegre et, modül olarak ekle: Meta’nın PrivacyLib’i",
        "difficulty": "ileri",
        "tags": ["privacy", "architecture", "security", "agent"],
        "summary": (
            "Meta’da birçok gizlilik gereksinimi aynı soruya iner: **bir verinin yalnızca izin "
            "verilen yerlere gittiğini kanıtlayabilir miyiz?** Bu ölçekte elle yapılan "
            "denetimler, sistemler değiştikçe gerçeğin gerisinde kalıyor. Meta bunu altyapının "
            "içinde cevaplayan **Privacy Aware Infrastructure (PAI)** geliştirmiş; veri "
            "anlama, data lineage ve bilgi akışı kontrolü sağlayan Policy Zones daha önceki "
            "yazılarda anlatılmıştı. Bu yazı sürecin son aşamasını, veri akışlarını sürekli "
            "uygulama ve izleme işini yapan **PrivacyLib**’i anlatıyor: yüzlerce veri ve "
            "işleme sisteminin client’larının içinde, veriye erişilen noktada çalışan ortak bir "
            "kütüphane.\n\n"
            "**Önceki durum.** Her gereksinim için, her sistemin client’ına ayrı bir enforcement "
            "entegrasyonu yazılıyordu. Yeni bir gereksinimi (örneğin purpose limitation ya da "
            "data flow discovery) tüm sistemlere yaymak aylar alabiliyordu. Her yeni gereksinimin "
            "aynı yeteneklere ihtiyacı vardı: geniş sistem kapsamı, aylar yerine haftalarda "
            "yayın, her veri erişiminde latency sorunu yaratmadan çalışma ve filoyu "
            "düşürmeden enforcement değişikliği yayma.\n\n"
            "**Çözüm: entegrasyon ile gereksinimi ayırmak.** Her sistem PrivacyLib’e bir kez "
            "entegre ediliyor. Bir gereksinim veriye erişim noktasında karşılanabiliyorsa, "
            "o gereksinim zaten entegre olan tüm sistemlerin paylaştığı bir **modül** olarak "
            "yazılıyor. İki tür modül var: **enforcing** modüller bir erişimi engelleyebilir "
            "(Policy Zones purpose limitation’ı bu yolla uygular); **observing** modüller "
            "yalnızca erişimi kaydeder (Privacy Probes, veri akışlarını keşfetmek için runtime "
            "sinyallerini toplar). Internal AI agent’lar veriye yeni bir yoldan eriştiğinde bir "
            "**Agent Observability** modülü eklendi ve PrivacyLib’e zaten entegre olan sistemler "
            "bunu yeni bir entegrasyon işi olmadan aldı. Yazının cümlesi: her yeni gizlilik "
            "yeteneği bir proje değil bir modül olarak geliyor. Agent’ların veri erişim yolları "
            "önceden bilinmeyebileceğinden, desteklenen yollardaki tool call’lar agent "
            "bağlamını PrivacyLib’e taşıyor; bu bağlam her erişimi kendi session’ına bağlıyor, "
            "böylece modüller veri kullanımını gözlemleyip izin verilmeyen işlemleri "
            "engelleyebiliyor.\n\n"
            "**Ölçek ve mühendislik zorlukları.** PrivacyLib yüzden fazla veri erişim "
            "kütüphanesi (key/value store’lardan AI özelliklerine kadar), production’da "
            "binlerce servis ve onların farklı kütüphane sürümleri, günde milyonlarca asset ve "
            "saniyede milyarlarca kontrol üzerinde çalışıyor. Üç sorun öne çıkıyor. "
            "**Coverage:** bir sistemin birden çok client kütüphanesi, eski entegrasyonları, "
            "doğrudan ağ çağrıları ve arkadaki depoya doğrudan erişimi olabilir; gereksinimin "
            "hangi yoldan gelinirse gelinsin tutması için hepsinin ele alınması gerekiyor. "
            "**Scale:** saniyede milyarlarca kontrolde, kontrol başına küçük bir maliyet bile "
            "tüm filoda ağır hâle geliyor; gereksinimler build zamanında en basit "
            "değerlendirilebilir biçimlerine derleniyor. **Reliability:** gizlilik mantığı kritik "
            "sistemlerin hot path’inde çalışıyor ve sistemlerin sahipleri kendi takvimlerinde "
            "yayın yapıyor; bir değişikliğin kendi başına test edilebilir ve geri alınabilir "
            "olması gerekiyor, çünkü fleet-wide rollback kurtarma yolu olamaz. Bu yüzden "
            "değişiklikler modül bazında simüle edilip yayılıyor.\n\n"
            "**Örnek: mesajlaşma metadata’sı.** Messenger’ın backend’i, içeriği olmayan mesaj "
            "metadata’sını (örneğin iletim izleri) işleyen birçok servis içeriyor ve bunlar bir "
            "`Logger` kütüphanesiyle data warehouse tablolarına yazıyor. Kayıt yazılmadan önce "
            "Logger içindeki PrivacyLib entegrasyonu Policy Zones’u çağırıyor. İlginç bir "
            "tasarım kararı: verinin gizlilik **annotation**’ı (`MESSAGING_TRAFFIC_METADATA`) o "
            "tabloya yazan servislere değil, **hedef tablonun konfigürasyonuna** bağlanıyor. "
            "Çünkü bir hedefin birçok yazıcısı olabilir ve her servis annotation’ı ayrı "
            "bildirirse bildirimler birbirini tutmayabilir."
        ),
        "key_points": [
            "Kuralı her sisteme tek tek kodlamak yerine, sistemi bir kez entegre edip kuralı modül olarak eklemek yeni gereksinimin maliyetini düşürür.",
            "Enforcing (engelleyen) ve observing (yalnızca kaydeden) modüller ayrı tutulursa, yeni bir kuralı önce gözlemleyip sonra zorlayabilirsin.",
            "Veriyi anlatan annotation’ı yazıcıya değil verinin hedefine bağla; tek doğruluk kaynağı olsun.",
            "Hot path’te çalışan kontrol, kendi başına test edilebilir ve geri alınabilir olmalı; toplu rollback kurtarma yolu değildir.",
            "Agent’ların erişim yolları önceden bilinmez; her tool call’a agent bağlamını (session) taşımak, erişimi izlenebilir kılar.",
        ],
        "why_it_matters": (
            "Gizlilik ve güvenlik kuralları genelde yazılımın dağınık yerlerine serpilir ve "
            "zamanla birbirinden ayrışır. Bu yazı, kuralı veriye erişim sınırında merkezî bir "
            "kütüphanede toplamanın hem kapsama hem hız hem de güvenilirlik sorunlarını nasıl "
            "çözdüğünü gösteriyor."
        ),
        "for_you": (
            "Küçük bir uygulamada aynı fikri şöyle uygularsın: veriye erişimi doğrudan "
            "repository çağrıları yerine tek bir ince katmandan geçir (Spring’de bir "
            "`AccessPolicy` servisi ya da bir interceptor). Hassas alanlara (kişisel veri, ödeme "
            "bilgisi) bir annotation koy (`@Sensitive(purpose = ...)`) ve kontrol bu tek "
            "katmanda yapılsın. Yeni bir kuralı önce yalnızca **loglayan** (observing) modda "
            "çalıştır, sonuçlara bak, sonra engelleyen (enforcing) moda al. Böylece yeni bir "
            "kuralın canlı trafiği sessizce bozmasını önlersin."
        ),
        "terms": [
            {"en": "purpose limitation", "tr": "purpose limitation", "definition": "Verinin yalnızca toplandığı amaç için kullanılabilmesi ilkesi."},
            {"en": "data lineage", "tr": "data lineage", "definition": "Bir verinin nereden geldiğini ve hangi sistemlerden geçtiğini izleyen kayıt."},
            {"en": "enforcing module", "tr": "enforcing module", "definition": "Bir veri erişimini engelleyebilen kontrol modülü."},
            {"en": "observing module", "tr": "observing module", "definition": "Erişimi engellemeden yalnızca kaydeden kontrol modülü."},
            {"en": "hot path", "tr": "hot path", "definition": "Her istekte çalışan, gecikmeye doğrudan etki eden kod yolu."},
        ],
    },
    {
        "url": "https://www.uber.com/blog/high-performance-search-platform/",
        "slot": "brief",
        "title_tr": "Onlarca ekip, tek arama index’i: Uber Freight’ın fragment composition yaklaşımı",
        "difficulty": "ileri",
        "tags": ["search", "architecture", "data engineering", "microservices"],
        "summary": (
            "Uber Freight 40’tan fazla microservice işletiyor ve arama, çoğu Uber kullanım "
            "senaryosundaki bir avuç kaynağın aksine yaklaşık yüz veri kaynağından ve tablodan "
            "veri çekmek zorunda. Üstelik servisler heterojen (işlemsel veritabanları, takip "
            "sistemleri, dış API’ler) ve veri farklı biçim ve SLA’larla geliyor. ‘Chicago’da önümüzdeki "
            "24 saatte yüklenecek X gönderici için tüm yükler’ gibi sorular birden çok servisi "
            "kapsıyor.\n\n"
            "Çözümün çekirdeği **deklaratif bir fragment composition framework’ü**: bir geliştirici "
            "iki soyutlamayla çalışıyor, **index** ve **fragment**. Her ekip kendi servisinin "
            "verisini bağımsız bir fragment olarak katkı veriyor ve fragment’lar ortak bir "
            "index’te birleşiyor. Bugün 70’ten fazla kaynak topic’i 300 fragment’a denormalize "
            "oluyor ve 20’den fazla index’e dağılıyor; sistem saniyede binlerce karmaşık sorgu "
            "sunuyor. Tasarımın hedefleri: değişimi ucuz tutmak (yeni alan ya da kaynak karmaşık "
            "kod olmadan eklenir), değişikliklerin saniyeler içinde aranabilir olması, her alanın "
            "kaynak sistemine kadar izlenebilmesi (data lineage) ve çağıranların sorguyu "
            "çalışma anında kendisinin kurabilmesi. Yazıya göre tasarım yıllar içinde sağlam "
            "kalmış: yeni iş senaryoları ve ardından tam bir search engine göçü, platform "
            "yeniden tasarlanmadan karşılanmış. Annotation DSL’i ve connector soyutlamaları "
            "hem batch hem streaming pipeline’larında paylaşılıyor; platform alanı ile kullanıcı "
            "alanı arasındaki net sınır sayesinde platform bileşenleri iş koduna dokunmadan "
            "değiştirilebiliyor."
        ),
        "key_points": [
            "Her ekibin kendi verisini bağımsız bir parça (fragment) olarak katkı verdiği, ortak bir index modeli ekipler arası bağımlılığı düşürür.",
            "Deklaratif tanım (annotation DSL), yeni kaynak eklemeyi kod yazmadan konfigürasyona indirir.",
            "Platform ile kullanıcı alanı arasındaki net sınır, altyapıyı iş kodunu bozmadan değiştirmeyi sağlar.",
        ],
        "for_you": (
            "Birden çok tablodan arama yapan bir ekranın varsa JOIN’li ağır sorgular yerine tek "
            "bir **denormalize edilmiş arama tablosu** (ya da OpenSearch/Postgres full-text "
            "index) tut. Her kaynak tablo, kendi alanlarını bu aramaya bir olay (event) ile "
            "güncellesin. Bu, okumayı hızlandırır ve her ekran için ayrı sorgu yazma ihtiyacını "
            "azaltır."
        ),
        "terms": [
            {"en": "denormalization", "tr": "denormalization", "definition": "Okuma hızı için verinin birden çok tablodan toplanıp tek bir yerde tekrarlanarak saklanması."},
            {"en": "fragment", "tr": "fragment", "definition": "Bir ekibin kendi servisinin verisinden ürettiği ve ortak index’e katkı verdiği bağımsız parça."},
            {"en": "data lineage", "tr": "data lineage", "definition": "Bir verinin nereden geldiğini ve hangi sistemlerden geçtiğini izleyen kayıt."},
        ],
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/how-anchorage-digital-and-turnkey-verify-code-with-aws-nitro-enclaves/",
        "slot": "brief",
        "title_tr": "‘Bu kod gerçekten çalıştı mı?’ sorusuna kriptografik cevap: Nitro Enclaves ile verifiable infrastructure",
        "difficulty": "orta",
        "tags": ["security", "attestation", "confidential computing", "AWS"],
        "summary": (
            "Kripto dünyasında bir cüzdan, bir işlemi ayrıştırmak ya da politikayı değerlendirmek "
            "için hesaplamayı üçüncü bir tarafa devrediyor ve her seferinde şu soru çıkıyor: bu "
            "servisin iddia ettiği kodu gerçekten çalıştırdığını nereden biliyorsun? Sözleşmesel "
            "güven, ağ çevresi güvenliği ve itibar kriptografik bir cevap vermiyor. Anchorage "
            "Digital ve Turnkey, açık kaynak, Rust ile yazılmış **VisualSign** adlı bir işlem "
            "ayrıştırıcısını AWS Nitro Enclaves içinde çalıştırıp sonuçları **attestation** "
            "tabanlı kanıtla döndürüyor. Çözdükleri problem **blind signing**: cüzdan bir "
            "işlemin tüm etkilerini gösteremediği için kullanıcı ham hex ya da kısmi bir özetle "
            "onay veriyor ve saldırganlar bunu kullanıyor. Bir ayrıştırıcının iki garantiye "
            "ihtiyacı var: **correctness** (denetlenen ve onaylanan kodun aynısı çalışıyor) ve "
            "**integrity** (çıktı, ayrıştırıcıdan cüzdana giderken değiştirilmedi). Yazı, aynı "
            "desenin yalnızca blockchain’le sınırlı olmadığını, yüksek güven gerektiren her iş "
            "akışına uyduğunu vurguluyor. 24 Eylül’de okuduğun Meta Private Processing ile aynı "
            "fikrin başka bir uygulaması."
        ),
        "key_points": [
            "‘Bize güvenin’ yerine ‘çalışan kodu kendiniz doğrulayın’ demek, güveni kanıta çevirir.",
            "Attestation, bir servisin hangi yazılımı çalıştırdığını donanım destekli imzayla gösterir.",
        ],
        "for_you": (
            "Bunu bugün bir kavram olarak kullan: üçüncü taraf bir servise hassas veri "
            "gönderiyorsan ‘servisin ne yaptığını nasıl doğrularım?’ diye sor. Pratik bir ilk "
            "adım: o servise gönderilen ve ondan dönen her şeyi **imzalı** ve zaman damgalı "
            "kaydet; sonradan bir anlaşmazlık olursa kanıtın olur."
        ),
        "terms": [
            {"en": "attestation", "tr": "attestation", "definition": "Bir sistemin hangi yazılımı çalıştırdığını donanım destekli imzayla kanıtlaması."},
            {"en": "blind signing", "tr": "blind signing", "definition": "Bir işlemin tüm etkilerini görmeden onay vermek."},
            {"en": "enclave", "tr": "enclave", "definition": "Ana sistemden yalıtılmış, içeriği operatör tarafından bile okunamayan güvenli çalışma alanı."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
