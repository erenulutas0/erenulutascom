"""12 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-12"

INTRO = (
    "İki yazı, iki “kanıtlanabilirlik” hikâyesi. WhatsApp, bir ML özelliğinin uçtan uca "
    "şifrelemeyi bozmadığını nasıl **kanıtlanabilir** kıldığını anlatıyor. Google ise LLM "
    "hatalarının çoğunun bilgi eksikliği değil, bilgiye ulaşamama olduğunu ölçüyor."
)

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/08/12/security/how-were-building-scam-alert-whatsapp/",
        "slot": "cover",
        "title_tr": "Şifreli mesajlarda dolandırıcılık uyarısı: cihaz üstü model ve doğrulanabilir gizlilik",
        "difficulty": "orta",
        "tags": ["gizlilik", "güvenlik", "on-device ML", "mimari"],
        "summary": (
            "WhatsApp, **Scam Alert** adlı yeni ve isteğe bağlı bir özelliğin teknik tasarımını, "
            "özellik sınırlı beta olarak çıkarken yayımladı. Özellik, kullanıcı açarsa cihaza bir ML "
            "modeli indiriyor ve kişi listesinde olmayan gönderenlerden gelen mesajları **cihazın "
            "içinde** sınıflandırıyor. Olası dolandırıcılıkta sohbette yalnızca kullanıcının gördüğü "
            "bir uyarı çıkıyor; mesaj içeriği sınıflandırma için cihazdan çıkmıyor ve otomatik "
            "raporlama yok.\n\n"
            "Tasarım üç taahhüde dayanıyor ve her biri mimariyle zorlanıp dışarıdan doğrulanabilir "
            "kılınmış. **Cihaz üstü işleme ve gizliliği koruyan analitik:** özelliğin çalışıp "
            "çalışmadığını ölçmek için gereken en küçük telemetri (uyarı ve eylem sayıları) "
            "güvenilir yürütme ortamı (TEE) içinde işleniyor ve Meta'ya yalnızca **diferansiyel "
            "gizli** toplulaştırmalar olarak ulaşıyor. **Hedefli model dağıtımı yok:** her model "
            "sürümü, dağıtılmadan önce herkese açık bir şeffaflık defterinde yayımlanıyor; yani belirli "
            "bir kullanıcıya özel model yollanamaz. **Doğrulanabilir davranış:** model ağırlıkları "
            "yayımlanıyor, böylece araştırmacılar modelin yalnızca dolandırıcılık için üretildiğini "
            "kontrol edebilir.\n\n"
            "Kullanıcı bir uyarıyı yanlış bulursa sohbeti güvenilir işaretleyebiliyor; isterse son "
            "5 mesajı doğruluğu artırmak için paylaşmayı seçebiliyor."
        ),
        "key_points": [
            "Gizlilik sözü, “güveniniz bize” ile değil, dışarıdan denetlenebilir mimari kararlarla veriliyor.",
            "Telemetri bile minimize edilmiş: sadece sayılar, TEE içinde, diferansiyel gizlilik gürültüsüyle.",
            "Şeffaflık defteri hedefli dağıtımı engelliyor: herkes aynı modeli alıyor.",
            "Kullanıcı kontrolü: özellik isteğe bağlı, sohbet güvenilir işaretlenebilir, paylaşım ayrı bir onaya bağlı.",
        ],
        "why_it_matters": (
            "Hassas veride “verinizi korumaya çalışıyoruz” demek yeterli değil. Güçlü ürünler, "
            "sözü **doğrulanabilir** hâle getiriyor: açık ağırlıklar, kamuya açık kayıtlar, "
            "bağımsız denetim. Bu, mühendislikte güvenin ölçülebilir bir özellik olabileceğini gösteriyor."
        ),
        "for_you": (
            "KlioAI'da kullanıcı ses kayıtları tutuyorsun. Bu yazıdan üç somut kural çıkar: "
            "(1) **Veri minimizasyonu**: sunucuya yalnızca gerçekten gereken şeyi yolla (ham ses "
            "yerine transkript ya da puan yeterliyse onu). (2) Telemetriyi baştan toplulaştırılmış "
            "tasarla: bireysel olay yerine sayaç. (3) Kullanıcıya açık ve ayrı bir izin ver: model "
            "iyileştirmesi için veri kullanımı varsayılan olmasın. Bunları baştan tasarlamak, "
            "sonradan eklemekten çok daha ucuz."
        ),
        "terms": [
            {"en": "end-to-end encryption (E2EE)", "tr": "uçtan uca şifreleme", "definition": "Mesajın yalnızca gönderen ve alıcı cihazlarda çözülebildiği, aradaki sunucunun okuyamadığı şifreleme."},
            {"en": "trusted execution environment (TEE)", "tr": "güvenilir yürütme ortamı", "definition": "İçindeki kodu ve veriyi sistem sahibinden bile koruyan donanım destekli yalıtılmış çalışma alanı."},
            {"en": "differential privacy", "tr": "diferansiyel gizlilik", "definition": "Toplulaştırılmış sonuca ayarlanmış gürültü ekleyerek tek bir kişinin verisinin etkisini matematiksel olarak sınırlama."},
            {"en": "transparency ledger", "tr": "şeffaflık defteri", "definition": "Yayımlanan sürümlerin değiştirilemez ve herkese açık biçimde kaydedildiği liste."},
        ],
    },
    {
        "url": "https://research.google/blog/empty-shelves-or-lost-keys-recall-is-the-bottleneck-for-parametric-factuality/",
        "slot": "brief",
        "title_tr": "Boş raf mı, kaybolmuş anahtar mı? LLM hatalarının çoğu hatırlama hatası",
        "difficulty": "orta",
        "tags": ["LLM", "değerlendirme", "araştırma", "doğruluk"],
        "summary": (
            "Bir LLM yanlış cevap verdiğinde sebep iki olabilir: olguyu hiç öğrenmemiş (**kodlama "
            "hatası**, boş raf) ya da öğrenmiş ama erişemiyor (**hatırlama hatası**, kayıp anahtar). "
            "Standart doğruluk metrikleri ikisini birbirine karıştırıyor, oysa çözümleri farklı: "
            "birincisi daha büyük model ya da daha fazla veri ister, ikincisi son eğitim ve "
            "çıkarım-zamanı yöntemleriyle de giderilebilir.\n\n"
            "Google'ın **bilgi profillemesi** çerçevesi soruyu sorudan olguya taşıyor: her olgu "
            "“hatırlanamıyor”, “doğrudan hatırlanıyor” ya da “yalnızca düşünerek hatırlanıyor” "
            "sınıflarından birine giriyor. Bulgu: Gemini 3 ve GPT-5 gibi öncü modeller olguların "
            "neredeyse hepsini kodluyor, ama birçoğunu hatırlamakta zorlanıyor."
        ),
        "key_points": [
            "Hatayı doğru teşhis etmek, çözümü seçmenin ön koşulu: kodlama ve hatırlama farklı müdahale ister.",
            "“Düşünerek hatırlanan” olgular, çıkarım zamanında akıl yürütmenin neden doğruluğu artırabildiğini açıklıyor.",
        ],
        "for_you": (
            "RAG sistemi kurarken aynı ayrımı yap: model cevabı yanlışsa sorun bilgiyi bağlama "
            "vermemek mi (retrieval hatası), yoksa verildiği hâlde kullanamamak mı? Mobit'teki doküman "
            "aramada hatalı bir cevabı incelerken önce doğru pasajın getirilen sonuçlar arasında olup "
            "olmadığına bak. Varsa sorun üretimde, yoksa getirmede; ikisini karıştırırsan yanlış yeri "
            "düzeltirsin."
        ),
        "terms": [
            {"en": "parametric knowledge", "tr": "parametrik bilgi", "definition": "Modelin ağırlıklarında saklanan, dış kaynak olmadan cevaplayabildiği bilgi."},
            {"en": "recall vs recognition", "tr": "hatırlama ve tanıma", "definition": "Hatırlama cevabı sıfırdan üretmek, tanıma ise seçenekler arasından doğruyu seçmektir."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
