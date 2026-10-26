"""7 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-07"

INTRO = "Netflix'in gerçek zamanlı dağıtık graf serisinin üçüncü bölümü: ingestion ve depolama bitti, şimdi sorgulama. İçinde her backend mühendisinin tanıdığı bir problem var: ardışık ağ çağrılarının gecikmeyi nasıl yediği."

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/how-and-why-netflix-built-a-real-time-distributed-graph-part-3-querying-the-graph-with-grpc-0f3468349607?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "Milyar kenarlı grafı 100 ms altında sorgulamak: önce genişlik, async ve tek istek",
        "difficulty": "ileri",
        "tags": [
            "graph",
            "distributed systems",
            "gRPC",
            "latency"
        ],
        "summary": "Netflix'in Real-Time Distributed Graph (RDG) serisinin ilk iki bölümü veriyi grafa dökmeyi (Flink ile ingestion) ve milyarlarca node ve kenarı tek haneli milisaniye gecikmeyle depolamayı anlatmıştı. Bu bölüm asıl soruyu soruyor: sürekli büyüyen milyar kenarlı bir grafı, çok farklı iş yükleri için nasıl **100 ms altında** cevaplatırsın? RDG şu an saniyede on binlerce, her biri farklı sorguya hizmet veriyor.\n\nSorgular iki uçta duruyor. **Sığ ve geniş**: yüksek hacimli güvenlik aramaları gibi, her adımda çok dallanan, I/O işleyen sorgular. **Derin ve dar**: “bu hesabın tüm profillerinde Stranger Things izleme geçmişi” gibi, bir adımın sonucunu beklemeden sonrakine geçemeyen, 3-4 adım zincirlenebilen sorgular. Her adım 10 ms ağ süresi tutarsa iki adım bir bayt işlenmeden 20 ms demek.\n\nTasarım kararları net: tüm çok adımlı mantığı **tek bir gRPC isteğine** paketlemek; **derinlik-öncelikli değil genişlik-öncelikli** gezinmek, çünkü her adım bir ağ çağrısı ise bir seviyedeki tüm node’ları toplu sorgulayıp paralel çağrılarla ilerlemek, yol yol gitmekten çok daha ucuz; ve **thread-per-request yerine async** çalışmak, çünkü gecikmeyi I/O belirliyor. Genişlik-öncelikli yaklaşımın bedeli bellek: her seviye bellekte tutuluyor, bunu kenar tipi başına sınırlarla yönetilebilir tutuyorlar.",
        "key_points": [
            "Gecikme bütçesini hop sayısı belirler; ardışık ağ çağrıları toplam süreye doğrusal biner.",
            "Genişlik-öncelikli gezinme, bir seviyedeki aramaları toplu ve paralel yapmayı mümkün kılar.",
            "Bellek bedeli kenar tipi başına sınırlarla sınırlanıyor: yüksek dallanma seviyesi bile yönetilebilir kalıyor.",
            "I/O ağırlıklı serviste thread başına istek yerine async model, boşta bekleyen thread'leri ortadan kaldırıyor."
        ],
        "why_it_matters": "Dağıtık sistemde performansı çoğunlukla algoritma değil, ağ turu sayısı belirler. “Kaç kez ağa çıkıyorum?” sorusu, “işlem kaç adım?” sorusundan daha belirleyicidir.",
        "for_you": "Bunun en tanıdık hâli JPA’daki **N+1 sorgu problemi**: bir listeyi çekip her satır için ayrı sorgu atmak, depth-first gezinmenin tam karşılığı. Çözümün adı da aynı: bulk load (`JOIN FETCH`, `IN (...)` ile batch). Spring Boot’un SQL log’larını açıp bir ekran için kaç sorgu attığını say; sayı sayfadaki öğe sayısıyla büyüyorsa aynı hatadasın.",
        "terms": [
            {
                "en": "breadth-first traversal",
                "tr": "breadth-first traversal",
                "definition": "Grafı yol yol değil seviye seviye dolaşma; aynı seviyedeki tüm node’ları birlikte işleme."
            },
            {
                "en": "fan-out",
                "tr": "fan-out",
                "definition": "Bir node’dan çıkan bağlantı (kenar) sayısı; yüksekse sorgu hızla genişler."
            },
            {
                "en": "async I/O",
                "tr": "async I/O",
                "definition": "Ağ ya da disk yanıtını beklerken thread'i bloklamayan çalışma modeli."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
