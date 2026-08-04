"""9 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-09"

INTRO = (
    "Günün kapağı 32 dakikalık bir okuma ve baştan sona bir takas anlatısı: "
    "elimizdeki kuantum sonrası imza algoritması ideal değil, ama beklemenin "
    "maliyeti kullanmanın maliyetinden yüksek. Mühendislikte kararların çoğu "
    "böyledir — en iyi seçenek değil, mevcut en iyi seçenek."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/ml-dsa-will-have-to-do/",
        "slot": "cover",
        "title_tr": "Mükemmeli beklemek bir strateji değil: ML-DSA ile yaşamayı öğrenmek",
        "difficulty": "ileri",
        "tags": ["kriptografi", "güvenlik", "protokol", "takas"],
        "summary": (
            "Onlarca yıldır güvendiğimiz RSA ve ECC, yeterince gelişmiş kuantum "
            "bilgisayarların saldırısına karşı savunmasız. Böyle bilgisayarlar "
            "henüz yok, ama beklenenden erken geliyor gibi görünüyorlar. "
            "Neyse ki çözüm hazır: kuantum saldırısına dayanıklı olacak şekilde "
            "tasarlanmış **ML-KEM** şifrelemesi ve **ML-DSA** imzalarına geçmek. "
            "İkisi de NIST tarafından, sekiz yıllık açık uluslararası bir "
            "yarışmanın ardından 2024'te standartlaştırıldı.\n\n"
            "Şifreleme tarafında geçiş çoktan başlamış: Cloudflare'in taşıdığı "
            "trafiğin çoğunluğu şimdiden ML-KEM kullanıyor ve böylece \"şimdi "
            "topla, sonra çöz\" saldırılarına karşı korunuyor.\n\n"
            "İmza tarafı ise yazının asıl konusu ve dürüst bir takas anlatısı. "
            "ML-DSA bugün standartlaştırılmış en iyi genel amaçlı kuantum sonrası "
            "imza şeması — **ama dezavantajları var**: ağ üzerinde çok daha büyük "
            "yer kaplıyor ve RSA/ECC ile yapabildiğimiz birçok numara ML-DSA ile "
            "yapılamıyor. Daha iyi kuantum sonrası imza şemaları var ama "
            "henüz hazır değiller.\n\n"
            "Sonuç, başlıktaki karar: daha iyisini bekleyemeyiz. Elimizdeki "
            "kusurlu araçla geçişe başlamak, mükemmel aracı beklerken savunmasız "
            "kalmaktan iyi."
        ),
        "key_points": [
            "Şifreleme ve imza farklı aciliyetlerde: şifrelenmiş veri bugün "
            "toplanıp yarın çözülebilir, imza ise ancak canlıyken kırılırsa işe yarar.",
            "ML-DSA'nın maliyeti boyut: daha büyük imzalar, her TLS el sıkışmasında "
            "daha fazla bayt demek.",
            "NIST'in sekiz yıllık açık yarışması, kriptografik standartların nasıl "
            "kurulduğunun iyi bir örneği — kapalı kapı ardında değil, kamuya açık.",
            "Cloudflare bu konuda 2021'den beri düzenli yazıyor; teknolojinin "
            "olgunlaşmasını yıllar boyunca izlemek başlı başına bir yöntem.",
        ],
        "why_it_matters": (
            "Mühendislikte en sık verilen yanlış karar, mükemmel çözümü beklemektir. "
            "Bu yazı karşı örneği veriyor: kusurları açıkça sayıp yine de "
            "harekete geçmek. \"Şu anki en iyi seçenek nedir ve beklemenin "
            "maliyeti nedir?\" sorusu, teknoloji seçimlerinin çoğunda doğru sorudur."
        ),
        "for_you": (
            "Kuantum sonrası kriptografiyi bugün uygulamayacaksın, ama iki şeyi al. "
            "Birincisi karar çerçevesi: bir kütüphane ya da yaklaşım seçerken "
            "\"ideal mi?\" diye sorma, \"beklemenin maliyeti kabul edilebilir mi?\" "
            "diye sor. İkincisi somut: TLS el sıkışmasının maliyetini anlamak "
            "backend mühendisliğinin parçası. İmza boyutu büyürse el sıkışma "
            "paketleri büyür, mobil ağlarda bu ölçülebilir gecikme demektir. "
            "KlioAI mobil uygulamasında bağlantı kurma süresini ölçüyorsan, "
            "bu maliyetin nereden geldiğini bilmek işine yarar — ve "
            "bağlantı yeniden kullanımının (connection reuse) neden bu kadar "
            "önemli olduğunu açıklar."
        ),
        "terms": [
            {
                "en": "ML-KEM / ML-DSA",
                "tr": "ML-KEM / ML-DSA",
                "definition": "NIST tarafından standartlaştırılan kuantum sonrası anahtar değişimi ve dijital imza algoritmaları.",
            },
            {
                "en": "RSA / ECC",
                "tr": "RSA / ECC",
                "definition": "Bugün yaygın kullanılan klasik açık anahtarlı kriptografi algoritmaları; yeterince güçlü kuantum bilgisayarlara karşı savunmasız.",
            },
            {
                "en": "TLS handshake",
                "tr": "TLS el sıkışması",
                "definition": "İstemci ile sunucunun şifreli bağlantı kurmadan önce anahtar ve kimlik üzerinde anlaştığı ilk aşama.",
            },
        ],
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/specification-driven-composition-for-flexible-data-workflows/",
        "slot": "brief",
        "title_tr": "Niyeti mantıktan ayırmak: veri pipeline'larında kopyala-yapıştır tuzağı",
        "difficulty": "orta",
        "tags": ["veri mühendisliği", "mimari", "tasarım", "serverless"],
        "summary": (
            "Veri pipeline'ları genelde basit betikler olarak başlar. Büyüdükçe "
            "dönüşüm mantığını kopyalarsın ve küçük bir değişiklik birden çok "
            "iş akışına çığ gibi yayılır. Dönüşüm mantığını betikler arasında "
            "kopyalayıp değiştirmek, ölçekte yönetilemez iş akışları üretir.\n\n"
            "Daha sinsi bir sonuç da var: her pipeline'ın ne yaptığını takip "
            "etmek zorlaşır çünkü **iş akışının niyeti kodun içine gömülüdür**. "
            "Bu görünürlük eksikliği, özellikle sağlık, finans ve yaşam "
            "bilimleri gibi düzenlemeye tabi alanlarda yönetişimi zorlaştırır.\n\n"
            "Önerilen desen **spesifikasyon-güdümlü kompozisyon**: iş akışının "
            "niyetini işleme mantığından ayırmak. Mantığı betiğe gömmek yerine, "
            "ne yapılacağını bildirimsel bir spesifikasyonda tanımlıyorsun; "
            "işleme motoru bunu okuyup uyguluyor. Sonuç: daha az tekrar, yeni "
            "veri kümesini devreye almanın kısalması ve iş akışları arasında "
            "tutarlılık."
        ),
        "key_points": [
            "Klasik problem: orkestrasyon, dönüşüm mantığı ve doğrulama kuralları "
            "aynı betikte iç içe. Yeni bir veri kümesi = kod değiştir ve yeniden dağıt.",
            "Doğrulama çoğu zaman yalnızca işleme sırasında yapılıyor, bu yüzden "
            "sorunlar geç ortaya çıkıyor.",
        ],
        "for_you": (
            "Bu deseni bu gazetenin pipeline'ında zaten görebilirsin: kaynak "
            "listesi `config.py` içinde bildirimsel olarak duruyor, çekme mantığı "
            "ise ayrı. Yeni bir kaynak eklemek için kod değil konfigürasyon "
            "değiştiriyorsun. Aynısını DBH'daki yakıt analizi tarzı bir işte de "
            "kur: hangi kolonun nasıl temizleneceğini koda gömmek yerine bir "
            "YAML/JSON şemasında tanımla. Bir avantajı daha var — spesifikasyon "
            "varsa doğrulamayı **işlemeden önce** yapabilirsin, yani hatayı "
            "veriyi işlemeye başlamadan yakalarsın."
        ),
        "terms": [
            {
                "en": "declarative specification",
                "tr": "bildirimsel spesifikasyon",
                "definition": "Nasıl yapılacağını değil ne istendiğini tarif eden yapılandırma; motor gerisini halleder.",
            },
            {
                "en": "data governance",
                "tr": "veri yönetişimi",
                "definition": "Verinin nereden geldiği, nasıl dönüştüğü ve kimin eriştiğinin izlenebilir olması.",
            },
        ],
    },
    {
        "url": "https://research.google/blog/sensorfm-towards-a-general-intelligence-and-interface-for-wearable-health-data/",
        "slot": "brief",
        "title_tr": "Bir trilyon dakikalık sensör verisiyle eğitilen temel model",
        "difficulty": "ileri",
        "tags": ["makine öğrenmesi", "zaman serisi", "araştırma", "sağlık"],
        "summary": (
            "SensorFM, giyilebilir sağlık verisi için bir **temel model** "
            "(foundation model). Beş milyon kişiden gelen **bir trilyon dakikadan "
            "fazla** sensör verisiyle önceden eğitilmiş. Model boyutu ile veriyi "
            "birlikte ölçekleyerek insan fizyolojisinin genel amaçlı bir "
            "temsilini öğreniyor ve bu temsil 35 farklı sağlık tahmin görevine "
            "aktarılabiliyor.\n\n"
            "Yaklaşımın farkı şu: etiketli veriyle görev görev eğitmek yerine, "
            "**etiketsiz** giyilebilir veriden nüfus ölçeğinde doğrudan "
            "öğreniyor. Sonuç, az etiketle uyarlanabilen ve eksik veriyi "
            "doldurabilen bir temsil.\n\n"
            "Veri kümesi 100'den fazla ülkeden, Eylül 2024 – Eylül 2025 arası, "
            "verilerinin araştırmada kullanılmasına rıza göstermiş kişilerden "
            "kimliksizleştirilerek örneklenmiş."
        ),
        "key_points": [
            "\"Temel model\" fikri metin ve görüntüden zaman serisine taşınıyor — "
            "aynı tarif: çok veri, öz-denetimli ön eğitim, sonra göreve uyarlama.",
            "35 göreve transfer olması, temsilin göreve özel değil genel "
            "olduğunun kanıtı.",
        ],
        "for_you": (
            "Tradebot'ta zaman serisi verisiyle çalışıyorsun ve buradaki fikir "
            "doğrudan ilgili: **öz-denetimli ön eğitim**. Etiketli veri (\"bu "
            "noktada al\") pahalı ve azdır; etiketsiz fiyat verisi ise "
            "bol. Modeli önce etiketsiz veriyle genel bir temsil öğrenmesi için "
            "eğitip (ör. maskelenmiş bölümü tahmin etme), sonra küçük etiketli "
            "setle uyarlamak, doğrudan etiketli veriyle eğitmekten genelde daha "
            "iyi sonuç verir. PyTorch'ta bunu denemek erişilebilir bir proje — "
            "ve portföyünde \"öz-denetimli ön eğitim uyguladım\" demek güçlü "
            "bir cümledir."
        ),
        "terms": [
            {
                "en": "foundation model",
                "tr": "temel model",
                "definition": "Geniş ve etiketsiz veriyle önceden eğitilip birçok farklı göreve uyarlanabilen büyük model.",
            },
            {
                "en": "self-supervised pre-training",
                "tr": "öz-denetimli ön eğitim",
                "definition": "Etiket olmadan, verinin kendisinden türetilen görevlerle (ör. eksik parçayı tahmin) model eğitme.",
            },
            {
                "en": "data infilling",
                "tr": "veri doldurma",
                "definition": "Eksik ya da kayıp ölçümlerin model tarafından makul biçimde tamamlanması.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
