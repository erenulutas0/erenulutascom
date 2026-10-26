"""28 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-28"

INTRO = "Netflix'ten cold-start (soğuk başlangıç) probleminin temiz bir çözümü: bir içeriğin görseline ID olarak değil, gerçekte ne gösterdiğine göre bak. Bu fikir kitap, ürün, belge, hangi alanda öneri yapıyorsan işe yarıyor."

DRAFTS = [
    {
        "url": "https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e?source=rss----2615bd06b42e---4",
        "slot": "cover",
        "title_tr": "Modele resmi göstermek: embedding ile cold-start'ı kısaltmak ve beş modeli bire indirmek",
        "difficulty": "ileri",
        "tags": [
            "embedding",
            "recommender systems",
            "cold-start",
            "personalization"
        ],
        "summary": "Netflix'te bir başlığın görseli ve otomatik oynayan önizlemesi (yazıda “asset”) başlı başına bir kişiselleştirme problemi: Squid Game için hangi görseli göstermelisin? Daha da zor soru bir başlık yayımlandığı anda, üzerinde neredeyse hiç etkileşim verisi yokken ne yapacağın.\n\nYıllarca modeller ilk soruyu iyi, ikincisini kötü cevapladı. Çünkü her asset'i **opak bir ID** olarak ele alıyorlardı: görselin içinde ne olduğunu bilmeden yalnızca hangisine tıklandığını öğreniyorlardı. Yeni yayınlanan başlığın asset'leri geçmişsiz olduğu için keşfi artırıp popülerlik sezgisellerine düşüyorlardı. Bu klasik **cold-start** problemi.\n\nÇözüm: modele görseli “göstermek”. Her görseli önceden eğitilmiş bir görsel-metin embedding modeli olan **CLIP** ile kodlayıp, asset temsiline ekliyorlar. Böylece yeni bir görsel, oluşturulduğu anda modelin zaten anladığı bir embedding ile geliyor; benzer görsellerden gelen zevk sinyalini hemen taşıyor ve model kişiselleştirmeye başlamak için çok daha az etkileşim geçmişine ihtiyaç duyuyor.\n\nİkinci kazanım **model konsolidasyonu**: bir başlığın görselleri farklı kanvaslarda (farklı kırpmalar) yer alıyor ve bu yüzden beş ayrı model çalışıyordu. CLIP embedding'leri kırpma, yeniden boyutlandırma ve en-boy oranına büyük ölçüde duyarsız olduğu için neredeyse aynı görseller neredeyse aynı vektöre düşüyor; tek bir birleşik model yeterli oluyor. Yazı üç üretim sistemini kapsıyor: görsel kişiselleştirme, sorguya duyarlı görsel sıralama ve video önizleme kişiselleştirme. Bir de pratik hile: yeni embedding'leri uçtan uca entegrasyon ve A/B testine girişmeden önce ucuz bir yolla seçmek.",
        "key_points": [
            "ID olarak temsil edilen varlık, yeni geldiğinde sıfırdan öğrenilmek zorunda; içerik embedding'i ise anında bilgi taşır.",
            "Önceden eğitilmiş embedding'i mevcut modele eklemek, sıfırdan bir model eğitmekten çok daha ucuz bir cold-start çözümü.",
            "Girdideki gereksiz varyasyona (kırpma, boyut) duyarsız temsil, birden çok modeli tek modele indirmeyi sağlıyor.",
            "Bir embedding'i tam entegrasyondan önce ucuz bir testle elemek, A/B testi bütçesini koruyor."
        ],
        "why_it_matters": "Cold-start, öneri sistemlerinin en yaygın acısıdır: yeni kullanıcı, yeni ürün, yeni belge. Çözümün ortak fikri, varlığı yalnızca geçmişte ne yaptığıyla değil **kendi içeriğiyle** tanımlamak.",
        "for_you": "Doküman arama için bu doğrudan işe yarar. Yeni yüklenen bir belge için henüz kimse arama yapmadı, tıklama verisi yok; ama belgenin içeriğinden üretilmiş embedding ilk günden aranabilir kılıyor, tam olarak Netflix’in yaptığı gibi. Bunu pgvector ile PostgreSQL’de yapabilirsin. Ayrıca ‘ID yerine içerik’ fikrini kullan: bir öğeyi yalnızca kimlik numarasıyla değil, konusunun embedding’iyle tanımla; yeni eklenen öğeler ilk günden benzerlerinin başarı verisinden yararlanır (cold-start çözümü).",
        "terms": [
            {
                "en": "cold-start",
                "tr": "cold-start",
                "definition": "Yeni bir kullanıcı ya da öğe için henüz etkileşim verisi olmadığından öneri yapılamama durumu."
            },
            {
                "en": "CLIP",
                "tr": "CLIP",
                "definition": "Görselleri ve metinleri aynı vektör uzayına gömen, önceden eğitilmiş multimodal model."
            },
            {
                "en": "model consolidation",
                "tr": "model consolidation",
                "definition": "Birbirine benzer işleri yapan birden çok modeli tek bir modele indirme."
            },
            {
                "en": "opaque ID",
                "tr": "opaque ID",
                "definition": "İçeriği hakkında hiçbir bilgi taşımayan, yalnızca ayırt etmeye yarayan tanımlayıcı."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
