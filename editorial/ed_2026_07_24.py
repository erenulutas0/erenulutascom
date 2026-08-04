"""24 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-24"

INTRO = (
    "Bugün tek yazı var ama iyisinden: Cloudflare internetin yönlendirme "
    "protokolünde kimsenin bakmadığı bir alana bakmış ve yolların %70'inde "
    "beklenmedik bir şey bulmuş. Yanına arşivden Uber'in Go performans yazısını "
    "koydum — ikisi de aynı türden bir iş: kimsenin bakmadığı yere bakmak."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/bgp-origin-attribute/",
        "slot": "cover",
        "title_tr": "İnternetin yolları neden beklendiği gibi çalışmıyor: BGP ORIGIN bulgusu",
        "difficulty": "ileri",
        "tags": ["ağ", "internet altyapısı", "protokol"],
        "summary": (
            "**BGP** (Border Gateway Protocol) internetin fiili yönlendirme "
            "protokolü. Otonom Sistemler (AS) — yani internet servis "
            "sağlayıcıları, bulut sağlayıcıları, büyük şirketler — trafiği nasıl "
            "gönderip almak istediklerini bu protokolle ifade eder. Bunun için "
            "**yol nitelikleri** (path attributes) kullanılır; yol seçim algoritması "
            "bu nitelikleri belirli bir sırayla işleyip en iyi yolu hesaplar.\n\n"
            "Cloudflare bu niteliklerden birine, zorunlu olan **ORIGIN**'e bakmış. "
            "ORIGIN her BGP duyurusunda bulunmak zorunda ve kural şu: onu duyuran "
            "yönlendirici bir kez ayarladıktan sonra hiçbir yönlendirici bunu "
            "değiştirmemeli.\n\n"
            "Bulgu çarpıcı: çok sayıda gözlem noktasında görülen yolların "
            "**yaklaşık %70'inde** ORIGIN değeri, onu duyuran otonom sistemin "
            "ayarladığından farklı. Yani spesifikasyonun \"değiştirilmemeli\" "
            "dediği alan, pratikte yaygın olarak değiştiriliyor.\n\n"
            "Bunun somut bir sonucu var. BGP yol seçiminde iki yolun Local "
            "Preference değeri ve AS_PATH uzunluğu eşitse, yönlendirici **daha "
            "düşük ORIGIN değerine sahip** yolu seçer. Yani sessizce değiştirilen "
            "bu alan, trafiğin internette hangi yoldan aktığını doğrudan etkiliyor."
        ),
        "key_points": [
            "ORIGIN üç değer alır: IGP (0), EGP (1, artık kullanılmayan eski protokol), "
            "INCOMPLETE (2).",
            "Halka açık BGP toplayıcılarında dağılım: %89,8 IGP, %3,5 EGP, %6,7 INCOMPLETE.",
            "Spesifikasyonun \"değiştirilmemeli\" dediği bir alanın %70 oranında "
            "değiştirilmesi, standart ile pratik arasındaki mesafenin iyi bir örneği.",
            "Etki teorik değil: eşitlik durumunda yol seçimini bu alan belirliyor.",
        ],
        "why_it_matters": (
            "Bu yazı bir mühendislik alışkanlığı öğretiyor: **spesifikasyonun ne "
            "dediğine değil, sistemin ne yaptığına bak.** Cloudflare'in avantajı "
            "özel bir zekâ değil, ölçüm yapabildiği bir konum — internetin geniş "
            "bir kesitini görebiliyorlar ve bu kesite bakmayı akıl ettiler. "
            "Kendi sistemlerinde de en değerli bulgular genelde \"herkesin doğru "
            "varsaydığı şeyi ölçtüm\" cümlesiyle başlar."
        ),
        "for_you": (
            "Doğrudan BGP ile çalışmayacaksın, ama iki şey işine yarar. Birincisi "
            "kavram: internet trafiğinin yolu tek bir otoritenin kararı değil, "
            "binlerce bağımsız sistemin tercihlerinin bileşimi — \"neden bu "
            "sunucuya gecikme yüksek?\" sorusunun cevabı bazen senin kodunda değil "
            "burada. İkincisi yöntem: Tradebot'ta bir varsayımın (\"borsa verisi "
            "her zaman sıralı gelir\", \"timestamp'ler hep artan\") doğru olduğunu "
            "test etmeden kabul ediyorsan, Cloudflare'in yaptığını küçük ölçekte "
            "yap — ölç ve dağılıma bak. Sistemlerdeki en pahalı hatalar, "
            "doğrulanmamış varsayımlardan çıkar."
        ),
        "terms": [
            {
                "en": "BGP (Border Gateway Protocol)",
                "tr": "sınır ağ geçidi protokolü",
                "definition": "İnternetteki bağımsız ağların birbirine hangi yolların üzerinden ulaşılacağını duyurduğu yönlendirme protokolü.",
            },
            {
                "en": "Autonomous System (AS)",
                "tr": "otonom sistem",
                "definition": "Tek bir kurumun yönettiği, kendi yönlendirme politikası olan ağ; internet bunların birleşimidir.",
            },
            {
                "en": "path attribute",
                "tr": "yol niteliği",
                "definition": "Bir BGP duyurusuna eklenen ve yol seçimini etkileyen metadata alanı.",
            },
        ],
    },
    {
        "url": "https://www.uber.com/blog/zero-growth-stack/",
        "slot": "archive",
        "title_tr": "Go'da yığın büyümesini engelleyerek %10 CPU kazanmak",
        "difficulty": "ileri",
        "tags": ["performans", "Go", "profilleme", "maliyet"],
        "summary": (
            "Uber'de servislerin yaklaşık %65'i Go ile çalışıyor ve bu 2 milyondan "
            "fazla çekirdeğe denk geliyor. Bu ölçekte genel bir %1 verimlilik "
            "iyileşmesi birkaç milyon dolar demek. Yazı bir servisin kullanımını "
            "%10 iyileştirmelerini anlatıyor.\n\n"
            "Problem Go çalışma zamanının bir takasından geliyor. Goroutine'ler "
            "(thread'lerin hafif alternatifi) küçük bir yığınla (**stack**) başlar "
            "— OS thread'lerinden çok daha fazla eşzamanlılık sağlamak için. Ama "
            "ayrılan boyut yetmezse Go özel bir kontrol yapar: **iki katı** "
            "büyüklükte yeni bir yığın oluşturur ve eskisinin içeriğini kopyalar "
            "(`runtime.morestack`). Bellek kullanımını düşük tutan bu mekanizma, "
            "ölçekte CPU'ya pahalıya patlıyor.\n\n"
            "Go 1.19 uyarlanabilir yığın boyutu getirmiş: ortalama yığın kullanımını "
            "takip edip başlangıç boyutunu ona göre ayarlıyor. Kısmen iyileştirmiş "
            "ama hâlâ pahalı olabiliyor. Uber'in denediği alternatiflerden biri "
            "goroutine havuzlama — tek sorumluluğu olan worker havuzlarında çok iyi "
            "çalışıyor."
        ),
        "key_points": [
            "Bellek ile CPU arasındaki takas: küçük başlayan yığın belleği korur ama "
            "tekrarlanan genişleme CPU yakar.",
            "Çözüm yığını istenen boyutta önceden ayırmak (preallocation) — "
            "tekrarlanan kopyalamayı ortadan kaldırıyor.",
            "Ölçek argümanı net: %1 verimlilik = milyonlarca dolar. Optimizasyonun "
            "değeri her zaman ölçeğe bağlı.",
        ],
        "why_it_matters": (
            "Bu yazı \"çalışma zamanı sana bir varsayılan verir ve o varsayılan "
            "senin iş yükün için yanlış olabilir\" dersinin ders kitabı örneği. "
            "Aynı desen JVM'de heap ve GC ayarlarında, Python'da GIL ve süreç "
            "havuzlarında, PostgreSQL'de `work_mem` ve bağlantı havuzunda karşına "
            "çıkar. Varsayılanlar genel amaçlıdır; senin yük profilin genel değildir."
        ),
        "for_you": (
            "Java tarafında bunun birebir karşılığı var ve senin işine daha yakın: "
            "JVM'de thread stack boyutu (`-Xss`), heap boyutu ve GC seçimi de aynı "
            "türden varsayılanlardır. Spring Boot uygulaman ölçeklenmeye başladığında "
            "\"neden bu kadar CPU yiyor?\" sorusunun cevabı kodda değil, çalışma "
            "zamanı ayarlarında olabilir. Ama yazının asıl dersi sıralama: Uber "
            "önce **profilledi**, sonra optimize etti. Sen de `async-profiler` ya "
            "da JFR ile alev grafiği (flame graph) çıkarmadan hiçbir şeyi "
            "optimize etme — tahminle yapılan optimizasyon genelde yanlış yeri düzeltir."
        ),
        "terms": [
            {
                "en": "goroutine",
                "tr": "goroutine",
                "definition": "Go'nun hafif eşzamanlılık birimi; işletim sistemi thread'inden çok daha ucuz.",
            },
            {
                "en": "stack growth",
                "tr": "yığın büyümesi",
                "definition": "Fonksiyon çağrı yığını ayrılan alanı aşınca daha büyük bir alan ayrılıp içeriğin kopyalanması.",
            },
            {
                "en": "preallocation",
                "tr": "önceden ayırma",
                "definition": "İhtiyaç duyulacak alanı baştan ayırarak sonradan büyütme maliyetinden kaçınma.",
            },
            {
                "en": "flame graph",
                "tr": "alev grafiği",
                "definition": "CPU zamanının hangi fonksiyonlarda geçtiğini gösteren, profilleme çıktısını görselleştiren grafik.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
