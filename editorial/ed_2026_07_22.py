"""22 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-22"

INTRO = (
    "Bugün dört yazı da aynı soruyu farklı yerlerden soruyor: bağlantı, "
    "uzman ya da istikrar yoksa sistem nasıl çalışmaya devam eder? "
    "Fabrikada internet yok, kırsalda doktor yok, kuantum bilgisayarda "
    "kalibrasyon durmuyor — her seferinde cevap sistemi kendi kendine "
    "yetebilir kılmaktan geçiyor."
)

DRAFTS = [
    {
        "url": "https://aws.amazon.com/blogs/architecture/architecting-offline-first-generative-ai-applications-for-edge-deployments-using-aws-services/",
        "slot": "cover",
        "title_tr": "İnternetin olmadığı yerde AI: çevrimdışı-öncelikli mimari",
        "difficulty": "orta",
        "tags": ["edge computing", "mimari", "LLM", "dayanıklılık"],
        "summary": (
            "Yazı somut bir rakamla açılıyor: Siemens'in raporuna göre Fortune 500 "
            "şirketleri plansız duruşlar yüzünden yılda tahmini 1,4 trilyon dolar "
            "kaybediyor — ve bu kayıp, sorunu hızlı tespit edip çözecek bilgi "
            "eksikliğiyle ağırlaşıyor. Üretken AI umut verici bir çözüm, ama "
            "endüstriyel ortamlarda ayrı bir mimari problem çıkarıyor: bulut "
            "bağlantısının güvenilmez ya da hiç olmadığı yerlere büyük ölçekli "
            "AI'ı nasıl taşırsın?\n\n"
            "Cevap **çevrimdışı-öncelikli** (offline-first) mimari: çıkarımı uca "
            "taşı, bulutu ise model özelleştirme, dağıtım orkestrasyonu ve "
            "sürekli iyileştirme için kullan. Yani bulut karar vermez, hazırlar. "
            "Kritik yol tamamen yerelde çalışır.\n\n"
            "Örnek senaryolar mimariyi somutlaştırıyor: bakım ekiplerinin canlı "
            "log akışlarıyla ilgili makine kılavuzlarını eşleştirememesi; uydu "
            "bağlantısı sınırlı açık deniz platformları ve boru hattı ekiplerinin "
            "güvenlik prosedürlerine ve mevzuat belgelerine anında erişme "
            "ihtiyacı; hassas tarım ekipmanı kullanan uzak tesisler."
        ),
        "key_points": [
            "Temel ilke: **kritik yol yerelde, iyileştirme bulutta.** Bağlantı "
            "koptuğunda sistem bozulmaz, sadece güncellenmez.",
            "Uçta çalıştırmak model boyutunu kısıtlar — küçük model + iyi "
            "retrieval, büyük model + kötü bağlantıya yeğdir.",
            "Bu desen AI'a özgü değil: çevrimdışı-öncelikli mobil uygulamalar "
            "yıllardır aynı mantıkla çalışıyor.",
        ],
        "why_it_matters": (
            "\"Bağlantı her zaman var\" varsayımı, yazılım mimarisinin en yaygın "
            "sessiz varsayımlarından biri. Bu varsayımı kaldırdığın anda tasarım "
            "değişir: durum nerede tutulur, çakışma nasıl çözülür, kullanıcı ne "
            "zaman uyarılır? Bu soruların cevabını baştan vermek, sonradan "
            "eklemekten çok daha ucuzdur."
        ),
        "for_you": (
            "KlioAI'da offline kayıt senkronizasyonu yaptığını CV'nde yazıyorsun — "
            "yani bu deseni zaten uyguladın. Bu yazı sana onu daha iyi "
            "anlatabilmeni sağlar: çevrimdışı-öncelikli tasarımın zor kısmı "
            "veriyi saklamak değil, **çakışma çözümü** (conflict resolution) ve "
            "**idempotency**'dir. Kullanıcı çevrimdışıyken bir kaydı iki kez "
            "gönderirse ne olur? Sunucudaki hâli daha yeniyse hangisi kazanır? "
            "Mülakatta \"offline sync yaptım\" demek yerine \"her isteğe istemci "
            "tarafında üretilen bir idempotency anahtarı koydum, sunucu aynı "
            "anahtarı ikinci kez görürse işlemi tekrarlamıyor\" diyebilmek "
            "seviye farkıdır."
        ),
        "terms": [
            {
                "en": "offline-first",
                "tr": "çevrimdışı-öncelikli",
                "definition": "Sistemin bağlantı olmadan da tam çalışacak şekilde tasarlanması; bağlantı bir iyileştirme, önkoşul değil.",
            },
            {
                "en": "edge inference",
                "tr": "uçta çıkarım",
                "definition": "Modelin bulutta değil, verinin üretildiği cihaz ya da yerel sunucuda çalıştırılması.",
            },
            {
                "en": "idempotency",
                "tr": "değişmezlik / tekrar-güvenliği",
                "definition": "Aynı isteğin birden çok kez işlenmesinin, bir kez işlenmesiyle aynı sonucu vermesi.",
            },
        ],
    },
    {
        "url": "https://research.google/blog/symptomai-towards-a-conversational-ai-agent-for-everyday-symptom-assessment/",
        "slot": "brief",
        "title_tr": "13.917 katılımcılı bir çalışma: değerlendirmeyi nasıl kurgularsın",
        "difficulty": "orta",
        "tags": ["araştırma", "değerlendirme", "sağlık", "LLM"],
        "summary": (
            "Google Research, semptom değerlendirmesi yapan konuşma tabanlı AI "
            "prototipleriyle ulusal ölçekte bir karşılaştırmalı çalışma yürütmüş. "
            "İlgi çekici kısım tıp değil, **deney tasarımı**.\n\n"
            "13.917 gönüllü katılımcı, semptomlarını beş farklı SymptomAI "
            "ajanından birine anlatmış — her ajan görüşmeyi farklı esneklik "
            "derecesinde yürütüyor. Yani tek bir sistemi test etmemişler, "
            "**varyasyonları** rastgele atamışlar.\n\n"
            "Değerlendirme de iki katmanlı. Birincisi: klinisyenler, SymptomAI'ın "
            "ürettiği ayırıcı tanıyı (DDx) diğer klinisyenlerin verdiğiyle "
            "karşılaştırmış — vakaların %50'sinden fazlasında SymptomAI'ınkini "
            "tercih etmişler. İkincisi: tanılar, katılımcıların görüşme öncesi "
            "Fitbit cihazlarından gelen biyosinyallerle karşılaştırılmış."
        ),
        "key_points": [
            "Rastgele atanmış varyantlar, tek bir sistemi test etmekten çok daha "
            "fazla bilgi veriyor: hangi tasarım tercihinin işe yaradığını gösteriyor.",
            "Bağımsız bir sinyalle (giyilebilir cihaz verisi) çapraz doğrulama, "
            "insan yargısının tek başına yeterli olmadığı yerlerde güven artırıyor.",
        ],
        "for_you": (
            "Buradaki yöntemi kendi LLM özelliklerine uygula. \"Prompt'u "
            "iyileştirdim, daha iyi oldu\" cümlesi ölçüm değildir. SymptomAI'ın "
            "yaptığı gibi yap: iki prompt varyantı kur, aynı girdileri ikisine "
            "de ver, çıktıları körlemesine (hangisi hangisi bilmeden) "
            "değerlendir. KlioAI'daki gramer düzeltmesi için 30 örnekten oluşan "
            "sabit bir test seti kurmak, her prompt değişikliğinde bir sayı "
            "vermeni sağlar. Bu seti bir kere kurmak, sonraki her kararı "
            "kolaylaştırır."
        ),
        "terms": [
            {
                "en": "differential diagnosis (DDx)",
                "tr": "ayırıcı tanı",
                "definition": "Belirtilere uyan olası hastalıkların olasılık sırasına göre listelenmesi.",
            },
            {
                "en": "randomized variant",
                "tr": "rastgele atanmış varyant",
                "definition": "Katılımcıların farklı sistem sürümlerine rastgele dağıtılması; hangi tasarımın etkili olduğunu ayırt etmeyi sağlar.",
            },
        ],
    },
    {
        "url": "https://aws.amazon.com/blogs/architecture/building-a-serverless-ai-assistant-at-pelago-concept-to-care-in-two-weeks/",
        "slot": "brief",
        "title_tr": "İki haftada olay-güdümlü AI asistanı: insan döngüde kalarak",
        "difficulty": "orta",
        "tags": ["serverless", "mimari", "LLM", "sağlık"],
        "summary": (
            "Pelago, madde kullanım bozukluğu desteği veren bir dijital klinik. "
            "Mühendislik ekibi, bakım ekibine **önerilen değerlendirmeler** "
            "üreten olay-güdümlü bir AI asistanını AWS serverless servisleriyle "
            "(Bedrock, Lambda) iki haftada kurmuş.\n\n"
            "Kısıtlar öğretici: davranışsal sağlık konuşmaları haftalar ve aylar "
            "boyunca birikiyor; koçların her cevapta bu geçmişi hesaba katması "
            "gerekiyor. Yani sistem tek bir mesaja değil, uzun bir ilişkiye bakmak "
            "zorunda.\n\n"
            "Kritik tasarım kararı ise şu: sistem **insanı döngüde tutuyor**. "
            "AI hastaya cevap yazmıyor; bakım ekibine bağlama duyarlı öneriler "
            "sunuyor, kararı insan veriyor. Sağlık alanının gerektirdiği "
            "denetim korunurken aylarca sürecek geliştirme işi ortadan kalkıyor."
        ),
        "key_points": [
            "Olay-güdümlü mimari: yeni bir mesaj geldiğinde tetiklenen Lambda, "
            "sürekli çalışan bir servise göre hem ucuz hem basit.",
            "\"AI öneriyor, insan karar veriyor\" ayrımı, riskli alanlarda ürünü "
            "hem kullanılabilir hem savunulabilir kılıyor.",
        ],
        "for_you": (
            "**İnsan döngüde** (human-in-the-loop) deseni, senin de varsayılanın "
            "olmalı. Bir LLM özelliğini üretime alırken sor: çıktı doğrudan "
            "kullanıcıya mı gidiyor, yoksa bir insan onayından mı geçiyor? "
            "İkincisi hem riski düşürür hem de sana etiketlenmiş veri kazandırır — "
            "insanın neyi düzelttiği, modelin nerede yanıldığının en iyi kaydıdır. "
            "Ayrıca olay-güdümlü mimariye dikkat et: Spring Boot'ta her şeyi "
            "senkron HTTP ile yapmak yerine, ağır işleri bir olay kuyruğuna "
            "atmak hem yanıt süresini düşürür hem sistemi dayanıklı kılar."
        ),
        "terms": [
            {
                "en": "human-in-the-loop",
                "tr": "insan döngüde",
                "definition": "Otomatik sistemin çıktısının, etki doğurmadan önce bir insan tarafından onaylandığı tasarım.",
            },
            {
                "en": "event-driven architecture",
                "tr": "olay-güdümlü mimari",
                "definition": "Bileşenlerin birbirini doğrudan çağırmak yerine olay yayınlayıp dinleyerek haberleştiği mimari.",
            },
        ],
    },
    {
        "url": "https://research.google/blog/towards-a-quantum-computer-that-learns-from-its-errors/",
        "slot": "brief",
        "title_tr": "Hatalarından öğrenen kuantum bilgisayar: sürekli kalibrasyon problemi",
        "difficulty": "ileri",
        "tags": ["araştırma", "kuantum", "pekiştirmeli öğrenme"],
        "summary": (
            "Google Quantum AI, pekiştirmeli öğrenmeyi (RL) kuantum hata "
            "düzeltmeyle birleştirip bir kuantum bilgisayarın **sürüklenmeye** "
            "(drift) sürekli uyum sağlayabildiğini ve uzun hesaplamalar boyunca "
            "kararlı kalabildiğini göstermiş.\n\n"
            "Problemin analojisi güzel: bir orkestrada kemanlar birkaç ölçüde bir "
            "akordunu kaybetseydi, topluluk sürekli durup akort yapmak zorunda "
            "kalırdı. Kuantum bilgisayar işletmenin bugünkü gerçeği bu. Kuantum "
            "bilgisayarlar temelde **analog** makineler ve sürüklenmeye duyarlı; "
            "güvenilir çalışma için kontrol parametrelerinin (frekans, genlik, "
            "faz) sürekli yeniden kalibre edilmesi gerekiyor.\n\n"
            "Zorluk şurada: konser salonunda akortsuz enstrüman hemen duyulur, "
            "kuantum dünyasında böyle bir lüks yok — qubit'leri ölçmek kuantum "
            "üst üste binme durumlarını çökertiyor. Yani \"dinlemenin kendisi "
            "performansı bozuyor\". Çözüm, otonom bir ajanın hata tespitlerinden "
            "öğrenerek binlerce parametreyi sürekli yönlendirmesi."
        ),
        "key_points": [
            "Sistemin durumunu doğrudan ölçemediğinde, dolaylı sinyallerden "
            "(hata tespitleri) öğrenmek tek yol.",
            "Sürekli kalibrasyon, tek seferlik ayardan farklı bir mühendislik "
            "problemi: sistem değişiyor, ayar da değişmeli.",
        ],
        "for_you": (
            "Kuantum senin alanın değil ama desen tanıdık olmalı: **sistemin "
            "gerçek durumunu doğrudan göremiyorsan, dolaylı sinyallerden çıkarım "
            "yap ve sürekli düzelt.** Tradebot'ta bir stratejinin \"gerçek "
            "kârlılığını\" anlık göremezsin; getiri, düşüş (drawdown) ve "
            "kayma (slippage) gibi dolaylı sinyallerden çıkarırsın. Ve piyasa "
            "koşulları değiştikçe parametrelerin de değişmeli — bir kez ayarlanıp "
            "unutulan bir strateji, sürüklenen bir kuantum bilgisayar gibidir."
        ),
        "terms": [
            {
                "en": "drift",
                "tr": "sürüklenme",
                "definition": "Bir sistemin parametrelerinin zamanla yavaşça kayması; ilk ayarların geçersizleşmesi.",
            },
            {
                "en": "reinforcement learning (RL)",
                "tr": "pekiştirmeli öğrenme",
                "definition": "Bir ajanın deneme-yanılma ve ödül sinyaliyle karar politikasını öğrenmesi.",
            },
            {
                "en": "quantum error correction",
                "tr": "kuantum hata düzeltme",
                "definition": "Kuantum bilgisayarlarda gürültü kaynaklı hataları tespit edip düzelten teknikler bütünü.",
            },
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
