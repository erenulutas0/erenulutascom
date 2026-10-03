"""21 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-21"

INTRO = (
    "Netflix'ten alışılmadık bir itiraf: “Bugün iki Flink autoscaler çalıştırıyoruz. Bu, "
    "istediğimizden tam olarak bir fazla.” Yazı, kendi yaptığını bırakıp hazır olanı benimsemenin "
    "gerçek maliyetini ve ölçüm tuzaklarını anlatıyor."
)

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/a-tale-of-two-flink-autoscalers-e9f6a1b1492b?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "İki autoscaler hikâyesi: dışarıdan izlemek ile içeriden akıl yürütmek",
        "difficulty": "ileri",
        "tags": ["Flink", "otomatik ölçekleme", "stream processing", "build vs buy"],
        "summary": (
            "Netflix 2017'den beri Apache Flink ile akış işliyor ve 2026 itibarıyla birden fazla AWS "
            "bölgesinde **30.000'den fazla Flink işi** çalıştırıyor. Çoğu elle değil, yönetilen "
            "platformları Data Mesh tarafından üretiliyor; daha küçük ama büyüyen bir kısmı kişiselleştirme, "
            "reklam ve canlı yayın gibi alanlarda ekiplerin kendi yazdığı işler. Yükleri günlük döngülerle, "
            "lansmanlarla ve bölgesel yük devirleriyle dalgalanıyor.\n\n"
            "Zirveye göre kaynak ayırmak israf, ortalamaya göre ayırmak ani yükte gecikme. Üstelik "
            "ölçekleme bedava değil: varsayılan olarak savepoint almak, işi düzgünce durdurmak ve yeni "
            "boyutta yeniden başlatmak demek; büyük durumlu işlerde bu dakikalar sürüyor.\n\n"
            "**İlk autoscaler** (yaklaşık 2019) bir akış işi gibi kurulmuştu: Mantis üzerinde, Atlas "
            "telemetri platformundan küme düzeyinde metrikleri (CPU, ağ, Kafka gecikmesi, giriş hızı) "
            "tüketiyordu. Ama **dışarıdan izlemenin tavanı** vardı: tüm kümeyi kaba konteyner "
            "metrikleriyle değerlendiriyor ve tek bir düğmeyi (toplam TaskManager sayısı) çevirdiği "
            "için işteki bütün operatörler birlikte ölçekleniyordu. Daha kötüsü, bir iş tamamen meşgul "
            "olup bunun hiçbiri CPU kullanımına yansımayabiliyordu.\n\n"
            "**İkinci autoscaler**, topluluğun Apache Flink Autoscaler'ı, içeriden akıl yürütüyor. "
            "Anahtar fikir her operatörün **gerçek işleme hızını (TPR)** tahmin etmek: tamamen meşgul "
            "olsa sürdürebileceği verim. Flink, her alt görev için saniyenin ne kadarının gerçek iş "
            "yaparak geçtiğini, geri basınç ve boşta bekleme süresinden ayrı raporluyor. Netflix şimdi "
            "ikisini birlikte işletiyor ve adım adım açık kaynak olana yakınsıyor."
        ),
        "key_points": [
            "Dışarıdan metrik (CPU) ile içeriden metrik (meşgul oranı) aynı şeyi söylemeyebilir; yanlış sinyal yanlış ölçekleme demek.",
            "Tek düğmeli ölçekleme (toplam TaskManager) her operatörü aynı oranda büyütür; darboğaz operatörü ayrı ölçeklemek daha verimli.",
            "Ölçeklemenin kendisinin maliyeti var (savepoint, durdur, yeniden başlat); bu yüzden gereksiz ölçekleme de pahalı.",
            "Kendi yazdığın altyapıyı sürdürmenin gizli fiyatı, hazır çözüm olgunlaştığında ortaya çıkıyor.",
        ],
        "why_it_matters": (
            "Otomatik ölçekleme kararı, beslendiği metrik kadar iyidir. Bu yazı, “CPU %40, "
            "demek ki rahatız” varsayımının ne zaman yalan söylediğini gösteriyor: iş doluyken CPU boş "
            "görünebilir. Doğru metrik, sistemin gerçekte neyi beklediğini ölçen metriktir."
        ),
        "for_you": (
            "Kendi servislerinde de kuyruğa bağlı bir tüketici çalıştırırsan aynı tuzak var: CPU'ya göre "
            "ölçekleme yapma, **kuyruk gecikmesine** (consumer lag) göre yap. Spring Boot tüketicin CPU'da "
            "%20 görünürken kuyruk büyüyorsa, iş bir dış çağrıyı bekliyordur. İkinci ders “build vs buy” "
            "için: bu gazetenin `fetch.py` içindeki RSS ayrıştırıcısı gibi küçük şeyleri kendin yazmak "
            "sorun değil; ama olgun bir kütüphane varsa onu benimseme zamanını bilmek de beceridir."
        ),
        "terms": [
            {"en": "autoscaler", "tr": "otomatik ölçekleyici", "definition": "Yüke göre kaynak miktarını insan müdahalesi olmadan artıran ya da azaltan bileşen."},
            {"en": "backpressure", "tr": "geri basınç", "definition": "Aşağı akıştaki bir bileşen yetişemediğinde, yukarıdaki üreticinin yavaşlatılması."},
            {"en": "savepoint", "tr": "kayıt noktası", "definition": "Flink işinin durumunun tutarlı bir anlık görüntüsü; durdurup yeniden başlatırken veri kaybını önler."},
            {"en": "true processing rate (TPR)", "tr": "gerçek işleme hızı", "definition": "Bir operatörün tamamen meşgul olsa sürdürebileceği teorik verim."},
        ],
    },
    {
        "url": "https://research.google/blog/how-mobility-gives-language-models-a-deeper-understanding-of-place/",
        "slot": "brief",
        "title_tr": "Bir mekânın kimliği ile işlevi aynı şey değil: hareketlilikle zenginleşmiş embedding",
        "difficulty": "orta",
        "tags": ["embedding", "araştırma", "coğrafi veri"],
        "summary": (
            "Dil modelleri mekânları (market, park, kafe gibi POI'ler) genelde adres, kategori ve metin "
            "açıklaması gibi **statik metadata** ile temsil eder. Google'ın önerdiği **ME-POIs** "
            "çerçevesi, mekânın iki imzasını ayırıyor: kâğıttaki kimliği (ad ve kategori) ve gerçek "
            "işlevsel ritmi (toplulaştırılmış ziyaret izi).\n\n"
            "Ziyaretlerin varış pencereleri, ayrılış eğilimleri ve tipik kalış süreleri bir zamansal "
            "kodlayıcıyla vektöre çevriliyor. “Uzun kuyruk” problemi de ele alınmış: ünlü yerlerin çok "
            "verisi var, küçük mahalle işletmelerinin çok az. Çözüm **mekânsal çok ölçekli ziyaret "
            "yayılımı**: bölgesel olarak benzer yerlerin davranışsal özelliklerini paylaşması. Sonuç, "
            "çalışma saati, fiyat seviyesi ve yoğunluk tahminlerinde iyileşme."
        ),
        "key_points": [
            "Statik metadata kimliği, davranış verisi işlevi anlatır; birleşince temsil zenginleşir.",
            "Az veriye sahip varlıklar için komşu varlıklardan bilgi ödünç almak, uzun kuyruk problemine pratik bir çözüm.",
        ],
        "for_you": (
            "Mobit'teki doküman arama için bir fikir: belgeleri yalnızca içeriğiyle embedding'leme; "
            "kullanım sinyalini de ekle (hangi belge hangi sorgularda açıldı, hangisi sık paylaşıldı). "
            "Metin “bu belge ne hakkında” der, kullanım “bu belge ne işe yarıyor” der. Yeni eklenen "
            "belgelerde veri azdır; aynı firmaya ait komşu belgelerden başlangıç sinyali almak "
            "burada anlatılan uzun kuyruk çözümünün küçük bir uyarlaması."
        ),
        "terms": [
            {"en": "point of interest (POI)", "tr": "ilgi noktası", "definition": "Haritada bir işletmeyi, parkı ya da simge yapıyı temsil eden kayıt."},
            {"en": "long tail", "tr": "uzun kuyruk", "definition": "Az sayıda yaygın öğenin yanında, her biri çok az veriye sahip çok sayıda nadir öğe."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
