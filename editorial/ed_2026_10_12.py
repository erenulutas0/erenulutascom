"""12 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-12"

INTRO = (
    "Canlı bir sistemin altındaki protokolü değiştirmek, protokolün kendisinden çok geçişin "
    "nasıl yapıldığıyla ilgilidir. Meta, Instagram Live’ın yükleme protokolünü kimse fark "
    "etmeden değiştirdi ve nasıl yaptığını anlatıyor. Yanında boşta duran çıkarım kapasitesini "
    "işe koşan bir sistem ve logları yola çıkmadan süzmek var."
)

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/10/12/video-engineering/shipping-media-over-quic-at-meta-scale-for-instagram-live-ingest/",
        "slot": "cover",
        "title_tr": "Canlı yayının altındaki protokolü değiştirmek: Instagram Live’da Media over QUIC",
        "difficulty": "ileri",
        "tags": ["ağ", "protokol", "video", "geçiş"],
        "summary": (
            "Instagram Live artık iOS ve Android’de canlı video yüklemesi (ingest) için açık "
            "standart **Media over QUIC (MoQ)** kullanıyor. İnternet yıllar içinde her biri kendi "
            "sorununa göre biçimlenmiş bir protokol yığını biriktirdi: yükleme için RTMP, oynatma "
            "için HLS ve DASH, gerçek zamanlı aramalar için WebRTC. Meta’da canlı yayın başlatıp "
            "aynı uygulamada sesli arama yapan biri **üç ayrı protokol yığınına** dokunuyor; her "
            "birinin kendi sunucu altyapısı, izlemesi ve uzmanlığı var. MoQ’un vaadi, yükleme, "
            "dağıtım ve oynatma için tek bir taşıma katmanı.\n\n"
            "**MoQ nasıl çalışır?** IETF’te Meta, Google, Akamai, Cisco, Cloudflare ve akademinin "
            "katılımıyla geliştirilen bir standart. Temel soyutlama **Track**: yayıncıların "
            "ittiği, abonelerin bir **aktarıcı (relay)** ağı üzerinden aldığı adreslenebilir medya "
            "nesnesi akışı. Aktarıcılar nesneleri medya içeriğini çözümlemeden önbelleğe alıp "
            "iletiyor. Öne çıkan özellikler: QUIC sayesinde akışlar arası TCP tarzı sıra başı "
            "tıkanması yok; önbellekleme ve çoğaltma protokolün içinde; aynı Track’in iki abonesi "
            "aynı anda **farklı gecikmelerde** çalışabiliyor (etkileşimli katılımcı için yaklaşık "
            "100 ms, arşiv için birkaç saniye); aktarıcılar tıkanıklıkta nesneleri metadata’ya göre "
            "düşürüp önceliklendirebiliyor; QUIC engellendiğinde standart bir TCP geri dönüşü var.\n\n"
            "**Geçiş nasıl yapıldı?** Canlı yükleme yaklaşık on yıldır Meta’nın kendi QUIC tabanlı "
            "protokolü RUSH üzerindeydi. Yazının itirafı şu: canlı bir sistemde taşıma protokolünü "
            "değiştirmenin zorluğu protokolle pek ilgili değil. Üç kısıtlı probleme böldüler. "
            "**İstemci:** açık kaynak MoQ kütüphaneleri moxygen üzerine kurulu bir yayıncı; tek bir "
            "yapılandırma parametresi yayın başına MoQ ya da RUSH seçiyor. **Arka ucu yeniden "
            "yazmak yerine uçta çeviri:** MoQ bağlantıları özel uç noktalarda sonlanıyor ve bir "
            "çeviri katmanı MoQ çerçevelerini arka ucun zaten anladığı RUSH biçimine dönüştürüyor. "
            "Aşağı akışta hiçbir şey değişmiyor; çevirici geçici bir iskele. **Sunucu taraflı "
            "yönlendirme:** yayın URL’si üretilirken deney grubuna göre MoQ uç noktası seçiliyor; "
            "böylece yayılım uygulama sürümünün benimsenmesine bağlı değil ve deney dakikalar "
            "içinde büyütülüp küçültülebiliyor.\n\n"
            "**Operasyonel engeller.** Taslak standart geliştirme sürerken değişti: belirli taslak "
            "sürümlerine sabitlendiler ve eski istemciler için uyumluluk katmanları tuttular. "
            "UDP/443 kurumsal ve operatör ağlarının azımsanmayacak bir bölümünde engelli: yayın "
            "başında TCP ve QUIC el sıkışmaları yarıştırılıyor, kazanan oturum boyunca "
            "kullanılıyor. QUIC şifrelemesi çerçeveleri kendi paket yakalamalarından da gizlediği "
            "için uca MoQ’u tanıyan izleme eklediler.\n\n"
            "**Sonuç:** aylarca süren deneyin ardından MoQ yolu, kalite ve güvenilirlik "
            "göstergelerinde RUSH ile **eşit** çıktı. Bu aşamanın hedefi iyileşme değil eşitlikti: "
            "üretimdeki bir taşıma katmanını kimseyi rahatsız etmeden değiştirebildiklerini "
            "gösterdi ve sonraki adımlar için temiz bir taban verdi."
        ),
        "key_points": [
            "Büyük bir geçişte ilk hedef iyileşme değil eşitliktir; eşitlik sonraki her adımın tabanıdır.",
            "Geçici bir çeviri katmanı, istemci ve arka uç değişikliklerini birbirinden ayırır.",
            "Yayılımı istemci sürümüne değil sunucu taraflı yönlendirmeye bağlamak, saniyeler içinde geri almayı sağlar.",
            "Yeni protokol her ağda çalışmaz; geri dönüş yolu tasarımın parçası olmalı.",
            "Şifreli protokolde hata ayıklama için gözlemlenebilirliği uç noktaya kendin koymalısın.",
        ],
        "why_it_matters": (
            "Çalışan bir sistemin temel bileşenini değiştirmek, mühendisliğin en riskli işlerinden "
            "biri. Bu yazıdaki üçlü (bayrakla seçilebilir yeni yol, geçici çeviri katmanı, sunucu "
            "taraflı yayılım) protokolden bağımsız, her büyük geçişe uyan bir kalıp."
        ),
        "for_you": (
            "Bu kalıbı bir sonraki büyük değişikliğinde uygula; örneğin Mobit’te mesajlaşmayı "
            "polling’den WebSocket’e ya da bir kütüphaneyi diğerine taşırken. **Bir:** yeni yolu "
            "bir özellik bayrağının arkasına koy ve eski yolu silme. **İki:** yeni istemciyi eski "
            "arka uca bağlayan ince bir uyarlayıcı (adapter) yaz; iki tarafı aynı anda değiştirme. "
            "**Üç:** bayrağı sunucuda tut ki uygulama güncellemesi beklemeden kapatabilesin. "
            "**Dört:** başarı ölçütünü baştan yaz: ‘hata oranı ve p95 gecikme eskisiyle aynı’. "
            "WebSocket için de aynı ders geçerli: bazı ağlar bağlantıyı keser, uzun yoklamaya "
            "(long polling) geri dönüş yolunu baştan tasarla."
        ),
        "terms": [
            {"en": "Media over QUIC (MoQ)", "tr": "QUIC üzerinden medya", "definition": "Canlı yayın ve gerçek zamanlı iletişim için QUIC üzerinde çalışan, IETF’te geliştirilen medya taşıma protokolü."},
            {"en": "ingest", "tr": "yayın yükleme", "definition": "Yayıncının cihazından sunucuya giden canlı video akışı."},
            {"en": "head-of-line blocking", "tr": "sıra başı tıkanması", "definition": "Kaybolan tek bir paketin, arkasındaki ilgisiz verilerin de beklemesine yol açması."},
            {"en": "relay", "tr": "aktarıcı", "definition": "Medya nesnelerini içeriğini çözmeden önbelleğe alıp abonelere ileten ara sunucu."},
            {"en": "feature flag", "tr": "özellik bayrağı", "definition": "Bir özelliği kod dağıtmadan açıp kapatmayı sağlayan yapılandırma anahtarı."},
        ],
    },
    {
        "url": "https://engineering.fb.com/2026/10/12/ml-applications/turning-opportunistic-ai-inference-capacity-into-better-ads-recommendations/",
        "slot": "brief",
        "title_tr": "Küresel olarak kıt, yerel olarak boşta: Meta atıl çıkarım kapasitesini nasıl kullanıyor",
        "difficulty": "ileri",
        "tags": ["ML altyapısı", "kapasite", "öneri sistemleri", "dayanıklılık"],
        "summary": (
            "Çıkarım filolarında bir paradoks var: kapasite küresel olarak kısıtlıyken yerel olarak "
            "anlamlı miktarda boşta kalabiliyor. Nedenleri tanıdık: filo tepe talebe göre "
            "kuruluyor ama trafik gün içinde değişiyor; donanım tedarik zincirinin takvimiyle, "
            "modeller ise başka bir takvimle geliyor. Meta bu boş cepleri ortak bir **fırsatçı "
            "kapasite havuzunda** toplayıp daha iyi reklam önerisine çeviriyor. Zorluk şu: bu "
            "kapasite ekiplere, bölgelere ve hızlandırıcı türlerine dağılmış ve çok kısa bir "
            "uyarıyla geri alınabiliyor.\n\n"
            "Sistem iki esneklik koluyla çalışıyor. **Rank More Ads (RMA):** sıralama aşamalarının "
            "değerlendirdiği aday sayısını artırıyor; ek adaylar getirme ve özellik işleme "
            "aşamalarından da geçtiği için hem CPU hem hızlandırıcı fazlası gerektiriyor. **Serve "
            "Better Models (SBM):** aday sayısını sabit tutup isteklerin daha büyük bir bölümünü "
            "daha güçlü bir modele yönlendiriyor; yalnızca hızlandırıcı fazlasını kullanabiliyor "
            "ve en çok fayda görecek istekleri değer sinyaliyle önceliklendiriyor. İkisi farklı "
            "kaynak bileşimleri tükettiği için birlikte daha geniş bir boşluğu dolduruyor. Temel "
            "iş yükünün kapasitesi fiziksel ve mantıksal yalıtımla korunuyor; kapasite çekilince "
            "**değere duyarlı yük atma** sistemi zarifçe geriletiyor."
        ),
        "key_points": [
            "Tepe yüke göre kurulan her sistem, günün çoğunda boşta kapasite taşır.",
            "Geri alınabilir kapasiteyi yalnızca vazgeçilebilir, ek değer üreten işe ver.",
            "Farklı kaynak bileşimi tüketen iki ayar düğmesi, tek düğmeden daha fazla boşluğu doldurur.",
            "Yük atarken rastgele değil, en az değerli isteği önce at.",
        ],
        "for_you": (
            "Küçük ölçekte aynı fikir: KlioAI’da zorunlu işi (kullanıcıya cevap) ve isteğe bağlı "
            "işi (daha ayrıntılı geri bildirim, ikinci bir model geçişi) ayır. Sistem rahatken "
            "isteğe bağlı işi çalıştır, kuyruk uzayınca ilk onu kapat. Bunun adı zarif bozulma "
            "(graceful degradation) ve bir `if (queueDepth > N)` kadar basit başlayabilir."
        ),
        "terms": [
            {"en": "opportunistic capacity", "tr": "fırsatçı kapasite", "definition": "O an boşta olan ama her an geri alınabilecek hesaplama kapasitesi."},
            {"en": "load shedding", "tr": "yük atma", "definition": "Aşırı yük altında sistemi ayakta tutmak için bazı istekleri bilerek reddetme ya da basitleştirme."},
            {"en": "graceful degradation", "tr": "zarif bozulma", "definition": "Kaynak azaldığında sistemin tümüyle çökmek yerine kaliteyi kademeli düşürmesi."},
        ],
    },
    {
        "url": "https://blog.cloudflare.com/transformers-on-logpush/",
        "slot": "brief",
        "title_tr": "Logu yola çıkmadan süz: Logpush Transformers",
        "difficulty": "başlangıç",
        "tags": ["loglama", "gözlemlenebilirlik", "maliyet", "gizlilik"],
        "summary": (
            "Ekipler Cloudflare loglarını SIEM’lere, analitik platformlarına ve nesne depolamaya "
            "aktarıyor. Loglar hedefe varmadan önce çoğu zaman sağlık kontrollerini çıkarmak, "
            "hassas alanları atmak ya da kayıtları yeniden biçimlendirmek gerekiyor ve bu, "
            "kurulup ölçeklenip izlenmesi gereken ayrı bir işleme servisi demek. Üstelik ekipler "
            "varır varmaz atacakları kayıtların aktarımı, alımı ve saklanması için de para ödüyor.\n\n"
            "**Transformers** bu işlemi aktarım hattının içine alıyor. Bir Transformer, belirli "
            "bir veri kümesi için yazılmış bir **SQL sorgusu**: kayıtları filtreliyor, hassas "
            "veriyi karartıyor ve alan ekleyip yeniden adlandırarak, çıkararak ya da iç içe "
            "koyarak çıktıyı biçimlendiriyor. Sorgu her toplu gönderime aktarımdan önce "
            "uygulanıyor. Örnek kullanım: birden çok CDN’den log toplayan bir ekip, kayıtları "
            "ortak şemaya oturtmak için sabit bir `provider` alanı ekliyor."
        ),
        "key_points": [
            "Kullanmayacağın veriyi taşımak ve saklamak için de ödersin; kaynağa en yakın yerde süz.",
            "Hassas alanı hedefte değil kaynakta karart; hedefe hiç ulaşmayan veri sızamaz.",
            "Dönüşümü SQL ile tanımlamak, ayrı bir servis işletme yükünü ortadan kaldırır.",
        ],
        "for_you": (
            "Spring Boot’ta aynı ilke: `/actuator/health` isteklerini erişim loguna yazma ve "
            "e-posta, token, TC kimlik no gibi alanları log satırına hiç koyma (Logback’te bir "
            "maskeleme dönüştürücüsü ya da log öncesi bir DTO). Logu sonradan temizlemek yerine "
            "baştan temiz yazmak hem ucuz hem güvenli."
        ),
        "terms": [
            {"en": "redaction", "tr": "karartma", "definition": "Hassas verinin kayıttan çıkarılması ya da maskelenmesi."},
            {"en": "NDJSON", "tr": "satır ayrımlı JSON", "definition": "Her satırın bağımsız bir JSON nesnesi olduğu metin biçimi; log aktarımında yaygın."},
        ],
    },
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
