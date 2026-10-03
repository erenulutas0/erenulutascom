"""11 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-11"

INTRO = (
    "Google'ın tıbbi AI sistemi AMIE artık video görüşmesi yapıyor. Tıbbı bir kenara koy: "
    "yazının mühendislik kısmı, konuşma hızıyla düşünme derinliğini aynı anda nasıl "
    "tutturduklarında yatıyor."
)

DRAFTS = [
    {
        "url": "https://research.google/blog/advancing-amie-towards-expert-level-audio-visual-clinical-consultations/",
        "slot": "cover",
        "title_tr": "Konuşma hızında düşünmek: AMIE'nin eşzamansız çoklu ajan mimarisi",
        "difficulty": "orta",
        "tags": ["agent", "çok kipli", "araştırma", "gerçek zamanlı sistemler"],
        "summary": (
            "Google Research, tıbbi akıl yürütme ve diyalog için geliştirdiği araştırma sistemi AMIE'nin "
            "**gerçek zamanlı video görüşmesi** yapan sürümünü (AMIE Video) tanıttı. Gemini ve Project "
            "Astra üzerine kurulu sistem, simüle edilmiş görüşmelerle yapılan rastgele kontrollü bir "
            "çalışmada uzman düzeyinde performans gösterdi.\n\n"
            "Motivasyon basit: metin tabanlı arayüz, muayenenin görsel ve işitsel boyutunu (yürüyüş, "
            "rahatsızlık işaretleri, nefes, muayene manevraları) çöpe atıyor. Hasta karmaşık fiziksel "
            "belirtileri yazıya dökmek zorunda kalıyor.\n\n"
            "Mühendislik problemi ise iki çelişen talep: sistem hastaya **doğal konuşma hızında** cevap "
            "verirken aynı anda **dikkatli klinik akıl yürütme** yapmalı. Çözüm, işi üç özelleşmiş ajan "
            "arasında bölen **eşzamansız çoklu ajan mimarisi**; ajanlar sürekli ve paralel çalışıyor. "
            "Yani konuşan katman, düşünen katmanı beklemiyor."
        ),
        "key_points": [
            "Hızlı yanıt ile derin akıl yürütme aynı ajanın işi olmaktan çıkarılıp ayrı ajanlara bölünüyor.",
            "Eşzamansız çalışma, konuşmanın akışını yavaş düşünce adımlarından yalıtıyor.",
            "Değerlendirme, rastgele atanmış simüle görüşmelerle yapılmış: kontrollü bir deney tasarımı.",
        ],
        "why_it_matters": (
            "Bu, 3 Ağustos'taki OpenAI ses sisteminin aynı dersi: gecikmeye duyarlı yolu "
            "ağır işten ayır. Gerçek zamanlı AI ürünlerinde mimari karar çoğu kez model seçiminden önce gelir."
        ),
        "for_you": (
            "KlioAI'daki konuşma pratiği özelliğinde “anlık geri bildirim” ile “derin değerlendirme” "
            "farklı işler: ilkini hızlı ve kısa bir yanıt olarak, ikincisini oturum bittikten sonra "
            "arka planda üretmek tam bu desen. İkisini aynı çağrıya sıkıştırırsan kullanıcı ya bekler "
            "ya da yüzeysel cevap alır."
        ),
        "terms": [
            {"en": "multi-agent architecture", "tr": "çoklu ajan mimarisi", "definition": "İşi birden fazla özelleşmiş ajan arasında bölüştüren sistem tasarımı."},
            {"en": "randomized controlled study", "tr": "rastgele kontrollü çalışma", "definition": "Katılımcıların koşullara rastgele atandığı, nedenselliği ölçebilen deney türü."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
