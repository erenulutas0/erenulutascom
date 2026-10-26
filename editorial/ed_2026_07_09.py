"""9 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-09"

INTRO = "Günün kapağı 32 dakikalık bir okuma ve baştan sona bir takas anlatısı: elimizdeki kuantum sonrası imza algoritması ideal değil, ama beklemenin maliyeti kullanmanın maliyetinden yüksek. Mühendislikte kararların çoğu böyledir — en iyi seçenek değil, mevcut en iyi seçenek."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/ml-dsa-will-have-to-do/",
        "slot": "cover",
        "title_tr": "Mükemmeli beklemek bir strateji değil: ML-DSA ile yaşamayı öğrenmek",
        "difficulty": "ileri",
        "tags": [
            "cryptography",
            "security",
            "protocol",
            "takas"
        ],
        "summary": "Onlarca yıldır güvendiğimiz RSA ve ECC, yeterince gelişmiş kuantum bilgisayarların saldırısına karşı savunmasız. Böyle bilgisayarlar henüz yok, ama beklenenden erken geliyor gibi görünüyorlar. Neyse ki çözüm hazır: kuantum saldırısına dayanıklı olacak şekilde tasarlanmış **ML-KEM** şifrelemesi ve **ML-DSA** imzalarına geçmek. İkisi de NIST tarafından, sekiz yıllık açık uluslararası bir yarışmanın ardından 2024'te standartlaştırıldı.\n\nŞifreleme tarafında geçiş çoktan başlamış: Cloudflare'in taşıdığı trafiğin çoğunluğu şimdiden ML-KEM kullanıyor ve böylece \"harvest now, decrypt later\" saldırılarına karşı korunuyor.\n\nİmza tarafı ise yazının asıl konusu ve dürüst bir takas anlatısı. ML-DSA bugün standartlaştırılmış en iyi genel amaçlı kuantum sonrası imza şeması — **ama dezavantajları var**: ağ üzerinde çok daha büyük yer kaplıyor ve RSA/ECC ile yapabildiğimiz birçok numara ML-DSA ile yapılamıyor. Daha iyi kuantum sonrası imza şemaları var ama henüz hazır değiller.\n\nSonuç, başlıktaki karar: daha iyisini bekleyemeyiz. Elimizdeki kusurlu araçla geçişe başlamak, mükemmel aracı beklerken savunmasız kalmaktan iyi.",
        "key_points": [
            "Şifreleme ve imza farklı aciliyetlerde: şifrelenmiş veri bugün toplanıp yarın çözülebilir, imza ise ancak canlıyken kırılırsa işe yarar.",
            "ML-DSA'nın maliyeti boyut: daha büyük imzalar, her TLS handshake’te daha fazla bayt demek.",
            "NIST'in sekiz yıllık açık yarışması, kriptografik standartların nasıl kurulduğunun iyi bir örneği — kapalı kapı ardında değil, kamuya açık.",
            "Cloudflare bu konuda 2021'den beri düzenli yazıyor; teknolojinin olgunlaşmasını yıllar boyunca izlemek başlı başına bir yöntem."
        ],
        "why_it_matters": "Mühendislikte en sık verilen yanlış karar, mükemmel çözümü beklemektir. Bu yazı karşı örneği veriyor: kusurları açıkça sayıp yine de harekete geçmek. \"Şu anki en iyi seçenek nedir ve beklemenin maliyeti nedir?\" sorusu, teknoloji seçimlerinin çoğunda doğru sorudur.",
        "for_you": "Post-quantum cryptography’yi bugün uygulamayacaksın ama iki şeyi al. Birincisi karar çerçevesi: bir kütüphane ya da yaklaşım seçerken ‘ideal mi?’ diye sorma, ‘beklemenin maliyeti kabul edilebilir mi?’ diye sor. İkincisi somut: TLS handshake’in maliyetini anlamak backend mühendisliğinin parçası. İmza boyutu büyürse handshake paketleri büyür, mobil ağlarda bu ölçülebilir gecikme demektir. Bir mobil uygulamada bağlantı kurma süresini ölçüyorsan, bu maliyetin nereden geldiğini bilmek işine yarar ve connection reuse’un neden bu kadar önemli olduğunu açıklar.",
        "terms": [
            {
                "en": "ML-KEM / ML-DSA",
                "tr": "ML-KEM / ML-DSA",
                "definition": "NIST tarafından standartlaştırılan kuantum sonrası key rollover ve dijital imza algoritmaları."
            },
            {
                "en": "RSA / ECC",
                "tr": "RSA / ECC",
                "definition": "Bugün yaygın kullanılan klasik açık anahtarlı kriptografi algoritmaları; yeterince güçlü kuantum bilgisayarlara karşı savunmasız."
            },
            {
                "en": "TLS handshake",
                "tr": "TLS handshake",
                "definition": "İstemci ile sunucunun şifreli bağlantı kurmadan önce anahtar ve kimlik üzerinde anlaştığı ilk aşama."
            }
        ]
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/specification-driven-composition-for-flexible-data-workflows/",
        "slot": "brief",
        "title_tr": "Niyeti mantıktan ayırmak: veri pipeline'larında kopyala-yapıştır tuzağı",
        "difficulty": "orta",
        "tags": [
            "data engineering",
            "architecture",
            "design",
            "serverless"
        ],
        "summary": "Veri pipeline'ları genelde basit betikler olarak başlar. Büyüdükçe dönüşüm mantığını kopyalarsın ve küçük bir değişiklik birden çok workflow’a çığ gibi yayılır. Dönüşüm mantığını betikler arasında kopyalayıp değiştirmek, ölçekte yönetilemez iş akışları üretir.\n\nDaha sinsi bir sonuç da var: her pipeline'ın ne yaptığını takip etmek zorlaşır çünkü **workflow’un niyeti kodun içine gömülüdür**. Bu görünürlük eksikliği, özellikle sağlık, finans ve yaşam bilimleri gibi düzenlemeye tabi alanlarda yönetişimi zorlaştırır.\n\nÖnerilen desen **spesifikasyon-güdümlü kompozisyon**: workflow’un niyetini işleme mantığından ayırmak. Mantığı betiğe gömmek yerine, ne yapılacağını bildirimsel bir spesifikasyonda tanımlıyorsun; işleme motoru bunu okuyup uyguluyor. Sonuç: daha az tekrar, yeni veri kümesini devreye almanın kısalması ve iş akışları arasında tutarlılık.",
        "key_points": [
            "Klasik problem: orkestrasyon, dönüşüm mantığı ve doğrulama kuralları aynı betikte iç içe. Yeni bir veri kümesi = kod değiştir ve yeniden dağıt.",
            "Doğrulama çoğu zaman yalnızca işleme sırasında yapılıyor, bu yüzden sorunlar geç ortaya çıkıyor."
        ],
        "for_you": "Bu deseni kendi veri pipeline’larında kur: kaynak listesini bir config dosyasında bildirimsel olarak tut, işleme mantığını ayrı yaz. Yeni bir kaynak eklemek için kod değil konfigürasyon değiştirirsin. Veri temizleme işlerinde de hangi kolonun nasıl temizleneceğini koda gömmek yerine bir YAML ya da JSON şemasında tanımla. Bir avantajı daha var: spesifikasyon varsa doğrulamayı **işlemeden önce** yapabilirsin, yani hatayı veriyi işlemeye başlamadan yakalarsın.",
        "terms": [
            {
                "en": "declarative specification",
                "tr": "declarative specification",
                "definition": "Nasıl yapılacağını değil ne istendiğini tarif eden yapılandırma; motor gerisini halleder."
            },
            {
                "en": "data governance",
                "tr": "data governance",
                "definition": "Verinin nereden geldiği, nasıl dönüştüğü ve kimin eriştiğinin izlenebilir olması."
            }
        ]
    },
    {
        "url": "https://research.google/blog/sensorfm-towards-a-general-intelligence-and-interface-for-wearable-health-data/",
        "slot": "brief",
        "title_tr": "Bir trilyon dakikalık sensör verisiyle eğitilen foundation model",
        "difficulty": "ileri",
        "tags": [
            "machine learning",
            "zaman serisi",
            "research",
            "health"
        ],
        "summary": "SensorFM, giyilebilir sağlık verisi için bir **foundation model** (foundation model). Beş milyon kişiden gelen **bir trilyon dakikadan fazla** sensör verisiyle önceden eğitilmiş. Model boyutu ile veriyi birlikte ölçekleyerek insan fizyolojisinin genel amaçlı bir temsilini öğreniyor ve bu temsil 35 farklı sağlık tahmin görevine aktarılabiliyor.\n\nYaklaşımın farkı şu: etiketli veriyle görev görev eğitmek yerine, **etiketsiz** giyilebilir veriden nüfus ölçeğinde doğrudan öğreniyor. Sonuç, az etiketle uyarlanabilen ve eksik veriyi doldurabilen bir temsil.\n\nVeri kümesi 100'den fazla ülkeden, Eylül 2024 – Eylül 2025 arası, verilerinin araştırmada kullanılmasına rıza göstermiş kişilerden kimliksizleştirilerek örneklenmiş.",
        "key_points": [
            "\"Foundation model\" fikri metin ve görüntüden zaman serisine taşınıyor — aynı tarif: çok veri, self-supervised pretraining, sonra göreve uyarlama.",
            "35 göreve transfer olması, temsilin göreve özel değil genel olduğunun kanıtı."
        ],
        "for_you": "Zaman serisi verisiyle çalışıyorsan buradaki fikir doğrudan ilgili: **self-supervised pretraining**. Etiketli veri (‘bu noktada al’) pahalı ve azdır; etiketsiz fiyat ya da sensör verisi bol. Modeli önce etiketsiz veriyle genel bir temsil öğrenmesi için eğitip (örneğin maskelenmiş bölümü tahmin etme), sonra küçük etiketli setle uyarlamak, doğrudan etiketli veriyle eğitmekten genelde daha iyi sonuç verir. PyTorch’ta bunu denemek erişilebilir bir proje.",
        "terms": [
            {
                "en": "foundation model",
                "tr": "foundation model",
                "definition": "Geniş ve etiketsiz veriyle önceden eğitilip birçok farklı göreve uyarlanabilen büyük model."
            },
            {
                "en": "self-supervised pre-training",
                "tr": "self-supervised pre-training",
                "definition": "Etiket olmadan, verinin kendisinden türetilen görevlerle (ör. eksik parçayı tahmin) model eğitme."
            },
            {
                "en": "data infilling",
                "tr": "data infilling",
                "definition": "Eksik ya da kayıp ölçümlerin model tarafından makul biçimde tamamlanması."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
