"""31 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-31"

INTRO = "Ayın son günü, tek yazı: Google'ın zaman serisi foundation model’i TimesFM'in üçüncü sürümü artık çok değişkenli. Zaman serisiyle çalışan herkes için, özellikle de piyasa verisiyle, “eğitmeden tahmin et” fikrinin ne vaat ettiğine bakmaya değer."

DRAFTS = [
    {
        "url": "https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/",
        "slot": "cover",
        "title_tr": "Eğitmeden tahmin: çok değişkenli zaman serileri için TimesFM-3",
        "difficulty": "ileri",
        "tags": [
            "zaman serisi",
            "temel model",
            "tahmin",
            "research"
        ],
        "summary": "2024'te çıkan TimesFM'den bu yana zaman serisi foundation model’leri perakende, finans, observability, üretim ve sağlık gibi alanlarda gerçek tahmin görevlerinde kullanılıyor. TimesFM-2.5'e kadar (Eylül 2025) modeller yalnızca **tek değişkenliydi**: tek bir serinin geçmişine bakarak tahmin ediyordu. Oysa gerçek problemlerin çoğu çok değişkenli: dondurma satışını tahmin ederken yalnızca geçmiş satışlar yetmez; ilişkili ürünlerin satışı, mağaza trafiği, hava tahmini, promosyonlar ve tatiller de gerekir.\n\n**TimesFM-3**, 330 milyon parametreli ve 1 trilyondan fazla zaman noktası içeren gerçek ve sentetik bir külliyatla önceden eğitilmiş. Görev özel fine-tuning gerektirmeden (**sıfır atış**, zero-shot) birlikte evrilen birden çok seriyi bir arada tahmin edip aralarındaki bağımlılıkları yakalıyor. Mimari, öncüllerinin yalnızca-kod-çözücü transformer'ı: ardışık 32 zaman adımı bir yama (patch) olarak gruplanıyor. Geçmiş-gelecek ortak değişkenler için “ileri bakış” stratejisi var: her token mevcut yamayı gelecek yamalarla birleştiriyor. Transformer yığını 2B bir ızgara olarak çalışıyor ve **zamansal dikkat** ile **seriler arası dikkat** katmanlar boyunca dönüşümlü uygulanıyor.\n\nBir diğer iyileştirme gecikme: önceki sürümler tahmini yama yama üretirken hata birikiyordu. TimesFM-3 **Contiguous Patch Masking** ile tüm tahmin ufkunu tek ileri geçişte üretiyor. Gift-Eval, FEV-Bench ve Time kıyaslamalarının üçünde de hem nokta hem olasılıksal tahmin metriklerinde en üst sırada.",
        "key_points": [
            "Tek değişkenliden çok değişkenliye geçiş: ilişkili serileri ve bilinen gelecek olaylarını modele katmak.",
            "Sıfır atış: her yeni veri kümesi için eğitim yok; model olduğu gibi çalıştırılıyor.",
            "Yama tabanlı tokenizasyon, uzun serileri verimli işlemenin yolu (32 adım = 1 token).",
            "Tüm ufku tek geçişte üretmek, sıralı üretimdeki hata birikimini ve gecikmeyi ortadan kaldırıyor."
        ],
        "why_it_matters": "Zaman serisi tahmininde yıllarca her veri kümesi için ayrı model eğitmek norm oldu. Foundation model’ler bunu “önce hazır modeli dene” noktasına çekiyor: eğitim maliyeti olmadan makul bir baseline veriyor.",
        "for_you": "Finansal verilerde bunu **baseline** olarak kullanabilirsin, strateji olarak değil. Getiri serilerinde signal-to-noise oranı çok düşüktür ve bir foundation model’in kıyaslamalardaki başarısı piyasada kâr anlamına gelmez; önce modelin tahminini ‘yarınki değer bugünküyle aynı’ gibi saf bir yöntemle (naive baseline) karşılaştır ve walk-forward doğrulamadan geçir. Daha güvenli kullanım alanı operasyonel veri: sistem metriklerinde, API gecikmelerinde ya da kullanım sayılarında ileriye dönük kapasite tahmini. Orada kazandırdığı şey eğitim zahmetinin ortadan kalkması.",
        "terms": [
            {
                "en": "zero-shot forecasting",
                "tr": "zero-shot forecasting",
                "definition": "Modeli yeni veri kümesinde ayrıca eğitmeden doğrudan tahmin yaptırma."
            },
            {
                "en": "multivariate time series",
                "tr": "multivariate time series",
                "definition": "Birbirini etkileyen birden fazla serinin birlikte ele alındığı zaman serisi."
            },
            {
                "en": "covariate",
                "tr": "covariate",
                "definition": "Hedef seriyi etkileyen ama kendisi tahmin edilmeyen dış değişken (hava durumu, promosyon gibi)."
            },
            {
                "en": "naive baseline",
                "tr": "naive baseline",
                "definition": "Karmaşık bir modelin değerini ölçmek için kullanılan en basit yöntem (örn. son değeri tekrar etmek)."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
