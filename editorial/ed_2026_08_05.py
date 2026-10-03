"""5 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-05"

INTRO = (
    "Meta'nın reklam sıralama sisteminden tek bir fikir: ağır işi çevrimdışına, hafif işi "
    "çevrimiçine ayır. Bu cümle her ölçekte geçerli; Meta bunu milisaniye bütçeli bir "
    "sistemde nasıl uyguladığını anlatıyor."
)

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/08/05/ml-applications/from-user-sequences-to-scaling-laws-a-multi-stage-architecture-for-metas-ads-ranking/",
        "slot": "cover",
        "title_tr": "Kullanıcı dizilerinden ölçekleme yasalarına: ağır modelleme çevrimdışı, sıralama çevrimiçi",
        "difficulty": "ileri",
        "tags": ["öneri sistemleri", "mimari", "ML altyapısı", "gecikme"],
        "summary": (
            "Meta'nın öneri platformları her gün milyarlarca etkileşim işliyor. Reklam sıralamada "
            "binlerce reklamı milisaniyeler içinde getirip sıralamak gerekiyor. Bu bütçe yüzünden "
            "birçok yaklaşım **melez** bir yapı kullanıyor: dizi modelini ve sıralama modelini "
            "birbirine bağlayan hibrit bir düzen.\n\n"
            "Yazı bu düzenin üç bedelini sayıyor: bileşenler arası **kayıplı bilgi aktarımı**, hâlâ süren "
            "elle özellik mühendisliği ve sıralama ile dizi modeli birbirini kısıtladığı için "
            "**ölçekleme tavanı**. Çözüm iki parça: (1) ağır kullanıcı modellemesini hafif çevrimiçi "
            "sıralama işinden ayıran **çok aşamalı dizi modeli**, (2) özellik etkileşimlerini doğrudan "
            "veriden öğrenen **yoğun tokenizasyon ve hedef-farkında dikkat** tekniği.\n\n"
            "Meta, bu gelişmelerin toplamda Instagram'da %6, Facebook'ta %3 dönüşüm artışı ve "
            "Facebook'ta %3,5 tıklama artışı sağladığını söylüyor. Mimari, şirketin GEM adlı "
            "üretken reklam öneri modelinin çekirdek parçası."
        ),
        "key_points": [
            "Ağır modelleme (kullanıcı dizisi) çevrimdışı, hafif sıralama çevrimiçi: iki iş farklı gecikme bütçelerine sahip.",
            "Hibrit düzenin kayıplı aktarımı ve ölçekleme tavanı, çok aşamalı ayrımla aşılıyor.",
            "Hedef, LLM tarzı ve öngörülebilir ölçekleme yasaları olan bir üretim platformu.",
        ],
        "why_it_matters": (
            "“Pahalı hesabı istek anından çıkar” ilkesi, öneri sistemlerinde de arama sistemlerinde de "
            "temel bir mühendislik hamlesidir. Gecikme bütçesi dar ise model büyüklüğünü artırmanın yolu, "
            "büyük kısmı istek yolundan çıkarmaktır."
        ),
        "for_you": (
            "Mobit'teki doküman aramada aynı deseni zaten kullanıyorsun: belge embedding'lerini önceden "
            "hesaplayıp saklıyor, sorgu anında yalnızca sorguyu vektörleştiriyorsun. Bu yazı, o kararın "
            "büyük ölçekli hâli. KlioAI'da da kullanıcının öğrenme profilini her istekte modele "
            "yeniden hesaplatmak yerine arka planda güncellenen bir özet olarak tutabilirsin."
        ),
        "terms": [
            {"en": "sequence modeling", "tr": "dizi modelleme", "definition": "Kullanıcı eylemlerinin sırasını ve zamanlamasını girdi olarak kullanan modelleme yaklaşımı."},
            {"en": "scaling laws", "tr": "ölçekleme yasaları", "definition": "Model, veri ve hesap büyüdükçe kalitenin ne ölçüde arttığını öngören ampirik ilişkiler."},
            {"en": "target-aware attention", "tr": "hedef-farkında dikkat", "definition": "Dikkat ağırlıklarını değerlendirilen reklama (hedefe) göre hesaplayan mekanizma."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
