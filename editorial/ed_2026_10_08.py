"""8 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-08"

INTRO = "Uber’in hukuk ekibi için yazdığı sözleşme agent’ının hikâyesi dört yinelemeden oluşuyor ve en kalıcı ders modelle ilgili değil: aracı avukatın zaten çalıştığı yere koymak ve geri bildirimini sisteme geri beslemek. Yanında Postgres’e dair iki yazı var: toplu veri yüklemenin darboğazı ve her kodlama agent’ına ayrı bir veritabanı dalı."

DRAFTS = [
    {
        "url": "https://www.uber.com/blog/building-ubers-redlining-agent/",
        "slot": "cover",
        "title_tr": "RAG yetmedi, geri bildirim işe yaradı: Uber’in sözleşme agent’ı dört yinelemede nasıl olgunlaştı",
        "difficulty": "orta",
        "tags": [
            "agent",
            "RAG",
            "LLM",
            "product"
        ],
        "summary": "Uber’de her yıl binlerce sözleşme müzakere ediliyor. İş yüksek riskli ve ayrıntıcı, ama içinde şaşırtıcı ölçüde yapı var: benzer maddeler, müşteriler arasında tekrar eden düzeltmeler (redline) ve yerleşik reasoning kalıpları. **Legal Redlining Agent (LRA)**, avukatların zaten çalıştığı yere, Microsoft Word’e eklenti olarak yerleşiyor: karşı tarafın düzeltmelerini buluyor, niyeti yorumluyor, politikaya uygun kabul/ret/değiştir önerisi veriyor, gerekçeli yorum yazıyor ve riskli maddeleri işaretliyor. Uber’in bildirdiği sonuç: ortalama inceleme süresinde %20’den fazla azalma ve yapay zekâ kararlarında %91 doğruluk. Avukatın yargısının yerini almıyor.\n\n**1. yineleme, RAG.** Hukuk ekibinin el kitapları ve örnek müzakere turları içeri alındı. Üç sorun çıktı: **isabetsiz anlamsal benzerlik** (gömülen ‘anahtar’ ile getirilmek istenen içerik doğası gereği farklıydı), **uygunsuz ton** (aşırı savunmacı ya da aşırı olumlu cevaplar) ve **genelleyememe** (el kitabında olmayan durumlarda fiilen rastgele cevaplar).\n\n**2. yineleme, geri bildirim.** Başta yalnızca avukatın kararı, metin ve bir ‘beğenmedim’ işareti saklanıyordu. Dönüm noktası, avukatın **beklediği eylemi, yorumunu ve sonunda kullandığı metni** toplamak oldu: böylece karşı tarafın niyeti doğrudan avukatın kesin diline eşlendi. Çalışma anında agent binlerce geçmiş etkileşimi tutan bu depoyu sorguluyor: önce metadata filtreli benzerlik araması havuzu yaklaşık 20 belgeye indiriyor, sonra bir LLM adayların niyetle gerçekten örtüştüğünü doğruluyor. Bağlam kurulurken **exponential decay ağırlığı** son kararları öne alıyor (değişen hukuki tutuma uyum, kavram kaymasına karşı) ve kabul/ret örnekleri dengeli tutuluyor. Sonuç: model fine-tuning olmadan neredeyse gerçek zamanlı öğrenen, dinamik few-shot bir sistem. Öneriyi etkileyen geçmiş geri bildirimler arayüzde gösteriliyor; bu şeffaflık güveni kuran şey.\n\n**3. yineleme, ton.** Hattın sonuna yalnızca üslubu ayarlayan ek bir LLM çağrısı kondu. Asıl kırılma, tonu tanımlayan dilin sahipliğini avukatlara vermek oldu: mühendisler promptun iskeletini, hukuk ekibi içeriğini yönetti ve günler içinde kendi seslerine oturttular. Çıkan ilke: çıktı biçimini doğrudan etkileyen promptları alan uzmanları yazmalı, yapay zekâ ekibi yalnızca iyi uygulamaları gözetmeli.\n\n**4. yineleme, agent ile değişiklik.** Asıl zaman kazancı karşı teklifi yazmakta. Düz metin üretimi terim uyduruyor ya da sözleşmenin tanımlı terimlerinden sapıyordu; ‘değiştir’ kararında geçmiş geri bildirim ve kurallara başvuran bir agent workflow’a geçildi. Yazı, bu ilk neslin bugünkü agent altyapıları yaygınlaşmadan kurulduğunu da not ediyor.",
        "key_points": [
            "Aracı kullanıcının çalıştığı yere koymak (Word eklentisi) benimsenmenin ön koşulu.",
            "Sorgu ile getirilmek istenen içerik farklı türdeyse düz gömme benzerliği isabetsiz kalır.",
            "‘Beğenmedim’ zayıf sinyaldir; uzmanın düzelttiği son metin güçlü sinyaldir.",
            "Yeni örneklere daha çok ağırlık vermek, değişen politikaya fine-tuning uyum sağlar.",
            "Ton ve biçim promptlarını alan uzmanı yazsın; mühendis iskeleti yönetsin."
        ],
        "why_it_matters": "Çoğu RAG projesi 1. yinelemede takılır: belgeleri gömüp arar ve sonuçların neden tutarsız olduğunu anlamaz. Uber’in yolu, kaliteyi asıl yükselten şeyin daha iyi bir model değil, uzman düzeltmelerinden oluşan ve sürekli büyüyen bir örnek deposu olduğunu gösteriyor.",
        "for_you": "Bir sınıflandırma hattı için hazır bir tarif. Bir insanın düzelttiği her kaydı (girdi, modelin cevabı, doğru cevap, tarih) bir tabloda sakla. Yeni kayıt gelince bu tablodan en benzer birkaç düzeltmeyi getirip prompt’a few-shot örnek olarak koy ve yeni düzeltmelere daha yüksek ağırlık ver (örneğin `exp(-gün/30)`). Fine-tuning yok, GPU yok, ama sistem her düzeltmeyle iyileşir. İki ayrıntıyı atlama: örneklerde sınıfları dengeli tut ve arayüzde ‘bu kararı şu geçmiş örnekler etkiledi’ diye göster. Bir ders daha: doküman aramayı ayrı bir ekran yapmak yerine kullanıcının zaten çalıştığı ekranın içine yerleştir.",
        "terms": [
            {
                "en": "redline",
                "tr": "redline",
                "definition": "Bir sözleşme taslağında karşı tarafın önerdiği, izlenebilir biçimde işaretlenmiş değişiklik."
            },
            {
                "en": "few-shot prompting",
                "tr": "few-shot prompting",
                "definition": "Modele görevi, promptun içine konan birkaç çözümlü örnekle öğretme."
            },
            {
                "en": "concept drift",
                "tr": "concept drift",
                "definition": "Doğru cevabın zamanla değişmesi; eski örneklerin güncelliğini yitirmesi."
            },
            {
                "en": "exponential decay",
                "tr": "exponential decay",
                "definition": "Bir değerin ağırlığını yaşı arttıkça sabit oranla düşüren ağırlıklandırma."
            },
            {
                "en": "metadata filtering",
                "tr": "metadata filtering",
                "definition": "Benzerlik aramasını, kayıtların etiketlerine göre önce daraltma."
            }
        ]
    },
    {
        "url": "https://www.databricks.com/blog/load-terabytes-data-minutes-lakebase-postgres",
        "slot": "brief",
        "title_tr": "Postgres’e bulk load’da darboğaz okuma değil, tek yazıcı",
        "difficulty": "ileri",
        "tags": [
            "Postgres",
            "data engineering",
            "performance",
            "Lakebase"
        ],
        "summary": "Postgres gibi operasyonel veritabanları, verinin küçük alt kümeleri üzerinde çok sayıda eşzamanlı, düşük gecikmeli sorgu için tasarlandı. Terabaytlarca veri yüklemek ya da tabloyu baştan sona tarayan analitik sorgular aynı kaynaklar için uygulama trafiğiyle yarışıyor. Databricks’in anlattığı müşteri günde yaklaşık 1 milyar satır yüklüyordu: yükleme 8 saatten uzun sürüyor, CPU ve belleği tümüyle dolduruyordu.\n\nYazının net tespiti: yüklemeyi dağıtık bir Spark işi olarak başlatsan bile her satır yine **tek bir Postgres yazıcısından** (`COPY`) geçmek zorunda. Kaynak tarafı yatay ölçeklenir, hedef tarafı ölçeklenmez; yürütücü eklemek taramayı hızlandırır ama darboğazı kaldırmaz. Lakebase’in çözümü (LTAP adını verdikleri mimari), ağır toplu işi birincil sunucudan alıp Spark’a vermek: veri sayfaları dağıtık motorda oluşturuluyor. Yazı bir sınırı da açıkça belirtiyor: ölçülen şey veri yükleme süresi; indeks oluşturmayı paralelleştirme çalışması sürüyor.",
        "key_points": [
            "Bir hattın hızını en dar noktası belirler; okuyucuyu paralelleştirmek tek yazıcıyı hızlandırmaz.",
            "Toplu iş ve canlı trafik aynı kaynakları paylaşıyorsa biri diğerini bozar.",
            "Bir ölçümün neyi kapsamadığını söylemek (burada indeks kurulumu) ölçümün kendisi kadar değerli."
        ],
        "for_you": "Piyasa ya da log verisini Postgres’e yüklerken satır satır `INSERT` yerine `COPY` kullan; fark onlarca kat olabilir. Büyük yüklemede index’leri ve constraint’leri önce kaldırıp yükleme bitince yeniden kur. Ve ağır yüklemeyi canlı sorgularla aynı sunucuda, aynı saatte çalıştırma.",
        "terms": [
            {
                "en": "bulk load",
                "tr": "bulk load",
                "definition": "Çok büyük miktarda verinin veritabanına tek seferde aktarılması."
            },
            {
                "en": "OLTP",
                "tr": "OLTP",
                "definition": "Çok sayıda kısa, eşzamanlı okuma-yazma işlemine göre tasarlanmış veritabanı iş yükü."
            },
            {
                "en": "single-writer bottleneck",
                "tr": "single-writer bottleneck",
                "definition": "Tüm yazmaların tek bir süreçten geçmek zorunda olması yüzünden oluşan rate limit."
            }
        ]
    },
    {
        "url": "https://www.databricks.com/blog/lakebase-and-agentic-sdlc-branching-databases-coding-agents",
        "slot": "brief",
        "title_tr": "Her kodlama agent’ına kendi veritabanı dalı",
        "difficulty": "orta",
        "tags": [
            "agent",
            "Postgres",
            "developer experience",
            "CI/CD"
        ],
        "summary": "Kodlama agent’larını paralel çalıştırmak olağan hâle geliyor ve araçlar buna göre gelişti. Geliştirme akışının gözden kaçan parçası ise veritabanı. Her agent’ın kod yazması, şema değişikliği uygulaması ve test çalıştırması gerekiyor; paylaşılan tek bir geliştirme veritabanında agent’lar şema değişikliklerinde çakışıyor, birbirinin verisini bozuyor ya da gerçeği yansıtmayan mock’lara dönüyor.\n\nKod tarafında çözüm **git worktree**: her agent’a kendi dizini ve dalı. Lakebase aynı yalıtımı veritabanına getiriyor: **copy-on-write** ile bütün veritabanı, boyutundan bağımsız olarak bir saniyenin altında dallanıyor; dal üst dalın verisini paylaşıyor ve yalnızca ayrıştıkça ek depolama tüketiyor, boştayken sıfıra ölçekleniyor. Agent migration’ı uyguluyor, testleri koşuyor, PR açıyor ve dal kapatılıyor. Önemli bir fark: Git’in aksine veritabanı dalları birleştirilmiyor; şema değişikliği ana dala migration dosyalarıyla taşınıyor.",
        "key_points": [
            "Paralel çalışan agent’lar için kod yalıtımı yetmez; veritabanı da yalıtılmalı.",
            "Copy-on-write, tam kopya maliyeti olmadan gerçek veriyle test etmeyi mümkün kılar.",
            "Veritabanı dalı birleştirilmez; değişiklik migration dosyasıyla taşınır."
        ],
        "for_you": "Bunu bugün ücretsiz araçlarla kurabilirsin: her git worktree için ayrı bir Docker Postgres konteyneri (farklı port) aç ve Flyway/Liquibase migration’larını o veritabanına uygula. Testlerde Testcontainers zaten aynı yalıtımı sağlıyor. Asıl alışkanlık: şema değişikliğini asla elle yapma, her zaman sürümlü bir migration dosyasıyla yap.",
        "terms": [
            {
                "en": "copy-on-write",
                "tr": "copy-on-write",
                "definition": "Kopyanın veriyi paylaştığı, yalnızca değiştirilen kısmın ayrıca saklandığı yöntem."
            },
            {
                "en": "git worktree",
                "tr": "git worktree",
                "definition": "Aynı deponun farklı dallarını ayrı dizinlerde aynı anda açık tutma özelliği."
            },
            {
                "en": "schema migration",
                "tr": "schema migration",
                "definition": "Veritabanı yapısındaki değişikliğin sürümlü ve tekrarlanabilir bir dosyayla uygulanması."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
