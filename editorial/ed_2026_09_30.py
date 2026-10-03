"""30 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-30"

INTRO = (
    "Yedekliliğin çalıştığını ancak kapatıp denediğinde bilirsin. AWS’nin yazısı, bir "
    "Availability Zone’u günlerce boşaltarak yapılan tatbikatların neleri ortaya çıkardığını "
    "anlatıyor. Yanında iki veritabanı haberi var: Spanner’ın her yerde çalışan sürümü ve "
    "Lakebase’de maliyet kontrolü."
)

DRAFTS = [
    {
        "url": "https://aws.amazon.com/blogs/architecture/running-multi-day-az-evacuation-drills-with-arc-zonal-shift/",
        "slot": "cover",
        "title_tr": "Bir Availability Zone’u günlerce boşaltmak: ARC Zonal Shift ile N-1 tatbikatı",
        "difficulty": "ileri",
        "tags": ["dayanıklılık", "AWS", "Kubernetes", "tatbikat"],
        "summary": (
            "‘Bir AZ düşerse ayakta kalırız’ cümlesi, bunu gerçekten denemedikçe bir varsayımdır. "
            "AWS’nin yazısı, bir Availability Zone’u **48-72 saat boyunca** trafikten çıkarıp "
            "sistemi **N-1** kapasiteyle (bir zone eksik) çalıştıran tatbikatları anlatıyor. "
            "Kısa bir tatbikat anlık sorunları yakalar; günlerce süren tatbikat ise zamanla ortaya "
            "çıkan sorunları yakalar.\n\n"
            "Tatbikatların açığa çıkardığı hata türleri öğretici: **otomatik ölçekleme** (kapasite "
            "kalan zone’larda yeterince hızlı büyüyor mu), **eski DNS kayıtları** (istemciler "
            "boşaltılmış zone’a hâlâ gidiyor mu), **nöbet ve rotasyon süreçleri** (insanlar ve "
            "runbook’lar çok günlük bir durumu kaldırıyor mu) ve **sabitlenmiş veritabanı "
            "bağlantıları** (bağlantılar eski zone’daki örneğe yapışık kalıyor).\n\n"
            "Mekanizma tarafında ARC Zonal Shift, Kubernetes (EKS) üzerinde ilgili zone’daki "
            "düğümleri yeni pod’lara kapatıyor (cordon) ve o zone’daki uç noktaları "
            "EndpointSlice’tan çıkarıyor; böylece trafik kalan zone’lara akıyor."
        ),
        "key_points": [
            "Yedekliliği test etmeyen sistem, yedekliliği olduğunu varsayan sistemdir.",
            "Günlerce süren tatbikat, saatlik tatbikatın göremediği zamanla biriken sorunları gösterir.",
            "Sorunların çoğu kodda değil çevrede: DNS, bağlantı havuzu, ölçekleme ve insan süreçleri.",
            "N-1 kapasite planı, kalan zone’ların tüm yükü kaldırabildiğini ölçmeden anlamsızdır.",
        ],
        "why_it_matters": (
            "Çok-AZ mimari çizmek kolay, çalıştığını kanıtlamak zor. Tatbikat, ‘olursa ne "
            "olur’ sorusunu planlı bir deneye çevirir ve gerçek kesintiden önce hataları ucuza bulur."
        ),
        "for_you": (
            "Bu desenin küçük ölçekli hâli bugün senin elinde: Tradebot ya da Mobit’i docker-compose "
            "ile çalıştırıyorsan, veritabanı konteynerini bilerek durdur ve uygulamanın ne kadar "
            "sürede toparlandığına bak. Bağlantı havuzun (HikariCP) ölü bağlantıyı tespit edip "
            "yeniden bağlanıyor mu? `maxLifetime` ve `connectionTimeout` ayarlarının anlamı tam "
            "burada ortaya çıkar. Sonucu bir `RESILIENCE.md` dosyasına ‘ne denedim, ne bozuldu, "
            "ne düzelttim’ diye yaz: mülakatta ‘dayanıklılığı test ettim’ diyebilmenin somut kanıtı."
        ),
        "terms": [
            {"en": "Availability Zone (AZ)", "tr": "erişilebilirlik bölgesi", "definition": "Bir bulut bölgesi içinde fiziksel olarak ayrı, bağımsız arızalanabilen veri merkezi grubu."},
            {"en": "zonal shift", "tr": "zone kaydırma", "definition": "Trafiği sorunlu ya da boşaltılan bir zone’dan diğer zone’lara yönlendirme."},
            {"en": "N-1", "tr": "N-1 kapasite", "definition": "Bir bileşen (örneğin bir zone) kaybedilse bile yükü taşıyabilecek kapasite planı."},
            {"en": "cordon", "tr": "düğümü kapatma", "definition": "Kubernetes’te bir düğüme yeni pod atanmasını engelleme."},
        ],
    },
    {
        "url": "https://cloud.google.com/blog/products/databases/spanner-omni-deploy-anywhere-version-of-spanner-is-now-ga/",
        "slot": "brief",
        "title_tr": "Spanner artık her yerde: Spanner Omni genel kullanıma açıldı",
        "difficulty": "orta",
        "tags": ["veritabanı", "Spanner", "dağıtık sistemler"],
        "summary": (
            "Google, Spanner’ın **istediğin yere kurulabilen** sürümü Spanner Omni’yi genel kullanıma "
            "açtı. Yazıya göre ürün yaklaşık 2 milyon kez indirilmiş; mimaride iş yapan **worker "
            "düğümleri** var ve denemek için ücretsiz bir geliştirici sürümü sunuluyor. Böylece "
            "Spanner’ın dağıtık, güçlü tutarlı veritabanı modelini yalnızca Google Cloud’da değil, "
            "kendi ortamında da denemek mümkün."
        ),
        "key_points": [
            "Yönetilen bir bulut veritabanı, kendi ortamında çalışacak biçimde paketlenebiliyor.",
            "Ücretsiz geliştirici sürümü, dağıtık SQL’i öğrenmek için düşük giriş bariyeri.",
        ],
        "for_you": (
            "Dağıtık veritabanı kavramlarını (güçlü tutarlılık, dağıtık işlem) öğrenmek için ücretsiz "
            "geliştirici sürümünü yerel makinede dene; bu gazetenin 2 Ekim sayısındaki Spanner "
            "queues yazısını da aynı ortamda deneyebilirsin."
        ),
        "terms": [
            {"en": "strong consistency", "tr": "güçlü tutarlılık", "definition": "Her okumanın en son yazılan değeri görmesini garanti eden tutarlılık modeli."},
        ],
    },
    {
        "url": "https://www.databricks.com/blog/practical-guide-cost-optimization-lakebase-postgres",
        "slot": "brief",
        "title_tr": "Postgres’te maliyeti düşüren üç ayar: paylaşımlı dallar, otomatik ölçekleme, sıfıra inme",
        "difficulty": "orta",
        "tags": ["Postgres", "maliyet", "Lakebase"],
        "summary": (
            "Databricks’in Lakebase rehberi maliyeti üç yerden kısmayı öneriyor. **Dallar (branch) "
            "depolamayı paylaşıyor**, yani bir geliştirme ya da test kopyası verinin tamamını "
            "ikinci kez saklamıyor. **Otomatik ölçekleme** ve **sıfıra inme (scale to zero)** boşta "
            "kalan hesaplama maliyetini azaltıyor. Veri senkronizasyonunda da üç mod var: "
            "**snapshot**, **triggered** ve **continuous**; ne kadar taze veri gerektiğine göre "
            "seçilince gereksiz sürekli senkronizasyon maliyeti önleniyor."
        ),
        "key_points": [
            "Dal depolamayı paylaşıyorsa test ortamı kopya maliyeti getirmez.",
            "Boşta kalan veritabanını kapatmak, en ucuz optimizasyondur.",
            "Senkronizasyon modunu tazelik ihtiyacına göre seç: her veri sürekli akmak zorunda değil.",
        ],
        "for_you": (
            "Aynı mantık kendi geliştirme ortamında da geçerli: Mobit için yalnızca ihtiyaç anında "
            "açılan bir test veritabanı kullan. Neon gibi dal destekli bir Postgres sağlayıcısı "
            "ile ücretsiz katmanda ‘her pull request için bir veritabanı dalı’ deseni denenebilir."
        ),
        "terms": [
            {"en": "scale to zero", "tr": "sıfıra ölçekleme", "definition": "Kullanılmayan hesaplama kaynağını tamamen kapatıp istek gelince yeniden açma."},
            {"en": "database branching", "tr": "veritabanı dallandırma", "definition": "Bir veritabanının kopyasını veriyi çoğaltmadan, sadece değişenleri saklayarak oluşturma."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
