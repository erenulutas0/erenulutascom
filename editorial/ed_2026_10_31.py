"""31 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-31"

INTRO = (
    "Gerçek veriyle test etmek herkesin istediği şey ama production veritabanının kopyasını her "
    "pull request için almak 20 dakika sürüyorsa kimse yapmaz. Haftanın son yazısı, "
    "veritabanını Git branch’i gibi dallandırarak bu süreyi nasıl kısalttıklarını anlatıyor."
)

DRAFTS = [
    {
        "url": "https://www.databricks.com/blog/lakebase-branching-cicd-lessons-100-pr-databases",
        "slot": "cover",
        "title_tr": "Her pull request için production kopyası: Lakebase branching ile CI/CD (Snorkel AI)",
        "difficulty": "orta",
        "tags": ["CI/CD", "database", "testing", "Postgres"],
        "summary": (
            "Snorkel AI kodu Kubernetes üzerine kurulu bir CI pipeline’ıyla yayınlıyor: her açık "
            "pull request ve bazı ad-hoc commit’ler kendi geçici Kubernetes namespace’ini "
            "(‘PR namespace’) alıyor; geliştirici branch’ini orada deploy edip birleştirmeden "
            "önce tüm test paketini çalıştırıyor. Testler en çok gerçek veriyle işe yarıyor. "
            "Production veritabanları Amazon Aurora PostgreSQL ve her PR namespace’ine ayrı bir "
            "kopya vermek zor kısımdı: bir kopyayı geri yüklemek ortamlar başına yaklaşık "
            "**20 dakika** sürüyordu; geliştiriciler gün boyu PR açarken ve merge queue her "
            "koşu için taze bir ortam isterken bu çok yavaş. Alternatifler (paylaşımlı staging "
            "veritabanı, kısaltılmış fixture ya da sentetik veri) gerçek veriyle test etmenin "
            "çözmeye çalıştığı sorunları geri getiriyor: testlerin birbirini bozması, eski "
            "şemalar ve yalnızca gerçek veri şekillerinde çıkan bug’lar.\n\n"
            "**Lakebase branching.** Lakebase, Databricks’in sunucusuz Postgres veritabanı; "
            "depolama ve hesaplama ayrı ve **veritabanını Git branch’i gibi dallandırmayı** "
            "destekliyor: herhangi bir zaman noktasından yeni, yalıtılmış, yazılabilir bir "
            "branch oluşturabilirsin. Branch’ler **copy-on-write**: oluşturmak bir metadata "
            "işlemi, veri kopyalanmıyor; yeni branch ana dalla aynı depolama sayfalarını "
            "paylaşıyor ve yalnızca değiştirdiği sayfalar yeni depolama olarak yazılıyor. "
            "Pratikte iki özellik deseni mümkün kılıyor: copy-on-write branching ve **branch "
            "expiration (TTL)**.\n\n"
            "**Akış dört adım.** **(1)** Ana dalda production’ın taze bir kopyasını tut: "
            "Lakebase standart Postgres olduğundan AWS DMS için hedef olabiliyor, özel araç "
            "gerekmiyor; Snorkel bir DMS görevini production Aurora’ya yöneltip Lakebase "
            "projesinin main branch’ine kopyalıyor. **(2)** PR açıldığında CI pipeline’ı "
            "Lakebase API’sini çağırıp main’den bir branch oluşturuyor, bir sona erme zamanı "
            "koyuyor ve bağlantı bilgilerini PR namespace’ine veriyor. **(3)** PR "
            "namespace’indeki uygulama branch’ine standart Postgres olarak bağlanıyor; testler "
            "migration çalıştırabilir, veri yazabilir ve şemayı değiştirebilir, production’ı, "
            "main’i ya da diğer PR’ları etkilemeden. **(4)** PR kapanınca ya da test geçince "
            "branch siliniyor; temizleme adımı çalışmazsa TTL son çare olarak branch’i kendisi "
            "düşürüyor.\n\n"
            "**İki güvenlik gereksinimi.** *Private connectivity:* production verisi Aurora’dan "
            "Lakebase’e ve Lakebase’den CI kümesine halka açık internet yerine özel ağ üzerinden "
            "akıyor. *Identity:* Snorkel’in iki tür veritabanı kullanıcısı var, PR ortamında hata "
            "ayıklamak için etkileşimli bağlanan geliştiriciler ve hiçbir insan olmadan "
            "çalışan CI pipeline’ları. Okta SSO tarayıcı tabanlı etkileşimli girişe göre "
            "kurulu olduğundan tasarım kullanıcı türüne göre ikiye bölünmüş."
        ),
        "key_points": [
            "Gerçek veriyle test etmek, paylaşımlı staging’in sorunlarını (testlerin birbirini bozması, eski şema) ortadan kaldırır.",
            "Copy-on-write branching, tam kopya almadan veritabanı ortamı oluşturmayı saniyelere indirir.",
            "Her geçici kaynağa bir TTL koy: temizleme adımı bir gün çalışmayacak.",
            "İnsan ve otomatik kullanıcılar için ayrı kimlik doğrulama yolları tasarla.",
        ],
        "why_it_matters": (
            "Test verisi sorunu çoğu ekipte ‘staging bir yerde’ diye çözülmüş görünür ama "
            "gerçek bug’lar gerçek veri şeklinde çıkar. Bu yazı, veritabanı ortamını bir "
            "pull request kadar ucuz ve geçici yapmanın CI’a ne kazandırdığını anlatıyor."
        ),
        "for_you": (
            "Bugün ücretsiz araçlarla basit bir sürümünü kurabilirsin. **(1)** CI’da her PR için "
            "Docker ile temiz bir Postgres container’ı aç (Testcontainers bunu tek satırda "
            "yapar) ve migration’ları sıfırdan uygula. **(2)** Gerçek şekilli veriye ihtiyaç "
            "varsa production’ın küçük, anonimleştirilmiş bir dump’ını bir kez al ve container "
            "imajına göm; test başında `pg_restore` ile yükle. **(3)** Neon gibi branching "
            "destekleyen bir Postgres sağlayıcısında her PR için bir database branch "
            "açıp PR kapanınca silmeyi dene. Hangi yolu seçersen seç, geçici ortama bir "
            "ömür (TTL) ver."
        ),
        "terms": [
            {"en": "copy-on-write", "tr": "copy-on-write", "definition": "Kopyanın veriyi paylaştığı, yalnızca değiştirilen kısmın ayrıca saklandığı yöntem."},
            {"en": "ephemeral environment", "tr": "ephemeral environment", "definition": "Bir iş için açılıp iş bitince silinen geçici ortam."},
            {"en": "TTL (time to live)", "tr": "TTL (time to live)", "definition": "Bir kaynağın kendiliğinden silineceği süre."},
            {"en": "merge queue", "tr": "merge queue", "definition": "Birleştirilecek değişiklikleri sırayla, her birini güncel ana dalla test ederek birleştiren kuyruk."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
