"""12 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-12"

INTRO = "İki yazı, iki “kanıtlanabilirlik” hikâyesi. WhatsApp, bir ML özelliğinin uçtan uca şifrelemeyi bozmadığını nasıl **kanıtlanabilir** kıldığını anlatıyor. Google ise LLM hatalarının çoğunun bilgi eksikliği değil, bilgiye ulaşamama olduğunu ölçüyor."

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/08/12/security/how-were-building-scam-alert-whatsapp/",
        "slot": "cover",
        "title_tr": "Şifreli mesajlarda dolandırıcılık uyarısı: cihaz üstü model ve doğrulanabilir gizlilik",
        "difficulty": "orta",
        "tags": [
            "privacy",
            "security",
            "on-device ML",
            "architecture"
        ],
        "summary": "WhatsApp, **Scam Alert** adlı yeni ve isteğe bağlı bir özelliğin teknik tasarımını, özellik sınırlı beta olarak çıkarken yayımladı. Özellik, kullanıcı açarsa cihaza bir ML modeli indiriyor ve kişi listesinde olmayan gönderenlerden gelen mesajları **cihazın içinde** sınıflandırıyor. Olası dolandırıcılıkta sohbette yalnızca kullanıcının gördüğü bir uyarı çıkıyor; mesaj içeriği sınıflandırma için cihazdan çıkmıyor ve otomatik raporlama yok.\n\nTasarım üç taahhüde dayanıyor ve her biri mimariyle zorlanıp dışarıdan doğrulanabilir kılınmış. **Cihaz üstü işleme ve gizliliği koruyan analitik:** özelliğin çalışıp çalışmadığını ölçmek için gereken en küçük telemetri (uyarı ve eylem sayıları) trusted execution environment (TEE) (TEE) içinde işleniyor ve Meta'ya yalnızca **diferansiyel gizli** toplulaştırmalar olarak ulaşıyor. **Hedefli model dağıtımı yok:** her model sürümü, dağıtılmadan önce herkese açık bir transparency ledger’da yayımlanıyor; yani belirli bir kullanıcıya özel model yollanamaz. **Doğrulanabilir davranış:** model ağırlıkları yayımlanıyor, böylece araştırmacılar modelin yalnızca dolandırıcılık için üretildiğini kontrol edebilir.\n\nKullanıcı bir uyarıyı yanlış bulursa sohbeti güvenilir işaretleyebiliyor; isterse son 5 mesajı doğruluğu artırmak için paylaşmayı seçebiliyor.",
        "key_points": [
            "Gizlilik sözü, “güveniniz bize” ile değil, dışarıdan denetlenebilir mimari kararlarla veriliyor.",
            "Telemetri bile minimize edilmiş: sadece sayılar, TEE içinde, diferansiyel gizlilik gürültüsüyle.",
            "Transparency ledger hedefli dağıtımı engelliyor: herkes aynı modeli alıyor.",
            "Kullanıcı kontrolü: özellik isteğe bağlı, sohbet güvenilir işaretlenebilir, paylaşım ayrı bir onaya bağlı."
        ],
        "why_it_matters": "Hassas veride “verinizi korumaya çalışıyoruz” demek yeterli değil. Güçlü ürünler, sözü **doğrulanabilir** hâle getiriyor: açık ağırlıklar, kamuya açık kayıtlar, bağımsız denetim. Bu, mühendislikte güvenin ölçülebilir bir özellik olabileceğini gösteriyor.",
        "for_you": "Kullanıcı ses kaydı gibi hassas veri tutan bir uygulama yazarsan bu yazıdan üç somut kural çıkar: **(1) Data minimization:** sunucuya yalnızca gerçekten gereken şeyi yolla (ham ses yerine transkript ya da puan yeterliyse onu). **(2)** Telemetriyi baştan aggregate tasarla: bireysel olay yerine sayaç. **(3)** Kullanıcıya açık ve ayrı bir izin ver: model iyileştirmesi için veri kullanımı varsayılan olmasın. Bunları baştan tasarlamak, sonradan eklemekten çok daha ucuzdur.",
        "terms": [
            {
                "en": "end-to-end encryption (E2EE)",
                "tr": "end-to-end encryption (E2EE)",
                "definition": "Mesajın yalnızca gönderen ve alıcı cihazlarda çözülebildiği, aradaki sunucunun okuyamadığı şifreleme."
            },
            {
                "en": "trusted execution environment (TEE)",
                "tr": "trusted execution environment (TEE)",
                "definition": "İçindeki kodu ve veriyi sistem sahibinden bile koruyan donanım destekli yalıtılmış çalışma alanı."
            },
            {
                "en": "differential privacy",
                "tr": "differential privacy",
                "definition": "Toplulaştırılmış sonuca ayarlanmış gürültü ekleyerek tek bir kişinin verisinin etkisini matematiksel olarak sınırlama."
            },
            {
                "en": "transparency ledger",
                "tr": "transparency ledger",
                "definition": "Yayımlanan sürümlerin değiştirilemez ve herkese açık biçimde kaydedildiği liste."
            }
        ]
    },
    {
        "url": "https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/",
        "slot": "brief",
        "title_tr": "Boş raf mı, kaybolmuş anahtar mı? LLM hatalarının çoğu hatırlama hatası",
        "difficulty": "orta",
        "tags": [
            "LLM",
            "evaluation",
            "research",
            "accuracy"
        ],
        "summary": "Bir LLM yanlış cevap verdiğinde sebep iki olabilir: olguyu hiç öğrenmemiş (**kodlama hatası**, boş raf) ya da öğrenmiş ama erişemiyor (**hatırlama hatası**, kayıp anahtar). Standart doğruluk metrikleri ikisini birbirine karıştırıyor, oysa çözümleri farklı: birincisi daha büyük model ya da daha fazla veri ister, ikincisi son eğitim ve inference-zamanı yöntemleriyle de giderilebilir.\n\nGoogle'ın **bilgi profillemesi** çerçevesi soruyu sorudan olguya taşıyor: her olgu “hatırlanamıyor”, “doğrudan hatırlanıyor” ya da “yalnızca düşünerek hatırlanıyor” sınıflarından birine giriyor. Bulgu: Gemini 3 ve GPT-5 gibi öncü modeller olguların neredeyse hepsini kodluyor, ama birçoğunu hatırlamakta zorlanıyor.",
        "key_points": [
            "Hatayı doğru teşhis etmek, çözümü seçmenin ön koşulu: kodlama ve hatırlama farklı müdahale ister.",
            "“Düşünerek hatırlanan” olgular, inference zamanında reasoning’in neden doğruluğu artırabildiğini açıklıyor."
        ],
        "for_you": "RAG sistemi kurarken aynı ayrımı yap: model cevabı yanlışsa sorun bilgiyi bağlama vermemek mi (retrieval hatası), yoksa verildiği hâlde kullanamamak mı? Hatalı bir cevabı incelerken önce doğru pasajın getirilen sonuçlar arasında olup olmadığına bak. Varsa sorun generation’da, yoksa retrieval’da; ikisini karıştırırsan yanlış yeri düzeltirsin.",
        "terms": [
            {
                "en": "parametric knowledge",
                "tr": "parametric knowledge",
                "definition": "Modelin ağırlıklarında saklanan, dış kaynak olmadan cevaplayabildiği bilgi."
            },
            {
                "en": "recall vs recognition",
                "tr": "recall vs recognition",
                "definition": "Hatırlama cevabı sıfırdan üretmek, tanıma ise seçenekler arasından doğruyu seçmektir."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
