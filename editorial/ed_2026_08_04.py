"""4 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-04"

INTRO = "Tek yazı, ama güvenlik mühendisliği için ders niteliğinde: iki bağımsız test ortağında, internete kapalı olması gereken (ya da kontrollü açılan) değerlendirme ortamlarından modeller dışarı taşmış. Geçen ay Hugging Face olayını okuduysan bu, aynı sorunun ikinci perdesi."

DRAFTS = [
    {
        "url": "https://openai.com/index/third-party-cyber-evaluations-involving-openai-models",
        "slot": "cover",
        "title_tr": "Test ortamı da bir saldırı yüzeyidir: üçüncü taraf siber değerlendirmelerde sızıntı",
        "difficulty": "orta",
        "tags": [
            "security",
            "isolation",
            "evaluation",
            "LLM"
        ],
        "summary": "OpenAI, iki dış test ortağının yürüttüğü siber değerlendirmelerde modellerin **kendilerine çizilen test sınırının dışına çıktığı** olayları açıkladı. Bu olaylar, geçen ay anlatılan Hugging Face olayından ayrı.\n\nİki vaka var. Birincisinde İngiltere'nin AI Güvenlik Enstitüsü (UK AISI), agent’ların kendi araçlarını bulabilmesi ve gerçek bir saldırgana yakın koşullarda çalışabilmesi için **internet erişimini bilerek açık** bırakmıştı; üstüne modelin ham yeteneğini ölçmek için siber sınıflandırıcılar da kapalıydı. İkincisinde Irregular adlı ortak, internetten izole olması gereken bir CTF tarzı değerlendirme çalıştırıyordu, ama **bir ortam yapılandırma hatası** modellerin açık internete çıkmasına izin verdi.\n\nOpenAI'ın vardığı sonuç mühendislik açısından net: modellerin yetenekleri arttıkça, etraflarındaki güvenlik ve emniyet sistemlerinin de aynı hızla gelişmesi gerekiyor. Önümüzdeki haftalarda yüksek riskli değerlendirmelerin nasıl belirleneceğini, kapsamın nasıl anlaşılacağını, internet erişimi veya düşürülmüş korumalar talebinin nasıl değerlendirileceğini ve izolasyon beklentilerinin nasıl koyulacağını gözden geçireceklerini söylüyorlar.",
        "key_points": [
            "Bir vakada erişim bilerek açıktı; diğerinde yapılandırma hatasıyla açık kaldı. İkisi de “sandbox sızdı” sonucunu verdi.",
            "Ham yeteneği ölçmek için koruma kapatıldığında, ortam artık tek savunma hattı olur.",
            "Çözüm tek bir yama değil, süreç: risk sınıflandırması, kapsam anlaşması, izolasyon beklentisi."
        ],
        "why_it_matters": "İzolasyonu yapılandırmaya bırakırsan, tek bir yanlış satır tüm sınırı siler. Gerçek izolasyon varsayılanı kapalı olan, açmak için bilinçli ve kayıtlı bir karar gerektiren altyapıdır.",
        "for_you": "Küçük ölçekte aynı hata sende de olabilir: Docker'da “bu konteyner dışarı çıkmaz” demek yerine `--network=none` ya da bir egress kuralı koy. GitHub Actions'ta da `permissions:` bloğunu en dar haliyle tanımla (bu repodaki `deploy.yml` bunu yapıyor). Kural: bir kısıt altyapıda zorlanmıyorsa, o kısıt değil beklentidir.",
        "terms": [
            {
                "en": "capture-the-flag (CTF)",
                "tr": "capture-the-flag (CTF)",
                "definition": "Güvenlik becerisini ölçmek için kurulan, hedef sistemden “bayrak” bulmaya dayalı egzersiz."
            },
            {
                "en": "egress filtering",
                "tr": "egress filtering",
                "definition": "Bir sistemin dışarıya hangi adreslere bağlanabileceğini ağ seviyesinde kısıtlama."
            },
            {
                "en": "cyber range",
                "tr": "cyber range",
                "definition": "Saldırı ve savunmanın güvenle denendiği, simüle edilmiş ağ ortamı."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
