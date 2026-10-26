"""17 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-17"

INTRO = "Günün kapağı arşivin en iyi yazılarından: Netflix, LLM'leri hazır API'lerden tüketmek yerine tüm yığını kendisi işletiyor ve hangi kararda neyi neden seçtiğini — üretimde nelerin tasarım aşamasında öngörülemediği dahil — açıkça anlatıyor. Bu tür \"kararların gerekçesi\" yazıları nadirdir."

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "Netflix LLM sunumunu neden kendi işletiyor — ve hangi takasları yaptı",
        "difficulty": "ileri",
        "tags": [
            "LLM",
            "infrastructure",
            "architecture",
            "GPU"
        ],
        "summary": "Çoğu kurum LLM'leri barındırılan API'ler üzerinden tüketiyor. Netflix daha ileri gitmiş: model dağıtımından inference’a kadar tüm yığını kendisi işletiyor — ve bunu ayrı bir ML silosunda değil, **mevcut üretim ortamının içinde** yapıyor. Yazının değeri de burada: sadece ne kurduklarını değil, neden öyle kurduklarını ve üretimin tasarım aşamasında görülmeyen neyi ortaya çıkardığını anlatıyor.\n\nMimari şöyle: üye ölçeğindeki ML, uçtan uca akışı yöneten **JVM tabanlı** birleşik bir sunum sistemiyle karşılanıyor — yönlendirme ve A/B testi mantığı, aday üretimi, özellik çekme, inference, son işleme ve her aşamada loglama. Çağıranlar inference’a iki yoldan ulaşıyor: bu sistem üzerinden **gRPC**, ya da yeni LLM tabanlı uygulamaların kullandığı doğrudan **HTTP** yolu.\n\nInference’ın nerede çalıştığı modele bağlı. Küçük CPU modelleri **süreç içinde** çalışıyor — uzak çağrı maliyeti ödenmiyor. Büyük modeller GPU istiyor; sunum sistemi ön ve son işlemeyi yerelde yapıp inference’ı uzak bir servise devrediyor. Motor olarak **vLLM** seçilmiş, üstünde Triton, onun da üstünde dağıtım, sürümleme, sağlık kontrolü, autoscaling ve çok-bölgeli yayılımı yöneten bir Java control plane var.\n\nYazı dört kararı bağımlılık sırasına göre işliyor — motor, paketleme, API yüzeyi ve yayılım — çünkü her biri bir sonrakini kısıtlıyor. Bu sıralama tek başına iyi bir mimari dersi.",
        "key_points": [
            "Küçük model süreç içinde, büyük model uzak GPU'da: tek bir dağıtım stratejisi yerine model boyutuna göre farklı yollar.",
            "İki API yüzeyi bir arada yaşıyor: eski consumer’lar için gRPC, yeni LLM uygulamaları için doğrudan HTTP.",
            "Kararlar bağımsız değil — motor seçimi paketlemeyi, paketleme API yüzeyini, o da yayılım stratejisini kısıtlıyor.",
            "Output constraints’in uygulanması (output constraints enforcement) ayrı bir tasarım başlığı olarak ele alınmış — modelin serbest metin üretmesine güvenilmiyor."
        ],
        "why_it_matters": "\"Kendimiz mi işletelim, hazır API mi kullanalım?\" sorusu her ekibin önüne gelecek. Netflix'in cevabı herkes için doğru değil — ölçekleri ve mevcut altyapıları bu kararı mantıklı kılıyor. Ama yazının aktardığı düşünme biçimi evrensel: kararları bağımsız seçimler gibi değil, birbirini kısıtlayan bir zincir olarak görmek.",
        "for_you": "Bu yazıyı bir mimari kontrol listesi gibi kullan. LLM çağrılarını bir backend’den yapıyorsan Netflix’in sorduğu soruların küçük ölçekli hâlini sen de sorabilirsin: **(1) API yüzeyi:** istemci doğrudan mı çağırıyor, yoksa backend üzerinden mi? Doğrudan çağırırsa API key istemcide olur, yapma. **(2) Rollout:** model ya da prompt değiştiğinde tüm kullanıcılara birden mi gidiyor? A/B testi ya da kademeli açılış var mı? **(3) Output constraint:** modelin döndürdüğü şeyi şemayla doğruluyor musun? Netflix’in ayrıca ele aldığı şey tam olarak bu ve her pipeline’da en kritik korumadır.",
        "terms": [
            {
                "en": "vLLM",
                "tr": "vLLM",
                "definition": "Büyük dil modellerini yüksek verimle sunmak için tasarlanmış açık kaynak inference motoru."
            },
            {
                "en": "control plane",
                "tr": "control plane",
                "definition": "Sistemin ne çalıştıracağına, nerede ve hangi sürümle karar veren yönetim katmanı; veriyi işleyen katmandan (data plane) ayrıdır."
            },
            {
                "en": "gRPC",
                "tr": "gRPC",
                "definition": "HTTP/2 üstünde çalışan, şema tabanlı servisler-arası çağrı protokolü."
            },
            {
                "en": "output constraints",
                "tr": "output constraints",
                "definition": "Modelin yalnızca belirli bir şemaya ya da biçime uyan çıktı üretmesini zorlayan mekanizma."
            }
        ]
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/eclipse-dataspace-components-on-aws-cost-optimization-strategies/",
        "slot": "brief",
        "title_tr": "Bulut maliyetini tahmin etmek: varsayımları yazmadan hesap yapılmaz",
        "difficulty": "orta",
        "tags": [
            "cost",
            "cloud",
            "architecture"
        ],
        "summary": "AWS'in üç bölümlük Eclipse Dataspace Components serisinin son yazısı; performans verimliliği, maliyet optimizasyonu ve sürdürülebilirlik üzerine. Ürün özelinden bağımsız olarak öğretici kısmı **yöntem**: hangi AWS servislerinin maliyeti sürüklediğini belirliyor, aylık maliyeti kritik ve kritik olmayan iş yükleri için ayrı ayrı tahmin ediyor ve harcamayı **%58'e kadar** düşüren stratejiler sunuyor.\n\nEn değerli parça, sayılara geçmeden önce açıkça listelenen varsayımlar tablosu: katılımcı başına 5 GB veri (6 aylık geçmiş ve yedekler dahil), ayda 20 GB ağ trafiği, ayda 100.000 API çağrısı, ayda 1.000 OAuth token isteği — ve her birinin gerekçesi.",
        "key_points": [
            "Maliyet tahmini varsayım listesi olmadan anlamsızdır; varsayımlar yazılınca tartışılabilir hâle gelir.",
            "Kritik ve kritik olmayan iş yüklerini ayrı fiyatlamak, gereksiz yüksek erişilebilirlik harcamasını önlüyor."
        ],
        "for_you": "Bir projeyi buluta taşımadan önce bu tabloyu taklit et. ‘Aylık kaç istek, kaç GB veri, kaç GB çıkış trafiği?’ sorularını yazıp gerekçeleriyle bir kenara koy. Elindeki veriyi (örneğin 1 TB) S3’e koysan aylık maliyeti ne olurdu, sorgu başına kaç GB taranırdı? Bu hesabı yapabilmek, bulut faturasının neden şiştiğini anlamanın tek yolu. Ayrıca en pahalı kalem genelde hesaplama değil **veri çıkışıdır** (egress); bunu bilmek çoğu mimari kararı değiştirir.",
        "terms": [
            {
                "en": "egress cost",
                "tr": "egress cost",
                "definition": "Buluttan dışarı çıkan veri için ödenen ücret; genelde depolama ve hesaplamadan daha pahalıya patlar."
            },
            {
                "en": "Well-Architected Framework",
                "tr": "Well-Architected Framework",
                "definition": "AWS'in bulut mimarilerini güvenlik, güvenilirlik, performans, maliyet ve operasyon eksenlerinde değerlendirme rehberi."
            }
        ]
    },
    {
        "url": "https://blog.cloudflare.com/wordpress-vulnerabilities/",
        "slot": "brief",
        "title_tr": "WAF kuralı yama değildir: iki WordPress açığı ve doğru tepki sırası",
        "difficulty": "başlangıç",
        "tags": [
            "security",
            "WAF",
            "vulnerability"
        ],
        "summary": "Cloudflare, WordPress'teki iki kritik açık için WAF koruması açtı: REST API'de **kimlik doğrulamasız uzaktan kod çalıştırma** (RCE) ve ilişkili bir **SQL enjeksiyonu**. WordPress güvenlik ekibi açıkları kamuya duyurmadan önce Cloudflare'e bildirmiş, böylece koruma hazır olmuş; kurallar 17 Temmuz 17:03 UTC'de tüm müşterilere (ücretsiz planlar dahil) açılmış.\n\nYazının en önemli cümlesi bir uyarı: **WAF korumaları müşteriler güncellerken maruziyeti azaltır, ama yamanın yerine geçmez.** Sürüm detayı da öğretici — SQL enjeksiyonu 6.8'den itibaren var, RCE ise yalnızca 6.9'dan itibaren. Bu yüzden 6.8.6 sadece SQLi'yi düzeltiyor, 6.9.5 ve 7.0.2 ikisini birden.",
        "key_points": [
            "Doğru sıra: WAF ile geçici koruma → yamayı uygula → sürümü doğrula. İlk adımda durmak yaygın bir hata.",
            "RCE yalnızca kalıcı nesne cache’i (persistent object cache) kullanılmadığında tetikleniyor — açıkların koşullu olması yaygındır."
        ],
        "for_you": "Buradan alınacak iki refleks var. Birincisi: bağımlılıklarını güncel tut — Dependabot ya da Renovate'i projelerine bugün kur, GitHub Actions ile zaten çalışıyorsun. İkincisi: SQL enjeksiyonu 2026'da hâlâ kritik açık listesinde. Sen JPA/Hibernate kullanıyorsun ama `@Query` içinde string birleştirme yaptığın her yer bir risk; her zaman parametreli sorgu kullan. Pandas/psycopg tarafında da aynısı — f-string ile SQL kurmak, kod incelemesinde reddedilmesi gereken bir desendir.",
        "terms": [
            {
                "en": "RCE (Remote Code Execution)",
                "tr": "RCE (Remote Code Execution)",
                "definition": "Saldırganın hedef sunucuda kendi kodunu çalıştırabilmesi; en yüksek önem derecesindeki açık türü."
            },
            {
                "en": "WAF (Web Application Firewall)",
                "tr": "WAF (Web Application Firewall)",
                "definition": "Uygulamaya gelen istekleri inceleyip zararlı desenleri engelleyen katman."
            },
            {
                "en": "CVE",
                "tr": "CVE",
                "definition": "Bilinen güvenlik açıklarına verilen standart tanımlayıcı numara."
            }
        ]
    },
    {
        "url": "https://openai.com/index/a-scorecard-for-the-ai-age",
        "slot": "brief",
        "title_tr": "Token başına maliyet yanlış metrik: başarılı sonuç başına maliyet",
        "difficulty": "başlangıç",
        "tags": [
            "cost",
            "LLM",
            "measurement",
            "product"
        ],
        "summary": "Yazının merkezinde bir metrik eleştirisi var. Yıllarca yazılımın başarısı benimsenme ile ölçüldü: alınan lisans, aktif kullanıcı, yenilenen abonelik. AI'da bu yetmiyor; ölçülmesi gereken **tamamlanan iş**.\n\nKilit argüman şu: **token başına maliyete bakmak yanıltıcıdır.** Daha ucuz bir modelin token'ı ucuz olabilir, ama iyi sonuç için daha çok deneme, daha çok zaman ve daha çok insan incelemesi gerekebilir. Daha yetenekli bir modelin token'ı pahalıdır ama aynı işi tek seferde bitirebilir. Önemli olan **başarılı bir sonucu üretmenin tam maliyeti**.\n\nPratik tavsiye de net: tek bir workflow’la başla, \"bitti\" ne demek tanımla ve o sonucu işin gerçekten yapıldığı sistemde ölç. Destek ekibi için \"bitti\" çözülen bir müşteri sorunudur; mühendislik ekibi için testleri geçen bir kod değişikliği.",
        "key_points": [
            "Dört soru: AI önemli bir iş mi tamamlıyor, her başarılı görev ne kadara mal oluyor, sonuca güvenilebiliyor mu, kullanım arttıkça birim değer artıyor mu?",
            "\"Bitti\" tanımını yapmadan ölçüm yapılamaz — bu, AI'dan bağımsız olarak da doğru."
        ],
        "for_you": "Kendi LLM pipeline’ında uygulanabilir bir ölçü: ‘özet başına maliyet’ değil, ‘elden geçirilmeden kullanılabilen çıktı başına maliyet’. Ucuz bir modelle beş kere deneyip düzeltmek, pahalı bir modelle bir kerede almaktan pahalı olabilir. Aynı hesabı bir değerlendirme özelliğinde de yap: kullanıcının düzeltmeden kabul ettiği çıktı oranı, token fiyatından çok daha anlamlı bir metriktir.",
        "terms": [
            {
                "en": "cost per successful outcome",
                "tr": "cost per successful outcome",
                "definition": "Bir işi gerçekten bitirmenin toplam maliyeti — başarısız denemeler ve insan düzeltmesi dahil."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
