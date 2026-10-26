"""13 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-13"

INTRO = "Bugünün kapağı, bu arşivdeki en dürüst yazı olabilir: Netflix'in ilk sürümü yerel ortamda kusursuz çalışmış, üretimde ise her şey kırılmış — ve hepsini tek tek anlatıyorlar. Yanında Meta'nın çekirdek zamanlayıcısıyla 28% gecikme kazandığı yazı var; ikisi birlikte \"ölçek nedir\" sorusunun iyi bir cevabı."

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/building-service-topology-at-scale-architecture-challenges-and-lessons-learned-f4b792f3f0d8?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "\"Yerelde mükemmel çalıştı\": Netflix'in servis haritası üretimde nasıl kırıldı",
        "difficulty": "ileri",
        "tags": [
            "distributed systems",
            "observability",
            "Kafka",
            "performance"
        ],
        "summary": "Netflix'in mühendisleri servis bağımlılıklarının gerçek zamanlı ve birleşik bir görünümüne ihtiyaç duyuyordu: sorunları daha hızlı gidermek, bir arızanın **blast radius’u** (blast radius) anlamak ve dağıtık mimaride yol bulmak için. Çözüm çok kaynaklı: eBPF ağ akışları, IPC metrikleri ve distributed tracing (tracing) verileri, birbirinden fiziksel olarak ayrı grafik katmanlarında toplanıp ayrı ayrı ya da birleşik sorgulanabiliyor.\n\nAma yazının değeri mimaride değil, itirafta. Kendi cümleleriyle: **ilk sürüm yerel ortamda kusursuz çalıştı. Üretim başka bir hikâyeydi.** Sonra sayıyorlar: Kafka consumer’ları geride kaldı. Örnekler bellek yetersizliğine düştü. Bazı node’lar diğerlerinin **100 katı** trafik aldı. Çöp toplama (GC) duraklamaları, asıl iş mantığından daha fazla CPU tüketti.\n\nMimarideki temel karar **akış-öncelikli** (streaming-first) olmak. Geleneksel servis topolojisi sistemleri toplu işleme kullanır: veriyi saatlik ya da günlük toplar, sonra tam snapshot’ları saklar. Orta ölçekte çalışır ama temel bir sorunu vardır — veriyi gördüğünde zaten eskimiştir. Bir üretim arızası sırasında bu işe yaramaz. Netflix bunun yerine çok-bölgeli Kafka akışlarından akış kayıtlarını ve Sunucu Gönderimli Olaylar (SSE) üzerinden IPC metriklerini sürekli alıp reaktif pipeline'lardan geçiriyor.",
        "key_points": [
            "\"Bazı node’lar 100 kat trafik aldı\" — dağıtık sistemlerde en sinsi problem **sıcak nokta** (hot partition): ortalama iyi görünür, birkaç node yanar.",
            "GC duraklamalarının iş mantığından fazla CPU yemesi, JVM tabanlı yüksek hacimli sistemlerin klasik tuzağı.",
            "Toplu işleme yerine akış: arıza anında saatlik özet işe yaramaz, gerçek zamanlı gerekir.",
            "Katmanları fiziksel olarak ayırmak, her veri kaynağının bağımsız ölçeklenmesini ve sorgulanmasını sağlıyor.",
            "Yazı bir başarı hikâyesi değil, açıkça bir **öğrenme yolculuğu** olarak sunuluyor."
        ],
        "why_it_matters": "Yeni mezun bir mühendisin en zor öğrendiği şey, \"çalışıyor\" ile \"ölçekte çalışıyor\" arasındaki farktır. Bu yazı o farkı listeleyerek gösteriyor: aynı kod, aynı mantık — ama veri hacmi ve eşzamanlılık değişince tamamen farklı bir sistem. Bu tür açık sözlü yazılar, yıllarca üretim deneyimi olmadan öğrenilemeyecek şeyleri öğretir.",
        "for_you": "Bu yazıyı iki kere oku ve şu üç şeyi not al. **Bir:** hot partition problemi: veriyi anahtara göre bölümlediysen ve trafiğin yüzde 60’ı tek bir anahtardaysa o bölüm diğerlerinin katbekat yükünü taşır. Partition key seçerken dağılıma bak, isme değil. **İki:** consumer lag: bir kuyruk sisteminde en kritik metrik budur ve mutlaka alarma bağlanmalıdır; Redis Streams ya da Kafka fark etmez. **Üç:** GC: Java tarafında yüksek hacimli bir servis yazıyorsan GC log’larını açıp pause sürelerine bakmayı öğren. ‘Uygulama yavaş’ şikâyetlerinin şaşırtıcı bir kısmının cevabı orada.",
        "terms": [
            {
                "en": "blast radius",
                "tr": "blast radius",
                "definition": "Bir bileşen arızalandığında etkilenen diğer bileşenlerin kapsamı."
            },
            {
                "en": "eBPF",
                "tr": "eBPF",
                "definition": "Linux çekirdeğinde güvenli şekilde kod çalıştırıp ağ ve sistem olaylarını gözlemlemeyi sağlayan teknoloji."
            },
            {
                "en": "consumer lag",
                "tr": "consumer lag",
                "definition": "Bir kuyruk consumer’ının, üretilen mesajların ne kadar gerisinde kaldığı; kuyruk sistemlerinin en kritik sağlık metriği."
            },
            {
                "en": "hot partition",
                "tr": "hot partition",
                "definition": "Yükün dengesiz dağılması sonucu diğerlerinden kat kat fazla trafik alan bölüm ya da node."
            },
            {
                "en": "garbage collection (GC) pause",
                "tr": "garbage collection (GC) pause",
                "definition": "JVM'in kullanılmayan belleği temizlerken uygulamayı kısa süre durdurması; sık olursa gecikmeyi ciddi bozar."
            }
        ]
    },
    {
        "url": "https://engineering.fb.com/2026/07/13/ml-applications/modernizing-the-meta-ads-service-with-an-open-source-kernel-scheduler/",
        "slot": "brief",
        "title_tr": "Çekirdek zamanlayıcısını değiştirerek p99 latency’de %28 kazanç",
        "difficulty": "ileri",
        "tags": [
            "Linux",
            "performance",
            "latency",
            "infrastructure"
        ],
        "summary": "Meta'nın reklam sunum filosu saniyede ortalama **5 milyondan fazla** istek işliyor — günde 400 milyarın üzerinde. Bu ölçekte birkaç milisaniyelik gecikme bozulması ciddi iş etkisi yaratıyor.\n\nProblem bir Linux çekirdek yükseltmesiyle çıkmış: v6.6'da gelen **EEVDF** zamanlayıcısı, reklam sunumunda gecikme regresyonuna ve sıralanan reklam sayısında düşüşe yol açmış. Çözüm için **sched_ext**'e gitmişler — çekirdek v6.12'de resmen giren, BPF tabanlı genişletilebilir zamanlayıcı çerçevesi. Yani zamanlama politikasını bir BPF programı olarak yazıp iş yüküne özel hâle getiriyorsun; çekirdek olaylar üzerinden bu programa çağrı yapıyor (thread uyanması, kuyruğa alma, dağıtım).\n\nSonuçlar somut: reklam getirme aşamasında **p99 gecikmede %28 azalma**, **3,28 megawatt** güç tasarrufu ve sıralanan reklam sayısında %1,1 artış.",
        "key_points": [
            "Genel amaçlı bir zamanlayıcı iyileştirmesi, belirli bir iş yükü için regresyon olabilir — \"daha iyi\" her zaman bağlama bağlıdır.",
            "sched_ext, Google'ın ghOSt yazarlarıyla ortak tasarlanıp upstream Linux'a girmiş; yani bu bir Meta içi çatal değil, herkesin kullanabileceği bir çerçeve.",
            "Güç tasarrufunun metrik olarak raporlanması, ölçekte performansın aynı zamanda bir enerji meselesi olduğunu gösteriyor."
        ],
        "for_you": "Çekirdek zamanlayıcısı yazmayacaksın, ama iki fikri al. Birincisi **p99 kavramı**: ortalama gecikme yalan söyler, kullanıcı deneyimini belirleyen consumer lag’dır. Kendi API'nde ortalama değil p95/p99 ölç — Spring Boot Actuator + Micrometer ile birkaç satırda çıkar. İkincisi: bir bağımlılığı yükselttiğinde performansın **iyileşeceğini varsayma**. Meta gibi ölç. Küçük ölçekte bile bir kütüphane sürümü yükseltmesinden sonra temel bir benchmark koşturmak, seni ileride günlerce hata avından kurtarır.",
        "terms": [
            {
                "en": "p99 latency",
                "tr": "p99 latency",
                "definition": "İsteklerin %99'unun altında kaldığı süre; en yavaş %1'i temsil eder ve kullanıcı deneyimini ortalamadan çok daha iyi anlatır."
            },
            {
                "en": "scheduler",
                "tr": "scheduler",
                "definition": "İşletim sisteminde hangi işin hangi CPU'da ne zaman çalışacağına karar veren çekirdek bileşeni."
            },
            {
                "en": "BPF",
                "tr": "BPF",
                "definition": "Çekirdek içinde güvenli, doğrulanmış küçük programlar çalıştırmayı sağlayan mekanizma."
            }
        ]
    },
    {
        "url": "https://blog.cloudflare.com/introducing-precursor/",
        "slot": "brief",
        "title_tr": "Bot fare hareketini taklit edemiyor: bilek fiziği bir sinyal",
        "difficulty": "orta",
        "tags": [
            "security",
            "bot tespiti",
            "signal design"
        ],
        "summary": "Cloudflare, oturum bazlı istemci tarafı doğrulama sistemi Precursor'ı duyuruyor. Mevcut durum şu: Turnstile günde yaklaşık 3 milyar kez çalışıyor ama yalnızca kritik anlarda (giriş, kayıt, ödeme). Bu, uygulamanın geri kalanında — insanların ve botların tüm kullanıcı yolculuğu boyunca nasıl etkileştiğinde — bir görünürlük boşluğu bırakıyor.\n\nYazının en keyifli kısmı sinyal tasarımı. Bir bot geliştiricisi fare hareketini insan gibi göstermeye çalıştığında genelde Gauss gürültüsü ya da rastgele gecikmeler ekliyor. Ama insan hareketi sadece \"gürültülü\" değil, **fizikle kısıtlı**: insan fare hareketi çoğu zaman bir yaydır — bileğin hareket açısı ve önkolun dönüşüyle sınırlıdır. Ayrıca bilişsel yük var: bir insanın onay kutusunu görmesiyle tıklaması arasında ölçülebilir bir gecikme oluyor.",
        "key_points": [
            "İyi bir sinyal taklit edilmesi zor olandır; rastgelelik eklemek fiziksel kısıtları taklit etmez.",
            "Tek bir ana bakmak yerine tüm oturumu değerlendirmek, her karara çok daha fazla sinyal katıyor."
        ],
        "for_you": "Buradaki düşünce biçimi genel: **sahtesi yapılması zor olan sinyali seç.** Kendi sistemlerinde de aynı soruyu sor: abonelik doğrulamasını istemciden gelen bir bayrağa bakarak mı yapıyorsun? O taklit edilebilir. Sunucu tarafında mağaza makbuzunu (receipt) doğrulamak taklit edilemez. Genel kural: güvenlik kararını, saldırganın kontrol ettiği bir veriye dayandırma. Bir de privacy tarafına dikkat et: davranışsal sinyal toplamak güçlü bir araç ama toplanan verinin kapsamı ve saklama süresi açıkça tanımlanmalı.",
        "terms": [
            {
                "en": "behavioral signal",
                "tr": "behavioral signal",
                "definition": "Kullanıcının etkileşim biçiminden (hareket, zamanlama, sıra) çıkarılan, kimlik doğrulamaya yardımcı veri."
            },
            {
                "en": "bot mitigation",
                "tr": "bot mitigation",
                "definition": "Otomatik istemcileri tespit edip engelleme ya da sürtünme ekleme pratiği."
            }
        ]
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/unlocking-the-future-of-video-data-march-networks-cloud-storage-on-aws/",
        "slot": "brief",
        "title_tr": "Petabyte'larca video: kısmi göç bile maliyeti ciddi düşürüyor",
        "difficulty": "başlangıç",
        "tags": [
            "storage",
            "cost",
            "cloud",
            "architecture"
        ],
        "summary": "Kurumsal video gözetim sistemleri binlerce lokasyonda petabyte'larca veri üretiyor. Klasik model her sahada yerel kayıt cihazları ve sunucular — yerel kontrol sağlıyor ama parçalı depolama ortamları yaratıyor ve sık donanım genişletmesi gerektiriyor. Saklama süreleri uyumluluk ve sorumluluk gerekçeleriyle uzadıkça altyapı ihtiyacı hızla büyüyor.\n\nMarch Networks çözümü S3 ve S3 Glacier üzerine kurmuş. Yazının en pratik gözlemi şu: **kısmi göç bile işe yarıyor** — yalnızca uzun vadeli saklama ve uyumluluk arşivlerini buluta taşımak bile altyapı maliyetini ciddi düşürüyor.",
        "key_points": [
            "Sıcak veri (son günler, sık erişilen) ile soğuk veri (arşiv) farklı depolama katmanlarına ait; ikisini aynı yerde tutmak pahalı.",
            "Göç bir \"ya hep ya hiç\" kararı değil — en pahalı ve en az erişilen dilimle başlamak en yüksek getiriyi verir."
        ],
        "for_you": "Storage tiering fikrini küçük projelerde de kullan. Geçmiş verin muhtemelen tek bir yerde duruyor ama son 3 ayın verisine erişim sıklığın ile 2 yıl önceki veriye erişim sıklığın aynı değil. Eski veriyi sıkıştırılmış Parquet olarak ucuz depolamada, sıcak veriyi hızlı diskte tutmak hem maliyeti hem sorgu süresini düşürür. Aynı mantık PostgreSQL’de table partitioning ile de kurulabilir: eski partition’ları ayrı bir tablespace’e alabilirsin.",
        "terms": [
            {
                "en": "storage tiering",
                "tr": "storage tiering",
                "definition": "Veriyi erişim sıklığına göre farklı maliyet/hız seviyelerindeki depolama katmanlarına yerleştirme."
            },
            {
                "en": "cold storage",
                "tr": "cold storage",
                "definition": "Nadiren erişilen veri için kullanılan, çok ucuz ama erişimi yavaş depolama sınıfı."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
