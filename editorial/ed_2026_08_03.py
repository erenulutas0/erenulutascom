"""3 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-03"

INTRO = "Bugünün ortak teması gecikme (latency) ve sınır çizmek: OpenAI ses sisteminde medya yolunu iş mantığından ayırıyor, Cloudflare Worker'lara ham TCP sokedi veriyor, Meta öneri modelini LLM ölçeğinde eğitirken hesap ile iletişimi birbirinden ayırmaya çalışıyor. Üçü de aynı dersi veriyor: hızlı sistemler, yavaş işi kritik yolun dışına atarak hızlanır."

DRAFTS = [
    {
        "url": "https://openai.com/index/continuous-voice-interaction-with-gpt-live",
        "slot": "cover",
        "title_tr": "Sesli AI'da altı ayda gerçek zamanlı mimari: sıra beklemeyi bırakmak",
        "difficulty": "orta",
        "tags": [
            "real-time systems",
            "latency",
            "architecture",
            "LLM"
        ],
        "summary": "İnsanlar konuşurken sırayı saniyenin küçük bir kesrinde devralır. Eski sesli asistanlar bunu yakalayamıyordu çünkü mimarileri sıra tabanlıydı (turn-based): önce küçük bir **turn detector** modeli \"kullanıcı sustu mu?\" diye karar veriyor, ancak ondan sonra büyük dil modeli çalışmaya başlıyordu. Erken karar verirse kullanıcının sözünü kesiyor, geç verirse sistem ağır hissettiriyordu.\n\nGPT-Live bu dedektörü ses yolundan tamamen çıkarmış. Model **full-duplex** çalışıyor: aynı anda hem dinliyor hem konuşuyor. Yani \"sıra kimde?\" kararı ayrı bir bileşenin tahmini olmaktan çıkıp modelin kendi işinin parçası oluyor.\n\nİşin mühendislik açısından asıl öğretici kısmı şu mimari karar: ses akışı ile uygulama mantığı iki ayrı yola ayrılmış. Ses, istemci ile model arasında kesintisiz bir **fast path**da (fast path) akıyor; araç çağırma, daha derin reasoning için GPT-5.5'e failover gibi işler ise **asenkron** bir yan yolda yürüyor. Böylece pahalı bir işlem sesin akışını durdurmuyor.\n\nBu ayrım olmadan sistem çalışmıyor, çünkü sürekli akışta tolerans yok: eski sıra tabanlı sistemde bir ses parçasının 50 ms geç gelmesi fark edilmezken, kesintisiz akışta aynı gecikme kulakta duyulabilir bir boşluk ya da cızırtı hâline geliyor.",
        "key_points": [
            "Turn detector'ı kaldırıp modeli full-duplex yapmak, \"tahmin et\" problemini tamamen ortadan kaldırıyor — çözülmesi zor bir problemi çözmek yerine yok etmek.",
            "Medya yolu ile kontrol yolu ayrıldı: ses kesintisiz akarken tool use ve model failover asenkron bir kanalda yürüyor.",
            "**Stateful inference** — model isteğe değil, oturuma bağlı. Bu, istekleri herhangi bir sunucuya dağıtmayı imkânsız kılıyor; yönlendirme oturum-farkında olmalı.",
            "Sürekli akışta hata bütçesi çok daha dar: taşıma, işleme ve inference’taki her gecikme doğrudan duyulabilir bir kusura dönüşüyor.",
            "Protokol seviyesine kadar inilmiş — ses taşıma katmanı da öngörülebilir gecikme için yeniden yazılmış."
        ],
        "why_it_matters": "\"Fast path / yavaş yol ayrımı\" bu yazının asıl dersi ve sesli AI'a özgü değil. Aynı desen ödeme sistemlerinde (yetkilendirme senkron, reconciliation asenkron), mesajlaşma uygulamalarında (mesaj iletimi senkron, bildirim ve arşivleme asenkron) ve arama sistemlerinde de aynı. Bir sistemi hızlandırmanın en güçlü yolu genellikle kodu optimize etmek değil, kritik yoldan iş çıkarmaktır.",
        "for_you": "Bir konuşma pratiği ya da sesli asistan özelliği tam olarak bu problemin küçük ölçekli hâli: kullanıcı konuşurken kaydı işleme, değerlendirme ve puanlama işlerinin hepsini cevap yolunda yaparsan uygulama ağır hisseder. Spring Boot tarafında kritik yolu ‘sesi al, akışı sürdür’ ile sınırlayıp değerlendirme, kayıt ve istatistik güncellemeyi bir kuyruğa (Redis Streams ya da basit bir async queue) atmak bu yazının doğrudan uygulaması olur. Bir de ‘stateful inference’ uyarısını not al: oturuma bağlı bir servisin önüne rastgele load balancer koyarsan oturumlar kopar; sticky routing gerekir.",
        "terms": [
            {
                "en": "full-duplex",
                "tr": "full-duplex",
                "definition": "Bir kanalın aynı anda hem veri alıp hem gönderebilmesi. Telsiz (sırayla) değil, telefon (aynı anda) gibi."
            },
            {
                "en": "turn detection",
                "tr": "turn detection",
                "definition": "Konuşmada karşı tarafın sözünü bitirip bitirmediğini tahmin eden bileşen."
            },
            {
                "en": "stateful inference",
                "tr": "stateful inference",
                "definition": "Modelin her isteği sıfırdan işlemeyip oturum boyunca biriken durumu koruması; ölçeklemeyi zorlaştırır çünkü istek belirli bir sunucuya bağlanır."
            },
            {
                "en": "fast path",
                "tr": "fast path",
                "definition": "Sistemde gecikmeye en duyarlı akış; buraya ek iş koymamak için özel olarak korunur."
            }
        ]
    },
    {
        "url": "https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/",
        "slot": "brief",
        "title_tr": "Meta reklam modelini LLM ölçeğinde eğitirken verimliliği ikiye katladı",
        "difficulty": "ileri",
        "tags": [
            "ML infrastructure",
            "GPU",
            "distributed training",
            "performance"
        ],
        "summary": "GEM, Instagram ve Facebook'un reklam önerilerini besleyen foundation model. Meta bunu binlerce GPU üzerinde eğitiyor ve 12 ayda toplam hesap gücünü 4 katına çıkarırken verimliliği (**MFU** — GPU'nun teorik kapasitesinin ne kadarının gerçekten kullanıldığı) %20-25'e, yani iki katına çıkarmış.\n\nYazının en çarpıcı iddiası şu: LLM'ler için optimize edilmiş altyapı öneri modellerine doğrudan aktarılamıyor. Sebebi veri: kullanıcı geçmişi kişiden kişiye çok değişken uzunlukta (**jagged input**), ve hepsini en uzun olana göre doldurmak hesabın %50'sine kadarını çöpe atıyor. Meta bu yüzden kendi çekirdek kütüphanesini yazmış (Jagged Flash Attention gibi) ve MXFP8 gibi çok düşük hassasiyetli sayı formatlarına inmiş.",
        "key_points": [
            "Ölçeklemek ≠ GPU eklemek: uçtan uca süre `max(hesap süresi, iletişim süresi)` ile belirleniyor, iletişim baskınsa yeni GPU'lar boş bekliyor.",
            "Reklam tahmini (CTR/CVR) sayısal olarak hassas; düşük hassasiyete naif geçiş model kalitesini bozuyor.",
            "Çözüm tek bir yerde değil: çekirdekler, sayı hassasiyeti, paralellik ve ağ topolojisi birlikte tasarlanmış."
        ],
        "for_you": "Bu yazıyı GPU sayısı için değil, **kaynak israfını ölçme alışkanlığı** için oku. ‘Padding yüzünden hesabın yüzde 50’si boşa gidiyor’ tespiti, değişken uzunluklu zaman serisi batch’lerinde birebir geçerli. PyTorch’ta değişken uzunluklu diziler için `pack_padded_sequence` ya da nested tensor kullanmak aynı israfı önler. Genel ders: bir işi hızlandırmadan önce kaç biriminin gerçekten işe yaradığını ölç.",
        "terms": [
            {
                "en": "MFU (Model FLOPs Utilization)",
                "tr": "MFU (Model FLOPs Utilization)",
                "definition": "GPU'nun teorik işlem kapasitesinin yüzde kaçının gerçekten faydalı hesaba gittiği. %20 bile büyük ölçekte iyi sayılır."
            },
            {
                "en": "jagged / ragged input",
                "tr": "jagged / ragged input",
                "definition": "Batch içindeki örneklerin farklı uzunlukta olması; sabit uzunluğa doldurulunca (padding) hesap israf edilir."
            }
        ]
    },
    {
        "url": "https://blog.cloudflare.com/grpc-workers/",
        "slot": "brief",
        "title_tr": "Cloudflare Workers artık ham TCP bağlantısı ve gRPC kabul ediyor",
        "difficulty": "orta",
        "tags": [
            "edge computing",
            "gRPC",
            "networking",
            "API"
        ],
        "summary": "Workers 2017'den beri HTTP dünyasında yaşıyordu. Şimdi `connect(socket)` adında yeni bir handler ile gelen ham **TCP** bağlantısını doğrudan alabiliyor. Bu soket bir Worker'dan diğerine, oradan bir Durable Object'e ve nihayetinde bir container içindeki sunucuya geçirilebiliyor.\n\nPratik sonucu: HTTP'ye sığmayan protokoller — gRPC'nin çift yönlü akışı, veritabanı protokolleri, özel binary protokoller — artık edge üzerinde çalışabiliyor. Yazıda Worker → Durable Object → Container zincirinin her adımı kısa kod örnekleriyle gösteriliyor.",
        "key_points": [
            "`connect(socket)` handler'ı soketi bir nesne gibi devredilebilir kılıyor; yönlendirme kararını kod veriyor.",
            "Worker'lar gRPC-web yazıp otomatik gRPC'ye çevrilebiliyor; tam çift yönlü akış için container gerekiyor.",
            "Şu an özel beta — üretim için değil, mimari fikir için okunmalı."
        ],
        "for_you": "gRPC backend mülakatlarında ‘REST mi gRPC mi?’ sorusuyla sık çıkıyor. Buradan alacağın net cevap şu: gRPC HTTP/2 ve TCP üstünde çalışır, asıl kazancı bidirectional streaming ve sıkı sözleşmedir (protobuf), ve tam da bu yüzden yalnızca HTTP destekleyen platformlarda çalıştırmak zordur. Mesajlaşma gibi gerçek zamanlı bir üründe WebSocket yerine gRPC streaming’i neden seçip seçmeyeceğini bu yazıdan sonra anlatabilirsin.",
        "terms": [
            {
                "en": "gRPC",
                "tr": "gRPC",
                "definition": "HTTP/2 üstünde çalışan, şema tabanlı (protobuf) ve akış destekli bir servisler-arası iletişim protokolü."
            },
            {
                "en": "Durable Object",
                "tr": "Durable Object",
                "definition": "Cloudflare'ın tekil, durum tutan hesaplama birimi; aynı anahtar hep aynı örneğe yönlenir."
            }
        ]
    },
    {
        "url": "https://blog.cloudflare.com/python-workers-rpc/",
        "slot": "brief",
        "title_tr": "Python ve JavaScript arasında şemasız RPC: tip sistemlerini köprülemek",
        "difficulty": "orta",
        "tags": [
            "RPC",
            "Python",
            "API",
            "interoperability"
        ],
        "summary": "Normalde iki farklı dilde yazılmış servisi konuşturmak için protobuf gibi dilden bağımsız bir serileştirme formatı seçersin, şema yazarsın, kod üretirsin. Cloudflare bu adımı tamamen atlıyor: TypeScript'te tanımlı bir metodu Python'dan doğrudan çağırabiliyorsun, şema yok, bağımlılık yok.\n\nYazının öğretici kısmı bunun nasıl mümkün olduğu. İki dilin tip sistemi farklı düşünüyor: JavaScript karmaşık parametreyi tek bir nesne olarak geçer, Python ise adlandırılmış argüman (keyword argument) kullanır. Köprü, Pyodide'nin FFI katmanı üzerinden bu farkı otomatik çeviriyor — JS `Date` nesnesi Python `datetime`'a dönüşüyor, fonksiyonlar iki yönde geçirilebiliyor, istisnalar çağrı noktasında fırlatılıyor.",
        "key_points": [
            "Şema yazmadan çapraz dil RPC — protobuf'un getirdiği bakım yükü ortadan kalkıyor.",
            "Çoğu durumda ağ üzerinden geçmiyor: çağrılan Worker aynı thread'de çalıştığı için maliyet neredeyse sıfır.",
            "Tip köprüleme kolay değil; asıl iş iki dilin çağrı geleneklerini eşlemekte."
        ],
        "for_you": "Sen zaten iki dilli çalışıyorsun: Java/Spring Boot backend + Python/LLM pipeline. Bugün bunları muhtemelen REST veya kuyrukla konuşturuyorsun. Bu yazı sana \"aradaki sınırın maliyeti nedir?\" sorusunu sordurmalı — serileştirme, şema bakımı, tip uyuşmazlığı. Kendi projende de aynı soruyu sor: Python tarafındaki kategorizasyon pipeline'ı ile Java servisi arasındaki sözleşmeyi kim koruyor, şema değişince ne kırılıyor?",
        "terms": [
            {
                "en": "RPC (Remote Procedure Call)",
                "tr": "RPC (Remote Procedure Call)",
                "definition": "Başka bir süreçteki/makinedeki fonksiyonu yerel fonksiyon gibi çağırma yöntemi."
            },
            {
                "en": "FFI (Foreign Function Interface)",
                "tr": "FFI (Foreign Function Interface)",
                "definition": "Bir dilin başka bir dilde yazılmış kodu çağırabilmesini sağlayan köprü katmanı."
            }
        ]
    },
    {
        "url": "https://cloud.google.com/blog/products/databases/unify-public-and-private-data-with-data-commons-on-spanner-graph/",
        "slot": "brief",
        "title_tr": "Cache katmanından graph veritabanına: Data Commons'ın mimari göçü",
        "difficulty": "orta",
        "tags": [
            "database",
            "graph",
            "RAG",
            "architecture"
        ],
        "summary": "Data Commons, BM'den Dünya Bankası'na 100+ kaynaktan gelen 400 milyar veri noktasını birleştiren açık bir knowledge graph. İlk kurulduğunda graph veritabanı teknolojisi olgun olmadığı için Bigtable üzerinde **önceden hesaplanmış cache** katmanıyla çalışıyordu.\n\nŞimdi Spanner Graph'a taşınmışlar ve kazanç listesi klasik bir \"cache borcu\" hikâyesi: önceden hesaplanan indeksler her güncellemede pahalı bir yeniden inşa gerektiriyordu; artık tek bir veri kümesini artımlı olarak güncelleyebiliyorlar. Ayrıca `kıta → ülke → il → ilçe` gibi çok adımlı gezinmeler sorgu anında yapılabiliyor — bu da **GraphRAG** akışlarının önünü açıyor.",
        "key_points": [
            "Önceden hesaplanmış cache hızlıdır ama güncellemeyi pahalılaştırır; bu takas her sistemde karşına çıkar.",
            "Çok adımlı ilişki sorgularını uygulama katmanında değil veritabanında yapmak kod karmaşıklığını ciddi düşürüyor.",
            "GraphRAG: modele düz metin parçaları yerine grafik üzerinde gezinerek toplanmış bağlam vermek."
        ],
        "for_you": "AI destekli doküman arama mimarisiyle doğrudan ilgili. Klasik RAG belgeleri parçalara bölüp embedding benzerliğiyle getirir ama ‘bu ihale hangi firmaya bağlı, o firmanın hangi belgeleri var?’ gibi ilişkisel sorularda benzerlik yetmez. Bu yazı ilişkinin kendisini modellemenin alternatifini gösteriyor. PostgreSQL kullanıyorsan Spanner’a geçmen gerekmez: recursive CTE ile aynı çok adımlı gezinmeyi yapabilirsin; önemli olan deseni tanımak.",
        "terms": [
            {
                "en": "knowledge graph",
                "tr": "knowledge graph",
                "definition": "Varlıkları node, aralarındaki ilişkileri kenar olarak tutan veri modeli."
            },
            {
                "en": "GraphRAG",
                "tr": "GraphRAG",
                "definition": "RAG'de bağlamı düz benzerlik yerine grafik üzerinde ilişkileri izleyerek toplama yöntemi."
            },
            {
                "en": "incremental update",
                "tr": "incremental update",
                "definition": "Tüm veriyi yeniden işlemek yerine yalnızca değişen kısmı güncelleme."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
