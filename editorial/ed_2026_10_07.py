"""7 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-07"

INTRO = "‘Her adıma bir agent koy’ cazip ama yanlış. Cloudflare’in güvenlik operasyonları için kurduğu sistemin ön yarısında hiç yapay zekâ yok ve yazının asıl dersi bu. Yanında, gecikmenin nanosaniyeyle ölçüldüğü bir dünya: bulutta yüksek frekanslı alım-satım."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/agentic-security-operations/",
        "slot": "cover",
        "title_tr": "Önce kanıtı kod toplasın, sonra model yorumlasın: Cloudflare’in multi-agent güvenlik hattı",
        "difficulty": "orta",
        "tags": [
            "agent",
            "security",
            "architecture",
            "LLM"
        ],
        "summary": "Güvenlik uyarıları nadiren tek tek gelir. Bir uyarı ortamda bir dalga yaratır ve bir analistin hangilerinin ilişkili olduğuna, ne anlama geldiklerine karar vermesi gerekir. Cloudflare, Managed Defense ekibi için bu işin büyük kısmını üstlenen multi-agent bir düzenek kurdu ve ilk denemenin neden başarısız olduğunu açıkça anlatıyor.\n\n**Tek agent neden başarısız oldu?** İlk prototipte tüm soruşturma tek bir genel amaçlı agent’a verildi. Faydalı analiz üretti ama kanıtın desteklemediği iddialar da uydurdu. Telemetri, dedektör açıklamaları, politikalar ve tehdit istihbaratı tek bir prompta ezilince rolleri birbirine karıştı. Üç tekrar eden sorun: **(1) Bağlam otoriteye dönüştü:** bir tespit, saldırının gerçekleştiğinin kanıtı değil bir hipotezdir; geniş bir agent bu ayrımı bulandırır. **(2) Kapsam kaydı:** agent yanlış hesabı, zaman aralığını ya da kaynağı sorgulayabilir; bir prompta sınır olarak güvenemezsin. **(3) Hata kayboldu:** bir sorgu zaman aşımına uğrarsa sonuç ‘bakılmadı’ ile ‘bakıldı ve bulunamadı’yı ayırt etmeyebilir.\n\n**Önce keşif, sonra inference.** Çözüm, kanıt toplamayı ve kapsam denetimini model analizinden önce uygulama koduna taşımak. Düzeneğin ön yarısında agent yok: deterministik kod, sürümlü API çağrılarıyla sabit bir keşif workflow çalıştırıp müşteri kimliğini, tespit geçmişini, trafik tabanını, uygulanan aksiyonun sonucunu ve ağ gözlemlerini topluyor. Bu sabit snapshot değerlendirmeyi de **tekrarlanabilir** yapıyor: agent’lar veriyi kendileri çekerse iki koşu girdileri değiştiği için farklı sonuç verebilir; aynı görüntü yeniden oynatılınca farklar yalnızca yorumdan gelir.\n\n**Gürültüyü erken ele.** Uyarıların çoğu olay değil. Bilinen yüksek hacimli gürültü geldiği anda deterministik olarak pasif sınıflanıyor. Geri kalan için hafif bir triage modeli (Cloudflare’in açık kaynak decision model Clef) her uyarıyı keşif verisiyle karşılaştırıyor: bu daha önce görüldü mü, analistler ne karar verdi?\n\n**Uzman agent’lar.** Derin inceleme gereken uyarılarda bir koordinatör dört uzman agent’ı paralel çalıştırıyor: trafik analizi, müşteri bağlamı, küresel telemetri ve tehdit istihbaratı. Bir sentez agent’ı onların **tipli bulgularını** tek bir tavsiyede birleştiriyor; yeni kanıt çekemiyor ve onaylı sözlüğün dışında bir sınıflandırma seçemiyor. Her görevi dar tutmak, desteksiz iddiaları yakalamayı ve tavsiyeleri denetlemeyi kolaylaştırıyor.",
        "key_points": [
            "Prompt bir güvenlik sınırı değildir; kapsamı kod zorlar.",
            "‘Bakılmadı’ ile ‘bakıldı, bulunamadı’ farklı sonuçlardır ve ayrı temsil edilmelidir.",
            "Veriyi model değil deterministik kod toplarsa değerlendirme tekrarlanabilir olur.",
            "Ucuz ve hızlı bir model önce gürültüyü eler; pahalı model yalnızca gerekene bakar.",
            "Dar görevli uzman agent’lar + yeni veri çekemeyen sentez agent’ı, uydurmayı yapısal olarak sınırlar."
        ],
        "why_it_matters": "Agent sistemlerinde hatanın kaynağı çoğu zaman model değil, modele bırakılan sorumluluğun genişliğidir. Bu yazı ‘ne kadarını koda, ne kadarını modele vermeli’ sorusuna üretimden gelen net bir cevap: veri toplama, kapsam ve sözlük kodda; yorum modelde.",
        "for_you": "Bir LLM hattına ve arama asistanına aynı üç kural uyar. **Bir:** modelin tool çağırarak veri çekmesine izin vermeden önce, ihtiyaç duyacağı veriyi kodla çek ve prompt’a hazır ver; hangi kaydın hangi kullanıcıya ait olduğunu SQL’deki `WHERE` belirlesin, prompt değil. **İki:** her tool sonucuna açık bir durum alanı ekle: `ok`, `empty`, `error`. Boş liste ile hata aynı görünürse model ‘bulunamadı’ diye uydurur. **Üç:** çıktıyı serbest metin yerine sabit bir sözlükle (`enum`) sınırla. Bu üç değişiklik, daha büyük bir modele geçmekten çoğu zaman daha fazla hata azaltır.",
        "terms": [
            {
                "en": "SIEM",
                "tr": "SIEM",
                "definition": "Güvenlik kayıtlarını toplayıp ilişkilendiren ve uyarı üreten sistem."
            },
            {
                "en": "triage",
                "tr": "triage",
                "definition": "Gelen uyarıları önem ve aciliyete göre hızlıca sınıflandırıp önceliklendirme."
            },
            {
                "en": "hallucination",
                "tr": "hallucination",
                "definition": "Modelin girdideki kanıtla desteklenmeyen bir bilgiyi doğruymuş gibi üretmesi."
            },
            {
                "en": "typed output",
                "tr": "typed output",
                "definition": "Biçimi ve izin verilen değerleri önceden şemayla sabitlenmiş model çıktısı."
            }
        ]
    },
    {
        "url": "https://cloud.google.com/blog/topics/financial-services/ultra-low-latency-solution-with-u4-enables-high-velocity-trading/",
        "slot": "brief",
        "title_tr": "Bulutta yüksek frekanslı alım-satım: gecikme değil, gecikmenin tutarlılığı",
        "difficulty": "ileri",
        "tags": [
            "latency",
            "networking",
            "finance",
            "infrastructure"
        ],
        "summary": "Sermaye piyasalarında paket zamanlamasındaki küçük oynamalar bile kuyruk önceliğini ve emrin gerçekleşmesini değiştirir. Google Cloud, **Ultra Low Latency (ULL)** çözümünü ve yeni U4 makine ailesini genel kullanıma açtı. Hedef yalnızca düşük gecikme değil, **determinizm**: kritik işlemin her seferinde aynı sürede bitmesi.\n\nTeknik parçalar öğretici: sanallaştırma kaynaklı titremeyi (jitter) azaltan **bare metal** makineler; yedekli A/B **multicast** piyasa veri akışlarının iki bağımsız ağ bağdaştırıcısından alınması, telemetri ve yönetimin üçüncü bir bağdaştırıcıya ayrılması; çekirdeği atlayan kullanıcı alanı ağ yığınları (**OpenOnload, DPDK**); ve ağ düzeyinde 10 nanosaniyenin altında timestamp sağlayan saat senkronizasyonu.",
        "key_points": [
            "Alım-satımda ortalama gecikmeden çok gecikmenin değişkenliği (jitter) önemlidir.",
            "Kritik veri yolunu yönetim ve telemetri trafiğinden fiziksel olarak ayırmak tutarlılık sağlar.",
            "Çekirdeği atlayan ağ yığınları, paket başına işletim sistemi maliyetini ortadan kaldırır."
        ],
        "for_you": "Bu ölçekte değilsin ama aynı ilke geçerli: bir stratejinin tepki süresini ölçerken ortalamaya değil **p99 ve en kötü duruma** bak, çünkü kayıp emirler oradan gelir. Her piyasa olayına geliş zamanı ve karar zamanı damgası koy, farkın dağılımını çıkar. Garbage collection pause’ları ya da log yazımı gibi kaynakları, kritik karar yolundan ayrı bir thread’e almak da aynı ‘yolu ayır’ fikrinin küçük hâli.",
        "terms": [
            {
                "en": "jitter",
                "tr": "jitter",
                "definition": "Gecikmenin bir istekten diğerine gösterdiği değişkenlik."
            },
            {
                "en": "kernel bypass",
                "tr": "kernel bypass",
                "definition": "Ağ paketlerini işletim sistemi çekirdeğine uğramadan doğrudan uygulamada işleme."
            },
            {
                "en": "multicast",
                "tr": "multicast",
                "definition": "Tek bir göndericinin aynı veriyi bir grup alıcıya aynı anda iletmesi."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
