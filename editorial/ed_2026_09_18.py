"""18 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-18"

INTRO = (
    "Bugünün ortak teması ‘doğru araçla doğru sınırı çekmek’. ReadyOn çok kiracılı güvenlikte "
    "tek duvara güvenmiyor, dört duvar örüyor. Netflix Java’yı komut satırında agent’lara "
    "ve insanlara kolaylaştırıyor. CSIRO ise ayda 40 sentlik bir genom sorgu servisi kurmuş."
)

DRAFTS = [
    {
        "url": "https://aws.amazon.com/blogs/architecture/readyons-four-walls-of-tenant-isolation-on-amazon-eks/",
        "slot": "cover",
        "title_tr": "Namespace bir güvenlik sınırı değildir: çok kiracılı Kubernetes’te dört duvar",
        "difficulty": "ileri",
        "tags": ["güvenlik", "Kubernetes", "çok kiracılılık", "izolasyon"],
        "summary": (
            "ReadyOn, Fortune 100 şirketlerine iş gücü yönetimi sunan, bordro verisi, organizasyon "
            "hiyerarşisi ve operasyonel analitik gibi çok hassas veri işleyen bir platformu Amazon EKS "
            "üzerinde çok kiracılı olarak işletiyor. Yazının çıkış noktası şu tespit: varsayılan bir "
            "Kubernetes kurulumu kutudan güvenli çıkmaz (anonim isteklerin API sunucusuna ulaşabilmesi, "
            "pod’ların varsayılan olarak root çalışması, ağ politikalarının sen yazana kadar olmaması).\n\n"
            "Çok kiracılılık tehdit modelini değiştiriyor: soru artık ‘yetkisiz biri kümeye "
            "ulaşabilir mi?’ değil, **‘Kiracı A, Kiracı B’nin verisine erişebilir mi?’** Çoğu "
            "platform tek bir yalıtım mekanizmasına, namespace’e dayanıyor; oysa Kubernetes "
            "tasarımcıları namespace’leri hiçbir zaman bir güvenlik sınırı olarak düşünmedi.\n\n"
            "ReadyOn’ın **Dört Duvar** modeli bağımsız dört katmanı birleştiriyor. **Duvar 1, namespace:** "
            "kiracı başına namespace, sıkı RBAC, kaynak kotaları ve admission kontrolü; hepsi bir "
            "Argo CD ApplicationSet’iyle üretiliyor, her kiracı özdeş yapılandırma alıyor. **Duvar 2, "
            "hesaplama:** Karpenter, kiracı başına ayrı otomatik ölçeklenen düğüm havuzları açıyor ve "
            "**çift taint** stratejisi kullanıyor: her düğüm hem kiracıyı hem iş yükü tipini belirten "
            "taint taşıyor, pod’un ikisini de tolere etmesi gerekiyor. **Duvar 3, ağ:** kiracı başına "
            "VPC güvenlik grupları veritabanı erişimini yalnızca o kiracının düğüm havuzuna kısıtlıyor; "
            "Kubernetes ağ politikaları namespace’ler arası varsayılan reddi uyguluyor; küme API sunucusu "
            "özel. **Duvar 4, veri:** kiracı başına ayrı Aurora kümesi ve kiracıya özgü Secrets Manager "
            "sırları; iş yükleri IRSA ile kısa ömürlü kimlik bilgisi kullanıyor.\n\n"
            "Mantık bileşik savunma: sınırı aşmak için yetkisiz bir kullanıcının Kubernetes API’sini, "
            "düğüm zamanlayıcısını, AWS’in yazılım tanımlı ağını ve veri katmanını **aynı anda** aşması "
            "gerekiyor."
        ),
        "key_points": [
            "Namespace mantıksal bir gruplamadır; kernel, düğüm ve ağ düzeyinde yalıtım sağlamaz.",
            "Her duvar farklı bir teknik gerektirdiği için tek bir açık tüm yalıtımı bozmaz (derinlemesine savunma).",
            "Kiracı kaynaklarının tamamı şablondan (ApplicationSet) üretiliyor: elle yapılandırma sapmaya yol açar.",
            "En güçlü yalıtım veri katmanında: kiracı başına ayrı veritabanı, ayrı sır, kısa ömürlü kimlik bilgisi.",
            "Maliyet bu güvenliğin fiyatı: yalıtım derecesi arttıkça kaynak paylaşımı ve verimlilik azalır.",
        ],
        "why_it_matters": (
            "Çok kiracılı sistemde gerçek risk dışarıdan saldırgan değil, bir kiracının bir hata ya da "
            "açık yüzünden başkasının verisini görmesidir. Yalıtım düzeyi, ne kadar hassas veri "
            "taşıdığına göre seçilen bir mimari karardır: ucuz ve paylaşımlı ile pahalı ve yalıtık "
            "arasında bir skala var."
        ),
        "for_you": (
            "Mobit’teki ERP uygulaması şirket bazlı doküman düzenlemesi yapıyor, yani sen de "
            "çok kiracılısın. En önemli soru: kiracı yalıtımını **uygulama kodunda** (`WHERE company_id "
            "= ?`) mı sağlıyorsun? O tek duvardır ve bir sorguda unutulan filtre başka şirketin "
            "verisini sızdırır. PostgreSQL’in **Row Level Security** özelliği ikinci bir duvar "
            "ekler: kural veritabanında durur ve unutulan bir filtreyi bile yakalar. Her kiracıya "
            "ayrı veritabanı vermek en güçlüsü ama pahalı; RLS çoğu proje için en iyi denge."
        ),
        "terms": [
            {"en": "multi-tenancy", "tr": "çok kiracılılık", "definition": "Aynı altyapıyı birbirinden bağımsız birden fazla müşterinin (kiracı) paylaşması."},
            {"en": "taint / toleration", "tr": "leke / tolerans", "definition": "Kubernetes’te belirli düğümlere yalnızca ilgili tolerasyonu taşıyan pod’ların yerleşmesini sağlayan mekanizma."},
            {"en": "RBAC", "tr": "rol tabanlı erişim denetimi", "definition": "İzinlerin kullanıcıya değil role bağlanıp rollerin kullanıcılara atandığı yetkilendirme modeli."},
            {"en": "row level security (RLS)", "tr": "satır düzeyi güvenlik", "definition": "Veritabanında hangi kullanıcının hangi satırları görebileceğini tanımlayan, sorgudan bağımsız kurallar."},
            {"en": "IRSA", "tr": "servis hesapları için IAM rolleri", "definition": "Kubernetes pod’larına, uzun ömürlü anahtar olmadan kısa ömürlü AWS yetkisi veren mekanizma."},
        ],
    },
    {
        "url": "https://netflixtechblog.com/leave-the-class-path-in-the-rearview-mirror-67a85b15b6be?source=rss----2615bd06b42e---4",
        "slot": "brief",
        "title_tr": "Java’yı komut satırında yeniden düşünmek: modül tanımı proje tanımıdır",
        "difficulty": "orta",
        "tags": ["Java", "araçlar", "agent", "geliştirici deneyimi"],
        "summary": (
            "Netflix JVM ekibi, Java Modül Sistemi üzerine kurulu ve birleştirilebilir komut satırı "
            "araçlarından oluşan **ja** ailesini önizlemeye açtı. Fikir: modül tanımı "
            "(`module-info`) projenin eksiksiz bir tanımı olsun, bağımlılık sürümleri `requires` "
            "satırlarının yanında dursun (`requires com.example.framework; // @1.2.3`).\n\n"
            "Gerekçeleri ilginç: Java geliştiricileri yıllarca grafik araçlarla (IDE) çok iyi "
            "hizmet aldığı için küçük, birleştirilebilir komut satırı araçlarına az ihtiyaç duydu. "
            "Ama **kodlama agent’ları** Java ile çalışınca bu boşluk hemen göze çarpıyor: agent’lar "
            "bağımlılıkları, dokümantasyonu ve kaynakları bulmakta zorlanıyor. Çözüm tek bir devasa "
            "araç değil: `jig` (modül sürümü çözümleme, derleme, Maven köprüsü), `jfmt` (biçimleyici), "
            "`jist` (indeks, LSP ya da MCP gerektirmeden kaynak-farkında sembol araması) ve "
            "`jdocserver` (yerel API dokümantasyonu). Hepsi JDK’nın araç keşif mekanizmasını "
            "kullanıyor."
        ),
        "key_points": [
            "Agent’lar için araç tasarlamak = insanlar için iyi komut satırı araçları tasarlamak: küçük, birleştirilebilir, indeks gerektirmeyen.",
            "Her özellik bağımsız bir aracın üstünde: `ja` yalnızca orkestrasyon, parçaları ayrı ayrı da kullanabilirsin.",
        ],
        "for_you": (
            "Java ana dilin, o yüzden buradaki ders doğrudan senin: bir aracı hem insana hem agent’a "
            "kolay yapan şey, **keşfedilebilir ve birleştirilebilir** olmasıdır. Kendi CLI’ını "
            "(bu gazetenin `python -m pipeline.cli` komutları gibi) yazarken her komutun tek iş "
            "yapmasını, çıktısının başka araçlara girdi olabilmesini ve `--help` metninin gerçekten "
            "açıklayıcı olmasını sağla."
        ),
        "terms": [
            {"en": "Java Module System", "tr": "Java Modül Sistemi", "definition": "Java 9 ile gelen, paketleri modüllere ve bağımlılıkları açık tanımlara bağlayan sistem."},
            {"en": "composable tool", "tr": "birleştirilebilir araç", "definition": "Tek iş yapan ve çıktısı başka araçlara girdi olabilen küçük komut satırı aracı."},
        ],
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/how-csiro-built-scalable-cost-optimized-genomic-variant-querying-on-aws/",
        "slot": "brief",
        "title_tr": "Veritabanı kurmadan genom sorgulamak: ayda yaklaşık 0,40 dolar",
        "difficulty": "orta",
        "tags": ["serverless", "maliyet", "veri mühendisliği", "Athena"],
        "summary": (
            "Avustralya’nın ulusal bilim kurumu CSIRO, genomik varyant verisini güvenle sorgulamak "
            "için **sBeacon** adlı sunucusuz bir çözüm kurmuş (GA4GH Beacon standardının üretime "
            "hazır bir uygulaması). Yapı taşları S3, Lambda, DynamoDB ve Athena.\n\n"
            "İddialar somut: yüz milyonlarca kişiyi ve milyarlarca genomik konumu kapsayan "
            "veri kümelerine ölçekleniyor; 1000 Genomes boyutundaki bir veri kümesi için aylık "
            "**yaklaşık 0,40 dolara** çalışıyor; gerçek sorgular yaklaşık 5 saniyede dönüyor. En "
            "dikkat çekici tasarım kararı: standart VCF dosyalarını **doğrudan tüketiyor**, veritabanına "
            "yükleme ve dönüştürme gerekmiyor. Merkezî veritabanı olmadığı için veri sahibinin "
            "elinde kalıyor, bu da gizlilik ve federasyon için avantaj."
        ),
        "key_points": [
            "Kullanılmadığında para harcamayan mimari (S3 + Lambda + Athena), seyrek sorgulanan büyük veri için ideal.",
            "Veriyi yüklemeden dosya olarak sorgulamak, onboarding süresini ve maliyeti düşürür.",
        ],
        "for_you": (
            "Tradebot’taki 1 TB’lık geçmiş veri için bu deseni düşün: veriyi Parquet olarak nesne "
            "depolamada tut, ihtiyaç anında DuckDB (yerelde) ya da Athena (bulutta) ile sorgula. "
            "Sürekli çalışan bir veritabanı ödemezsin, yalnızca sorguladığın veri kadar ödersin. "
            "DuckDB özellikle denemeye değer: `pip install duckdb` ile Parquet dosyalarını doğrudan "
            "SQL ile sorgulayabilirsin, sunucu kurmadan."
        ),
        "terms": [
            {"en": "serverless", "tr": "sunucusuz", "definition": "Sunucu yönetmeden, yalnızca çalıştığı süre kadar ücretlendirilen çalışma modeli."},
            {"en": "VCF (variant call format)", "tr": "varyant çağrı biçimi", "definition": "Genomik varyantları saklayan standart metin tabanlı dosya biçimi."},
            {"en": "Parquet", "tr": "Parquet", "definition": "Analitik sorgular için optimize edilmiş sütun tabanlı dosya biçimi."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
