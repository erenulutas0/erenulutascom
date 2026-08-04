"""7 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-07"

INTRO = (
    "Arşivin ilk günü. Üç yazı da aynı temayı taşıyor: bireysel olarak en iyi "
    "karar, sistem için en iyi karar olmayabilir. Felaket kurtarmada, trafikte "
    "ve log incelemesinde — üçünde de kazanan, bütüne bakan taraf."
)

DRAFTS = [
    {
        "url": "https://aws.amazon.com/blogs/architecture/sp-globals-innovative-disaster-recovery-strategy-using-amazon-fsx-for-netapp-ontap-snapshots/",
        "slot": "cover",
        "title_tr": "Felaket kurtarmada ara mod: salt-okunur devretme",
        "difficulty": "orta",
        "tags": ["felaket kurtarma", "veritabanı", "mimari", "dayanıklılık"],
        "summary": (
            "Kuruluşların karmaşık SQL Server altyapıları için yüksek "
            "erişilebilirlik ve felaket kurtarma (HA/DR) çözümleri kurma "
            "zorunluluğu var — veri erişilebilirliğini ve bütünlüğünü korumak "
            "için. S&P Global Market Intelligence, Capital IQ platformu için "
            "bunu Amazon FSx for NetApp ONTAP üzerine kurmuş.\n\n"
            "Çözümün en öğretici kısmı ikili bir seçim yerine **ara bir mod** "
            "sunması: ikincil bölgede **salt-okunur moda anında devretme** "
            "(failover). Yani felaket anında sistem ya tamamen çalışıyor ya "
            "tamamen kapalı değil — okuma yapılabilen, yazma yapılamayan bir "
            "orta hâlde ayakta kalıyor.\n\n"
            "Bu ayrım pratikte çok değerli. Çoğu iş yükünde okuma trafiği "
            "yazmadan kat kat fazladır; salt-okunur bir sistem kullanıcıların "
            "büyük kısmına hizmet vermeye devam eder. Ayrıca yazmayı kapatmak, "
            "bölünmüş beyin (split-brain) riskini ortadan kaldırır — iki bölge "
            "aynı anda yazarsa veriyi uzlaştırmak çok daha zor bir problemdir.\n\n"
            "Yazı ayrıca bulut göçlerinde kavram kanıtının (POC) rolüne değiniyor: "
            "standart belirlemek, riski azaltmak ve hızı korurken iş ve teknik "
            "doğrulama yapmak."
        ),
        "key_points": [
            "\"Açık ya da kapalı\" yerine kademeli hizmet seviyeleri tasarlamak, "
            "dayanıklılığın en pratik biçimi.",
            "Anlık görüntü (snapshot) tabanlı replikasyon, tam yedekten çok daha "
            "hızlı devretme sağlıyor.",
            "Salt-okunur devretme, veri tutarlılığını koruma açısından da "
            "güvenli: çift yazma riski yok.",
        ],
        "why_it_matters": (
            "Felaket kurtarma planı olmayan sistem, sadece henüz felaket "
            "yaşamamış sistemdir. Ama iyi bir DR planının işareti \"her şeyi "
            "yedekliyoruz\" değil, **RTO ve RPO hedeflerinin açıkça tanımlanmış "
            "olmasıdır**: ne kadar sürede ayağa kalkmalıyız ve en fazla ne kadar "
            "veri kaybını kabul ediyoruz? Bu iki sayı verilmeden yapılan "
            "yatırım, ya yetersiz ya da gereksiz pahalı olur."
        ),
        "for_you": (
            "Bu iki kısaltmayı ezberle, mülakatta çıkar: **RTO** (Recovery Time "
            "Objective) — kabul edilebilir kesinti süresi; **RPO** (Recovery "
            "Point Objective) — kabul edilebilir veri kaybı. KlioAI için sor: "
            "veritabanı bozulursa kaç saatlik kullanıcı verisini kaybetmeyi "
            "göze alabilirsin? Cevap \"hiç\" ise sürekli replikasyon gerekir; "
            "\"bir gün\" ise günlük yedek yeterlidir — ve maliyet farkı büyüktür. "
            "Bir de şunu yap: **yedeğinden geri dönmeyi bir kere gerçekten "
            "dene.** Test edilmemiş yedek, yedek değildir; bunu felaket anında "
            "öğrenmek en pahalı öğrenme biçimidir."
        ),
        "terms": [
            {
                "en": "failover",
                "tr": "devretme",
                "definition": "Ana sistem çalışamaz hâle geldiğinde hizmetin yedek sisteme geçirilmesi.",
            },
            {
                "en": "RTO / RPO",
                "tr": "kurtarma süresi / kurtarma noktası hedefi",
                "definition": "RTO ne kadar sürede ayağa kalkılacağını, RPO en fazla ne kadar veri kaybının kabul edildiğini tanımlar.",
            },
            {
                "en": "split-brain",
                "tr": "bölünmüş beyin",
                "definition": "İki düğümün birbirini görmeyip ikisinin de kendini lider sanması; çelişkili yazmalar üretir.",
            },
            {
                "en": "snapshot",
                "tr": "anlık görüntü",
                "definition": "Bir depolama biriminin belirli bir andaki durumunun hızlıca alınan kopyası.",
            },
        ],
    },
    {
        "url": "https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/",
        "slot": "brief",
        "title_tr": "Herkes en kısa yolu seçerse herkes gecikir: ağ-farkında yönlendirme",
        "difficulty": "orta",
        "tags": ["optimizasyon", "araştırma", "sistem tasarımı"],
        "summary": (
            "Google Research, Nature Cities'te yayımlanan çalışmasında navigasyon "
            "platformlarının trafiği iyileştirmek için kullanılmasına dair "
            "ilk büyük ölçekli gerçek dünya araştırmasını sunuyor. Bulgu: "
            "sürücülerin **küçük bir kısmını** bile koordine etmek ağ "
            "verimliliğini iyileştiriyor.\n\n"
            "Yazının açtığı soru bir mühendis için çok tanıdık: karayolu "
            "trafiği, havacılığın hava sahasını ya da internetin veri "
            "paketlerini yönettiği gibi sistem çapında yönetilebilir mi? "
            "Kara ulaşımının tarihsel olarak fiziksel bir kontrol kulesi "
            "olmadı, ama dijital platformlar daha koordineli bir geleceğin "
            "kapısını aralıyor.\n\n"
            "Altta yatan kavram bilgisayar biliminde iyi bilinen bir sonuç: "
            "her aktör kendi için en iyi yolu seçtiğinde ortaya çıkan denge, "
            "sistem için en iyi çözümden **daha kötü** olabilir."
        ),
        "key_points": [
            "Bireysel optimum ile toplam optimum aynı değil — trafikte, ağ "
            "yönlendirmesinde ve kaynak paylaşımında hep böyle.",
            "Küçük bir azınlığı koordine etmek bile ölçülebilir kazanç "
            "veriyor; herkesi ikna etmek gerekmiyor.",
        ],
        "for_you": (
            "Bu, dağıtık sistemlerde doğrudan karşına çıkacak bir olgu. "
            "Klasik örnek: bir servis hata alınca hemen yeniden dener. Her "
            "istemci için makul olan bu davranış, hepsi aynı anda yaptığında "
            "zaten zorlanan sunucuyu tamamen düşürür — **retry storm**. "
            "Çözümler tam olarak \"koordinasyon\" fikrinden geliyor: üstel "
            "geri çekilme, rastgele **jitter** eklemek ve devre kesici "
            "(circuit breaker). Kod yazarken \"benim isteğim için en iyisi ne?\" "
            "yerine \"herkes bunu yaparsa ne olur?\" diye sormayı alışkanlık "
            "hâline getir — bu tek soru, ölçeklenebilir sistem tasarımının "
            "önemli bir kısmını kapsıyor."
        ),
        "terms": [
            {
                "en": "selfish routing",
                "tr": "bencil yönlendirme",
                "definition": "Her aktörün yalnızca kendi maliyetini düşünerek yol seçmesi; toplam verimliliği düşürebilir.",
            },
            {
                "en": "retry storm",
                "tr": "yeniden deneme fırtınası",
                "definition": "Çok sayıda istemcinin aynı anda yeniden denemesiyle zaten zorlanan sistemin tamamen çökmesi.",
            },
            {
                "en": "jitter",
                "tr": "rastgele sapma",
                "definition": "Yeniden deneme sürelerine eklenen rastgelelik; istemcilerin aynı anda tekrar denemesini önler.",
            },
        ],
    },
    {
        "url": "https://openai.com/index/australian-payments-plus",
        "slot": "brief",
        "title_tr": "4 saatlik mutabakat incelemesi 30 dakikaya: log izinde zaman damgası tutarsızlığı",
        "difficulty": "başlangıç",
        "tags": ["hata ayıklama", "LLM", "ödeme sistemleri", "operasyon"],
        "summary": (
            "Australian Payments Plus (AP+) Avustralya'da ödeme ve kimlik "
            "altyapısı işletiyor. Ekipleri şema kuralları, teknik "
            "spesifikasyonlar, üye yükümlülükleri, operasyonel süreçler, siber "
            "güvenlik ve düzenleyici beklentiler arasında çalışıyor — hızın "
            "önemli olduğu ama doğruluk ve hesap verebilirliğin daha önemli "
            "olduğu bir alan.\n\n"
            "Paylaşılan en somut örnek bir hata ayıklama vakası: bir mutabakat "
            "(reconciliation) sorununda ekipler, sistem logları ve mutabakat "
            "verisi arasında **ince bir zaman damgası tutarsızlığını** izlemek "
            "için Codex kullanmış. Günlerce sürebilecek elle inceleme "
            "**30 dakikaya** inmiş — önceki süre 4 saat olarak veriliyor.\n\n"
            "Diğer sayılar: çalışanların %77'si haftada 2+ saat tasarruf "
            "bildiriyor, %80'i yaratıcılık ya da iş kalitesinde iyileşme "
            "belirtiyor."
        ),
        "key_points": [
            "En değerli kullanım karmaşık yaratıcı iş değil, **sıkıcı ve "
            "hacimli** iş: çok sayıda log satırında bir tutarsızlık aramak.",
            "Ödeme sistemlerinde zaman damgası tutarsızlıkları klasik bir "
            "hata kaynağı — saat dilimi, saat kayması, sıralama.",
        ],
        "for_you": (
            "Buradaki hata sınıfını tanı: **zaman damgası tutarsızlığı**. "
            "Tradebot'ta bunu mutlaka yaşamışsındır — borsa saati mi, sunucu "
            "saati mi, UTC mi? Kural basit ama sürekli ihlal edilir: "
            "**her zaman damgasını UTC olarak sakla, yalnızca gösterirken "
            "yerel saate çevir.** PostgreSQL'de `timestamptz` kullan, "
            "`timestamp` değil; Java'da `Instant` kullan, `LocalDateTime` "
            "değil. İkinci ders ise LLM kullanımıyla ilgili: modeli \"bana "
            "kod yaz\" için değil, \"bu 50.000 satır logda tutarsızlığı bul\" "
            "için kullanmak çok daha yüksek getirili. İnsanın sıkıldığı, "
            "makinenin sıkılmadığı işler."
        ),
        "terms": [
            {
                "en": "reconciliation",
                "tr": "mutabakat",
                "definition": "İki ayrı sistemin kayıtlarının birbirini tutup tutmadığının karşılaştırılması (ör. banka kaydı ile iç kayıt).",
            },
            {
                "en": "clock skew",
                "tr": "saat kayması",
                "definition": "Farklı sunucuların saatlerinin birbirinden sapması; olayların yanlış sırada görünmesine yol açar.",
            },
            {
                "en": "UTC",
                "tr": "UTC",
                "definition": "Saat dilimlerinden bağımsız evrensel zaman standardı; veri saklamanın doğru birimi.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
