"""7 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-07"

INTRO = "Arşivin ilk günü. Üç yazı da aynı temayı taşıyor: bireysel olarak en iyi karar, sistem için en iyi karar olmayabilir. Felaket kurtarmada, trafikte ve log incelemesinde — üçünde de kazanan, bütüne bakan taraf."

DRAFTS = [
    {
        "url": "https://aws.amazon.com/blogs/architecture/sp-globals-innovative-disaster-recovery-strategy-using-amazon-fsx-for-netapp-ontap-snapshots/",
        "slot": "cover",
        "title_tr": "Felaket kurtarmada ara mod: salt-okunur failover",
        "difficulty": "orta",
        "tags": [
            "felaket kurtarma",
            "database",
            "architecture",
            "resilience"
        ],
        "summary": "Kuruluşların karmaşık SQL Server altyapıları için yüksek erişilebilirlik ve felaket kurtarma (HA/DR) çözümleri kurma zorunluluğu var — veri erişilebilirliğini ve bütünlüğünü korumak için. S&P Global Market Intelligence, Capital IQ platformu için bunu Amazon FSx for NetApp ONTAP üzerine kurmuş.\n\nÇözümün en öğretici kısmı ikili bir seçim yerine **ara bir mod** sunması: ikincil bölgede **salt-okunur moda anında failover** (failover). Yani felaket anında sistem ya tamamen çalışıyor ya tamamen kapalı değil — okuma yapılabilen, yazma yapılamayan bir orta hâlde ayakta kalıyor.\n\nBu ayrım pratikte çok değerli. Çoğu iş yükünde okuma trafiği yazmadan kat kat fazladır; salt-okunur bir sistem kullanıcıların büyük kısmına hizmet vermeye devam eder. Ayrıca yazmayı kapatmak, split-brain (split-brain) riskini ortadan kaldırır — iki bölge aynı anda yazarsa veriyi uzlaştırmak çok daha zor bir problemdir.\n\nYazı ayrıca bulut göçlerinde kavram kanıtının (POC) rolüne değiniyor: standart belirlemek, riski azaltmak ve hızı korurken iş ve teknik doğrulama yapmak.",
        "key_points": [
            "\"Açık ya da kapalı\" yerine kademeli hizmet seviyeleri tasarlamak, dayanıklılığın en pratik biçimi.",
            "Snapshot (snapshot) tabanlı replikasyon, tam yedekten çok daha hızlı failover sağlıyor.",
            "Salt-okunur failover, veri tutarlılığını koruma açısından da güvenli: çift yazma riski yok."
        ],
        "why_it_matters": "Felaket kurtarma planı olmayan sistem, sadece henüz felaket yaşamamış sistemdir. Ama iyi bir DR planının işareti \"her şeyi yedekliyoruz\" değil, **RTO ve RPO hedeflerinin açıkça tanımlanmış olmasıdır**: ne kadar sürede ayağa kalkmalıyız ve en fazla ne kadar veri kaybını kabul ediyoruz? Bu iki sayı verilmeden yapılan yatırım, ya yetersiz ya da gereksiz pahalı olur.",
        "for_you": "Bu iki kısaltmayı ezberle, mülakatta çıkar: **RTO** (Recovery Time Objective), kabul edilebilir kesinti süresi; **RPO** (Recovery Point Objective), kabul edilebilir veri kaybı. Kendi uygulaman için sor: veritabanı bozulursa kaç saatlik kullanıcı verisini kaybetmeyi göze alabilirsin? Cevap ‘hiç’ ise sürekli replication gerekir, ‘bir gün’ ise günlük backup yeterlidir ve maliyet farkı büyüktür. Bir de şunu yap: **backup’tan geri dönmeyi bir kere gerçekten dene.** Test edilmemiş backup, backup değildir; bunu felaket anında öğrenmek en pahalı öğrenme biçimidir.",
        "terms": [
            {
                "en": "failover",
                "tr": "failover",
                "definition": "Ana sistem çalışamaz hâle geldiğinde hizmetin yedek sisteme geçirilmesi."
            },
            {
                "en": "RTO / RPO",
                "tr": "RTO / RPO",
                "definition": "RTO ne kadar sürede ayağa kalkılacağını, RPO en fazla ne kadar veri kaybının kabul edildiğini tanımlar."
            },
            {
                "en": "split-brain",
                "tr": "split-brain",
                "definition": "İki node’un birbirini görmeyip ikisinin de kendini lider sanması; çelişkili yazmalar üretir."
            },
            {
                "en": "snapshot",
                "tr": "snapshot",
                "definition": "Bir depolama biriminin belirli bir andaki durumunun hızlıca alınan kopyası."
            }
        ]
    },
    {
        "url": "https://research.google/blog/the-power-of-collaboration-how-we-can-reduce-traffic-congestion/",
        "slot": "brief",
        "title_tr": "Herkes en kısa yolu seçerse herkes gecikir: ağ-farkında yönlendirme",
        "difficulty": "orta",
        "tags": [
            "optimizasyon",
            "research",
            "system design"
        ],
        "summary": "Google Research, Nature Cities'te yayımlanan çalışmasında navigasyon platformlarının trafiği iyileştirmek için kullanılmasına dair ilk büyük ölçekli gerçek dünya araştırmasını sunuyor. Bulgu: sürücülerin **küçük bir kısmını** bile koordine etmek ağ verimliliğini iyileştiriyor.\n\nYazının açtığı soru bir mühendis için çok tanıdık: karayolu trafiği, havacılığın hava sahasını ya da internetin veri paketlerini yönettiği gibi sistem çapında yönetilebilir mi? Kara ulaşımının tarihsel olarak fiziksel bir kontrol kulesi olmadı, ama dijital platformlar daha koordineli bir geleceğin kapısını aralıyor.\n\nAltta yatan kavram bilgisayar biliminde iyi bilinen bir sonuç: her aktör kendi için en iyi yolu seçtiğinde ortaya çıkan denge, sistem için en iyi çözümden **daha kötü** olabilir.",
        "key_points": [
            "Bireysel optimum ile toplam optimum aynı değil — trafikte, ağ yönlendirmesinde ve kaynak paylaşımında hep böyle.",
            "Küçük bir azınlığı koordine etmek bile ölçülebilir kazanç veriyor; herkesi ikna etmek gerekmiyor."
        ],
        "for_you": "Bu, dağıtık sistemlerde doğrudan karşına çıkacak bir olgu. Klasik örnek: bir servis hata alınca hemen yeniden dener. Her istemci için makul olan bu davranış, hepsi aynı anda yaptığında zaten zorlanan sunucuyu tamamen düşürür — **retry storm**. Çözümler tam olarak \"koordinasyon\" fikrinden geliyor: exponential backoff, rastgele **jitter** eklemek ve circuit breaker (circuit breaker). Kod yazarken \"benim isteğim için en iyisi ne?\" yerine \"herkes bunu yaparsa ne olur?\" diye sormayı alışkanlık hâline getir — bu tek soru, ölçeklenebilir sistem tasarımının önemli bir kısmını kapsıyor.",
        "terms": [
            {
                "en": "selfish routing",
                "tr": "selfish routing",
                "definition": "Her aktörün yalnızca kendi maliyetini düşünerek yol seçmesi; toplam verimliliği düşürebilir."
            },
            {
                "en": "retry storm",
                "tr": "retry storm",
                "definition": "Çok sayıda istemcinin aynı anda yeniden denemesiyle zaten zorlanan sistemin tamamen çökmesi."
            },
            {
                "en": "jitter",
                "tr": "jitter",
                "definition": "Yeniden deneme sürelerine eklenen rastgelelik; istemcilerin aynı anda tekrar denemesini önler."
            }
        ]
    },
    {
        "url": "https://openai.com/index/australian-payments-plus",
        "slot": "brief",
        "title_tr": "4 saatlik reconciliation incelemesi 30 dakikaya: log izinde timestamp tutarsızlığı",
        "difficulty": "başlangıç",
        "tags": [
            "debugging",
            "LLM",
            "payments",
            "operasyon"
        ],
        "summary": "Australian Payments Plus (AP+) Avustralya'da ödeme ve kimlik altyapısı işletiyor. Ekipleri şema kuralları, teknik spesifikasyonlar, üye yükümlülükleri, operasyonel süreçler, siber güvenlik ve düzenleyici beklentiler arasında çalışıyor — hızın önemli olduğu ama doğruluk ve hesap verebilirliğin daha önemli olduğu bir alan.\n\nPaylaşılan en somut örnek bir debugging vakası: bir reconciliation (reconciliation) sorununda ekipler, sistem logları ve reconciliation verisi arasında **ince bir timestamp tutarsızlığını** izlemek için Codex kullanmış. Günlerce sürebilecek elle inceleme **30 dakikaya** inmiş — önceki süre 4 saat olarak veriliyor.\n\nDiğer sayılar: çalışanların %77'si haftada 2+ saat tasarruf bildiriyor, %80'i yaratıcılık ya da iş kalitesinde iyileşme belirtiyor.",
        "key_points": [
            "En değerli kullanım karmaşık yaratıcı iş değil, **sıkıcı ve hacimli** iş: çok sayıda log satırında bir tutarsızlık aramak.",
            "Ödeme sistemlerinde timestamp tutarsızlıkları klasik bir hata kaynağı — saat dilimi, clock skew, sıralama."
        ],
        "for_you": "Buradaki hata sınıfını tanı: **timestamp tutarsızlığı**. Borsa saati mi, sunucu saati mi, UTC mi? Kural basit ama sürekli ihlal edilir: **her timestamp’i UTC olarak sakla, yalnızca gösterirken yerel saate çevir.** PostgreSQL’de `timestamptz` kullan, `timestamp` değil; Java’da `Instant` kullan, `LocalDateTime` değil. İkinci ders LLM kullanımıyla ilgili: modeli ‘bana kod yaz’ için değil, ‘bu 50.000 satır logda tutarsızlığı bul’ için kullanmak çok daha yüksek getirili. İnsanın sıkıldığı, makinenin sıkılmadığı işler.",
        "terms": [
            {
                "en": "reconciliation",
                "tr": "reconciliation",
                "definition": "İki ayrı sistemin kayıtlarının birbirini tutup tutmadığının karşılaştırılması (ör. banka kaydı ile iç kayıt)."
            },
            {
                "en": "clock skew",
                "tr": "clock skew",
                "definition": "Farklı sunucuların saatlerinin birbirinden sapması; olayların yanlış sırada görünmesine yol açar."
            },
            {
                "en": "UTC",
                "tr": "UTC",
                "definition": "Saat dilimlerinden bağımsız evrensel zaman standardı; veri saklamanın doğru birimi."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
