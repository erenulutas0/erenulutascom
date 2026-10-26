"""31 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-31"

INTRO = "Bugünün ortak sorusu \"aynı veriye iki farklı iş yükü nasıl erişir?\" Cloudflare bunu ağ protokolü seviyesinde çözüyor, Databricks veritabanı seviyesinde, Netflix ise analitik veri modelleme seviyesinde. Üçünü arka arkaya okuyunca aynı problemin farklı katmanlardaki hâli olduğu görülüyor."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/moq-relays/",
        "slot": "cover",
        "title_tr": "MoQ: canlı video, görüntülü arama ve mesajlaşmayı tek protokole indirmek",
        "difficulty": "orta",
        "tags": [
            "networking",
            "protocol",
            "real-time systems",
            "latency"
        ],
        "summary": "**MoQ** (Media over QUIC), IETF'te geliştirilen açık bir protokol — HTTP, TLS ve QUIC'i de standartlaştıran kurum. Cloudflare geçen yıl MoQ'yu tüm sunucularında açmıştı; şimdi eksik olan parçayı ekliyor: izolasyon ve erişim kontrolü. Yeni sağlama API'siyle uygulamana özel bir relay (relay) oluşturup yayıncılar ve aboneler için ayrı kimlik bilgileri verebiliyorsun.\n\nProtokolün modeli basit ve öğretici: bir **publish/subscribe** (publish/subscribe) sistemi. Yayıncı isimlendirilmiş veri akışları gönderir, aboneler o akışları isimle ister. Aralarında relay’ler durur — bunlar sadece her akışı isteyen herkese kopyalayan CDN sunucuları. Kritik nokta: **relay verinin içine hiç bakmaz.**\n\nBu tek tasarım kararı büyük bir sonuç doğuruyor. Relay’ler içeriği umursamadığı için, eskiden her biri ayrı bir sistem gerektiren şeyler — canlı video, görüntülü arama, düşük gecikmeli mesajlaşma — aynı protokolün üstünde taşınabiliyor. Altta HTTP/3'ün taşıma katmanı olan QUIC var; gecikmeyi düşük tutan da o.\n\nPratik sonuç: kendi özel sunucu filonu kurup işletmene gerek kalmıyor. Tek bir API üzerinden bir CDN'e yayın yapıyor, hem düşük gecikme hem büyük ölçeği çok daha ucuza alıyorsun.",
        "key_points": [
            "Relay içeriğe bakmaz — bu \"aptal ara katman\" kararı, protokolün genel amaçlı olmasını sağlayan şey.",
            "Publish/subscribe modeli isimlendirilmiş akışlar üzerinden çalışıyor; abone akışı adıyla istiyor.",
            "QUIC üstünde çalışıyor: TCP'nin head-of-line blocking (head-of-line blocking) sorunu olmadan düşük gecikme.",
            "Şu an beta ve ücretsiz; draft-14 ve draft-16 sürümleri destekleniyor — yani protokol hâlâ hareket hâlinde."
        ],
        "why_it_matters": "\"Ara katman veriyi anlamasın\" ilkesi, dayanıklı sistem tasarımının en güçlü kurallarından biri. İçeriği anlamayan bir bileşen, içerik değiştiğinde bozulmaz; genel amaçlı kalır ve ölçeklemesi kolaylaşır. Aynı ilkeyi mesaj kuyruklarında, load balancer’larda ve proxy'lerde de görürsün — MoQ bunun canlı medyaya uygulanmış hâli.",
        "for_you": "Bir mesajlaşma uygulamasında muhtemelen WebSocket kullandın. Bu yazı o kararı sorgulatacak bir karşılaştırma veriyor: WebSocket TCP üstünde tek bir akıştır, bir paket kaybolduğunda arkasındaki her şey bekler (head-of-line blocking). QUIC bunu bağımsız akışlarla çözer. Ayrıca publish/subscribe modelini kendi sistemine taşıyabilirsin: mesajları doğrudan alıcıya itmek yerine bir kanala yayınlamak, grup mesajlaşmasını ve çoklu cihaz senkronizasyonunu ciddi şekilde basitleştirir. Redis Pub/Sub ile aynı deseni bugün deneyebilirsin.",
        "terms": [
            {
                "en": "publish/subscribe (pub/sub)",
                "tr": "publish/subscribe (pub/sub)",
                "definition": "Göndericinin alıcıyı bilmediği, mesajların isimlendirilmiş kanallara yayınlandığı iletişim modeli."
            },
            {
                "en": "relay",
                "tr": "relay",
                "definition": "Veriyi kaynaktan alıp isteyen herkese kopyalayan ara sunucu; içeriği yorumlamaz."
            },
            {
                "en": "QUIC",
                "tr": "QUIC",
                "definition": "UDP üstünde çalışan, HTTP/3'ün taşıma katmanı olan protokol; bağımsız akışlarla head-of-line blocking’i önler."
            },
            {
                "en": "head-of-line blocking",
                "tr": "head-of-line blocking",
                "definition": "Sıradaki ilk paket geciktiğinde arkasındaki tüm paketlerin beklemek zorunda kalması."
            }
        ]
    },
    {
        "url": "https://www.databricks.com/blog/backstage-lakebase-part-3",
        "slot": "brief",
        "title_tr": "Aynı Postgres'e iki kimlik doğrulama yolu: bedeli olan bir uzlaşma",
        "difficulty": "orta",
        "tags": [
            "database",
            "PostgreSQL",
            "authentication",
            "data engineering"
        ],
        "summary": "Databricks, geliştirici portalı Backstage'i Lakebase (yönetilen Postgres) üzerinde çalıştırma serisinin üçüncü bölümünde işletim verisiyle analitik veriyi birleştiriyor. Normal bir kurulumda \"bulut maliyetimizi hangi altyapı yaratıyor ve sahibi kim?\" sorusu iki sınır geçiyor: sahiplik grafiği Backstage'de, maliyet verisi veri ambarında. Cevap için ETL, Jira kaydı ya da Slack mesajı gerekiyor.\n\nAsıl öğretici kısım gizlenmemiş bir zorluk: Lakehouse Federation'ın Postgres bağlayıcısı yalnızca statik kullanıcı/parola destekliyor, oysa Lakebase uygulama kimliklerini OAuth ile doğruluyor. Çözüm, ayrı bir SCRAM-SHA-256 Postgres rolü açmak. Sonuç, yazarların kendi cümlesiyle: **artık aynı veritabanı için iki ayrı kimlik doğrulama yolu yönetiyorsun.**",
        "key_points": [
            "İş yükü başına ayrılan hesaplama sayesinde FinOps analisti ağır sorgular çalıştırırken canlı portal etkilenmiyor (katalog sorguları 55-65 ms).",
            "Ürün dokümantasyonunda nadir görülen bir dürüstlük: geçici çözümün yarattığı bakım borcu açıkça yazılmış."
        ],
        "for_you": "‘Operasyonel veritabanına analitik sorgu atmak’ sorusu her projede çıkar. Canlı veri yazan tabloya ağır bir analiz sorgusu attığında yazma gecikmesinin nasıl bozulduğunu muhtemelen gördün. PostgreSQL’de bunun karşılığı bir **read replica** kurup analitik sorguları oraya yöneltmek. Yazının ikinci dersi daha genel: bir entegrasyonu kurmak için ikinci bir authentication yolu açmak zorunda kalıyorsan bu geçici çözümü kodun içine gömme; belgele, çünkü bir yıl sonra ‘bu rol niye var?’ diye soran sen olacaksın.",
        "terms": [
            {
                "en": "federation",
                "tr": "federation",
                "definition": "Farklı sistemlerdeki veriyi taşımadan, tek bir sorgu arayüzünden birlikte sorgulama."
            },
            {
                "en": "read replica",
                "tr": "read replica",
                "definition": "Ana veritabanının salt-okunur kopyası; ağır okuma sorgularını asıl sistemden ayırmak için kullanılır."
            }
        ]
    },
    {
        "url": "https://netflixtechblog.com/modeling-device-capabilities-for-analytics-e7607acebde8?source=rss----2615bd06b42e---4",
        "slot": "brief",
        "title_tr": "Netflix cihaz yeteneklerini analitik için nasıl modelliyor",
        "difficulty": "başlangıç",
        "tags": [
            "veri modelleme",
            "analitik",
            "data engineering"
        ],
        "summary": "Netflix 4K'dan bulut oyunculuğuna kadar geniş bir özellik yelpazesini çok çeşitli cihazlarda sunuyor — ama her cihaz aynı değil. RAM, CPU çekirdek sayısı, ekran yetenekleri ve platform desteği bazı özelliklerin belirli modellerde çalışamayacağı anlamına geliyor.\n\nÇözüm iki tablo deseni: **kümülatif tablo** her cihazın en güncel yetenek durumunu tutuyor (ekran boyutu, desteklenen video profilleri gibi). **Histogram tablosu** ise son 28 günün aktif cihaz sayılarını model ve yazılım sürümüne göre kırıyor, ve belirli bir yeteneği destekleyen cihaz oranını veriyor: örneğin \"playready %100, hevc %20\".",
        "key_points": [
            "İki farklı soru, iki farklı tablo: \"bu cihaz neyi destekliyor?\" ile \"kaç cihaz bunu destekliyor?\" aynı şemayla verimli cevaplanmıyor.",
            "Yetenek verisiyle feature flag'leri birleştirmek, özelliğin ne kadar yayıldığını (feature penetration) ölçmeyi mümkün kılıyor."
        ],
        "for_you": "Kısa bir yazı ama içindeki desen çok kullanışlı: **mevcut durum tablosu** ile **zaman içinde aggregate edilmiş tabloyu** ayırmak. ‘Bu kullanıcının aboneliği aktif mi?’ ile ‘son 28 günde kaç kullanıcı pratik yaptı?’ sorularını aynı tablodan cevaplamaya çalışırsan ikisi de yavaşlar. Birincisi index’li tekil okuma, ikincisi önceden aggregate edilmiş bir özet tablo ister. Bu ayrım OLTP/OLAP ayrımının en küçük ve en pratik hâli.",
        "terms": [
            {
                "en": "cumulative table",
                "tr": "cumulative table",
                "definition": "Her varlığın en güncel durumunu tutan, sürekli güncellenen tablo."
            },
            {
                "en": "feature flag",
                "tr": "feature flag",
                "definition": "Bir özelliği kod dağıtmadan açıp kapatmayı sağlayan konfigürasyon anahtarı."
            }
        ]
    },
    {
        "url": "https://openai.com/index/building-abundant-intelligence",
        "slot": "brief",
        "title_tr": "Zeka ucuzlayınca ne değişir: model seçimi bir maliyet kararıdır",
        "difficulty": "başlangıç",
        "tags": [
            "LLM",
            "cost",
            "product"
        ],
        "summary": "OpenAI'ın altyapı ve fiyatlandırma üzerine yazısı. Ana tez basit: AI altyapısı büyük olduğu için değil, mümkün kıldığı şey yüzünden değerli. Faydalı zekânın maliyeti düştükçe, yapılmaya değer iş miktarı artıyor.\n\nSomut kısım fiyat değişikliği: GPT-5.6 Luna'nın fiyatı %80, Terra'nın %20 düşürülmüş. Luna artık milyon girdi token'ı başına 0,20 dolar. Fast mode ise iki katı fiyata 2,5 kata kadar hız veriyor — zekâda değişiklik yok.\n\nYazının en kullanışlı cümlesi bir soru yeniden çerçevelemesi: \"hangi model hangi göreve ait?\" yanlış soru. Doğru soru şu — **bu sonuç ne kadar zekâ gerektiriyor, ne kadar hızlı gerekiyor, ve maliyeti ne olmalı?**",
        "key_points": [
            "Aynı model ailesinde hız ve fiyat ayrı eksenler; zekâyı düşürmeden hız satın alabiliyorsun.",
            "Model seçimi bir mimari karar değil, iş yükü başına verilen bir maliyet-gecikme-kalite kararı."
        ],
        "for_you": "Bu tam olarak bir LLM pipeline’ında vereceğin karar. Aynı sistemde farklı işler farklı model ister: bir girdiyi puanlayıp elemek ucuz ve hızlı bir model işi, ana çıktıyı üretmek ise en iyi modeli hak ediyor. Gramer düzeltmesi ile konuşma değerlendirmesi de aynı modeli gerektirmiyor. Tek bir model seçip her yere koymak ya kaliteden ya paradan kaybettirir.",
        "terms": [
            {
                "en": "input/output token pricing",
                "tr": "input/output token pricing",
                "definition": "LLM maliyetinin, gönderilen ve üretilen token sayısına göre ayrı ayrı hesaplanması."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
