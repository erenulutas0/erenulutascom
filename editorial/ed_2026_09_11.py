"""11 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-11"

INTRO = "Saniyede 70 milyon istek, 500 petabayt veri, haftada 1 milyar kullanıcı. OpenAI’ın depolama platformu bir Python kütüphanesi olarak başlamış. Yazının değeri rakamlarda değil, ‘kütüphane olarak başlayan şeyi ne zaman servise çeviririz’ kararında."

DRAFTS = [
    {
        "url": "https://openai.com/index/scaling-storage-one-billion-users-part-one",
        "slot": "cover",
        "title_tr": "İstemci kütüphanesinden servise: OpenAI’ın Habitat depolama platformu neden Python’da kaldı",
        "difficulty": "ileri",
        "tags": [
            "storage",
            "architecture",
            "technical debt",
            "scaling"
        ],
        "summary": "Habitat, OpenAI ürünlerinin ihtiyaç duyduğu bilgiye hızlı ve güvenilir erişmesi için kurulan çevrimiçi depolama platformu. Bugün **saniyede 70 milyondan fazla isteği** işliyor, haftada 1 milyar kişinin kullandığı ürünleri destekliyor, yaklaşık 40 coğrafi bölgede çalışıyor ve **500 petabayttan fazla veri** sunuyor. Başlangıcı ise çok mütevazı: DevDay 2023’te GPT’ler için, tek bir veritabanına bağlanan basit bir **Python istemci kütüphanesi** olarak çıktı.\n\nKütüphane fikri işe yaradı: ürün mühendisleri şema arama, yönlendirme, yetkilendirme, şifreleme, serileştirme ve bağlantı havuzlamayı düşünmek zorunda değildi; hatta verinin Azure Cosmos DB’den mi, cache’ten mi geldiğini bile bilmiyorlardı. Yetenekler (istemci tarafı cache, sıkıştırma, şifreleme) paylaşılan kütüphaneye kolayca eklendi.\n\n2025 ortasında istemci tarafı uygulama sınırına dayandı. Servis sayısı büyüyünce geriye uyumlu protokol değişikliği yapmak imkânsızlaştı. Yazıdaki örnek çok öğretici: en kritik veri kümelerinin bölge kesintisindeki etkisini azaltmak için bunları bölgesel dağıtık Cosmos DB hesaplarına taşımak istediler. Bu, istemciye yönlendirme mantığı eklemeyi (feature flag arkasında), tüm istemcilere yaymayı ve sonra bayrağı açmayı gerektirdi. Onlarca servisi koordine etmek **günler** sürdü; gölgeleme eklemek birkaç gün daha, bir hata düzeltmesi yine birkaç gün. Sonunda tam bayrağı açma aşamasında bir ekip kendi servisini ilgisiz bir sebeple hatalı eski istemciye geri aldı ve kaçınmaya çalıştıkları kesinti yaşandı.\n\nKarar: Habitat’ı kendi **servisine** çıkarmak. Kazanç: dağıtım, observability ve platform geliştirmeleri için tek kontrol noktası; erişim denetimi, audit log ve altta yatan depolamaya erişimi merkezî uygulamak için tek darboğaz (güvenlik açısından avantaj). Bilinçli bir seçim daha: **servisi Python’da bıraktılar.** Python’un yüksek verimli bir servis için ek ağ gecikmesi ve CPU/bellek maliyeti getireceğini, 100 kat ölçekte kabul edilemeyeceğini ve eninde sonunda yeniden yazılacağını biliyorlardı; ama bunu ‘stratejik bir technical debt’ olarak gördüler: öncelik maliyet değil, ürün geliştiricileri engelden kurtarmak ve platform kararlılığıydı. Üstüne, kendi kodlama modellerinin ilerlemesinin gelecekte bu göçü kolaylaştıracağına dair hesaplı bir bahis de oynadılar. Bu, iki bölümlük serinin ilk yazısı.",
        "key_points": [
            "Kütüphane olarak dağıtılan altyapıda her değişiklik onlarca servisin dağıtım koordinasyonu demek; hata düzeltmesi bile günler alıyor.",
            "Servise çıkarmak tek kontrol noktası verir: dağıtım, observability, erişim denetimi ve audit log merkezileşir.",
            "Technical debt bilinçli alınabilir: öncelik ürün ekiplerini engelden kurtarmaksa yavaş dili geçici kabul etmek savunulabilir.",
            "Kütüphane + feature flag’la yayılım, tek bir geride kalmış istemci yüzünden bütün planı bozabilir."
        ],
        "why_it_matters": "‘Paylaşılan kütüphane mi, servis mi?’ sorusu her büyüyen sistemde çıkar. Kütüphane başlangıçta çok hızlıdır (ağ atlaması yok, tek dağıtım) ama sürümler dağılınca değişim maliyeti üstel artar. Servis ise başlangıçta yavaş ve pahalı, ölçekte ucuzdur.",
        "for_you": "Bu kararı küçük ölçekte yaşayacaksın: ortak bir ‘common’ modülünü birden fazla projeye kopyalıyorsan, her projede farklı sürümde kalır. İşaretleri tanı: ‘bir hata düzelttim ama üç yerde güncellemem gerekiyor’. Bunun iki ucu var: ortak kodu bir **versiyonlanan paket** yap ya da küçük bir **servise** çıkar. İkinci ders mülakat için altın değerinde: ‘Bilinçli technical debt aldım, çünkü öncelik teslimat hızıydı, ve ödeme planı şuydu’ diyebilmek, her şeyi mükemmel yapmaya çalışmaktan daha olgun bir cevaptır.",
        "terms": [
            {
                "en": "blast radius",
                "tr": "blast radius",
                "definition": "Bir arıza ya da hatanın etkileyebileceği bileşen ve kullanıcı kapsamı."
            },
            {
                "en": "shadowing",
                "tr": "shadowing",
                "definition": "Yeni mantığı gerçek trafikte çalıştırıp sonucunu etkisiz biçimde eskisiyle karşılaştırma."
            },
            {
                "en": "feature flag",
                "tr": "feature flag",
                "definition": "Bir davranışı kod dağıtmadan açıp kapatmayı sağlayan yapılandırma anahtarı."
            },
            {
                "en": "change data capture (CDC)",
                "tr": "change data capture (CDC)",
                "definition": "Veritabanındaki değişiklikleri akış olarak diğer sistemlere aktarma tekniği."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
