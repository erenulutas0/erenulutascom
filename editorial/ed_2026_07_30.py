"""30 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-30"

INTRO = (
    "Bugünün teması \"elle yazılmış karmaşıklığı neyle değiştiriyoruz?\" "
    "Netflix binlerce elle üretilmiş özelliği bir dil modeline bırakıyor, "
    "Databricks on yıllık stored procedure'ları bir agent'a çevirtiyor, "
    "Google Cloud ise binlerce veritabanı parolasını IAM gruplarına devrediyor. "
    "Üçünde de kazanç aynı yerden geliyor: bakım yükünün azalması."
)

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/genrec-towards-llm-native-recommendation-at-netflix-f20be6f643e3?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "Netflix öneri sistemini dil modeline devretti: GenRec",
        "difficulty": "ileri",
        "tags": ["öneri sistemleri", "LLM", "ML altyapısı", "mimari"],
        "summary": (
            "Netflix'in üretimdeki öneri modelleri **binlerce elle üretilmiş özellik** "
            "(hand-crafted feature) üzerine kurulu: kullanıcılar, içerikler ve "
            "etkileşimler için tasarlanmış özellikler, artı dizi modelleme, özellik "
            "etkileşimleri ve çok-görevli hedefler için özelleşmiş mimariler. Yıllar "
            "içinde olgunlaşmış bir yığın — ama karmaşıklığı yüzünden yeni bir "
            "kullanım senaryosunu eklemek pahalı. Yeni bir içerik türü ya da yeni bir "
            "ekran eklemek ciddi özellik mühendisliği, mimari değişiklik, altyapı "
            "işi ve deney gerektiriyor.\n\n"
            "GenRec bu problemi tersten çözüyor. Netflix kendi temel dil modelini "
            "kendi verisiyle **post-training**'den geçirip bir sıralama (ranking) "
            "modeline dönüştürmüş. Yaklaşımın adımları şöyle: kullanıcı geçmişini, "
            "içerik metadata'sını ve bağlamı **metne çeviriyor** (verbalize); "
            "Netflix'e uyarlanmış temel modeli sıralama için post-train ediyor; "
            "üstüne katalog-farkında bir skorlama başlığı ekliyor; ödül sinyalleriyle "
            "uzun vadeli üye değerine hizalıyor.\n\n"
            "Sonuç dikkat çekici: geniş ölçekli bir A/B testinde, iyi ayarlanmış "
            "üretim modeline karşı hem kısa hem uzun vadeli metriklerde istatistiksel "
            "olarak anlamlı iyileşme sağlamış — ve bunu etiketli verinin ve girdi "
            "sinyallerinin **küçük bir kısmıyla** yapmış. Maliyet tarafında ise "
            "Netflix'in LLM sunum yığınında **prefill-only** modda çalışıyor."
        ),
        "key_points": [
            "Ana kazanç doğrulukta değil, karmaşıklıkta: binlerce özellik yerine "
            "metne çevrilmiş geçmiş, çok daha az bakım.",
            "\"Verbalization\" fikri basit ama güçlü: yapılandırılmış veriyi metne "
            "çevirip modelin dünya bilgisinden faydalanmak.",
            "Prefill-only çalıştırmak maliyeti düşürüyor — model uzun metin üretmiyor, "
            "yalnızca skorluyor.",
            "Az veriyle daha iyi sonuç, olgun bir sistemi değiştirmenin en zor "
            "gerekçesini karşılıyor: geçiş maliyetini haklı çıkarıyor.",
        ],
        "why_it_matters": (
            "Öneri sistemleri on yıldır özellik mühendisliğiyle ilerliyordu; her "
            "iyileşme yeni bir sinyal, yeni bir kolon, yeni bir pipeline demekti. "
            "Bu yazı o yaklaşımın sonuna işaret ediyor. Daha genel dersi ise şu: "
            "olgun bir sistemin asıl maliyeti çalıştırmak değil, **değiştirebilmek**. "
            "Yeni bir gereksinim geldiğinde ne kadar iş çıkıyorsa, mimarinin gerçek "
            "fiyatı odur."
        ),
        "for_you": (
            "Tradebot'ta özellik mühendisliği yaptıysan bu yazı doğrudan sana. "
            "Muhtemelen fiyat, hacim, volatilite üzerinden onlarca gösterge "
            "hesapladın; her yeni fikir yeni bir kolon ve yeni bir pipeline demekti. "
            "GenRec'in sorduğu soru şu: bu sinyalleri elle üretmek yerine ham "
            "geçmişi metne çevirip modele versen ne olurdu? Küçük ölçekte bunu "
            "deneyebilirsin — ama asıl alacağın ders \"LLM kullan\" değil, "
            "**bakım maliyetini bir metrik olarak ölçmek**. \"Yeni bir varlık "
            "eklemek kaç saatimi alıyor?\" sorusunun cevabı, mimarinin sağlık "
            "göstergesidir."
        ),
        "terms": [
            {
                "en": "feature engineering",
                "tr": "özellik mühendisliği",
                "definition": "Ham veriden modelin kullanacağı anlamlı sinyalleri elle tasarlama ve hesaplama işi.",
            },
            {
                "en": "post-training",
                "tr": "sonradan eğitim",
                "definition": "Önceden eğitilmiş bir temel modeli, belirli bir görev ve veri kümesi için ek eğitimden geçirme.",
            },
            {
                "en": "ranker",
                "tr": "sıralama modeli",
                "definition": "Aday içerikleri kullanıcıya uygunluk sırasına dizen model.",
            },
            {
                "en": "prefill-only",
                "tr": "yalnızca ön-doldurma",
                "definition": "Modelin yeni token üretmeden sadece girdiyi işleyip bir skor çıkarması; üretim aşaması olmadığı için çok daha ucuz.",
            },
        ],
    },
    {
        "url": "https://cloud.google.com/blog/products/containers-kubernetes/reduce-your-agents-costs-with-gke-agent-sandbox/",
        "slot": "brief",
        "title_tr": "Agent'lar dalgalı çalışır: boşta bekleyen izolasyonun maliyeti",
        "difficulty": "orta",
        "tags": ["Kubernetes", "izolasyon", "maliyet", "altyapı"],
        "summary": (
            "AI agent'ları **dalgalı** (bursty) çalışır: bir süre yoğun biçimde "
            "istek işler veya kod çalıştırır, sonra kullanıcı girdisi ya da dış "
            "tetikleyici beklerken uzun süre boş kalır. Statik kaynak ayırırsan "
            "boştaki agent'lar hâlâ CPU ve bellek tüketiyor.\n\n"
            "Güvenlik tarafında ise güvenilmeyen kod çalıştırmak güçlü izolasyon "
            "gerektiriyor. Yaygın yaklaşım her agent'ı kendi microVM'inde "
            "(Kata containers gibi) çalıştırmak — donanım seviyesinde izolasyon "
            "verir. Ama duvara çabuk toslar: her microVM kendi misafir işletim "
            "sistemini taşır, o da bellek ve CPU yer. Yani agent'a kalan kaynak "
            "azalır."
        ),
        "key_points": [
            "Soru net: sabit bir hesaplama alanına, güvenilirlikten ödün vermeden "
            "daha çok agent nasıl sığdırılır?",
            "İzolasyonun bir fiyatı var ve bu fiyat çalışan iş yükü başına değil, "
            "**ayrılmış kutu başına** ödeniyor.",
        ],
        "for_you": (
            "\"Kullanıcı kodu çalıştırmak\" ihtiyacı bir gün karşına çıkarsa "
            "(ör. KlioAI'da kullanıcıya kod alıştırması yaptırmak), ilk refleks "
            "Docker konteyneri olacaktır. Bu yazının hatırlattığı şey Docker'ın "
            "**güvenlik sınırı değil paketleme sınırı** olduğu: aynı çekirdeği "
            "paylaşırlar. Güvenilmeyen kod için gVisor ya da microVM gerekir, ve "
            "onun da bir bedeli vardır. Daha genel ders: bir kaynağın kullanılmadığı "
            "sürede de para ödüyorsan, mimarinin ölçek ekonomisi bozuktur — "
            "boşta duran her şeyin faturasını hesapla."
        ),
        "terms": [
            {
                "en": "bursty workload",
                "tr": "dalgalı iş yükü",
                "definition": "Kısa yoğun aktivite dönemleriyle uzun boşluk dönemlerinin birbirini izlediği kullanım deseni.",
            },
            {
                "en": "microVM",
                "tr": "mikro sanal makine",
                "definition": "Hafifletilmiş bir sanal makine; konteynerden güçlü ama kendi işletim sistemini taşıdığı için maliyetli izolasyon sağlar.",
            },
        ],
    },
    {
        "url": "https://cloud.google.com/blog/products/databases/alloydb-adds-group-authentication-to-secure-enterprise-scale-and-ai-agents/",
        "slot": "brief",
        "title_tr": "Veritabanı parolaları bir operasyonel vergi: IAM grup kimlik doğrulaması",
        "difficulty": "orta",
        "tags": ["veritabanı", "güvenlik", "kimlik doğrulama", "PostgreSQL"],
        "summary": (
            "Veritabanı güvenliği klasik olarak kırılgan bir dengeye dayanıyor: "
            "geliştiricinin istediği ayrıntılı kontrol ile binlerce ayrı veritabanı "
            "parolasını yönetmenin idari yükü. Yazının kullandığı ifade iyi — "
            "parolalar bir **operasyonel vergi** ve aynı zamanda bir güvenlik açığı.\n\n"
            "AlloyDB artık IAM grup kimlik doğrulamasını destekliyor. Bireysel "
            "kimlikleri tek tek veritabanı kullanıcılarına eşlemek yerine gruplar "
            "üzerinden erişim veriliyor. Yazının açıkça saydığı üç problem: "
            "işe alımda her yeni kişi için ayrı kullanıcı açma darboğazı, işten "
            "ayrılmada erişimin her yerden tamamen kaldırıldığından emin olamama, "
            "ve dev/staging/prod arasında izinlerin zamanla birbirinden ayrışması "
            "(**policy drift**)."
        ),
        "key_points": [
            "Cazip kaçamak: tüm uygulamayı tek bir güçlü servis hesabıyla çalıştırmak. "
            "Bedeli, risk yüzeyinin büyümesi ve denetim izinin kaybolması.",
            "Sorun kimlik doğrulamanın kendisi değil, **kimlik yaşam döngüsünün** "
            "veritabanından ayrı yönetilmesi.",
        ],
        "for_you": (
            "Küçük projelerde herkes `.env` dosyasındaki tek bir Postgres parolasını "
            "paylaşır — sen de büyük ihtimalle öyle yapıyorsun, ve o ölçekte sorun "
            "değil. Ama şu iki soruyu sorabilir olman lazım: bir ekip arkadaşı "
            "ayrıldığında parolayı değiştirmen mi gerekiyor, ve loglara baktığında "
            "\"bu sorguyu kim attı\" sorusuna cevap verebiliyor musun? İkisine de "
            "\"hayır\" diyorsan, paylaşılan tek kimlik hem güvenlik hem denetim "
            "borcudur. Mülakatta bu farkındalık, IAM'i ezberlemekten daha değerli."
        ),
        "terms": [
            {
                "en": "IAM (Identity and Access Management)",
                "tr": "kimlik ve erişim yönetimi",
                "definition": "Kimin hangi kaynağa erişebileceğini merkezî olarak tanımlayan sistem.",
            },
            {
                "en": "policy drift",
                "tr": "politika kayması",
                "definition": "Aynı olması gereken ortamların (dev/staging/prod) izinlerinin zamanla birbirinden ayrışması.",
            },
            {
                "en": "audit log",
                "tr": "denetim kaydı",
                "definition": "Hangi kimliğin ne zaman hangi işlemi yaptığını tutan, sonradan incelenebilir kayıt.",
            },
        ],
    },
    {
        "url": "https://www.databricks.com/blog/convert-proprietary-code-open-ansi-sql-genie-code",
        "slot": "brief",
        "title_tr": "Eski veri ambarı göçü: karmaşıklık puanı ve bağımlılık grafiği",
        "difficulty": "orta",
        "tags": ["SQL", "göç", "veri mühendisliği", "agent"],
        "summary": (
            "Databricks, eski veri ambarlarındaki tescilli SQL lehçelerini "
            "(T-SQL, Snowflake, Redshift, Oracle, BigQuery, Teradata) açık ANSI "
            "SQL'e çeviren bir agent duyuruyor. Ürün duyurusu olmasına rağmen "
            "içindeki iki fikir her göç projesinde işe yarar.\n\n"
            "Birincisi **karmaşıklık puanlaması**: agent her dosyayı analiz edip "
            "puanlıyor; yalnızca ANSI SQL'e temiz eşlenen özellikler içeren bir "
            "dosya \"düşük karmaşıklık\" alıyor. İkincisi **soy ağacı (lineage)** "
            "çıkarımı: eski sistemdeki tablolar, görünümler ve saklı yordamlar "
            "arasındaki tüm ilişkiler haritalanıyor. Grafik iki dosyanın ortak "
            "bağımlılığı olmadığını gösteriyorsa, o ikisi bağımsız taşınabilir."
        ),
        "key_points": [
            "Karmaşıklık + soy ağacı birlikte şu soruyu cevaplıyor: neyi, hangi "
            "sırayla ve neyle birlikte taşımalıyım?",
            "Göç projesini \"ekip kurup yönettiğin bir proje\" olmaktan çıkarıp "
            "\"yapılandırıp izlediğin bir süreç\" hâline getirme iddiası.",
        ],
        "for_you": (
            "Büyük bir göç işine girdiğinde ilk yapman gereken şey kod yazmak değil, "
            "**envanter ve bağımlılık haritası** çıkarmak — bu yazının asıl dersi bu. "
            "Aynı yaklaşımı çok daha küçük ölçekte de kullanabilirsin: bir refactor "
            "öncesi hangi modülün neye bağlı olduğunu çıkarıp bağımsız parçaları "
            "önce taşımak, riski ciddi düşürür. Python'da `ast` modülüyle import "
            "grafiği çıkarmak yarım saatlik bir iş, ama planı tamamen değiştirir."
        ),
        "terms": [
            {
                "en": "data lineage",
                "tr": "veri soy ağacı",
                "definition": "Bir verinin hangi kaynaktan çıkıp hangi dönüşümlerden geçtiğini gösteren bağımlılık haritası.",
            },
            {
                "en": "stored procedure",
                "tr": "saklı yordam",
                "definition": "Veritabanının içinde saklanan ve orada çalışan, iş mantığı barındıran SQL programı.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
