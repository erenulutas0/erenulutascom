"""1 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-01"

INTRO = "Cumartesi sakin geçti. Günün tek yazısı OpenAI'ın matematik sonuçları — mühendislikten uzak görünüyor ama içinde çok somut bir sayı var. Yanına arşivden Netflix'in \"veri kanaryası\" yazısını koydum: kodu test ediyoruz da veriyi kim test ediyor sorusunun cevabı."

DRAFTS = [
    {
        "url": "https://openai.com/index/ten-advances-in-mathematics",
        "slot": "cover",
        "title_tr": "On açık matematik problemi ve 2.000 dolarlık token faturası",
        "difficulty": "orta",
        "tags": [
            "LLM",
            "research",
            "cost"
        ],
        "summary": "OpenAI, yayımlanmamış bir modelin uzun süredir açık duran on matematik ve teorik bilgisayar bilimi problemini çözdüğünü ya da ciddi ilerleme kaydettiğini duyuruyor. Problemler yüksek boyutlu geometri, kodlama teorisi, aritmetik devre karmaşıklığı, grup teorisi, kuantum karmaşıklığı ve kafes tabanlı kriptografi gibi alanlara yayılıyor.\n\nMühendislik açısından yazıdaki en dikkat çekici cümle sonuçların kendisi değil, dipnottaki maliyet: bu çözümleri bulmak için gereken toplam token miktarı **yaklaşık 2.000 dolar** tutuyor. Yani on yıllardır açık duran problemler, bir mühendisin aylık bulut faturasından ucuza deneniyor. İkinci dikkat çekici nokta ise doğrulanabilirlik: matematik, çıktının doğru olup olmadığının kesin olarak kontrol edilebildiği ender alanlardan biri — bu yüzden \"model uydurdu mu?\" sorusu burada anlamlı bir şekilde cevaplanabiliyor.",
        "key_points": [
            "Sonuçlar arasında küre paketleme yoğunluğu için yeni üst sınırlar, ikili kodlar için üstel olarak iyileştirilmiş sınırlar ve Connes'in sertlik varsayımının çürütülmesi var.",
            "Toplam hesaplama maliyeti ~2.000 dolar — asıl haber bu olabilir.",
            "Matematik, LLM çıktısının bağımsız olarak doğrulanabildiği bir alan; bu, sonuçları çoğu \"AI şunu yaptı\" iddiasından daha güvenilir kılıyor."
        ],
        "why_it_matters": "Bir alanda ilerlemenin darboğazı \"fikir üretmek\" ise ve fikir üretmek ucuzluyorsa, darboğaz **doğrulamaya** kayar. Yazılımda da aynı şey oluyor: kod üretmek ucuzladıkça değerli olan şey kodu yazmak değil, doğru olduğunu ispatlayan test ve tip sistemlerini kurmak.",
        "for_you": "Buradan çıkaracağın pratik ders şu: LLM’i devreye soktuğun her yerde ‘çıktıyı ne doğrulayacak?’ sorusunun bir cevabı olmalı. Bir trading stratejisini modelin önermesi kolay; onu backtest ve walk-forward doğrulamasından geçirmeden kabul etmek pahalı. Aynı şekilde bir LLM sınıflandırma pipeline’ında: modelin verdiği etiketi schema, enum ya da iş kuralı ile doğrulayabiliyorsan güvenebilirsin; doğrulayamıyorsan eline geçen şey yalnızca inandırıcı bir tahmin.",
        "terms": [
            {
                "en": "open problem",
                "tr": "open problem",
                "definition": "Bir alanda uzun süredir çözülememiş, üzerinde çalışılan matematiksel soru."
            },
            {
                "en": "verifiability",
                "tr": "verifiability",
                "definition": "Bir çıktının doğru olup olmadığının bağımsız ve kesin biçimde kontrol edilebilmesi."
            }
        ]
    },
    {
        "url": "https://netflixtechblog.com/the-data-canary-how-netflix-validates-catalog-metadata-18b699d58e36?source=rss----2615bd06b42e---4",
        "slot": "archive",
        "title_tr": "Kodu kanarya ile test ediyoruz da veriyi kim test ediyor?",
        "difficulty": "orta",
        "tags": [
            "data engineering",
            "resilience",
            "observability",
            "pipeline"
        ],
        "summary": "Netflix'te bir üretim arızası oldu: kod deploy edilmemişti, konfigürasyon değişmemişti. Ama daha önceki bir olaya müdahale ederken elle yapılan bir düzeltme, bir veri akışını bozmuş ve bir grup içerik için onu boş hâle getirmişti. Sonuç anında görüldü — eksik metadata yüzünden manifest üretilemedi, katalog servisi hata verdi, oynatma bozuldu.\n\nİşin can alıcı kısmı şu: Netflix'in gelişmiş **kod kanaryası** (canary deployment) hiçbir şey yakalamamıştı. Çünkü kod değişmemişti — veri değişmişti. Bu olay şunu ortaya çıkardı: kod dağıtımlarını doğrulayabiliyorlar ama yüksek hızlı veri pipeline'ları için eşdeğer bir mekanizmaları yoktu.\n\nKurdukları çözüm, veri dönüşümlerini **üretim trafiğiyle** doğrulayan otomatik bir kanarya sistemi. 10 dakikanın altında sorunu tespit edip bozuk verinin üyelere ulaşmasını engelliyor. Zorluk da burada: mevcut kanarya analiz araçları istatistiksel güvene ulaşmak için 30-60 dakika istiyor, oysa iki veri döngüsü arasındaki pencere çok daha kısa.",
        "key_points": [
            "Arıza kod değişikliğinden değil veri değişikliğinden geldi — mevcut tüm koruma mekanizmaları kör kaldı.",
            "\"Veri dağıtımlarına kod dağıtımlarıyla aynı titizlikle davranmak gerekiyor\" — yazının tek cümlelik özeti.",
            "Zaman kısıtı tasarımı belirledi: klasik kanarya analizi 30-60 dakika istiyor, buradaki bütçe tek bir veri döngüsü.",
            "Doğrulama sentetik veriyle değil gerçek üretim trafiğiyle yapılıyor."
        ],
        "why_it_matters": "Çoğu ekip CI/CD'yi kurar, testleri yazar, kanarya dağıtımı yapar — ve sonra veriyi tamamen denetimsiz bırakır. Oysa veri odaklı sistemlerde arızaların önemli bir kısmı koddan değil veriden gelir: boş bir alan, değişen bir şema, bozulan bir kaynak. Bu yazı o kör noktayı isimlendiriyor.",
        "for_you": "Bu en çok işine yarayacak yazılardan biri. Bir veri kaynağı bir gün formatı değiştirirse ya da bir alanı boş göndermeye başlarsa, pipeline muhtemelen sessizce yanlış sonuç üretir. Uygulanabilir hâli şu: her ETL adımının sonuna ucuz **invariant kontrolleri** koy: satır sayısı bir önceki koşunun yüzde 20’sinden az mı, kritik kolonlarda null oranı sıçradı mı, kategori dağılımı tanınmayacak kadar kaydı mı? Pandas’ta bu birkaç `assert` satırı ama arızayı production’a çıkmadan yakalamanın en ucuz yolu.",
        "terms": [
            {
                "en": "canary deployment",
                "tr": "canary deployment",
                "definition": "Yeni sürümü önce küçük bir trafik dilimine verip metrikleri izleyerek yaygınlaştırma yöntemi."
            },
            {
                "en": "data canary",
                "tr": "data canary",
                "definition": "Aynı fikrin veriye uygulanmışı: yeni üretilen veri kümesini yayımlamadan önce doğrulayıp bozuksa engelleme."
            },
            {
                "en": "manifest",
                "tr": "manifest",
                "definition": "Video oynatıcısına hangi parçaların hangi kalitede nereden çekileceğini söyleyen tanım dosyası."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
