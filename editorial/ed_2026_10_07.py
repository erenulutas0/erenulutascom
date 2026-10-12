"""7 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-07"

INTRO = (
    "‘Her adıma bir agent koy’ cazip ama yanlış. Cloudflare’in güvenlik operasyonları için "
    "kurduğu sistemin ön yarısında hiç yapay zekâ yok ve yazının asıl dersi bu. Yanında, "
    "gecikmenin nanosaniyeyle ölçüldüğü bir dünya: bulutta yüksek frekanslı alım-satım."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/agentic-security-operations/",
        "slot": "cover",
        "title_tr": "Önce kanıtı kod toplasın, sonra model yorumlasın: Cloudflare’in çok ajanlı güvenlik hattı",
        "difficulty": "orta",
        "tags": ["agent", "güvenlik", "mimari", "LLM"],
        "summary": (
            "Güvenlik uyarıları nadiren tek tek gelir. Bir uyarı ortamda bir dalga yaratır ve bir "
            "analistin hangilerinin ilişkili olduğuna, ne anlama geldiklerine karar vermesi gerekir. "
            "Cloudflare, Managed Defense ekibi için bu işin büyük kısmını üstlenen çok ajanlı bir "
            "düzenek kurdu ve ilk denemenin neden başarısız olduğunu açıkça anlatıyor.\n\n"
            "**Tek ajan neden başarısız oldu?** İlk prototipte tüm soruşturma tek bir genel amaçlı "
            "ajana verildi. Faydalı analiz üretti ama kanıtın desteklemediği iddialar da uydurdu. "
            "Telemetri, dedektör açıklamaları, politikalar ve tehdit istihbaratı tek bir prompta "
            "ezilince rolleri birbirine karıştı. Üç tekrar eden sorun: **(1) Bağlam otoriteye "
            "dönüştü:** bir tespit, saldırının gerçekleştiğinin kanıtı değil bir hipotezdir; geniş "
            "bir ajan bu ayrımı bulandırır. **(2) Kapsam kaydı:** ajan yanlış hesabı, zaman aralığını "
            "ya da kaynağı sorgulayabilir; bir prompta sınır olarak güvenemezsin. **(3) Hata "
            "kayboldu:** bir sorgu zaman aşımına uğrarsa sonuç ‘bakılmadı’ ile ‘bakıldı ve "
            "bulunamadı’yı ayırt etmeyebilir.\n\n"
            "**Önce keşif, sonra çıkarım.** Çözüm, kanıt toplamayı ve kapsam denetimini model "
            "analizinden önce uygulama koduna taşımak. Düzeneğin ön yarısında ajan yok: "
            "deterministik kod, sürümlü API çağrılarıyla sabit bir keşif iş akışı çalıştırıp "
            "müşteri kimliğini, tespit geçmişini, trafik tabanını, uygulanan aksiyonun sonucunu ve "
            "ağ gözlemlerini topluyor. Bu sabit anlık görüntü değerlendirmeyi de **tekrarlanabilir** "
            "yapıyor: ajanlar veriyi kendileri çekerse iki koşu girdileri değiştiği için farklı "
            "sonuç verebilir; aynı görüntü yeniden oynatılınca farklar yalnızca yorumdan gelir.\n\n"
            "**Gürültüyü erken ele.** Uyarıların çoğu olay değil. Bilinen yüksek hacimli gürültü "
            "geldiği anda deterministik olarak pasif sınıflanıyor. Geri kalan için hafif bir "
            "triyaj modeli (Cloudflare’in açık kaynak karar modeli Clef) her uyarıyı keşif "
            "verisiyle karşılaştırıyor: bu daha önce görüldü mü, analistler ne karar verdi?\n\n"
            "**Uzman ajanlar.** Derin inceleme gereken uyarılarda bir koordinatör dört uzman ajanı "
            "paralel çalıştırıyor: trafik analizi, müşteri bağlamı, küresel telemetri ve tehdit "
            "istihbaratı. Bir sentez ajanı onların **tipli bulgularını** tek bir tavsiyede "
            "birleştiriyor; yeni kanıt çekemiyor ve onaylı sözlüğün dışında bir sınıflandırma "
            "seçemiyor. Her görevi dar tutmak, desteksiz iddiaları yakalamayı ve tavsiyeleri "
            "denetlemeyi kolaylaştırıyor."
        ),
        "key_points": [
            "Prompt bir güvenlik sınırı değildir; kapsamı kod zorlar.",
            "‘Bakılmadı’ ile ‘bakıldı, bulunamadı’ farklı sonuçlardır ve ayrı temsil edilmelidir.",
            "Veriyi model değil deterministik kod toplarsa değerlendirme tekrarlanabilir olur.",
            "Ucuz ve hızlı bir model önce gürültüyü eler; pahalı model yalnızca gerekene bakar.",
            "Dar görevli uzman ajanlar + yeni veri çekemeyen sentez ajanı, uydurmayı yapısal olarak sınırlar.",
        ],
        "why_it_matters": (
            "Agent sistemlerinde hatanın kaynağı çoğu zaman model değil, modele bırakılan "
            "sorumluluğun genişliğidir. Bu yazı ‘ne kadarını koda, ne kadarını modele vermeli’ "
            "sorusuna üretimden gelen net bir cevap: veri toplama, kapsam ve sözlük kodda; "
            "yorum modelde."
        ),
        "for_you": (
            "DBH’daki LLM hattına ve Mobit’in arama asistanına aynı üç kural uyar. **Bir:** modelin "
            "araç çağırarak veri çekmesine izin vermeden önce, ihtiyaç duyacağı veriyi kodla çek ve "
            "prompta hazır ver; hangi kaydın hangi kullanıcıya ait olduğunu SQL’deki `WHERE` "
            "belirlesin, prompt değil. **İki:** her araç sonucuna açık bir durum alanı ekle: "
            "`ok`, `empty`, `error`. Boş liste ile hata aynı görünürse model ‘bulunamadı’ diye "
            "uydurur. **Üç:** çıktıyı serbest metin yerine sabit bir sözlükle (`enum`) sınırla. "
            "Bu üç değişiklik, daha büyük bir modele geçmekten çoğu zaman daha fazla hata azaltır."
        ),
        "terms": [
            {"en": "SIEM", "tr": "güvenlik bilgi ve olay yönetimi", "definition": "Güvenlik kayıtlarını toplayıp ilişkilendiren ve uyarı üreten sistem."},
            {"en": "triage", "tr": "triyaj", "definition": "Gelen uyarıları önem ve aciliyete göre hızlıca sınıflandırıp önceliklendirme."},
            {"en": "hallucination", "tr": "uydurma", "definition": "Modelin girdideki kanıtla desteklenmeyen bir bilgiyi doğruymuş gibi üretmesi."},
            {"en": "typed output", "tr": "tipli çıktı", "definition": "Biçimi ve izin verilen değerleri önceden şemayla sabitlenmiş model çıktısı."},
        ],
    },
    {
        "url": "https://cloud.google.com/blog/topics/financial-services/ultra-low-latency-solution-with-u4-enables-high-velocity-trading/",
        "slot": "brief",
        "title_tr": "Bulutta yüksek frekanslı alım-satım: gecikme değil, gecikmenin tutarlılığı",
        "difficulty": "ileri",
        "tags": ["gecikme", "ağ", "finans", "altyapı"],
        "summary": (
            "Sermaye piyasalarında paket zamanlamasındaki küçük oynamalar bile kuyruk önceliğini "
            "ve emrin gerçekleşmesini değiştirir. Google Cloud, **Ultra Low Latency (ULL)** "
            "çözümünü ve yeni U4 makine ailesini genel kullanıma açtı. Hedef yalnızca düşük "
            "gecikme değil, **determinizm**: kritik işlemin her seferinde aynı sürede bitmesi.\n\n"
            "Teknik parçalar öğretici: sanallaştırma kaynaklı titremeyi (jitter) azaltan **bare "
            "metal** makineler; yedekli A/B **multicast** piyasa veri akışlarının iki bağımsız ağ "
            "bağdaştırıcısından alınması, telemetri ve yönetimin üçüncü bir bağdaştırıcıya "
            "ayrılması; çekirdeği atlayan kullanıcı alanı ağ yığınları (**OpenOnload, DPDK**); ve "
            "ağ düzeyinde 10 nanosaniyenin altında zaman damgası sağlayan saat senkronizasyonu."
        ),
        "key_points": [
            "Alım-satımda ortalama gecikmeden çok gecikmenin değişkenliği (jitter) önemlidir.",
            "Kritik veri yolunu yönetim ve telemetri trafiğinden fiziksel olarak ayırmak tutarlılık sağlar.",
            "Çekirdeği atlayan ağ yığınları, paket başına işletim sistemi maliyetini ortadan kaldırır.",
        ],
        "for_you": (
            "Tradebot bu ölçekte değil ama aynı ilke geçerli: stratejinin tepki süresini ölçerken "
            "ortalamaya değil **p99 ve en kötü duruma** bak, çünkü kayıp emirler oradan gelir. "
            "Her piyasa olayına geliş zamanı ve karar zamanı damgası koyup farkın dağılımını "
            "çıkar. Garbage collection duraksamaları ya da log yazımı gibi kaynakları, kritik "
            "karar yolundan ayrı bir iş parçacığına almak da aynı ‘yolu ayır’ fikrinin küçük hâli."
        ),
        "terms": [
            {"en": "jitter", "tr": "titreme", "definition": "Gecikmenin bir istekten diğerine gösterdiği değişkenlik."},
            {"en": "kernel bypass", "tr": "çekirdek atlama", "definition": "Ağ paketlerini işletim sistemi çekirdeğine uğramadan doğrudan uygulamada işleme."},
            {"en": "multicast", "tr": "çoklu yayın", "definition": "Tek bir göndericinin aynı veriyi bir grup alıcıya aynı anda iletmesi."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
