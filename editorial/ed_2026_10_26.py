"""26 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-26"

INTRO = "Netflix’te pik günlerde yaklaşık 100.000 workload başarısız oluyor ve debugging bir kez daha insanların zamanını yiyor. Çözüm ‘LLM’e logları ver’ değil, LLM’i deterministik bir sistemin etrafına sarmak oldu. Yanında OpenAI mühendislerinin incident’larda hızı nasıl kullandığına dair kısa bir iç örnek."

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/making-failure-diagnosis-reliable-with-pensive-ai-6b0811a1c015?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "Log’u LLM’e vermek yetmez: Netflix Pensive AI’da deterministik sistemin etrafına AI sarmak",
        "difficulty": "orta",
        "tags": [
            "LLM",
            "observability",
            "debugging",
            "data platform"
        ],
        "summary": "Netflix’te data ve ML kullanıcıları her gün milyonlarca workload çalıştırıyor (Titus, Spark, Trino, Druid gibi motorlarda) ve pik günlerde yaklaşık 100.000 tanesi başarısız oluyor. Başarısızlık yalnızca başlangıç: birinin birkaç log arasında faydalı sinyali bulması, sebebin kendi kodunda mı platformda mı olduğuna karar vermesi ve yeniden deneme, yeniden yapılandırma ya da yükseltme kararı vermesi gerekiyor. İlk çözüm **Pensive** idi: başarısız workload loglarını toplayıp regex ve elle yazılmış Java kurallarıyla hataları çıkaran ve sınıflandıran, yeniden deneme ya da düzeltme önerisini Maestro gibi ürünlere ileten bir auto-diagnosis sistemi. Başarısızlıkların yaklaşık yüzde 50’sini self-service ve bazen otomatik yaptı. Ama kurallar yalnızca bilinen kalıplarda çalışıyor: kapsam, birinin yeni bir hata kalıbını fark edip kural yazması ve engine ile log formatları değiştikçe güncel tutmasıyla büyüyor. Üç aylık bir dönemde Pensive yaklaşık yedi milyon sınıflandırma yaptı ve yarısı ‘unknown’ kovasına düştü.\n\n**Pensive AI**’nın hedefi, modeli logların önüne koymak değil; kapsamı deterministik parçaları bırakmadan genişletmek. Yazının tasarım ilkesi: **AI’ı deterministik süreçlerin etrafına sarmak**, bu da geniş kapsam, düşük gecikme, kontrollü maliyet ve yazılım yaşam döngüsü boyunca kolay bakım sağlıyor. İki yol var ve birbirini tamamlıyor: **error extraction** her başarısızlıkta otomatik çalışıyor (hızlı ilk bakış, düşük maliyet) ve **on-demand debugging** kullanıcı istediğinde loglardaki semptomlara bakıp LLM’in kendi bilgisi ve reasoning’iyle daha derin kök neden analizi yapıyor (biraz daha yüksek gecikme ve maliyet).\n\n**Bölüm 1: faydalı hatayı bulmak.** Eski kurallar kesin ama her biri belirli bir log şeklini yakalıyor (ör. bir Spark container’ın bellek sınırını aşması için bir regex). Pensive AI kuralı olmayan hataları da buluyor ve bir platform yükseltmesinden sonra şekli değişen tanıdık hatalara uyum sağlıyor. Mühendislik açısından öğretici bir karar: çıktı token’ı üretmek girdi token’ı okumaktan çok daha yavaş olduğundan, uzun hata mesajlarını model yeniden yazarsa pahalı ve yavaş olurdu. Bu yüzden her logun **satırları numaralandırılıyor** ve modele `{lineNumber, text}` kayıtları veriliyor; model metni kopyalamak yerine hangi satırların hata olduğunu döndürüyor. Log kaynağı başına çağrılar paralel çalışıyor ve hepsi Maestro’nun timeout’unun içinde belirlenmiş tek bir deadline’ı paylaşıyor; süreyi kaçıran çağrı sonuçtan çıkarılıyor ve hepsi beklenmiyor. Veri sözleşmesi de yeniden tasarlandı: eski model tek bir düz hata string’iydi, yenisi her log kaynağı için bir hata listesi ve kaynağa derin bağlantılar döndürüyor.\n\n**Bölüm 2: tam teşhis ve ürün deneyimi.** Pensive AI Debugging, başarısız bir step attempt’i analiz edip kök neden ve önerilen düzeltmeleri sunuyor; programatik API’lerden, MCP’den ve ürün arayüzünden (Data Portal) erişiliyor. Üretimi onlarca saniye ile bir dakika arası sürebildiğinden isteğe bağlı çalıştırılıyor. Bu seçim cache için sağlam bir birim yaratıyor: her debugging cevabı **step attempt’e göre cache’leniyor**; ikinci istek yeni bir AI çağrısı değil bir key-value okuması. Cache’lenmiş cevabı oku, yoksa üret ya da var olanı yeniden üretip üzerine yaz şeklinde üç başlatma biçimi var; arayüz ve programatik kullanım için farklı ihtiyaçları karşılıyor.\n\n**Erken sonuçlar.** AI error extraction artık başarısızlıkların yüzde 100’ünü kapsıyor (eski Pensive’in unknown dediği hatalar dahil). Pensive AI’ı kullanmayan başarısız step attempt’lerde, kullananlara göre ortalama yüzde 321 daha fazla manuel debug-log inceleme eylemi görüldü; yazı bunun nedensel bir iddia değil gözlemsel bir karşılaştırma olduğunu özellikle belirtiyor. Göç hâlâ sürüyor: yeni AI hata alanını şimdilik Data Portal’ın başarısız Maestro step arayüzü okuyor, diğer yüzeyler sırada.",
        "key_points": [
            "LLM’i deterministik sistemin yerine değil, onun kapsamını genişletmek için etrafına koy.",
            "Output token’ı pahalıdır: modele metni kopyalatmak yerine satır numarası döndürt.",
            "Paralel çağrıları ortak bir deadline’a bağla; geç kalanı sonuçtan çıkar, hepsini bekleme.",
            "Pahalı analizi isteğe bağlı yap, sonucunu cache’le; ucuz ilk bakışı her hatada otomatik çalıştır.",
            "Kendi sonucunu abartma: gözlemsel karşılaştırmayı nedensel gibi sunma."
        ],
        "why_it_matters": "‘Logu LLM’e ver, cevap versin’ demo’da çalışır, ölçekte maliyet, gecikme ve tutarsızlıkla patlar. Bu yazı bir LLM özelliğini production’da sürdürülebilir kılan mühendislik kararlarını gösteriyor: sınırlı çıktı, deadline, cache, ve eski sistemle yan yana çalışan bir göç.",
        "for_you": "Bir log analizi ya da debugging asistanı yazarsan üç kuralı baştan uygula. **(1)** Logu satır numarasıyla modele ver ve modelden yalnızca ilgili satır numaralarını ve kısa bir açıklamayı JSON olarak iste; metni modele yeniden yazdırma. **(2)** Hata imzasını (örneğin istisna sınıfı ve ilk stack frame) anahtar yapıp sonucu cache’le: aynı hata ikinci kez gelince LLM çağırma. **(3)** Bilinen sık hataları regex ile çöz, LLM’i yalnızca ‘unknown’ kovasına çağır ve kovanın oranını izle; bu oran düşüyorsa sistem işe yarıyor demektir.",
        "terms": [
            {
                "en": "error extraction",
                "tr": "error extraction",
                "definition": "Uzun bir log içinden hatayı açıklayan satırları ayıklayıp çıkarma."
            },
            {
                "en": "deadline",
                "tr": "deadline",
                "definition": "Bir işlemin tamamlanması gereken, sonrasında sonucun beklenmediği süre sınırı."
            },
            {
                "en": "root cause analysis",
                "tr": "root cause analysis",
                "definition": "Bir arızanın görünen belirtisinden değil asıl nedeninden başlayarak çözümleme."
            },
            {
                "en": "self-service",
                "tr": "self-service",
                "definition": "Kullanıcının başka bir ekibe başvurmadan sorunu kendi başına çözebilmesi."
            }
        ]
    },
    {
        "url": "https://openai.com/index/openai-cut-incident-investigation",
        "slot": "brief",
        "title_tr": "Incident’ta 30 saniye eşiği: OpenAI mühendisleri hızlı bir kodlama agent’ını nasıl kullanıyor",
        "difficulty": "başlangıç",
        "tags": [
            "incident response",
            "agent",
            "developer experience",
            "OpenAI"
        ],
        "summary": "OpenAI, Codex’in yüksek hızlı modu Ultrafast’i iç kullanım örneği olarak anlatıyor (kendi ürününü anlatan bir yazı; abartı payı olabilir). Mühendisler için incident response’ta varsayılan olmuş: bir şey bozulduğunda dakikalarca cevap beklemek sorunu büyütüyor. Bir mühendis incident için bir Slack kanalı açıp Codex’i olayı izlemesi, araştırması ve gelen soruları yanıtlaması için görevlendiriyor ve ‘birçok olası nedeni aynı anda arayabildiğini’ söylüyor. Bir güvenlik mimarı, yapılandırılmış ve yapılandırılmamış veriyi toplayıp normalleştirme ve bağlam verme işinin bir iki saatten 10-15 dakikaya, bazen neredeyse gerçek zamana indiğini aktarıyor.\n\nYazının asıl gözlemi hız eşiği: bir mühendis bir AI cevabı 30 saniyeden uzun sürerse Slack’e bakıp bir iş arkadaşına sorduğunu, ama işlerinin çoğunun artık bu eşiğin altında kaldığını söylüyor. Başka bir mühendis eskiden Codex’e bir şey sorup aynı anda kendisi de bakmak zorunda kaldığını, artık odağını bölmeden beklediğini anlatıyor. Bu tür testler iç kullanıcı anlatılarına dayanıyor; bağımsız ölçüm değil.",
        "key_points": [
            "Yanıt süresi bir eşiğin altına inince insanlar aracı beklemek yerine kullanır; eşik yaklaşık 30 saniye olarak anlatılıyor.",
            "Incident’ta birden çok hipotezi aynı anda aramak, tek tek denemekten hızlıdır.",
            "İç kullanıcı anlatıları değerli ipuçlarıdır ama ölçüm değildir."
        ],
        "for_you": "Incident ya da debugging için bir araç yazarsan ‘ilk anlamlı cevap’ süresini ölç ve 30 saniyenin altını hedefle. Hız için model boyutunu küçültmeden önce bağlamı kısalt ve aramaları paralelleştir: aynı soruyu log, metrik ve son deploy’lar için eşzamanlı sormak çoğu zaman en büyük kazanç.",
        "terms": [
            {
                "en": "incident response",
                "tr": "incident response",
                "definition": "Üretimdeki bir arızayı tespit etme, teşhis etme ve giderme süreci."
            },
            {
                "en": "latency",
                "tr": "latency",
                "definition": "Bir isteğin gönderilmesi ile cevabın gelmesi arasındaki süre."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
