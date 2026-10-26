"""29 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-29"

INTRO = "Günün en iyi yazısı OpenAI'dan geliyor ve konusu model değil: bir benchmark puanının aslında modeli değil onu çalıştıran *harness*'ı ölçtüğünü gösteriyorlar. İki API ayarı açınca puan üçe katlanmış. Bunu okuduktan sonra hiçbir benchmark tablosuna aynı gözle bakmayacaksın."

DRAFTS = [
    {
        "url": "https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores",
        "slot": "cover",
        "title_tr": "İki ayar puanı üçe katladı: benchmark modeli mi harness'ı mı ölçüyor?",
        "difficulty": "orta",
        "tags": [
            "evaluation",
            "LLM",
            "agent",
            "context management"
        ],
        "summary": "OpenAI kendi modelinin bir benchmark'taki düşük puanına şaşırmış. GPT-5.6 Sol matematikte açık problemler çözüyor, Pokémon FireRed'i bitiriyor — ama 2B bulmaca oyunlarından oluşan ARC-AGI-3'te sadece %7,8 alıyor. Soru şu: 2B bulmacalar modeller için gerçekten mi bu kadar zor, yoksa başka bir şey mi oluyor?\n\nCevap ikincisi. Yazının kilit cümlesi şu: **benchmark'lar modelleri yalıtılmış hâlde ölçmez.** Aynı zamanda daha az görünür tercihleri de ölçerler — API ayarları, harness tasarımı ve prompt'lama. ARC-AGI-3 kasıtlı olarak jenerik bir harness kullanıyor: araç yok, özel özellik yok. Gerekçesi savunulabilir — basit harness modelin eksiklerini daha görünür kılar ve karşılaştırmayı adil tutar. Ama ticari geliştiriciler harness'ı optimize eder, dolayısıyla ölçülen şey iki dünyada aynı değildir.\n\nOpenAI, ChatGPT ve Codex'te zaten kullandıkları iki API ayarını açmış: **retained reasoning** (reasoning’in turlar arası korunması) ve **compaction** (bağlam dolduğunda geçmişin özetlenmesi). Sonuç: puan üçe katlanmış ve çıktı token'ları 6 kat azalmış. Yani hem daha iyi hem daha ucuz.",
        "key_points": [
            "Aynı model, aynı görev, farklı harness → 3 kat fark. Puan farkının kaynağı modelde değildi.",
            "Retained reasoning: modelin bir turdaki reasoning’ini sonraki turda kaybetmemesi. Agentic döngülerde tekrar tekrar aynı şeyi düşünmesini önler.",
            "Compaction: bağlam sınırına yaklaşırken geçmişi özetleyip yer açma. Uzun süren agent oturumlarında zorunlu hâle geliyor.",
            "İyileşme token maliyetiyle gelmedi — tersine 6 kat daha az çıktı token'ı kullanıldı."
        ],
        "why_it_matters": "Model karşılaştırma tablolarını okurken bu yazıyı hatırla. Bir puan her zaman \"model + harness + prompt + ayarlar\" bileşiminin puanıdır. Kendi ürününde bir modeli değerlendirirken de aynısı geçerli: iki modeli farklı harness'larla karşılaştırırsan ölçtüğün şey model değil, senin kurulumundur.",
        "for_you": "Bu yazı en somut faydalanabileceğin şeylerden biri. Bir LLM özelliği yazarken ‘model kötü’ sonucuna varmadan önce şunları kontrol et: context yönetimi doğru mu, önceki turların reasoning’i korunuyor mu, prompt yapısı görevi net anlatıyor mu, tool açıklamaları modele *ne zaman* çağıracağını söylüyor mu? Beklenenden kötü sonuç alıyorsan ilk şüphelin model değil harness olsun. Ayrıca kendi evaluation setini kur: 20-30 gerçek örnek üzerinde kendi ölçümünü yapmak, dışarıdaki hiçbir benchmark tablosundan alamayacağın bir bilgidir.",
        "terms": [
            {
                "en": "harness",
                "tr": "harness",
                "definition": "Modeli çalıştıran çerçeve: prompt yapısı, araçlar, bağlam yönetimi, döngü mantığı. Modelin kendisi kadar sonucu belirler."
            },
            {
                "en": "retained reasoning",
                "tr": "retained reasoning",
                "definition": "Modelin bir turda ürettiği düşünme adımlarının sonraki turlarda da bağlamda kalması."
            },
            {
                "en": "compaction",
                "tr": "compaction",
                "definition": "Konuşma geçmişi context window’u doldurmaya yaklaşınca eski kısmın özetlenerek yer açılması."
            },
            {
                "en": "benchmark",
                "tr": "benchmark",
                "definition": "Modelleri standart bir görev kümesinde ölçen test; sonucu kurulum tercihlerinden bağımsız değildir."
            }
        ]
    },
    {
        "url": "https://blog.cloudflare.com/post-quantum-authentication-to-origins/",
        "slot": "brief",
        "title_tr": "Kuantum sonrası kimlik doğrulama: neden şifrelemeden sonra sıra buna geldi",
        "difficulty": "ileri",
        "tags": [
            "security",
            "cryptography",
            "TLS",
            "networking"
        ],
        "summary": "Cloudflare'in kuantum sonrası (post-quantum) geçiş yol haritasında önemli bir eşik: origin sunucularına yapılan kimlik doğrulama artık kuantum sonrası algoritmalarla korunuyor.\n\nYazının en öğretici kısmı **neden şimdi** sorusunun cevabı. Son yıllarda odak şifrelemedeydi ve gerekçesi \"harvest now, decrypt later\" (harvest-now/decrypt-later) saldırısıydı: saldırgan şifreli veriyi sessizce biriktirir, gelecekte kuantum bilgisayarla çözmeyi umar. Kimlik doğrulamada ise böyle bir gecikme yok — bir imzayı kırmak ancak canlıyken işe yarar. Ama kuantum hesaplama ve kriptanalizdeki son gelişmeler takvimleri öne çektiği için, artık klasik kimlik bilgilerini kırıp **kimliğe bürünme** (impersonation) saldırısı yapabilecek saldırganlara karşı da hazırlık başladı.",
        "key_points": [
            "Cloudflare tam kuantum sonrası güvenlik için 2029'u hedefliyor; bu ilk kilometre taşı.",
            "Ziyaretçi→Cloudflare ve Cloudflare→origin bağlantıları farklı tehdit profillerine sahip; ikisi ayrı ayrı ele alınıyor.",
            "Yazıda \"utanç verici bir itiraf\" bölümü var — mühendislik yazılarında nadir görülen bir dürüstlük."
        ],
        "for_you": "Post-quantum cryptography bugün senin işin değil, ama iki kavram doğrudan işine yarar. Birincisi **mTLS** (mutual TLS (mTLS)): sadece sunucu değil istemci de sertifikayla kimliğini kanıtlar — servisler arası iletişimde API anahtarından çok daha güçlüdür ve Spring Boot ile yapılandırılabilir. İkincisi tehdit modeli düşünmek: \"bu veri 10 yıl sonra çözülse zarar verir mi?\" sorusu, sağlık ya da finans verisi tutan her sistemde bugün sorulması gereken bir soru.",
        "terms": [
            {
                "en": "post-quantum cryptography",
                "tr": "post-quantum cryptography",
                "definition": "Kuantum bilgisayarların kırabileceği klasik algoritmaların yerine geçen, kuantuma dayanıklı şifreleme ve imza yöntemleri."
            },
            {
                "en": "harvest-now, decrypt-later",
                "tr": "harvest-now, decrypt-later",
                "definition": "Bugün çözülemeyen şifreli veriyi biriktirip gelecekte çözmeyi hedefleyen saldırı stratejisi."
            },
            {
                "en": "mTLS (mutual TLS)",
                "tr": "mTLS (mutual TLS)",
                "definition": "Hem sunucunun hem istemcinin sertifikayla kimliğini kanıtladığı TLS kurulumu."
            }
        ]
    },
    {
        "url": "https://openai.com/index/gpt-5-6-frontier-intelligence-efficiency",
        "slot": "brief",
        "title_tr": "Modeli hızlandırmak yetmiyor: inference yığınının her katmanı",
        "difficulty": "orta",
        "tags": [
            "LLM",
            "performance",
            "infrastructure",
            "cost"
        ],
        "summary": "OpenAI, GPT-5.6 ailesinin verimlilik kazanımlarını anlatıyor ve yazının değerli kısmı model değil **inference yığını** (inference stack). Ana tez tek cümlede: bir model yalıtılmış hâlde çok verimli olabilir, ama istekler kötü dağıtılıyorsa, donanım boş bekliyorsa ya da veri hareketi hesabı yavaşlatıyorsa sunması yine de pahalıdır.\n\nSaydıkları optimizasyon katmanları klasik sistem mühendisliği: yük dengeleme, speculative decoding (speculative decoding), caching ve çekirdek (kernel) optimizasyonu. Yani kazanç tek bir yerden değil, her katmandan biraz gelmiş.",
        "key_points": [
            "Talep kapasiteden hızlı büyüdüğünde verimlilik bir sistem tasarım kısıtı hâline geliyor.",
            "Aynı model ailesinde Sol/Terra/Luna gibi kademeler var — zekâ, hız ve fiyat ayrı eksenler."
        ],
        "for_you": "\"Sistem yalıtılmış hâlde hızlı ama üretimde yavaş\" durumu senin de başına gelecek. Bunun tipik sebepleri bu yazıdakilerle aynı: istekler eşit dağılmıyor, kaynak boşta bekliyor, veri gereksiz yere ağdan geçiyor. Spring Boot'ta bir endpoint'in yerelde 20 ms, üretimde 400 ms sürmesinin cevabı genelde kodda değil bu üç yerden birindedir. Ölçmeden optimize etmeye başlama — önce nerede beklendiğini bul.",
        "terms": [
            {
                "en": "inference",
                "tr": "inference",
                "definition": "Eğitilmiş bir modeli çalıştırıp çıktı üretme aşaması."
            },
            {
                "en": "speculative decoding",
                "tr": "speculative decoding",
                "definition": "Küçük ve hızlı bir modelin birkaç token'ı tahmin etmesi, büyük modelin bunları toplu doğrulaması; üretimi hızlandırır."
            }
        ]
    },
    {
        "url": "https://cloud.google.com/blog/products/data-analytics/introducing-the-borderless-lakehouse/",
        "slot": "brief",
        "title_tr": "Veriyi taşımadan sorgulamak: Iceberg REST kataloğu",
        "difficulty": "orta",
        "tags": [
            "data engineering",
            "data warehouse",
            "architecture"
        ],
        "summary": "Google Cloud, Apache Iceberg üzerine kurulu \"sınırsız lakehouse\" iyileştirmelerini duyuruyor: şirket içi sistemler, farklı bulutlar ve SaaS uygulamaları tek bir sorgu yüzeyinden erişilebiliyor — veriyi **taşımadan**.\n\nTeknik anahtar Iceberg REST kataloğu üzerinden **katalog federation’ı**. Dosyaları kopyalamadan uzak veriyi keşfedip sorgulayabiliyorsun; farklı veri ekipleri Iceberg verisinin aynı kopyası üzerinde çalışıyor. SAP, Salesforce, Workday gibi uygulamalara sıfır-kopya entegrasyon da aynı fikrin uzantısı: BigQuery canlı uygulama verisini karmaşık ETL kurmadan doğrudan sorguluyor.",
        "key_points": [
            "\"Kopyalama yerine federation\" son yılların en belirgin veri mimarisi eğilimi — her kopya bir tutarsızlık kaynağı.",
            "Iceberg açık bir tablo formatı; kilitlenmeyi (vendor lock-in) azaltması bu mimarinin can damarı."
        ],
        "for_you": "Buradaki ilke küçük projelerde de geçerli: **her veri kopyası bir senkronizasyon borcudur.** Bir raporlama ihtiyacı için tabloyu ikinci bir yere kopyalamadan önce sor — kaynağı doğrudan sorgulayabilir miyim? PostgreSQL tarafında `postgres_fdw` (foreign data wrapper) tam olarak bunu yapar: başka bir veritabanındaki tabloyu yerelmiş gibi sorgularsın, kopya tutmadan. Küçük ölçekte federation’ın ne olduğunu anlamanın en fast path’ı.",
        "terms": [
            {
                "en": "Apache Iceberg",
                "tr": "Apache Iceberg",
                "definition": "Nesne depolamadaki büyük veri kümelerini tablo gibi yönetmeyi sağlayan açık tablo formatı."
            },
            {
                "en": "zero-copy",
                "tr": "zero-copy",
                "definition": "Veriyi çoğaltmadan, bulunduğu yerde sorgulama yaklaşımı."
            },
            {
                "en": "catalog federation",
                "tr": "catalog federation",
                "definition": "Farklı sistemlerdeki tablo kataloglarının tek bir arayüzden görünür kılınması."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
