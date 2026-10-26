"""15 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-15"

INTRO = "Arama ve öneri sistemlerinde yeni bir beklenti var: tek en iyi sonuç değil, birbirini tamamlayan bir sonuç kümesi. Google’ın yazısı bunun maliyet sorununu ele alıyor: her sorguda pahalı reasoning yapmak yerine, öğrenmeyi bir kez ve çevrimdışı yapmak."

DRAFTS = [
    {
        "url": "https://research.google/blog/bypassing-inference-bottlenecks-accelerating-complex-ai-search-with-retrieve-for-train/",
        "slot": "cover",
        "title_tr": "Pahalı düşünmeyi sorgu anından eğitime taşımak: Retrieve-for-Train",
        "difficulty": "ileri",
        "tags": [
            "search",
            "RAG",
            "reinforcement learning",
            "cost"
        ],
        "summary": "Modern arama ve öneri uygulamalarından artık tek en iyi eşleşme değil, **tutarlı bir sonuç kümesi** bekleniyor. ‘Kamp malzemesi’ arayan biri dört kişilik çadırın on küçük varyasyonunu istemez; çadır, uyku tulumu, taşınabilir ocak ve kafa lambası gibi birbirini tamamlayan bir küme ister. Sistemler bunun için **query fan-out** (query fan-out) kullanıyor: geniş bir isteği ilişkili alt sorgulara bölüp olası ilgi alanlarını kapsamak. Maliyet sorunu şu: veritabanını bilen bir ayrıştırmayı LLM’e her sorguda inference anında yaptırmak büyük bir ‘düşünme bütçesi’ harcatıyor.\n\nGoogle’ın ICML 2026 makalesindeki **Retrieve-for-Train** çerçevesi önce **öğretmeni** eğitiyor: 4 milyar parametreli açık modeller (Gemma3-4B, Qwen3-4B), her ana istek için tam 10 alt sorgu üretecek şekilde reinforcement learning’le (GRPO ve soft PPO) ince ayarlanıyor. Ödül, öğeleri tek tek puanlayan klasik alaka değil, **küme düzeyinde** üç rakip sütunun ağırlıklı toplamı. Bu üçlü birbirini dengeleyen ‘karşı çıpalar’ olarak tasarlanmış: yalnızca veri tabanına oturmayı ödüllendirirsen model anlamsız ama matematiksel olarak doğru noktaya düşen diziler üretip sistemi kandırıyor; hizalama eklersen bu kez isteği tekrar eden eş anlamlılara çöküyor. **Vendi Score** ile çeşitliliği ödüle katmak bu kestirme yolları kapatıyor.\n\nİkinci adım **damıtma**: öğretmenin öğrendiği davranış 53,9 milyon parametreli küçük bir **diffusion model’e** aktarılıyor. Bu model tüm hedef yönleri sürekli gömme uzayında tek bir, autoregressive olmayan paralel geçişte üretiyor ve autoregressive yaklaşıma göre 12-20 kat hızlanma sağlıyor. Büyük bağlam gruplarında autoregressive dallandırma gecikmesi doğrusal artıp yaklaşık 50 saniyeye çıkarken, diffusion model saniyenin altı ile birkaç saniye arasında kalıyor. Değerlendirme moda (kullanıcı kombinleri, CLIP ile) ve müzik (uzman çalma listeleri, MuLan ile) alanlarında yapılmış; tek sorgu, sıfır atışlı genişletme ve Best-of-N baz çizgilerinin hepsini geçmiş. Sıfır atışlı LLM’ler ‘bohemian festival style’ ve ‘bohemian festival fashion’ gibi neredeyse eş anlamlı alt sorgular üretirken, Retrieve-for-Train ‘bot’ ya da ‘dantel’ gibi gerçekten farklı yönlere dallanıyor.",
        "key_points": [
            "Kümenin kalitesi (çeşitlilik, kapsama, tamamlayıcılık) tek tek öğelerin alakasından ayrı bir hedeftir.",
            "Pahalı reasoning’i her sorguda yapmak yerine bir kez, çevrimdışı eğitime taşımak gecikme ve maliyeti düşürür.",
            "Soyut hedefler (‘çeşitli ve stokta olsun’) ölçülebilir bir ödül fonksiyonuna çevrilebilir.",
            "Öğretmen (RL ile eğitilmiş LLM) ve öğrenci (küçük diffusion model) ayrımı: kaliteyi öğretmen, hızı öğrenci sağlıyor."
        ],
        "why_it_matters": "Üretimde LLM’i her istekte ‘düşündürmek’ en pahalı yoldur. Bu yazı, tekrar eden bir görev için reasoning’i eğitim zamanına kaydırmanın genel bir desen olduğunu gösteriyor: bir kez pahalı öğren, her seferinde ucuz uygula.",
        "for_you": "RAG’inde tek bir arama yerine alt sorgulara bölme (query decomposition) kullanıyorsan bu doğrudan senin problemin. ‘Şu ihalenin tüm riskleri’ gibi geniş bir soruyu LLM’e her seferinde alt sorulara bölttürüyorsan, bu çağrıyı ölçüp maliyetini gör. Basit bir ilk adım: sık gelen geniş sorular için alt sorgu şablonlarını bir kez çıkarıp cache’le. Reinforcement learning gerekmeden de ‘inference anındaki işi önceden hesapla’ ilkesinin yarısını elde edersin. Çeşitlilik için de MMR (maximal marginal relevance) gibi basit bir re-ranking, benzer sonuçların sıralamayı doldurmasını engeller.",
        "terms": [
            {
                "en": "query fan-out",
                "tr": "query fan-out",
                "definition": "Geniş bir isteği, olası ilgi alanlarını kapsayacak birkaç ilişkili alt sorguya bölme."
            },
            {
                "en": "slate",
                "tr": "slate",
                "definition": "Kullanıcıya birlikte sunulan, bir bütün olarak değerlendirilen öğeler listesi."
            },
            {
                "en": "test-time compute",
                "tr": "test-time compute",
                "definition": "Modelin cevap üretirken harcadığı ek hesaplama; arttıkça gecikme ve maliyet de artar."
            },
            {
                "en": "maximal marginal relevance (MMR)",
                "tr": "maximal marginal relevance (MMR)",
                "definition": "Sonuçları hem alakalı hem birbirinden farklı olacak şekilde seçen yeniden sıralama tekniği."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
