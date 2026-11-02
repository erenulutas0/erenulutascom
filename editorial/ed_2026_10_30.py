"""30 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-30"

INTRO = (
    "Bir sertifika otoritesinin (CA) anahtarlarının birkaç küçük sayıdan oluştuğunu hayal et: "
    "saniyeler içinde geri çıkarılabilen, herkesin taklit edebileceği bir güven zinciri. "
    "Cloudflare’in eMudhra takibi, böyle bir olayda neyin yamalandığını ve gerçekte ne "
    "denendiğini anlatıyor."
)

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/emudhra-patching/",
        "slot": "cover",
        "title_tr": "Anahtarı ‘4’ olan CA: eMudhra’nın zayıf anahtarlarının istismarı ve yamalanması",
        "difficulty": "orta",
        "tags": ["security", "PKI", "TLS", "incident"],
        "summary": (
            "19 Ekim 2026’da Cloudflare, eMudhra’nın sekiz **intermediate** anahtarının inanılmaz "
            "derecede zayıf olduğunu öğrendi. Yazının benzetmesiyle: internetin korunduğu 115 "
            "haneli bir sayıyı seçmeleri gerekirken CA’nın seçtiği sayı **4**'tü. Diğer yedi "
            "anahtar da benzer biçimde zayıftı (56, 66, 115, 155, 156, 230 ve 237). Daha "
            "önceki CA ihlallerinden (DigiNotar, TÜRKTRUST, Trustwave) farkı şu: o olaylarda "
            "anahtarlara erişim bir ölçüde sınırlıydı. Burada ise intermediate private key’ler "
            "herkes tarafından, kamuya açık sertifikalardan neredeyse anında geri "
            "çıkarılabiliyor. Bu da **herkesin** bu anahtarları bağımsız olarak elde edip, "
            "yamalanmamış ve Certificate Transparency’yi zorunlu tutmayan bir client’ın kabul "
            "edeceği, herhangi bir domain için sertifika üretebilmesi demek. eMudhra public CA "
            "işinden çıktığını duyurdu ve bunu bir key generation script’indeki hataya bağladı "
            "ama script’i henüz paylaşmadı. Bir de ilginç ayrıntı: bir certificate revocation "
            "list’i (CRL) belki doğru üretilmiş bir anahtarla imzaladılar, sonra zayıf anahtarla "
            "imzalanmış hâliyle düzelttiler.\n\n"
            "**Cloudflare’in yaması.** Yüksek öncelikli sistemlerin hepsi yamalandı; birkaç düşük "
            "etkili bilet üzerinde çalışılıyor. En çok giden TLS bağlantısını yapan, müşteri "
            "origin’lerine bakan Pingora proxy’leri saatler içinde zayıf eMudhra anahtarlarını "
            "reddedecek biçimde güncellendi.\n\n"
            "**İstismar görüldü mü?** Cloudflare, bir sertifikanın bu zayıf anahtarlarla "
            "imzalandığı her durumu yakalamak için Pingora’ya log ekledi. Bir hafta sonra yaklaşık "
            "22.000 zayıf-anahtarlı handshake denemesi görüldü; bunların üçte ikisi, geliştirici "
            "rehberinde anılan `emudhra.we-have-a-problem.com` gibi test siteleriydi. Yaklaşık 160 "
            "handshake ise öne çıkıyordu: sertifikaların Subject Alternative Name alanları, "
            "handshake’te istenen SNI ile ilgisi olmayan başka kuruluşların domain’lerini "
            "adlandırıyordu. Cloudflare yazıyı, güvenlik için önerilen düzeltmeler ve kuruluşların "
            "atması gereken sonraki adımlarla bitiriyor."
        ),
        "key_points": [
            "Bir güven zincirinin gücü, en zayıf anahtarı kadardır; anahtar üretimi sıradan bir script’e emanet edilmemeli.",
            "Certificate Transparency, sahte sertifikaları herkesin görebilmesini sağlayarak ikinci bir savunma katmanı oluşturur.",
            "Giden (outbound) bağlantılarda da sertifika doğrulamasını sıkılaştırmak gerekir; çoğu ekip yalnızca gelen trafiğe bakar.",
            "Bir kusur duyurulunca ‘istismar edildi mi?’ sorusunu cevaplamak için önceden log ve ölçüm olması gerekir.",
        ],
        "why_it_matters": (
            "TLS güvenliği çoğunlukla ‘sertifikayı bir CA imzaladıysa güvenilirdir’ varsayımına "
            "dayanır. Bu olay, o varsayımın ne kadar kırılgan olduğunu ve zincirin birkaç "
            "noktasında yapılacak sıkılaştırmanın (CT zorunluluğu, kendi giden trafiğini "
            "izleme) neden önemli olduğunu gösteriyor."
        ),
        "for_you": (
            "Üç somut adım. **(1)** Kendi servislerinin TLS client’larında güvenilen CA "
            "listesine (trust store) bak ve gereksiz kökleri çıkar; ‘çoğu zaman sistem varsayılanı’ "
            "demek yeterli değil. **(2)** Kritik bir servise bağlanırken sertifika pinning ya da "
            "yalnızca belirli bir CA’ya izin veren bir kısıt eklemeyi düşün (iç servisler için). "
            "**(3)** Çıkış trafiğinde (örneğin ödeme sağlayıcı ya da bir üçüncü taraf API’ye) "
            "TLS handshake hatalarını ve beklenmeyen sertifika zincirlerini logla ve alarma bağla; "
            "Cloudflare’in istismar girişimlerini görmesini sağlayan şey de bu log’du."
        ),
        "terms": [
            {"en": "certificate authority (CA)", "tr": "certificate authority (CA)", "definition": "Sertifikaları imzalayarak bir domain’in kimliğini doğrulayan, güvenilen kuruluş."},
            {"en": "intermediate certificate", "tr": "intermediate certificate", "definition": "Kök CA ile son kullanıcı sertifikası arasındaki, imza yetkisi olan ara sertifika."},
            {"en": "Certificate Transparency (CT)", "tr": "Certificate Transparency (CT)", "definition": "Verilen tüm sertifikaların herkese açık, değiştirilemez günlüklere kaydedilmesi sistemi."},
            {"en": "SNI", "tr": "SNI", "definition": "Server Name Indication: istemcinin handshake sırasında ulaşmak istediği domain adını bildirmesi."},
            {"en": "trust store", "tr": "trust store", "definition": "Bir sistemin güvendiği kök sertifika otoritelerinin listesi."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
