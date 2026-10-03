"""27 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-27"

INTRO = (
    "Uber'den, bu arşivdeki en pratik maliyet yazısı: kodun %70'inden fazlasını agent'ların "
    "yazdığı bir şirkette AI harcaması nasıl kontrol altında tutuluyor? Cevap model seçmek değil, "
    "maliyeti ölçülebilir parçalara bölmek."
)

DRAFTS = [
    {
        "url": "https://www.uber.com/blog/efficient-software-factory/",
        "slot": "cover",
        "title_tr": "Yazılım fabrikasını verimli işletmek: AI maliyetini parçalara bölüp ölçmek",
        "difficulty": "orta",
        "tags": ["agent", "maliyet", "ölçüm", "LLM"],
        "summary": (
            "Uber'de AI araçları yazılım geliştirmenin her aşamasına girmiş durumda: **pull request'lerin "
            "%70'inden fazlası** yerel ya da bulut agent'lara atfediliyor. Mühendisler yazılım yaşam "
            "döngüsü boyunca 3.600'ü aşkın agent becerisi (skill) yazmış ve günde 30 binin üzerinde "
            "beceri çalıştırılıyor. Oturumların artan bir kısmını insan değil, kod incelemesi, CI "
            "hatalarını kendi kendine onarma, görsel doğrulamalı uçtan uca PR'lar, nöbet alarmlarının "
            "triyajı ve hata ayıklama yapan **otomatik yönetilen agent'lar** başlatıyor. Şubat'tan "
            "Ağustos'a kadar haftalık aktif kullanıcılar 7, haftalık agent istekleri 9,4 kat arttı; "
            "toplam AI harcaması ise nisandan beri görece sabitlendi.\n\n"
            "Bunu sağlayan şey maliyet denklemi: bir agent oturumunun maliyeti, ayrı ayrı ölçülüp "
            "optimize edilebilen terimlere ayrıştırılıyor. Kaldıraçlar da bu terimlere göre: "
            "**token fiyatı** için kıyaslama güdümlü, Pareto-optimal model seçimi ve model varsayılanları; "
            "**istek başına token** için 400K bağlam sınırı ve varsayılan orta akıl yürütme çabası, "
            "prompt önbellekleme, araç arama, CLI ile çözülen MCP çağrıları, araç çağrılarını "
            "toplu yapan “code mode” ve ağ geçidi üzerinden yönlendirilen SaaS MCP'leri.\n\n"
            "Ölçüm tarafı haftalık ve aylık izlenen metrik katmanlarından oluşuyor: portföy (para nereye "
            "gidiyor), araç başına birim ekonomisi (araç ucuzluyor mu yoksa kullanım mı kayıyor), model "
            "ekonomisi (hangi model sürümü faturayı gerçekten değiştirdi), **sürücü ayrıştırması** "
            "(sayının neden değiştiği, açıklanmamış kalıntı bırakmadan) ve yönetilen agent çıktıları "
            "(değer başına maliyet düşüyor mu, model geçişlerinde kalite korunuyor mu). Uber, spesifik "
            "kazançların kendi ortamına özgü olduğunu, ama gerçek iş üzerinde kıyaslama yapıp doğruluk ve "
            "maliyeti optimize etme yönteminin evrensel olduğunu vurguluyor."
        ),
        "key_points": [
            "Harcamayı kısmak için önce ölçmek gerekiyor: maliyet = fiyat × token × istek gibi bağımsız terimlere ayrılmış.",
            "Sürücü ayrıştırması: değişimi ardışık olarak açıklayıp artık bırakmamak, “neden pahalandı?” sorusunu kesin yanıtlar.",
            "Varsayılanlar büyük kaldıraç: 400K bağlam tavanı ve orta akıl yürütme çabası herkes için ayarlanmış başlangıç.",
            "Kıyaslamayı kendi gerçek işin üzerinde yap; kamuya açık benchmark senin iş yükün değil.",
            "Kullanımın 9 kat artması harcamanın artması anlamına gelmek zorunda değil.",
        ],
        "why_it_matters": (
            "AI kullanımı yaygınlaştıkça asıl mühendislik problemi “çalışıyor mu” sorusundan “neye ne "
            "kadar mal oluyor ve daha ucuz yolu var mı” sorusuna kayıyor. Bu yazı, o sorunun "
            "pratikte nasıl yönetildiğinin ender somut örneklerinden."
        ),
        "for_you": (
            "Bu gazetenin kendi pipeline'ında uygulayabilirsin: her LLM çağrısında `usage` alanındaki "
            "girdi, çıktı ve önbellek token'larını bir CSV'ye yaz; maliyeti `token × fiyat × çağrı` diye "
            "ayır. Bir ay sonra “Haiku'ya geçince fatura ne kadar değişti?” sorusunu tahminle değil "
            "veriyle cevaplarsın. KlioAI'da da aynısı: kullanıcı başına LLM maliyetini ölç, abonelik "
            "fiyatıyla yan yana koy. Ve Uber'in üç basit kaldıracını hemen dene: sistem promptunu "
            "önbelleğe al, bağlama gereksiz veri koyma, akıl yürütme çabasını varsayılan olarak "
            "orta tut."
        ),
        "terms": [
            {"en": "Pareto-optimal", "tr": "Pareto-optimal", "definition": "Bir ölçütü (örn. maliyet) iyileştirmek için diğerinden (örn. kalite) ödün vermek gerekmeyen en iyi seçenekler kümesi."},
            {"en": "agent skill", "tr": "agent becerisi", "definition": "Bir agent'ın belirli bir iş için yeniden kullanabildiği, adlandırılmış talimat ve araç paketi."},
            {"en": "prompt caching", "tr": "prompt önbellekleme", "definition": "Tekrar eden prompt önekini yeniden işlemek yerine önbellekten okuyarak maliyet ve süreyi düşürme."},
            {"en": "MCP (Model Context Protocol)", "tr": "model bağlam protokolü", "definition": "Modellerin dış araç ve veri kaynaklarına standart bir arayüzle bağlanmasını sağlayan protokol."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
