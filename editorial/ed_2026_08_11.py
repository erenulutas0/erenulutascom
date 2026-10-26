"""11 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-11"

INTRO = "Google'ın tıbbi AI sistemi AMIE artık video görüşmesi yapıyor. Tıbbı bir kenara koy: yazının mühendislik kısmı, konuşma hızıyla düşünme derinliğini aynı anda nasıl tutturduklarında yatıyor."

DRAFTS = [
    {
        "url": "https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/",
        "slot": "cover",
        "title_tr": "Konuşma hızında düşünmek: AMIE'nin eşzamansız multi-agent architecture",
        "difficulty": "orta",
        "tags": [
            "agent",
            "multimodal",
            "research",
            "real-time systems"
        ],
        "summary": "Google Research, tıbbi reasoning ve diyalog için geliştirdiği araştırma sistemi AMIE'nin **gerçek zamanlı video görüşmesi** yapan sürümünü (AMIE Video) tanıttı. Gemini ve Project Astra üzerine kurulu sistem, simüle edilmiş görüşmelerle yapılan rastgele kontrollü bir çalışmada uzman düzeyinde performans gösterdi.\n\nMotivasyon basit: metin tabanlı arayüz, muayenenin görsel ve işitsel boyutunu (yürüyüş, rahatsızlık işaretleri, nefes, muayene manevraları) çöpe atıyor. Hasta karmaşık fiziksel belirtileri yazıya dökmek zorunda kalıyor.\n\nMühendislik problemi ise iki çelişen talep: sistem hastaya **doğal konuşma hızında** cevap verirken aynı anda **dikkatli klinik reasoning** yapmalı. Çözüm, işi üç özelleşmiş agent arasında bölen **eşzamansız multi-agent architecture**; agent’lar sürekli ve paralel çalışıyor. Yani konuşan katman, düşünen katmanı beklemiyor.",
        "key_points": [
            "Hızlı yanıt ile derin reasoning aynı agent’ın işi olmaktan çıkarılıp ayrı agent’lara bölünüyor.",
            "Eşzamansız çalışma, konuşmanın akışını yavaş düşünce adımlarından yalıtıyor.",
            "Değerlendirme, rastgele atanmış simüle görüşmelerle yapılmış: kontrollü bir deney tasarımı."
        ],
        "why_it_matters": "Bu, 3 Ağustos'taki OpenAI ses sisteminin aynı dersi: gecikmeye duyarlı yolu ağır işten ayır. Gerçek zamanlı AI ürünlerinde mimari karar çoğu kez model seçiminden önce gelir.",
        "for_you": "Bir konuşma uygulamasında ‘anlık geri bildirim’ ile ‘derin değerlendirme’ farklı işler: ilkini hızlı ve kısa bir cevap olarak, ikincisini oturum bittikten sonra arka planda üretmek tam bu desen. İkisini aynı çağrıya sıkıştırırsan kullanıcı ya bekler ya da yüzeysel cevap alır.",
        "terms": [
            {
                "en": "multi-agent architecture",
                "tr": "multi-agent architecture",
                "definition": "İşi birden fazla özelleşmiş agent arasında bölüştüren sistem tasarımı."
            },
            {
                "en": "randomized controlled study",
                "tr": "randomized controlled study",
                "definition": "Katılımcıların koşullara rastgele atandığı, nedenselliği ölçebilen deney türü."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
