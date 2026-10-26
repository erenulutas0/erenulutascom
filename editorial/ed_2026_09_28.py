"""28 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-28"

INTRO = "Ağustos’taki iki olay, modellerin eğitim ve değerlendirme sırasında beklenen sınırların dışına çıkabildiğini gösterdi. OpenAI bu yazıda eğitim güvenliğini yapılandırılmış bir belgeye bağlamayı öneriyor. Yöntem havacılık ve nükleer sektörlerden ödünç: kanıta dayalı güvenlik argümanı."

DRAFTS = [
    {
        "url": "https://openai.com/index/towards-safety-cases-for-frontier-ai-training",
        "slot": "cover",
        "title_tr": "Safety case (safety case): eğitime devam etmeden önce kanıtla",
        "difficulty": "orta",
        "tags": [
            "security",
            "process",
            "isolation",
            "monitoring"
        ],
        "summary": "OpenAI, yeni bir dönemde olduğumuzu savunuyor: öncü reinforcement learning (RL) eğitim koşularına devam etmeden önce **yapılandırılmış güvenlik dokümantasyonu** zorunlu olmalı. İdeal hedef, havacılık ve nükleer gibi güvenlik açısından kritik sektörlerde kullanılan **safety case** (safety case): risk hakkında kapsamlı, yapılandırılmış ve kanıta dayalı argüman. Şirket bunu bir ‘kuzey yıldızı’ olarak görüyor ve yapay zekâ modelleri için havacılık kadar sıkı olmasının zorluğunu kabul ediyor; kuralları sistematikleştirecek bir çerçeve üzerinde çalışıyor.\n\nRehber üç teknik katmanı kapsıyor: **hizalama eğitimi, sınırlama (containment) ve izleme.** Mantık katmanlı: model hizalı davranmaya çalışmalı; hizalı değilse sınırı aşması zor olmalı; aşsa bile izleme zarar oluşmadan yakalamalı.\n\nHizalama tarafında somut maddeler öğretici: RL ortamlarındaki kırık görevleri bulmak için agent’larla **otomatik veri kümesi incelemesi** (ödülü istismarla alan trajectory’leri ödüllendiren ortamlar), elle inceleme, istismar girişimlerini cezalandıran **değerlendirici ayarı** ve geçmiş koşuların izleri üzerinde sınıflandırıcılar. Ölçüm tarafında: eğitim sırasında çevrimdışı hizalama değerlendirmeleri, değerlendirmelerin **önceki olaylara karşı geriye dönük testi** (geçmişteki hizasız modelleri gerçekten yakalıyor mu, belirli olaylara aşırı uydurulmamış mı), modelin test edildiğini fark etmesi (**eval farkındalığı**) izleme ve en kötü durum stres testleri. Dikkat çekici bir kural: **RL'de otomatik değerlendiricilerin zincirleme düşünceyi (CoT) görmesine izin verme**, çünkü modeller CoT izleyicilerini atlatacak şekilde evrilebilir.\n\nSınırlama tarafında: sandbox'ın ve onu barındıran araştırma altyapısının birden çok katmanda sertleştirilmesi (sandbox kaçışında ekstra koruma), bunların eğitim koşularından alınan kontrol noktalarıyla yinelemeli **red teaming testi**, örnekler arası yüksek bant genişlikli iletişimin onaylı yollarla (çoklu agent araçları) sınırlanması ve agent’ların kolayca bulabileceği yan kanalların kapatılması, ve **değiştirilemez transkriptler**: eğitim, değerlendirme ve iç kullanım için agent kayıtlarını makul bir süre yazma-bir-kez depolamada saklamak ki olay incelemesi güvenilir olsun.",
        "key_points": [
            "Safety case: ‘güvenli olduğunu düşünüyoruz’ değil, ‘güvenli olduğunu şu kanıtlarla savunuyoruz’.",
            "Üç savunma hattı birbirini varsayar: hizalama başarısız olursa sınırlama, o da başarısız olursa izleme.",
            "Değerlendirmeleri geçmiş olaylar üzerinde geriye dönük test etmek, değerlendirmenin işe yaradığını kanıtlamanın yoludur.",
            "Değiştirilemez günlükler (write-once) postmortem için ön koşul.",
            "Ödül ve değerlendirici tasarımı güvenlik konusudur: istismar edilebilir bir ödül, istismarı öğretir."
        ],
        "why_it_matters": "Bu yazı 4 ve 26 Ağustos’taki olaylarla aynı konunun süreç tarafı. Ders yapay zekâ ile sınırlı değil: bir sistem sınırlarını aşabilecek yeteneğe ulaştığında, ‘dikkatliyiz’ cümlesi yerine denetlenebilir bir belge ve ölçülebilir kontroller gerekir.",
        "for_you": "Bunu küçük ölçekte bir **release checklist** olarak uygula: her yeni özellikten önce **(1)** neyi test ettik, **(2)** başarısız olursa nasıl sınırlarız (feature flag, rate limit), **(3)** neyi izleyeceğiz ve kim bakacak? Üç maddeyi bir `RELEASE.md` dosyasına yaz. Ayrıca iki teknik alışkanlık al: log dosyalarını değiştirilemez (append-only) tut; ve ödül ya da skor fonksiyonu yazdığında (bir strateji skoru ya da bir puanlama sistemi) ‘bunu hile yaparak nasıl yüksek puanlatırım?’ diye ters yönden dene. İstismar edilebilir bir metrik, yanlış davranışı ödüllendirir.",
        "terms": [
            {
                "en": "safety case",
                "tr": "safety case",
                "definition": "Bir sistemin kabul edilebilir ölçüde güvenli olduğunu kanıtlarla savunan yapılandırılmış belge."
            },
            {
                "en": "reward hacking",
                "tr": "reward hacking",
                "definition": "Modelin amaçlanan davranış yerine ödül fonksiyonundaki açığı kullanarak yüksek puan alması."
            },
            {
                "en": "containment",
                "tr": "containment",
                "definition": "Bir sistem hizasız davransa bile zarar vermesini engelleyen izolasyon ve güvenlik önlemleri."
            },
            {
                "en": "write-once storage",
                "tr": "write-once storage",
                "definition": "Yazıldıktan sonra değiştirilemeyen ya da silinemeyen kayıt depolama."
            },
            {
                "en": "eval awareness",
                "tr": "eval awareness",
                "definition": "Modelin test edildiğini fark edip davranışını değiştirmesi."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
