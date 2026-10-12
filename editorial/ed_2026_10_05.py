"""5 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-05"

INTRO = (
    "Bir agent’a takvimini, e-postanı ve ödeme yetkini verdiğinde asıl soru ‘bu veriye "
    "erişebilir mi’ değil, ‘bu veriyi şu anda, şu kişiye aktarması uygun mu’ olur. Google "
    "Research’ün 50’den fazla araştırmacıyla hazırladığı rapor, gizliliği tam bu soruyla "
    "tanımlayan bir kuramı agent’lara uyguluyor."
)

DRAFTS = [
    {
        "url": "https://research.google/blog/open-and-emergent-problems-in-agentic-privacy-and-security-a-contextual-angle/",
        "slot": "cover",
        "title_tr": "Gizlilik bir izin kutusu değil, bağlama uygun bilgi akışıdır: agent’lar için Contextual Integrity",
        "difficulty": "orta",
        "tags": ["agent", "gizlilik", "güvenlik", "araştırma"],
        "summary": (
            "LLM tabanlı agent’lar plan üretip dış araçları çağırarak çok adımlı işleri bizim "
            "yerimize yapıyor. Faydalı olmaları için kişisel veriye ve sonuç doğuran eylemlere "
            "erişmeleri gerekiyor; ama deterministik klasik yazılımdan farklı davrandıkları için "
            "alışılmış güvenlik yaklaşımları yetmiyor. Google Research, 2025 sonunda New York’ta "
            "düzenlenen CAPS çalıştayının çıktısı olan ve 50’den fazla akademi ve sektör "
            "araştırmacısının katkı verdiği bir rapor yayımladı.\n\n"
            "Raporun temeli **Contextual Integrity (CI)** kuramı. CI gizliliği ‘sır tutmak’ ya da "
            "‘kontrol’ olarak değil, yerleşik toplumsal normlara göre **uygun bilgi akışı** olarak "
            "tanımlıyor. Bir norm üç şeyle belirleniyor: **aktörler** (kim, kime, kim hakkında bilgi "
            "gönderiyor), **bilgi türü** (sağlık kaydı, finansal kayıt gibi) ve **aktarım ilkesi** "
            "(gizlilik, karşılıklılık gibi akışı yöneten kural). Yazıdaki örnek: hediye alışveriş "
            "listeni sanal bir alışveriş asistanıyla paylaşırsın, ama ailen ve arkadaşlarınla "
            "paylaşmazsın. Aynı veri, farklı bağlamda farklı karar.\n\n"
            "Rapor bu fikri bilgi paylaşımından eylemlere genişletiyor ve buna **bağlamsal güvenlik** "
            "diyor: bir eylemi çalıştırmadan önce toplumsal ve bağlamsal olarak uygun olup olmadığını "
            "değerlendiren sistemler. Yazarlara göre elle verilen izinler ve uzmanların yazdığı "
            "politikalar, uzun süren ve çok sayıda işi kendi başına yürüten agent’lara ölçeklenmiyor. "
            "Üst düzey normlar ile alt düzey erişim kuralları arasında hep bir anlam boşluğu vardı; "
            "LLM’ler ilk kez gerçekten bağlama bağlı, makinenin okuyabildiği politika yazma fırsatı "
            "veriyor. Önerilen yön **bağlamsal politika motorları** ile model ve kullanıcı düzeyindeki "
            "ilerlemeleri birleştiren çok katmanlı bir yaklaşım.\n\n"
            "Değerlendirme tarafında da bir çağrı var: yüksek özerklikli, çok ajanlı sistemler için "
            "standart ölçütler ve dinamik ‘Agent Gym’ ortamları."
        ),
        "key_points": [
            "Gizlilik ‘bu veri gizli mi’ değil, ‘bu akış bu bağlamda uygun mu’ sorusudur.",
            "Bir norm üç parçadır: aktörler, bilgi türü, aktarım ilkesi.",
            "Sabit izin listeleri uzun süre kendi başına çalışan agent’lara ölçeklenmez.",
            "Savunma tek katmanda değil: sistem, model, kullanıcı ve ekosistem düzeyinde birlikte.",
        ],
        "why_it_matters": (
            "Agent’lara verilen yetki arttıkça ‘erişim var / yok’ ikiliği yetersiz kalıyor. Bu rapor "
            "bir çözüm değil, araştırma gündemi; ama sorunu doğru adlandırıyor ve izin modeli "
            "tasarlarken kullanabileceğin net bir kavram çerçevesi veriyor."
        ),
        "for_you": (
            "KlioAI ya da Mobit’e bir agent özelliği eklerken izinleri ‘okuyabilir / yazabilir’ diye "
            "değil, üçlüyle tanımlamayı dene: **kim** (hangi kullanıcı adına), **ne tür veri** "
            "(ihale belgesi, kişisel not, ödeme bilgisi) ve **nereye** (kullanıcının kendisine mi, "
            "üçüncü bir tarafa mı). Pratikte bu, araç çağrılarından önce çalışan küçük bir kontrol "
            "fonksiyonu demek: `allow(actor, data_type, destination)`. Dışarıya veri gönderen her "
            "araç (e-posta, webhook) için bu kontrolü kodda zorunlu tut; modelin promptuna "
            "‘paylaşma’ yazmak bir sınır değildir."
        ),
        "terms": [
            {"en": "Contextual Integrity (CI)", "tr": "bağlamsal bütünlük", "definition": "Gizliliği, bilginin bulunduğu bağlamın normlarına uygun biçimde akması olarak tanımlayan kuram."},
            {"en": "transmission principle", "tr": "aktarım ilkesi", "definition": "Bir bilgi akışının hangi koşulla yapıldığını belirleyen kural; örneğin gizlilik ya da karşılıklılık."},
            {"en": "policy engine", "tr": "politika motoru", "definition": "Bir eylemin ya da veri akışının izinli olup olmadığına kurallara göre karar veren bileşen."},
            {"en": "agentic AI", "tr": "ajan tabanlı yapay zekâ", "definition": "Plan yapıp araç çağırarak çok adımlı işleri kendi başına yürüten yapay zekâ sistemleri."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
