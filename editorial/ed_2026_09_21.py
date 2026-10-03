"""21 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-21"

INTRO = (
    "Meta dokuz yıldır kullandığı kaynak atama çözücüsünü açık kaynak yaptı. Yazının değeri "
    "kütüphanenin kendisinden çok bir tasarım fikrinde: problemi tarif etmek ile çözmek ayrı "
    "katmanlar olmalı. Bu fikir optimizasyonla hiç ilgin olmasa da işine yarar."
)

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/09/21/open-source/rebalancer-generic-high-performance-library-assignment-problems/",
        "slot": "cover",
        "title_tr": "Problemi tarif etmek ile çözmek ayrı iştir: Meta’nın açık kaynak atama çözücüsü Rebalancer",
        "difficulty": "ileri",
        "tags": ["optimizasyon", "kaynak ataması", "açık kaynak", "tasarım"],
        "summary": (
            "Elinde bir nesne kümesi ve bir kutu (bin) kümesi var; nesneleri, belirli kısıtları "
            "sağlayarak ve bazı hedefleri optimize ederek kutulara nasıl atarsın? Bu soru Meta'nın "
            "altyapı yığınının her katmanında çıkıyor: donanım yerleşimi (rafları elektrik arıza "
            "alanlarına yaymak), servis yerleşimi (sunucuları servislere atamak), görev yerleşimi "
            "(görevleri sunuculara atamak) ve trafik yönlendirme (milyarlarca kullanıcının trafiğini "
            "coğrafi olarak dağılmış veri merkezlerine yollamak).\n\n"
            "Yeniden kullanılabilir bir çerçevenin iki zorluğu var: **kullanılabilirlik** (pratisyenler "
            "gerçek hayat politikalarını biçimsel optimizasyonun gerektirdiği kesin formüllere "
            "çevirmekte zorlanıyor) ve **ölçeklenebilirlik** (NP-zor problemleri ticari çözücüler "
            "verimli çözemiyor). **Rebalancer**, problemin **belirtimini çözümünden ayırarak** ikisini "
            "birden ele alıyor. Problem; nesneler, kutular, kısıtlar ve hedeflerle tanımlanıyor, sonra "
            "bir **ifade grafiğine** (yönlü döngüsüz graf) çevriliyor. Çözücü bu grafikten yararlanarak "
            "ya yerel arama sezgiseli tasarlıyor ya da ticari (FICO Xpress, Gurobi) veya açık kaynak "
            "(HiGHS) bir çözücüyle çözülebilen karma tamsayılı programlama (MIP) modeli kuruyor.\n\n"
            "Belirtim dili üç adımda soyutlama seviyesini yükseltiyor: temel modelleme yapıları "
            "(boyutlar, bölümler, kapsamlar, kullanım), bu yapılar üzerinde yaygın ifadeler (SUM, MAX "
            "gibi toplulaştırmalar) ve düzinelerce hazır hedef ve kısıtı sunan üst düzey ‘spec’ API’si "
            "(‘her rafta tek iş tipi olsun’ için `GroupCountSpec`, dengeli dağılım için `BalanceSpec` "
            "gibi). Spec’ler, yeniden kullanılabilen hazır tarifler.\n\n"
            "İki çözüm tekniği var. **Optimal çözücü** ifade grafiğini MIP çözücülere verir; ama her "
            "nesne için bir ikili karar değişkeni gerektirdiğinden model boyutu en kötü durumda "
            "O(nesne × kutu) ile **ikinci dereceden** büyür ve en büyük problemler hiçbir MIP "
            "çözücüye sığmaz. **Yerel arama çözücüsü** doğrudan ifade grafiği üzerinde çalışır: mevcut "
            "atamanın çevresindeki komşulukta bazı nesneleri başka kutuya taşıyıp en çok iyileşen "
            "kısıt ihlal etmeyen hamleyi uygular. Komşuluk büyüklüğü en kötü durumda O(nesne + kutu), "
            "yani bellek sorunu olmadan çok büyük problemleri modelleyebilir; saniyede milyonlarca "
            "değerlendirme yapılabiliyor."
        ),
        "key_points": [
            "Belirtim (ne istiyorum?) ile çözüm (nasıl bulurum?) ayrılınca aynı problem farklı çözücülerle çözülebilir.",
            "Hazır ‘spec’ler domain bilgisini yeniden kullanılabilir hâle getiriyor: her ekip aynı kısıtı yeniden yazmıyor.",
            "Kesin çözüm ile ölçek arasında takas: optimal çözücü küçük/orta, yerel arama çok büyük problemler için.",
            "Önce başlangıç ataması ve durma koşulu verilir; çözücü ‘yeterince iyi’ bir çözüme zamana bağlı yaklaşır.",
        ],
        "why_it_matters": (
            "Birçok altyapı sorunu (iş zamanlama, yük dengeleme, kapasite planı) aslında atama "
            "problemidir ama ad hoc kodla çözülür. Problemi deklaratif tarif edip çözücüyü "
            "değiştirebilmek, SQL’in veri sorgularına getirdiği şeyin optimizasyondaki karşılığı."
        ),
        "for_you": (
            "Hemen deneyebileceğin yer: `scipy.optimize.milp` (arka planda HiGHS kullanır) ile küçük "
            "bir atama problemi çözmek. Örneğin Tradebot’ta sermayeyi belirli kısıtlarla (varlık "
            "başına tavan, toplam risk limiti) varlıklara dağıtmak ya da Mobit’te zamanlanmış "
            "işleri çalışanlara eşit yükle dağıtmak. Daha önemlisi tasarım dersi: kısıtları kodun "
            "içine ‘if’ olarak gömmek yerine, bildirimsel bir listede (‘her sunucuda en fazla 3 "
            "iş’, ‘iki kopya aynı rafta olmasın’) tutarsan hem testi hem değişimi kolaylaşır."
        ),
        "terms": [
            {"en": "assignment problem", "tr": "atama problemi", "definition": "Nesneleri kısıtlar altında, bir hedefi optimize edecek şekilde kutulara yerleştirme problemi."},
            {"en": "mixed integer program (MIP)", "tr": "karma tamsayılı program", "definition": "Bazı değişkenlerin tam sayı olmak zorunda olduğu doğrusal optimizasyon problemi."},
            {"en": "local search", "tr": "yerel arama", "definition": "Mevcut çözümü küçük değişikliklerle iyileştirerek ilerleyen sezgisel arama."},
            {"en": "fault domain", "tr": "arıza alanı", "definition": "Tek bir arızanın birlikte etkileyebileceği bileşenler grubu (aynı raf, aynı elektrik hattı gibi)."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
