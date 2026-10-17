"""16 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-16"

INTRO = (
    "Bir agent’ın kaç kez doğru cevap verdiğini ölçmek, onu inşa etmekten zor. Google’ın "
    "değerlendirme (eval) dersleri tam bu açığı kapatıyor. Yanında Netflix’in ‘aynı şeye "
    "üç araçta üç ad veriyoruz’ sorununu bir ontolojiyle çözmesi ve npm’deki kötü amaçlı "
    "ikili dosyaları yakalamaya çalışan bir LLM hattı var."
)

DRAFTS = [
    {
        "url": "https://cloud.google.com/blog/topics/developers-practitioners/four-eval-engineering-lessons/",
        "slot": "cover",
        "title_tr": "Agent’ı kapanış cümlesine göre notlama: dört eval mühendisliği dersi",
        "difficulty": "orta",
        "tags": ["agent", "değerlendirme", "test", "LLM"],
        "summary": (
            "Yazının tezi: agent’lı bir sistemin asıl zorluğu inşası değil ölçümü. Yazar, "
            "Google’da yıllardır değerlendirme mühendisliği yürütüyor ve yeni Google Cloud Developer "
            "eklentisini bu ilkeleri gerçek geliştirici iş akışlarında denemek için bir test yatağı "
            "olarak kullanmış. Çıkan dört ders:\n\n"
            "**1. Özeti değil yürütme adımlarını notla.** İlk değerlendirmede agent’ın son metin "
            "cevabını bir LLM hakemi (LLM-as-judge) kontrol listesine göre puanlıyordu. 11 "
            "istemlik ilk sette otomatik hakem üç istemi başarısız saydı; ham araç çağrısı "
            "kayıtları okununca eklentinin üçünü de geçtiği görüldü. Örnek: rubrik, hiçbir şeyi "
            "çalıştırmadan önce komut sözdizimini kontrol etmeyi istiyordu; agent ilk adımda "
            "`gcloud help run services list` çalıştırmıştı, ama son mesajı kalıcı veri kaybı "
            "uyarısına odaklandığı için bunu anmamıştı. Hakem, doğru işi yaptığı hâlde bunu "
            "övünerek söylemediği için agent’ı cezalandırdı. Hakem yalnızca agent’ın ne yazdığını "
            "görüyor, ne yaptığını değil. Ders: agent’ı kapanış konuşmasıyla değil, ham yürütme "
            "izleriyle puanla.\n\n"
            "**2. Eşzamansız işlemler için tasarla.** Telemetriyi düz, sıralı bir olay listesine "
            "indirmek eşzamanlı araç çağrılarını gizler ve davranış hatalarının kritik "
            "nedenlerinden biri bu. Güncel agent altyapıları birden çok araç çağrısını tek bir "
            "turda toplu gönderiyor. Yazıdaki örnekte bir ortamı inceleyip belge arayan agent’ta "
            "beceri yükleme çağrısı ve iki belge araması aynı `tool_calls` yükünde eşzamanlı "
            "gitti; beceri çok adımlı bir yönerge olduğu hâlde ona kendi turu verilmedi, "
            "yönergesi agent’ın eylemlerini hiç etkilemedi. Telemetri tur yapısını atarsa "
            "mühendisler agent’ın açık yönergeyi neden yok saydığını günlerce arar. Ders: "
            "telemetri çıkarıcıda tur yapısını koru.\n\n"
            "**3. Canlı koşu ve ‘kuru koşu’yu yan yana test et.** Canlı koşular genellikle ikinci "
            "adımda beklenmedik bir izin hatasına çarpıp denemek istediğin davranışa varmadan "
            "kesiliyor. Bu yüzden kimlik bilgileri çıkarılmış, agent’tan ne yapacağını anlatmasının "
            "istendiği bir sadece-plan koşusu da gerekiyor. En önemli bulguların yaklaşık yarısı iki "
            "koşu arasındaki farktan çıktı. Örnek: bir karşılama isteminde canlı koşu hemen proje "
            "listesi çağrısında takıldı; sadece-plan koşusu 8.000 karakterlik bir plan üretti ve "
            "kuruluş politikalarını, yönetici onaylarını ve yönetişimi tümüyle yok saydı. Canlı koşu "
            "büyük bir akıl yürütme kusurunu maskelemişti.\n\n"
            "**4. ‘Altın kümeleri’ kalıcı referans yap.** Model mimarileri birkaç ayda bir, agent "
            "altyapıları ve eklenti standartları sürekli değişiyor. Değerlendirmeyi, deterministik "
            "olmayan ortamlar için sürekli entegrasyon testi gibi ele alıp altyapı, canlı model ve "
            "araçları birlikte gerçekçi görevlerde sına. Tüm yörüngeyi (ne düşündü, hangi komutu "
            "çalıştırdı, bir şeyi bozmadan çözdü mü) yakala ve ideal yolu bilen insan "
            "uzmanların hazırladığı altın kümelerle puanla. Yazar ‘tek seferlik demo’yu (bir "
            "istemle koca bir oyun yazdırıp değerlendirme saymak) bir gösteriş metriği olarak "
            "nitelendiriyor: gerçek iş çok adımlı etkileşimleri, izinleri ve yıkıcı sonuçlardan "
            "kaçınmayı ölçmek demek, örneğin ‘maliyet tasarrufu fırsatı bul’ denince yanlışlıkla "
            "projeyi silmemek."
        ),
        "key_points": [
            "Agent’ı son mesajına göre değil, gerçekte ne çalıştırdığına göre değerlendir.",
            "Telemetrinde tur yapısını koru: eşzamanlı araç çağrıları yönergenin etkisini sessizce yok edebilir.",
            "Canlı ve sadece-plan koşularını yan yana çalıştır; ikisi arasındaki fark en önemli bulguları verir.",
            "Altın kümeleri uzmanlar hazırlasın; model değişince bile referans kalsın.",
            "Tek seferlik demo değerlendirme değildir; değerlendirme paketi gerekir.",
        ],
        "why_it_matters": (
            "Agent’lar yazıyla nitelendirilen ama eylemle sonuç veren sistemler. Değerlendirmeyi "
            "yalnızca çıktı metnine bakarak yaparsan hem iyi agent’ı cezalandırır hem de kötü "
            "agent’ı geçirirsin. Bu dört ders, o açığı kapatan en pratik kurallar."
        ),
        "for_you": (
            "Bunu DBH’daki LLM hattına ve ileride yapacağın agent özelliklerine doğrudan "
            "uygulayabilirsin. **(1) Altın küme:** elle doğruladığın 30-50 kayıtlık bir CSV "
            "tut (girdi, beklenen çıktı). Prompt ya da modeli her değiştirdiğinde bu kümeyi "
            "çalıştırıp doğruluğu karşılaştır; ‘daha iyi hissettiriyor’ yerine sayı gör. **(2) "
            "Yürütme izi:** bir agent yazarsan her araç çağrısını (ad, argüman, sonuç, tur "
            "numarası) bir JSON satırı olarak kaydet ve testi bu kayıtlara karşı yaz: ‘silmeden önce "
            "listeledi mi?’. **(3) Kuru koşu:** yıkıcı bir araç varsa agent’a bir `dry_run=True` "
            "modu ver ve önce onu değerlendir. Bu, hem güvenli hem de ucuz."
        ),
        "terms": [
            {"en": "eval (evaluation)", "tr": "değerlendirme", "definition": "Bir modelin ya da agent’ın davranışını tekrarlanabilir testlerle ölçme."},
            {"en": "LLM-as-judge", "tr": "hakem olarak LLM", "definition": "Bir modelin çıktısını başka bir LLM’e puanlatma yöntemi."},
            {"en": "trajectory", "tr": "yörünge", "definition": "Bir agent’ın görevi çözerken attığı adımların ve araç çağrılarının tam kaydı."},
            {"en": "golden set", "tr": "altın küme", "definition": "Doğru cevabı uzmanlarca belirlenmiş, referans olarak kullanılan test örnekleri."},
            {"en": "dry run", "tr": "kuru koşu", "definition": "Gerçek etki yaratmadan bir işlemin ne yapacağını gösteren deneme."},
        ],
    },
    {
        "url": "https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf?source=rss----2615bd06b42e---4",
        "slot": "brief",
        "title_tr": "Aynı şeye üç araçta üç ad: Netflix’in gözlemlenebilirlik ontolojisi",
        "difficulty": "ileri",
        "tags": ["gözlemlenebilirlik", "bilgi grafı", "agent", "Netflix"],
        "summary": (
            "Netflix’te ana ekran 1,5 saniye yavaşlıyor, alarm çalıyor, ve nedeni bulmak dört saat "
            "sürüyor. Zamanın çoğu zor bir hesaba değil, gözlem sistemlerinin zaten bildiği ama hiçbir "
            "yerde okunabilir biçimde yazılmamış ilişkileri yeniden kurmaya gidiyor. Her sistem "
            "kendi içinde tutarlı, dışarıya kapalı: bir şey bir sistemde ‘uygulama’, ötekinde "
            "‘servis’, üçüncüsünde ‘küme’ oluyor; adları bir ek, bir büyük harf ya da bir "
            "yeniden adlandırma ayırıyor. Eksik olan, operasyonel dünyadaki varlıklar üzerine "
            "açık ve makinece okunabilir bir anlaşma.\n\n"
            "Çözüm bir **ontoloji**: türlerin, özelliklerin ve ilişkilerin biçimsel tanımı; birimi "
            "**üçlü** (özne, yüklem, nesne). Örneğin `api-gateway ownedBy Team Bedrock` ya da "
            "`INC-5377 affects api-gateway`. Böylece ‘Team Bedrock’ın sahip olduğu uygulamaları "
            "etkileyen olaylar’ gibi üç araçta aranan bir soru tek sorguya iniyor. W3C yığınıyla "
            "kurulmuş (RDF, OWL, SHACL, SPARQL) ve verisi Netflix’in kendi RDF veritabanı QuipuDB’de.\n\n"
            "İki karar öğretici: **genel bir ‘Service’ türünü reddettiler** (araçlarda dört farklı "
            "anlama geliyor); her uygulama tek bir türe çözülüyor ve yaklaşık 49.000 kayıtlı yazılım "
            "kataloğuna karşı doğrulanmadan oluşturulmuyor, ayrıca bağımlılık kenarlarına sınır "
            "konuyor. İkincisi, **olay Slack kanallarındaki akıl yürütmeyi modellemek**: denenip "
            "bırakılan hipotezler, işe yarayan hafifletme, kim neyi neden bildi. Kanal sessizleşince "
            "bu bilgi buharlaşıyor; 200 mesajlık, 50 kişilik bir olay kanalı sıralı üçlülere "
            "dönüşüyor.\n\n"
            "En ilginç fikir **belirsizlikten determinizm**: LLM’ler özetliyor, bulanık eşleştirme "
            "servis adlarını çözüyor, olasılıksal bir motor nedensel zincir öneriyor; hiçbiri aynı "
            "çıktıyı iki kez garanti etmez. Ama ontoloji çıktı uzayını öyle sıkı daraltıyor ki "
            "(LLM serbest metin yazabilir ama tür sistemini bozan bir üçlü yayamaz; kategori "
            "önceden verilmiş bir listeden seçilir) sonuç, her seferinde aynı SPARQL cevabını "
            "veren deterministik bir grafik."
        ),
        "key_points": [
            "Olayı çözmenin yavaş kısmı çoğu zaman hesaplama değil, sistemler arası adlandırma farklarını eşleştirmektir.",
            "Ortak bir veri modeli (ontoloji), aynı varlığın farklı adlarını tek kimliğe indirir.",
            "LLM çıktısını şemayla kısıtlamak, rastgele bir süreci tutarlı bir sözleşmeye çevirir.",
            "Olay kanallarındaki akıl yürütme belgelenmezse kaybolur.",
        ],
        "for_you": (
            "Küçük bir ölçekte aynı sorunu kendi projelerinde de yaşarsın: aynı müşteri bir "
            "tabloda `musteri_id`, bir logda `customerId`, bir ekranda adı ile geçer. Bir "
            "kimlik sözlüğü tutmak ve her veri girişini ona karşı doğrulamak, DBH’daki kategori "
            "kodlarında yaptığın normalizasyonun genelleştirilmiş hâli. Modelden JSON isterken "
            "`enum` ile izin verilen değerleri sabitlemek ise burada anlatılan ‘çıktı uzayını "
            "daralt’ fikrinin en basit biçimi."
        ),
        "terms": [
            {"en": "ontology", "tr": "ontoloji", "definition": "Bir alandaki varlık türlerinin, özelliklerinin ve aralarındaki ilişkilerin biçimsel tanımı."},
            {"en": "triple (RDF)", "tr": "üçlü", "definition": "Bir olguyu özne-yüklem-nesne biçiminde ifade eden en küçük bilgi birimi."},
            {"en": "knowledge graph", "tr": "bilgi grafı", "definition": "Varlıkları ve aralarındaki ilişkileri düğüm ve kenarlarla tutan veri yapısı."},
            {"en": "MELT", "tr": "MELT", "definition": "Metrics, Events, Logs, Traces: gözlemlenebilirliğin dört temel veri türü."},
        ],
    },
    {
        "url": "https://www.databricks.com/blog/closing-binary-blind-spot-domain-knowledge-injection-llm-malware-triage-npm-packages",
        "slot": "brief",
        "title_tr": "npm’deki gizli ikili dosya: LLM’e alan bilgisini prompt’la enjekte etmek",
        "difficulty": "ileri",
        "tags": ["güvenlik", "tedarik zinciri", "LLM", "npm"],
        "summary": (
            "Databricks, kasım 2025’ten beri npm kayıt defterindeki kötü amaçlı paketleri "
            "topluyor. OSV tavsiyeleriyle doğrulanmış 11.413 paket sürümünün yüzde 96,2’sinde "
            "kötü amaçlı kod kaynakta saklı ya da harici bir sunucudan indiriliyor. Kalan yüzde 3,8’i "
            "(432 sürüm) ikili dosya gömüyor. Az ama tehlikeli: temiz görünen kaynak ve "
            "metadata arasına yerleştirilmiş, sembolleri silinmiş opak bir ikili dosya, LLM’i "
            "‘zararsız’ kararına kaydırabiliyor. İkili dosyalı paketler, yalnızca kaynaklılara "
            "göre iki kattan fazla sıklıkla kesin bir ‘kötü amaçlı’ karara ulaşamıyor "
            "(yüzde 14,4 ve yüzde 6,2).\n\n"
            "Ekibin hattı: npm kaydını gerçek zamanlı izleyen bir tarayıcı; önce YARA, Semgrep ve "
            "npm API ile statik aşama, sonra derlenmiş dosya için bir ikili analiz modülü; "
            "çıktılar yapılandırılmış bir prompt’a toplanıyor ve LLM gerekçeli bir karar veriyor, "
            "gerekirse en çok üç turda ek dosya isteyebiliyor. Çalışma, farklı gizleme "
            "düzeylerinde yapay ikili yükler (kimlik bilgisi hırsızı, dropper, ters kabuk vb.) "
            "üretip LLM’lerin bunları nasıl yorumladığını ölçüyor, hataların sistematik olup "
            "olmadığına bakıyor ve boşluğu amaca yönelik, ucuz bir **alan bilgisi kodlamasıyla** "
            "kapatıyor; yazarlar bunun hem ucuz hem de üst düzey modeller için tespiti "
            "iyileştirdiğini bildiriyor. Yaklaşım, uzman verisiyle açık modelleri ince ayarlamanın "
            "tersi: bilgiyi ağırlıklara gömmek yerine istemde veriyor; böylece kapalı modellere de "
            "uygulanabiliyor ve tehdit manzarası değişince yeniden eğitim gerekmiyor."
        ),
        "key_points": [
            "Nadir ama opak girdi (derlenmiş ikili dosya), LLM’in en kolay yanıldığı yerdir.",
            "Önce klasik statik araçlar (YARA, Semgrep), sonra LLM: model tek başına yeterli değil.",
            "Alan bilgisini istemde vermek, kapalı modellerde ince ayara gerek bırakmadan işe yarar.",
        ],
        "for_you": (
            "Güvenlik tarafında somut bir alışkanlık: bir bağımlılık eklemeden önce `npm audit` ya da "
            "`pip-audit` çalıştır, kilit dosyasını (`package-lock.json`) depoya koy ve CI’de sürümü sabitle. "
            "LLM tarafında ders şu: modelin zayıf olduğu girdi türü için istemin içine kısa bir "
            "‘nasıl bakılır’ rehberi koymak (örneğin DBH’da belirsiz bir kategori için karar "
            "kuralları), çoğu zaman ince ayardan ucuz ve hızlı bir ilk adımdır."
        ),
        "terms": [
            {"en": "supply chain attack", "tr": "tedarik zinciri saldırısı", "definition": "Hedefi doğrudan değil, kullandığı bağımlılığı ya da paketi ele geçirerek vurma."},
            {"en": "YARA", "tr": "YARA", "definition": "Dosyalarda kötü amaçlı yazılım örüntülerini kural tabanlı arayan araç."},
            {"en": "triage", "tr": "triyaj", "definition": "Şüpheli öğeleri önem ve risk derecesine göre hızlıca sınıflandırma."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
