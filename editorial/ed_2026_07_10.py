"""10 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-10"

INTRO = "Bugünün kapağı, işe yarayan bir optimizasyonun altındaki varsayım çürüdüğünde ne olduğunu anlatıyor: Cloudflare'in \"en yakın sunucuyu bul\" algoritması, bulut kaynaklarında tutunacak bir şey bulamıyor. Yanına arşivden iki yazı ekledim — kendi yazdığın kuyruğu silmek ve embedding'lerle öneri kurmak."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/smart-tiered-cache-for-public-clouds/",
        "slot": "cover",
        "title_tr": "Ölçüm tutunacak bir şey bulamayınca: anycast ve cache verimliliği",
        "difficulty": "ileri",
        "tags": [
            "caching",
            "networking",
            "CDN",
            "architecture"
        ],
        "summary": "2021'de çıkan **Smart Tiered Cache**'in fikri basitti: sitenin arkasındaki her kaynak (origin) için Cloudflare, gerçek zamanlı gecikme ölçümlerine bakarak tek bir **en iyi üst katman** veri merkezi seçer. Tek anahtarı çevirirsin, ağdan kaynağına en fast path bulunur.\n\nBu, bir kaynak IP'si sabit bir yerde durduğu sürece çalışıyor. **Genel bulut kaynakları genelde durmuyor.** Anycast ya da bölgesel unicast ön yüzlerin arkasında oturuyorlar; yani tek bir kaynak IP'si aynı anda bir düzine Cloudflare veri merkezine eşit derecede yakın görünebiliyor — ve gecikme ölçümlerinin tutunacak bir şeyi kalmıyor.\n\nSmart Tiered Cache bu durumu **güvenli yoldan** ele alıyor: net bir kazanan yoksa birden fazla üst katmana düşüyor. Hiçbir şey bozulmuyor. Sadece tek bir en yakın katmanı değerli kılan şeyi kaybediyorsun: **cache verimliliği**. Çünkü aynı içerik birden fazla üst katmanda ayrı ayrı cache’lenir; her biri kaynağa ayrı gider.\n\nÇözüm bir **bölge ipucu** (region hint) vermene izin vermek. Bu ipuçla Cloudflare, kaynak IP'si her yere yakın görünse bile bulut kaynağını doğru bölgeye eşleyip daha iyi birincil ve yedek üst katman seçebiliyor.",
        "key_points": [
            "Sessiz bozulma (graceful degradation) doğru tasarım — ama neyi kaybettiğini bilmek gerekiyor: burada kaybedilen doğruluk değil verimlilik.",
            "Anycast bir adresi çok yerde duyurur; bu ağ katmanında harika, ama \"nerede?\" sorusunu cevapsız bırakır.",
            "Otomatik keşif başarısız olduğunda çözüm, insanın bildiği bilgiyi sisteme **ipucu** olarak vermek."
        ],
        "why_it_matters": "Her otomatik optimizasyon bir varsayıma dayanır. Bu yazı o varsayımı (\"kaynak sabit bir yerdedir\") ve çürüdüğünde ne olduğunu açıkça gösteriyor. Kendi sistemlerinde de sor: bu otomatik davranış hangi varsayıma dayanıyor ve varsayım bozulduğunda sistem ne yapıyor — gürültülü mü başarısız oluyor, yoksa sessizce mi kötüleşiyor?",
        "for_you": "İki kavram burada senin için kritik. **Anycast:** aynı IP adresinin dünyada birçok noktadan duyurulması, trafiğin en yakın noktaya gitmesi. 1.1.1.1 ve 8.8.8.8 böyle çalışır. **Tiered cache:** uç sunucuların doğrudan kaynağa gitmek yerine bir ara cache katmanından geçmesi — 100 uç sunucu ıskaladığında kaynağa 100 değil 1 istek gider. Bu ikinci fikri kendi ölçeğinde de kur: Spring Boot uygulamanda uygulama içi cache (Caffeine) ile paylaşılan Redis cache’ini birlikte kullanmak tam olarak tiered cache’tir ve veritabanına giden yükü ciddi düşürür.",
        "terms": [
            {
                "en": "anycast",
                "tr": "anycast",
                "definition": "Aynı IP adresinin birden çok konumdan duyurulması; ağ, isteği en yakın konuma yönlendirir."
            },
            {
                "en": "tiered cache",
                "tr": "tiered cache",
                "definition": "Uç cache’lerin kaynağa doğrudan gitmek yerine bir ara cache katmanından geçmesi; kaynak yükünü azaltır."
            },
            {
                "en": "graceful degradation",
                "tr": "graceful degradation",
                "definition": "Bir bileşen ideal çalışamadığında sistemin tamamen durmak yerine daha düşük verimle çalışmaya devam etmesi."
            }
        ]
    },
    {
        "url": "https://netflixtechblog.com/how-netflix-simplified-batch-compute-with-kueue-87860682629c?source=rss----2615bd06b42e---4",
        "slot": "archive",
        "title_tr": "Kendi yazdığın kuyruğu silmek: Netflix'in Kueue'ya geçişi",
        "difficulty": "orta",
        "tags": [
            "Kubernetes",
            "batch processing",
            "migration",
            "infrastructure"
        ],
        "summary": "Netflix hesaplama altyapısını daha Kubernetes-yerel hâle getirme yolculuğunda, Kubernetes ekosisteminden bileşenleri kendi konteyner platformu Titus'a dahil ediyor. Örneklerden biri **Kueue**: toplu iş yükleri için bulut-yerel bir iş kuyruğu sistemi.\n\nKueue, kendi geliştirdikleri **CMB** (Compute Managed Batch) çözümündeki özel kuyruklama ve zamanlama mantığının büyük kısmının yerini almış. CMB'nin yaptığı işler tanıdık: bir **tenant hiyerarşisi** üzerinden iş yüklerini yönetip kuyruklamak, öncelikle sıralı çalıştırma sağlamak ve kapasiteyi tenant bazında yönetmek. Tenant’lar organizasyon, platform ya da uygulama bazında gruplama sağlıyor ve her tenant’ın bir kapasite yapılandırması var — ağırlık ve diğer tenant’lardan izolasyon garantileri dahil.\n\nYazı milyonlarca toplu işin nasıl taşındığını da anlatıyor.",
        "key_points": [
            "Kendi yazdığın altyapıyı, olgunlaşan bir ekosistem bileşeniyle değiştirmek bakım yükünü kalıcı olarak düşürür.",
            "Tenant hiyerarşisi + kapasite ağırlıkları, çok takımlı bir platformda adil paylaşımın standart çözümü.",
            "Göç \"milyonlarca iş\" ölçeğinde yapılmış — yani kesintisiz geçiş tasarımı işin asıl zor kısmı."
        ],
        "why_it_matters": "Her ekip bir noktada \"bunu kendimiz mi yazsak?\" sorusuyla karşılaşır. Netflix bir zamanlar evet demiş, çünkü o gün hazır bir şey yoktu. Şimdi ekosistem olgunlaşınca kendi çözümünü emekliye ayırıyor. Bu ikinci karar, ilkinden daha zor ve daha değerli: yazdığın koda bağlanmamak.",
        "for_you": "Bu yazının bir alt seviyedeki karşılığını sen de yaşayacaksın: kendi yazdığın yardımcı sınıflar ve altyapı kodu. ‘Ben yazdım, çalışıyor’ bir kodu tutmak için yeterli sebep değil; bakımını kim yapacak sorusu daha önemli. Kubernetes tarafında şu ayrımı öğren: **Deployment** sürekli çalışan servisler için, **Job/CronJob** başlayıp biten işler için. Günlük çalışan bir veri pipeline’ı bir CronJob’un tam örneği; GitHub Actions cron’u da aynı işi yapan daha basit bir araç.",
        "terms": [
            {
                "en": "batch workload",
                "tr": "batch workload",
                "definition": "Başlayıp tamamlanan, sürekli çalışmayan hesaplama işi (rapor üretme, veri işleme gibi)."
            },
            {
                "en": "multi-tenancy",
                "tr": "multi-tenancy",
                "definition": "Aynı platformu birden çok takımın/uygulamanın paylaşması; adil kapasite paylaşımı gerektirir."
            },
            {
                "en": "job queueing",
                "tr": "job queueing",
                "definition": "Çalıştırılacak işlerin öncelik ve kapasiteye göre sıraya alınıp zamanlanması."
            }
        ]
    },
    {
        "url": "https://www.uber.com/blog/innovative-recommendation-applications-using-two-tower-embeddings/",
        "slot": "archive",
        "title_tr": "Two-Tower embedding: öneri sistemlerinin çalışan iskeleti",
        "difficulty": "ileri",
        "tags": [
            "recommender systems",
            "embedding",
            "ML infrastructure"
        ],
        "summary": "Uber'in ML ekibi 2022'de embedding'lere yatırım yapmış ve odak noktası **Two-Tower Embeddings (TTE)** olmuş. Amaç öneri sistemlerini beslemek: yemek siparişi verenler (eater) ve restoranlar (store) için embedding üretip uygulamak.\n\nEmbedding'in tanımı yazıda net veriliyor: bir varlığın (mağaza, kullanıcı, ürün, sürücü, konum) zengin bir temsili. İnsan dostu özellikleri — mağaza menüsü, ürün fiyatı, kullanıcının tercih ettiği mutfak, geçmiş siparişleri — makine öğrenmesi dostu vektörlere dönüştürüyor.\n\n\"Two-tower\" adı mimariden geliyor: iki ayrı ağ (kule), biri kullanıcıyı biri öğeyi kendi vektörüne çeviriyor; eşleşme skoru bu iki vektörün benzerliği. Bunun pratik değeri büyük — öğe vektörlerini önceden hesaplayıp saklayabilirsin, sorgu anında yalnızca kullanıcı vektörünü hesaplayıp en yakın komşuları ararsın.\n\nYol da dürüstçe anlatılmış: yaklaşım yaklaşık bir yıl sonra yayına girmiş, ve şehir bazında binlerce modelden tek bir küresel bağlamsal modele doğru evrilmiş.",
        "key_points": [
            "İki kule ayrımı, öğe tarafını önceden hesaplanabilir kılıyor — gerçek zamanlı öneri bu sayede mümkün.",
            "\"Binlerce şehir modeli\"nden \"tek küresel model\"e geçiş, ML sistemlerinde tekrarlanan bir olgunlaşma yolu.",
            "Bir yıllık geliştirme süresi açıkça yazılmış — gerçekçi bir beklenti çıpası."
        ],
        "why_it_matters": "Embedding'ler bugün arama, öneri ve RAG'in ortak dili. Two-tower mimarisi bu alanın en yaygın ve en pratik deseni; anlamak, \"benzerlik araması nasıl çalışıyor?\" sorusunun kapısını açar.",
        "for_you": "Embedding ve RAG ile çalışıyorsan buradan alacağın şey somut: **two-tower ayrımını** kendi sisteminde tanı. Bir doküman aramada belge embedding’lerini önceden hesaplayıp saklıyorsan (item tower), sorgu geldiğinde yalnızca sorguyu vektörleştiriyorsan (query tower), aynı desendesin. Bir adım ilerisi: iki tarafı aynı hazır modelle değil, kendi verinle eğitilmiş iki ayrı kuleyle temsil etmek; Uber’in yaptığı bu ve alana özgü aramada belirgin fark yaratır. Ayrıca **approximate nearest neighbor** (ANN) aramasını öğren: pgvector bunu PostgreSQL’de doğrudan veriyor.",
        "terms": [
            {
                "en": "embedding",
                "tr": "embedding",
                "definition": "Bir varlığın anlamsal özelliklerini taşıyan sayısal vektör temsili."
            },
            {
                "en": "two-tower model",
                "tr": "two-tower model",
                "definition": "Kullanıcı ve öğeyi ayrı ağlarla vektöre çevirip benzerliklerini karşılaştıran öneri mimarisi."
            },
            {
                "en": "approximate nearest neighbor (ANN)",
                "tr": "approximate nearest neighbor (ANN)",
                "definition": "Milyonlarca vektör arasında en benzerlerini, tam doğruluktan biraz ödün vererek çok hızlı bulma tekniği."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
