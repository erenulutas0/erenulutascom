"""2 Kasım 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-11-02"

INTRO = (
    "Bir şey değiştiğinde her şeyi baştan hesaplamak basittir ve doğru olduğundan emin olmak "
    "kolaydır. Cloudflare’in DNS ekibi, bu basitliğin 20 milyon kayıtlı zone’larda neden "
    "çöktüğünü ve ‘en küçük güvenli işi’ kanıtlamanın neden asıl zor kısım olduğunu anlatıyor."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/dns-targeted-zone-builds/",
        "slot": "cover",
        "title_tr": "En küçük güvenli build’i kanıtlamak: Cloudflare DNS’te bellek kullanımını yüzde 85 düşüren targeted build planner",
        "difficulty": "ileri",
        "tags": ["DNS", "architecture", "performance", "distributed systems"],
        "summary": (
            "Cloudflare’in DNS propagation pipeline’ındaki Zone Builder, 2022’de saniyede yaklaşık "
            "250 DNS kayıt değişikliği alıyordu; bugün yaklaşık 700 (ayrıca yaklaşık 100 zone "
            "ayarı gibi başka olay). Yazının tespiti: sorun olay sayısı değil, bazı olayların "
            "gerektirdiği işin türü ve bu işin zone büyüklüğüyle büyümesi. Bazı zone’lar artık "
            "20 milyondan fazla kayıt tutuyor ve yüzlerce milyona doğru büyümesi bekleniyor. Her "
            "olay bir saat başlatıyor: değişikliğin authoritative DNS sunucularının kullanabileceği "
            "veriye dönüşme süresi. Bu işe **build** deniyor: build, veritabanındaki mevcut durumu "
            "okuyor, edge’de kullanılan biçime çeviriyor ve değişenleri Quicksilver’a (dağıtık "
            "key-value store) yazıyor.\n\n"
            "**Pipeline.** Müşteri bir kaydı API ya da dashboard ile değiştirir ya da başka bir "
            "Cloudflare servisi bir zone ayarını değiştirir; değişiklik veritabanına yazılır; bir "
            "Kafka olayı üretilir; DNS Kafka Aggregator birkaç topic’ten gelen olayları birleştirip "
            "Zone Builder’a verir; Zone Builder gerekli zone verisini okuyup DNS sunucularının "
            "anladığı key’lere çevirir, bu key’leri Quicksilver’la karşılaştırır ve yalnızca "
            "değişeni yazar.\n\n"
            "**Full build neden ölçeklenmedi?** Orijinal Zone Builder’ın tek bir faydalı özelliği "
            "vardı: zone’un neden değiştiğini bilmesi gerekmiyordu, mevcut veritabanı durumundan "
            "istenen durumu baştan kuruyordu. Yani zone’u ve ayarlarını oku, her DNS kaydını oku, "
            "hepsini Quicksilver key’lerine çevir, eskilerle karşılaştır, eskiyi sil ve "
            "değişeni yaz. Son yazma yalnızca değişeni içerse de full build her kaydı yine okuyor, "
            "encode ediyor ve karşılaştırıyor ve bunu yaparken tüm zone’u bellekte tutuyor. "
            "Küçük zone’da ucuz; onlarca milyon kayıtlı en büyük zone’larda zone belleğe "
            "sığmıyor. 2022’de per-record build’ler full build’lerden ortalama 150 kat, bir milyon "
            "kayıtlı bir test zone’unda 4.250 kat hızlıydı ve yazı bir sonraki adımı zone "
            "ayarları için aynısını yapmak olarak bırakmıştı.\n\n"
            "**Neden ‘değişen ayarı yeniden build et’ demek yetmiyor?** Bir kayıt olayı neyin "
            "değiştiğini söyler; bir zone olayı ise birçok Cloudflare ürününden gelebilir, "
            "zone’un neden değiştiğini söylemeyebilir ve aynı ada sahip birkaç zone’un ortak "
            "verisini değiştirebilir. Gereğinden fazla iş seçersen kapasite israf olur; "
            "gereğinden az seçersen edge’de eski ya da yanlış DNS verisi kalabilir. Örnek: "
            "Universal SSL’i açmak ya da kapatmak metadata’yı günceller ve zone apex’indeki "
            "(example.com gibi çıplak domain) CAA kayıtlarını değiştirebilir.\n\n"
            "**Çözüm: kanıtlanabilir en küçük build’i seçen bir planner ve aynı zone’un "
            "işlerini birleştiren yeni bir scheduler.** Zone ayarı değişiklikleri artık onlarca "
            "milyon kayıtlı zone’ları yeniden build etmiyor. İkisi birlikte tepe bellek "
            "kullanımını yüzde 85 düşürdü ve açılan boşluk, pipeline’ın dayanıklılık için "
            "her zaman beklediği bazı bekleme sürelerini güvenle kısaltmaya izin verdi: bir DNS "
            "değişikliğinin Quicksilver’a yazılma süresi yarıya indi. Planner beş tür build "
            "arasından seçiyor: yalnızca belirli isimlerdeki kayıtlar (A, AAAA, TXT, CNAME "
            "değişiklikleri gibi), kayıtlar ve metadata (nameserver ve wildcard değişiklikleri), "
            "apex ve metadata (Universal SSL gibi ayarlar), purge (artık yayınlanmaması gereken "
            "zone’u kaldırma) ve kanıtlanamayan her durumda full zone.\n\n"
            "**Beş problem.** Olayların neyin değiştiğini söylemesi gerekti: üretici, değişen "
            "alanları ve ayarları (mümkünse önceki ve yeni değerleriyle) olaya eklemeye başladı. "
            "Ama her olay o kadar belirgin değil: bazı veritabanı fonksiyonları yalnızca bir "
            "timestamp güncelleyip ‘zone hakkında bir şey değişti’ diyor ve bu bazen zararsız "
            "bir kayıt tutma, bazen başka yerde veri değiştiği anlamına geliyor. Çağıran "
            "tanımlanana kadar yalnızca timestamp’i değişen bir güncelleme full build "
            "tetiklemeye devam ediyor; eksik detay, bilinmeyen olay ya da zone’un herhangi bir "
            "yerindeki kaydı etkileyebilecek her değişiklik için aynı kural geçerli. Geri kalan "
            "problemler: her değişikliği en küçük doğru build’e eşlemek, aynı ada sahip tüm "
            "zone’ların paylaştığı veriyi hesaba katmak, olay ile build arasında veritabanının "
            "değişebilmesi ve işleri birleştirirken hiçbir Kafka mesajının kaybolmaması."
        ),
        "key_points": [
            "Basit ve her zaman doğru çalışan ‘her şeyi baştan hesapla’ yaklaşımı belirli bir ölçekte bellekte ve sürede çöker.",
            "Artımlı (incremental) iş yapmanın zor kısmı hesaplama değil, hangi işin güvenle atlanabileceğini kanıtlamaktır.",
            "Kanıtlayamadığın her durumda güvenli varsayılan, en büyük iştir (full build); optimizasyon bunu yalnızca kanıtlanınca atlar.",
            "Olay, neyin değiştiğini taşırsa tüketici daha küçük iş seçebilir; ‘bir şey değişti’ demek tüketiciye hiçbir seçenek bırakmaz.",
            "Kaynak kullanımını düşürmek, bekleme sürelerini kısaltacak güvenli bir boşluk yaratır.",
        ],
        "why_it_matters": (
            "Cache invalidation ve incremental build problemlerinin ortak yanı ‘ne kadarını yeniden "
            "hesaplamalıyım?’ sorusudur. Bu yazı, soruyu cevaplamak için olay şemasını "
            "zenginleştirmenin, güvenli varsayılana düşmenin ve en küçük kanıtlanmış işi "
            "seçmenin birlikte nasıl çalıştığını gösteriyor."
        ),
        "for_you": (
            "Aynı kalıbı bir cache ya da bir türetilmiş tablo için uygulayabilirsin. **(1)** Bir "
            "değişiklik olayına ‘ne değişti’ bilgisini ekle (`changed_fields`) ve tüketici yalnızca "
            "etkilenen kısmı yeniden hesaplasın. **(2)** Neyin etkilendiğinden emin olmadığın "
            "durumlarda her zaman tam yeniden hesaplamaya düş, ama bunu loglayıp sayaçla; "
            "bu oran düşüyorsa olay şemasını iyileştiriyorsun demektir. **(3)** Aynı anahtar için "
            "kısa sürede gelen birden çok olayı tek bir işe birleştir (debounce). Bu üçü, "
            "bir arama index’ini ya da bir materialized view’ı güncel tutan her sistemde işe yarar."
        ),
        "terms": [
            {"en": "incremental build", "tr": "incremental build", "definition": "Her şeyi baştan hesaplamak yerine yalnızca değişenden etkilenen kısmı yeniden hesaplama."},
            {"en": "DNS zone", "tr": "DNS zone", "definition": "Bir domain’e ait DNS kayıtlarının ve ayarlarının toplamı."},
            {"en": "authoritative DNS server", "tr": "authoritative DNS server", "definition": "Bir domain için kesin cevabı veren, kayıtları tutan DNS sunucusu."},
            {"en": "apex", "tr": "apex", "definition": "Bir domain’in çıplak hâli, örneğin example.com (alt alan adı olmadan)."},
            {"en": "debounce", "tr": "debounce", "definition": "Kısa sürede gelen birden çok olayı tek bir işlemde birleştirme."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
