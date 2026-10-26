"""28 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-28"

INTRO = "Bugünün kapağı internetin ne kadar kırılgan olduğunu hatırlatıyor: bir tayfun, bir sınav dönemi kararı, bir elektrik kesintisi — üçü de milyonlarca insanı çevrimdışı bırakabiliyor. Altyapı çalışırken görünmez, bozulduğunda tüm karmaşıklığı ortaya çıkıyor."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/q2-2026-internet-disruption-summary/",
        "slot": "cover",
        "title_tr": "İnternetin kırılganlığı: 2026 ikinci çeyreğinin büyük kesintileri",
        "difficulty": "başlangıç",
        "tags": [
            "internet infrastructure",
            "networking",
            "observability"
        ],
        "summary": "Cloudflare'in çeyreklik kesinti özeti, iyi bir açılış cümlesiyle başlıyor: çoğu altyapı gibi, internetin kırılganlığını da göz ardı etmek kolay — **çalıştığı sürece**. Bozulduğunda karmaşıklığı tüm çıplaklığıyla görünüyor.\n\n2026'nın ikinci çeyreğindeki bulgular üç farklı kesinti türünü gösteriyor. **Doğa olayları:** Guam'ın hemen kuzeyinden geçen Süper Tayfun Sinlaku, çeyreğin en uzun kesintisine yol açmış — ada doğrudan darbe almasa da tropik fırtına gücündeki rüzgârlar altyapıyı düşürmüş. Venezuela ve Tanzanya'daki kesintiler ise elektrik kaynaklı. **Devlet müdahalesi:** en sık görülen kesintiler Sudan'da sınav dönemlerindeki devlet kaynaklı kapatmalar. **Geri dönüş:** İran, uzun bir aradan sonra ulusal internet erişimini yeniden açmış.\n\nMetodolojik olarak da öğretici: Cloudflare bu kesintileri kendi ağındaki trafik verisiyle tespit edip Cloudflare Radar üzerinde işaretliyor — yani gözlem, tek bir ağın kendi konumundan yapılan bir inference.",
        "key_points": [
            "Kesinti sebepleri teknik değil çoğunlukla fiziksel ve politik: hava, elektrik, devlet kararı.",
            "En uzun kesinti ile en sık kesinti farklı kategorilerden geliyor — \"kaç kere\" ile \"ne kadar süre\" ayrı metrikler.",
            "Ölçüm bir bakış açısıdır: Cloudflare'in gördüğü, Cloudflare'in trafiğinden görünenle sınırlı ve bunu açıkça söylüyorlar."
        ],
        "why_it_matters": "Bulutta çalışan bir mühendis olarak varsayımın \"internet var\" olur. Bu rapor o varsayımın bazı coğrafyalarda ne kadar zayıf olduğunu gösteriyor. Küresel kullanıcıya hizmet veren bir ürün tasarlıyorsan, bağlantı kalitesi bir özellik değil bir kısıttır.",
        "for_you": "Kullanıcılarının bağlantı kalitesi şehirden şehre değişiyorsa bu yazının pratik karşılığı şu: uygulamanı kötü ağ koşullarında test et. Chrome DevTools’ta network throttling, Android’de geliştirici seçenekleriyle yavaş ağ simülasyonu var. Test ederken şunlara bak: istek timeout’u ne kadar, retry var mı ve **exponential backoff** uygulanıyor mu, bağlantı yokken kullanıcıya ne gösteriliyor? Bu üç sorunun cevabı, uygulamanın kötü ağda kullanılabilir olup olmadığını belirler.",
        "terms": [
            {
                "en": "internet shutdown",
                "tr": "internet shutdown",
                "definition": "Bir devletin belirli bir bölgede ya da ülke genelinde internet erişimini kasten kesmesi."
            },
            {
                "en": "exponential backoff",
                "tr": "exponential backoff",
                "definition": "Başarısız isteği yeniden denerken bekleme süresini kademeli artırma; sunucuyu yeniden deneme seliyle boğmayı önler."
            }
        ]
    },
    {
        "url": "https://openai.com/index/scientific-computing-agentic-ai",
        "slot": "brief",
        "title_tr": "Makale ekindeki kod: bilimsel yazılımın kırılganlık problemi",
        "difficulty": "başlangıç",
        "tags": [
            "software quality",
            "research",
            "agent"
        ],
        "summary": "Bilimsel hesaplama modern araştırmanın temel direği, ama veriyi analiz eden yazılım veri üretim hızına yetişemiyor. Sebep yazıda açıkça anlatılıyor: yaygın kullanılan araştırma araçlarının çoğu bir makaleye eşlik eden kod olarak başlamış — mühendislik deneyimi sınırlı, paketleme, test, optimizasyon ve uzun vadeli bakım için zamanı olmayan küçük akademik ekipler tarafından yazılmış.\n\nSonuç: sürekli bakım gerektiren, yavaş ve kırılgan iş akışlarına dayanan bir bilimsel altyapı. Ve bu kısıtlar keşfin hızını doğrudan yavaşlatıyor.\n\nOpenAI, çoğu yaşam bilimlerinde olmak üzere sekiz agent destekli bilimsel hesaplama projesini kapsayan keşifsel bir saha raporu paylaşıyor — beşi yalnızca Codex, üçü Codex ve Claude Code kombinasyonuyla. Vaka çalışmalarını araştırmacıların kendileri yazmış.",
        "key_points": [
            "Problem yeni bir problem değil: \"çalışan kod\" ile \"sürdürülebilir kod\" arasındaki fark, akademide özellikle keskin.",
            "Agent'ların buradaki değeri yaratıcılık değil, sıkıcı işi üstlenmek: paketleme, test yazma, optimizasyon."
        ],
        "for_you": "Bu yazıdaki gözlem kendi projelerine de uyar. Araştırma ve deney kodu muhtemelen production kodundan farklı standartta; bu normal ve doğru. Ama ikisi arasındaki sınırı **bilinçli** çiz: `notebooks/` altındaki keşif kodu ile `src/` altındaki production kodunu ayır ve bir şey deneysellikten çıkıp kalıcı hâle geldiğinde taşırken test yaz. Bilimsel yazılımın düştüğü tuzak tam olarak bu sınırın hiç çizilmemesidir: bir gün prototip olan şey, üç yıl sonra kimsenin dokunmaya cesaret edemediği kritik altyapı olur.",
        "terms": [
            {
                "en": "research code",
                "tr": "research code",
                "definition": "Bir fikri denemek için hızla yazılan, kalıcılık ve bakım hedefi olmayan kod."
            },
            {
                "en": "technical debt",
                "tr": "technical debt",
                "definition": "Hızlı ilerlemek için ertelenen kalite işinin, ilerleyen zamanda faiziyle ödenmesi."
            }
        ]
    },
    {
        "url": "https://cloud.google.com/blog/topics/retail/best-buy-scales-secure-ai-access-with-workforce-identity-federation/",
        "slot": "brief",
        "title_tr": "Kullanıcı senkronizasyon pipeline'ını silmek: doğrudan federation",
        "difficulty": "orta",
        "tags": [
            "authentication",
            "security",
            "cloud",
            "operasyon"
        ],
        "summary": "Best Buy, Google Cloud kullanımını genişletirken iki ölçekleme sorunuyla karşılaşmış: binlerce kullanıcıyı Microsoft Entra ID'den senkronize ederken riski azaltmak ve idari sürtünmeyi yönetmek.\n\nEski durum tanıdık: kullanıcıları Entra ID'den Google Cloud'a kopyalayan karmaşık senkronizasyon pipeline'ları. Çözüm ise pipeline'ı iyileştirmek değil **ortadan kaldırmak** — Workforce Identity Federation ile geliştiriciler ayrı bir kimlik deposu olmadan, mevcut Microsoft kimlikleriyle doğrudan bulut kaynaklarına erişiyor.\n\nYazıdaki en iyi cümle, eski desen hakkında: **\"Bu desen küçük ölçekte çalışabilir, ama ekibin büyüdükçe sessizce bir yükümlülüğe dönüşür.\"**",
        "key_points": [
            "Senkronizasyon pipeline'ları her zaman bir gecikme ve tutarsızlık kaynağıdır — kaldırılabiliyorsa kaldırmak en iyi optimizasyondur.",
            "Servis hesaplarını doğrudan federation’la değiştirmek, hem denetimi hem iptal etmeyi (revocation) basitleştiriyor."
        ],
        "for_you": "\"Küçük ölçekte çalışır, büyüdükçe sessizce yükümlülüğe dönüşür\" cümlesini bir kontrol sorusuna çevir: şu an yaptığım şey 10 kat büyüsem de çalışır mı? Kimlik yönetiminde bunun somut hâli şu — projelerinde paylaşılan servis hesapları ve elle dağıtılan anahtarlar varsa, bunlar ekip büyüdüğünde ilk kırılacak yerdir. Öğrenilecek kavram **OIDC**: kendi kullanıcı deposunu tutmak yerine kimliği bir sağlayıcıya devretmek. Spring Security ile kurmak yarım günlük iş ve hem güvenliği hem de \"şifremi unuttum\" akışını sana yazdırmaktan kurtarır.",
        "terms": [
            {
                "en": "identity federation",
                "tr": "identity federation",
                "definition": "Kullanıcıları kopyalamadan, başka bir sistemin kimlik doğrulamasına güvenerek erişim verme."
            },
            {
                "en": "OIDC (OpenID Connect)",
                "tr": "OIDC (OpenID Connect)",
                "definition": "OAuth 2.0 üzerine kurulu, kimlik doğrulamayı standartlaştıran protokol."
            },
            {
                "en": "service account",
                "tr": "service account",
                "definition": "İnsan değil bir uygulama adına kimlik doğrulayan hesap; paylaşıldığında denetim izi kaybolur."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
