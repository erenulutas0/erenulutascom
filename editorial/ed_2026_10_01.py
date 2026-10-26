"""1 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-01"

INTRO = "Bir sınıflandırma kararı için bile büyük bir dil modelini çağırmak çoğu zaman gereğinden pahalı ve yavaş. Cloudflare’in açık kaynak ‘karar modelleri’ bu açığı hedefliyor. Yanında bir yedekleme sorusu: bozuk bir yazma fark edildiğinde veritabanını ne kadar hızlı geri alabilirsin?"

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/clef-decision-models/",
        "slot": "cover",
        "title_tr": "Karar vermek için sohbet modeli gerekmez: Cloudflare Clef",
        "difficulty": "orta",
        "tags": [
            "LLM",
            "classification",
            "open source",
            "performance"
        ],
        "summary": "Cloudflare, **Clef** adlı bir decision model (decision model) ailesini açık kaynak (Apache 2.0) olarak yayımladı. Decision model, serbest metin üretmek yerine önceden tanımlı seçenekler arasından seçim yapan bir model: örneğin bir isteğin etki şiddetini ‘etki yok / küçük / büyük / kritik’ olarak puanlamak ya da bir alan adını sınıflandırmak. Çıktı katı biçimde tiplenmiş (strictly typed) olduğundan sonucu ayrıştırmak için metin işlemek gerekmiyor.\n\nClef’in öne çıkan özellikleri: görselleri sınıflandırabilen bir **görü kodlayıcısı**, **64k context window** (Cloudflare’in önceki modeli Jev’de 32k) ve Jev ile API uyumluluğu. İki boyutu var: daha güçlü **Clef** ve gecikmeye duyarlı kararlar için **Clef-Flash**. Alan sınıflandırma örneğinde Clef 2,2 saniyede cevap veriyor; karşılaştırılan gpt-oss-120b 4,7 saniyede.\n\nHızın nedeni mimaride: Clef, Qwen tabanlı bir model üzerinde yalnızca **prefill** geçişi yapıyor ve geçerli şema seçeneklerini **paralel puanlıyor**. Karar adımı autoregressive olmadığından token token ara metin üretilmiyor. Cloudflare ayrıca bu modeller için fine-tuning (fine-tuning) hizmeti sunuyor: önce ileri konuşlandırılmış mühendis ekibiyle, ileride kendin kullanabileceğin bir platform olarak.",
        "key_points": [
            "Seçenekli karar problemi için serbest metin üretmek hem yavaş hem hata yapmaya açık.",
            "Typed output (şemaya uyan seçim) ayrıştırma hatalarını ortadan kaldırır.",
            "Prefill-only ve paralel puanlama: üretim yok, token token bekleme yok.",
            "Decision model ne kadar küçük ve hızlıysa, onu isteğin her adımında çağırmak o kadar mümkün olur."
        ],
        "why_it_matters": "LLM’leri her işte kullanma eğilimi maliyet ve gecikme biriktirir. Bu yazı, işin doğasına uygun daha dar bir araç seçmenin (sınıflandırma için decision model) hem hızı hem güvenilirliği artırdığını gösteriyor.",
        "for_you": "Bir LLM hattında bunu doğrudan düşünebilirsin: bir belgeyi ‘yakıt, elektrik, su’ gibi sabit kategorilere ayırmak serbest metin üretimi gerektirmez. Mevcut çağrıyı JSON şeması ve `enum` ile kısıtlayıp çıktıyı doğrula; ya da küçük, açık bir model denemesi yap ve doğruluk ile süreyi ölç. Sorgu türünü (arama mı, soru mu) belirleyen bir adım için de aynı yaklaşım geçerli.",
        "terms": [
            {
                "en": "decision model",
                "tr": "decision model",
                "definition": "Serbest metin üretmek yerine verilen seçenekler arasından seçim yapan model."
            },
            {
                "en": "prefill",
                "tr": "prefill",
                "definition": "Girdi token’larının modelden tek seferde geçirilip işlendiği aşama."
            },
            {
                "en": "autoregressive",
                "tr": "autoregressive",
                "definition": "Çıktıyı her adımda bir token olarak, önceki tokenlara bakarak üretme yöntemi."
            },
            {
                "en": "fine-tuning",
                "tr": "fine-tuning",
                "definition": "Hazır bir modeli kendi veriyle belirli bir göreve uyarlamak için ek eğitme."
            }
        ]
    },
    {
        "url": "https://www.databricks.com/blog/lakebase-postgres-branch-based-restores-fast-recovery-scale",
        "slot": "brief",
        "title_tr": "100 TB’lık veritabanını saniyeler içinde geri almak: dal tabanlı restore",
        "difficulty": "ileri",
        "tags": [
            "Postgres",
            "backup",
            "architecture",
            "database"
        ],
        "summary": "Geleneksel yönetilen Postgres’te point-in-time recovery (PITR) (PITR) üç adımdan oluşur: yeni bir örnek ayağa kaldırmak, snapshot’u (snapshot) nesne depolamadan diske çekmek ve WAL kayıtlarını hedef ana kadar yeniden oynatmak. Veritabanı büyüdükçe bunlar saatler sürer. Bir kopya (replica) donanım arızasında kurtarır, ama kötü bir yazma kopyaya da yansımışsa yalnızca geri yükleme çözer.\n\nLakebase hesaplamayı ve depolamayı ayırıyor; veritabanı geçmişi zaten nesne depolamada referans verilebilir durumda tutuluyor. Bu yüzden geri yükleme veri kopyalamıyor, **belirli bir timestamp’ta bir dal (branch) oluşturuyor**: bu bir metadata işlemi. Databricks, 100 TB’lık veritabanında bile süreyi saniyelere indirdiğini söylüyor.",
        "key_points": [
            "Kopya (replica) donanım arızasına karşı korur; hatalı yazmaya karşı korumaz.",
            "Hesaplama ve depolama ayrıldığında geri yükleme kopyalama işi olmaktan çıkar.",
            "Geçmişi nesne depolamada tutmak, geri dönüşü bir metadata işlemine çevirir."
        ],
        "for_you": "Kendi Postgres’inde bile PITR’ı bir kez dene: WAL arşivlemeyi aç, bir tabloyu kasten boz ve belirli bir ana geri dön. Geri yükleme süresini ölçmek, ‘yedeğim var’ ile ‘yedeğimden ne kadar sürede dönerim’ arasındaki farkı gösterir.",
        "terms": [
            {
                "en": "point-in-time recovery (PITR)",
                "tr": "point-in-time recovery (PITR)",
                "definition": "Veritabanını geçmişteki belirli bir ana döndürme."
            },
            {
                "en": "WAL (write-ahead log)",
                "tr": "WAL (write-ahead log)",
                "definition": "Değişikliklerin kalıcı hâle gelmeden önce sırayla yazıldığı kayıt; geri yüklemede yeniden oynatılır."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
