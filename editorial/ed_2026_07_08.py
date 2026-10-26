"""8 Temmuz 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-07-08"

INTRO = "Günün kapağı, herkesin puanına baktığı bir benchmark'ın aslında bozuk olduğunu anlatıyor — hem de onu kullanan şirketin kendi ağzından. Test setinin kendisini denetlemek, testten geçmekten daha değerli bir iş."

DRAFTS = [
    {
        "url": "https://openai.com/index/separating-signal-from-noise-coding-evaluations",
        "slot": "cover",
        "title_tr": "Bozuk benchmark: testin kendisini denetlemek",
        "difficulty": "orta",
        "tags": [
            "evaluation",
            "testing",
            "LLM",
            "metodoloji"
        ],
        "summary": "Model yeteneklerini doğru ölçmek, dağıtım ve güvenlik kararları için kritik. Değerlendirmelerin kusurlu olması sadece bir sayıyı bozmaz — yetenekler hakkında yanlış bir anlayış yaratır, güvenlik gerekçelerini yanlış temsil eder ve araştırma önceliklerini saptırır.\n\nOpenAI önce en yaygın kullanılan kodlama benchmark'larından **SWE-bench Verified**'ı incelemiş ve temel tasarım ile **kontaminasyon** sorunları bulmuş: benchmark artık yazılım geliştirme yetenekleri hakkında anlamlı sinyal vermiyordu. Topluluğu SWE-Bench Pro'ya geçmeye teşvik etmişler.\n\nSonra aynı denetimi **SWE-Bench Pro'ya** da yapmışlar — kendi önerdikleri alternatife. Yöntem şu: bir veri noktası analizi pipeline'ı, modelin görev denemelerini, görev metadata'sını ve başarısızlık izlerini inceleyip olası değerlendirme kusurlarını işaretliyor; işaretlenen her görev sonra elden geçiriliyor.\n\nBulunan sorunlar dört kategoriye ayrılmış. Birincisi ve en öğreticisi: **overly strict test’ler** — prompt'ta belirtilmeyen uygulama detaylarını dayatıyor ve işlevsel olarak doğru olan birçok çözümü geçersiz sayıyor.",
        "key_points": [
            "Kontaminasyon: test verisinin eğitim verisine sızması. Model \"çözmüyor\", hatırlıyor olabilir.",
            "Overly strict test, sadece benchmark'ların değil senin test paketinin de sorunu: davranışı değil uygulamayı test eden test, refactor'ı imkânsızlaştırır.",
            "Kendi önerdikleri alternatifi de denetlemişler — metodolojik dürüstlüğün iyi bir örneği.",
            "Kusurları bulmak için otomatik bir tarama + insan incelemesi birleşimi kullanılmış."
        ],
        "why_it_matters": "Bir sayıya bakıp karar veriyorsan, o sayının nasıl üretildiğini bilmek zorundasın. Bu, model benchmark'larından çok daha geniş bir ilke: test kapsamı yüzdesi, uptime oranı, müşteri memnuniyeti skoru — hepsi ölçüm tasarımının ürünüdür ve ölçüm bozuksa sayı yalan söyler, üstelik güvenle söyler.",
        "for_you": "Buradaki ‘overly strict test’ kategorisi her geliştiriciyi ilgilendiriyor. Test yazarken sor: bu test **davranışı** mı yoksa **implementasyonu** mu doğruluyor? `assertEquals(3, service.getUsers().size())` davranışı test eder; `verify(repository).findAllByStatusOrderByIdAsc()` implementasyonu test eder ve o metodun adını değiştirdiğin anda, kod hâlâ doğru çalışırken test kırılır. Böyle testler refactor yapmaktan alıkoyar. İkinci ders: kendi evaluation setini periyodik olarak gözden geçir. Bir puanlama ya da filtre sistemi kuruyorsan üç ay sonra neyi elediğine bakıp işe yarayıp yaramadığını denetle.",
        "terms": [
            {
                "en": "benchmark contamination",
                "tr": "benchmark contamination",
                "definition": "Test verisinin modelin eğitim verisine karışması; model çözmek yerine hatırladığı için puan şişer."
            },
            {
                "en": "overly strict test",
                "tr": "overly strict test",
                "definition": "İstenen davranış yerine belirli bir uygulama biçimini dayatan test; doğru çözümleri de reddeder."
            },
            {
                "en": "failure trace",
                "tr": "failure trace",
                "definition": "Bir denemenin nerede ve neden başarısız olduğunu gösteren adım adım kayıt."
            }
        ]
    },
    {
        "url": "https://openai.com/index/k-12-educators-practical-skills",
        "slot": "brief",
        "title_tr": "Haftada 5,9 saat: bir verimlilik iddiasını nasıl okumalı",
        "difficulty": "başlangıç",
        "tags": [
            "measurement",
            "training",
            "research"
        ],
        "summary": "OpenAI Academy, Walton Family Foundation iş birliğiyle K-12 öğretmenleri için uygulamalı bir AI eğitim programı düzenliyor. Duyurunun içindeki tek somut sayı ilginç: Walton Family Foundation ve Gallup araştırmasına göre AI araçlarını **haftada en az bir kez** kullanan öğretmenler, ortalama **haftada 5,9 saat** tasarruf ettiklerini **tahmin ediyor**.\n\nBu cümledeki iki kelime önemli: \"tahmin ediyor\" ve \"en az bir kez kullanan\". Yani sayı ölçülmüş bir tasarruf değil, kullanıcıların kendi beyanı; ve karşılaştırma grubu zaten aracı benimsemiş olanlar.",
        "key_points": [
            "Öz-bildirimli (self-reported) tasarruf, ölçülmüş tasarruftan sistematik olarak yüksek çıkar.",
            "\"Kullananlar\" ile \"kullanmayanlar\" arasındaki farkın bir kısmı araçtan değil, kullanmayı seçen insanların farkından gelir."
        ],
        "for_you": "Bunu bir okuma alışkanlığı olarak al: bir verimlilik iddiası gördüğünde üç soru sor. Sayı ölçüldü mü yoksa beyan mı? Karşılaştırma grubu kim? Kim finanse etti? Bu sinizm değil, temel metodoloji. Kendi işinde de aynısı geçerli: ‘kullanıcılar yüzde 30 daha hızlı öğreniyor’ demek istiyorsan bunu ankete değil ürün içi ölçüme dayandır. Beyan edilen fayda pazarlama, ölçülen fayda mühendisliktir.",
        "terms": [
            {
                "en": "self-reported data",
                "tr": "self-reported data",
                "definition": "Katılımcıların kendi beyanına dayanan veri; hatırlama ve beklenti yanlılığına açıktır."
            },
            {
                "en": "selection bias",
                "tr": "selection bias",
                "definition": "Karşılaştırılan grupların, ölçülen etkiden bağımsız olarak baştan farklı olması."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
