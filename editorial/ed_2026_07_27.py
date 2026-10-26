"""27 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-27"

INTRO = "Pazar günü iki yazı: biri \"debugging’i zor bir protokolü nasıl yaklaşılabilir hâle getirdik\", diğeri işin kendisinin nasıl değiştiğine dair veri. Arşivden de 600.000 testi otomatik taşıyan bir göç hikâyesi ekledim — Java yazan herkesin okuması gereken cinsten."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/",
        "slot": "cover",
        "title_tr": "Hata ayıklanamayan protokolü araçla ehlileştirmek: pvcli",
        "difficulty": "orta",
        "tags": [
            "privacy",
            "tooling",
            "protocol",
            "open source"
        ],
        "summary": "Gizliliği koruyan protokollerde hata ayıklamak zor. **Oblivious HTTP** (OHTTP) dört farklı taraf arasında birkaç adımdan oluşuyor; üstüne ikili HTTP kodlaması ve birden fazla taslak RFC'ye dağılmış detaylar ekleniyor. Cloudflare bu protokolleri saniyede milyonlarca istek ölçeğinde işletirken öğrendiklerini temiz bir komut satırı aracına sarmış ve açık kaynak yapmış: **pvcli**, Apache-2.0 lisansıyla.\n\nAracın gösterdiği şey basit ama etkili: eskiden dört tarafı ayrı ayrı kurup elle takip etmeni gerektiren tam bir OHTTP isteği, artık tek satırda çalışıyor — relay, gateway ve origin dahil.\n\nMotivasyon bölümü de öğretici. Cloudflare'in gizlilik ürün ailesi büyüdükçe (Privacy Proxy, Privacy Gateway — Apple'ın Private Relay'ini ve Microsoft Edge'in Secure Network VPN'ini besleyen altyapılar) sorunu teşhis etmek de zorlaşmış. Yani araç bir pazarlama ürünü değil, kendi operasyonel acılarının çözümü.",
        "key_points": [
            "OHTTP'nin zorluğu tek bir karmaşık adım değil: dört taraf, ikili kodlama ve dağınık taslak spesifikasyonlar bir araya geliyor.",
            "Karmaşık bir protokolü benimsetmenin en etkili yolu, onu tek komutta denenebilir hâle getirmek.",
            "Aracın kaynağı gerçek operasyon deneyimi — saniyede milyonlarca istek."
        ],
        "why_it_matters": "Bir teknolojinin benimsenmesini belirleyen şey çoğu zaman teknolojinin kendisi değil, etrafındaki araçlardır. Hata ayıklanamayan bir sistem, ne kadar iyi tasarlanmış olursa olsun üretimde kullanılmaz. \"Bu sistemde bir şey ters gittiğinde nasıl anlarım?\" sorusu, tasarımın kendisi kadar tasarımın parçasıdır.",
        "for_you": "Bu yazıdaki alışkanlığı kendi projelerine taşı: kurduğun her karmaşık akış için küçük bir teşhis aracı yaz. Bir RAG sistemi için bir CLI düşün: bir sorgu ver, hangi belgelerin getirildiğini, similarity skorlarını ve modele giden nihai prompt’u bassın. Python’da `argparse` ile yarım saatlik bir iş ama ‘neden bu cevabı verdi?’ sorusunu dakikalar yerine saniyeler içinde cevaplatır. Mülakatta göstereceğin şey de bu tür araçlardır: sistemi yazmak kadar sistemi anlaşılır kılmak da mühendislik.",
        "terms": [
            {
                "en": "Oblivious HTTP (OHTTP)",
                "tr": "Oblivious HTTP (OHTTP)",
                "definition": "İsteği gönderen ile hedef sunucu arasına aracılar koyarak, hiçbir tarafın hem kimliği hem içeriği görememesini sağlayan protokol."
            },
            {
                "en": "relay / gateway",
                "tr": "relay / gateway",
                "definition": "OHTTP'de aracılar: relay kimin istediğini bilir ama içeriği göremez; geçit içeriği görür ama kimin istediğini bilmez."
            },
            {
                "en": "RFC draft",
                "tr": "RFC draft",
                "definition": "Henüz standart hâline gelmemiş, üzerinde çalışılan internet protokol belgesi."
            }
        ]
    },
    {
        "url": "https://openai.com/index/how-ai-is-expanding-what-people-do-at-work",
        "slot": "brief",
        "title_tr": "Task crossover: işler değil, işi kimin yaptığı değişiyor",
        "difficulty": "başlangıç",
        "tags": [
            "kariyer",
            "LLM",
            "research"
        ],
        "summary": "OpenAI'ın ekonomi araştırması 800.000'den fazla ABD kullanıcı mesajını incelemiş. Bulgu: işle ilgili mesajların **%16,8'i** ve mesleğe özgü mesajların **%43,5'i** başka bir meslekle ilişkilendirilen görevlerle ilgili.\n\nBuna **task crossover** (task crossover) diyorlar: tarihsel olarak bir mesleğe ait olan işin, başka bir meslekten insanın AI kullanımında görünmesi. Küçük işletme sahibi metin yazıyor, sözleşme inceliyor, temel finansal analiz yapıyor. Satışçı, eskiden analiste gidecek bir veri setini kendisi keşfediyor. Pazarlamacı, geliştiriciyi beklemeden web sitesindeki sorunu çözüyor.\n\nYazının kendi vurgusu şu: AI ile ilgili çoğu çalışma sabit bir görev listesiyle başlayıp \"model bunu yapabilir mi?\" diye soruyor. Bu araştırma farklı bir şeye işaret ediyor — AI **kimin hangi görevi üstlendiğini** de değiştiriyor.",
        "key_points": [
            "Değişim \"işler yok oluyor\" değil, iş sınırları bulanıklaşıyor biçiminde görünüyor.",
            "Bu, yeni mezun bir mühendis için hem fırsat hem risk: senin işine başkaları girebilir, sen de başkalarının işine girebilirsin."
        ],
        "for_you": "Kariyer açısından buradan çıkan ders net: bir aracı kullanabilmek artık ayırt edici değil; kimin ne yapabildiği hızla eşitleniyor. Ayırt edici olan **derinlik**. Herkes bir LLM’e sorgu yazabiliyorsa değerin bir sistemin neden yavaşladığını bulabilmen, bir veritabanı index’inin nasıl seçileceğini bilmen, bir distributed system’de hangi consistency garantisinin gerektiğini kestirebilmen olacak. Bu gazeteyi okumanın sebebi de tam olarak bu: yüzeyde kalmamak.",
        "terms": [
            {
                "en": "task crossover",
                "tr": "task crossover",
                "definition": "Bir mesleğe ait sayılan işin, başka meslekten kişiler tarafından yapılmaya başlanması."
            }
        ]
    },
    {
        "url": "https://www.uber.com/blog/junit-migration/",
        "slot": "archive",
        "title_tr": "600.000 testi elle taşımadan JUnit 5'e geçmek",
        "difficulty": "orta",
        "tags": [
            "Java",
            "testing",
            "migration",
            "otomasyon"
        ],
        "summary": "Uber'in Java monorepo'sunda test paketinin ana çerçevesi JUnit 4'tü. Çalışıyordu, ama sekiz yıl önce çıkan JUnit 5'in yeteneklerini kullanmalarını engelliyordu — ve JUnit 4'ün aktif geliştirmesi 2021'de durmuştu, yani hata düzeltmeleri ve güvenlik yamaları da gelmiyordu.\n\nÖlçek şu: **15 milyon satır kodda 600.000'den fazla JUnit 4 testi.** Elle göç, geliştiricilerin Jupiter API'sini öğrenmesini ve özel test paketlerini taşımasını gerektirecekti — devasa bir mühendislik saati. Üstüne Uber Bazel kullanıyor ve Bazel'ın yerel JUnit 5 desteği yoktu. Yani problem hem teknik hem kültüreldi: geliştiricileri ikna etmek.\n\nSonuçlar: Bazel'da JUnit 5 desteği açılmış ve tüm test modülleri JUnit Platform'a alınmış (Vintage ve Jupiter motorlarıyla JUnit 4 ve 5 birlikte destekleniyor). **4 ay içinde 75.000'den fazla test sınıfı** taşınmış, 1,25 milyondan fazla satır değiştirilmiş, 5.000'den fazla otomatik değişiklik seti üretilmiş.",
        "key_points": [
            "Anahtar tasarım kararı: iki çerçeveyi aynı anda çalıştırabilmek (Vintage + Jupiter). Böylece göç tek seferde değil aşamalı yapılabiliyor.",
            "Göç merkezîleştirilmiş — her ekibe \"kendi testlerinizi taşıyın\" demek yerine tek bir ekip otomatik dönüşüm yazmış.",
            "Kültürel boyut teknik boyut kadar açıkça ele alınmış."
        ],
        "why_it_matters": "Büyük göçlerin başarısızlık sebebi genelde teknik değil, koordinasyon. \"Herkes kendi parçasını taşısın\" yaklaşımı yıllarca sürüncemede kalan yarım göçler üretir. Uber'in yaptığı şey — bir kere otomasyon yaz, merkezden uygula, geçiş döneminde ikisini birlikte çalıştır — her ölçekte doğru desendir.",
        "for_you": "Bu, Java tarafında doğrudan uygulayabileceğin bir yazı. Kendi projelerinde bile aynı deseni kullan: bir kütüphane sürümü yükseltirken \"hepsini bir seferde değiştir\" yerine köprü katmanı kurup aşamalı geç. Ayrıca **OpenRewrite** gibi araçları öğren — Java'da otomatik kod dönüşümü yapan, tam da Uber'in yaptığı işi yapan araçlardır. Mülakatta \"600.000 testi nasıl taşırsın?\" sorusuna \"elle taşımam, dönüşüm kuralı yazar ve iki çerçeveyi bir süre birlikte çalıştırırım\" diyebilmek çok güçlü bir cevaptır.",
        "terms": [
            {
                "en": "monorepo",
                "tr": "monorepo",
                "definition": "Bir şirketin tüm projelerini tek bir sürüm kontrol deposunda tutması."
            },
            {
                "en": "Bazel",
                "tr": "Bazel",
                "definition": "Google kaynaklı, büyük monorepo'lar için tasarlanmış derleme ve test aracı."
            },
            {
                "en": "codemod",
                "tr": "codemod",
                "definition": "Kaynak kodu programatik olarak analiz edip toplu şekilde değiştiren betik ya da araç."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
