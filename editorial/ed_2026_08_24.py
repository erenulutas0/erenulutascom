"""24 Ağustos 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-08-24"

INTRO = "Meta'dan iki yazı, aynı sorunun iki yüzü: yapay zekâ eğitiminde darboğaz hesap değil iletişim. Biri çipin içine ağı gömüyor, diğeri ağ protokolünü baştan yazıyor. Donanım yazıları gibi görünse de içlerindeki fikir yazılımcılar için de geçerli."

DRAFTS = [
    {
        "url": "https://engineering.fb.com/2026/08/24/networking-traffic/mtia-300-meta-training-chip-built-in-nics/",
        "slot": "cover",
        "title_tr": "İletişimi birinci sınıf vatandaş yapmak: ağı çipin içine gömen MTIA 300",
        "difficulty": "ileri",
        "tags": [
            "hardware",
            "ML infrastructure",
            "networking",
            "distributed training"
        ],
        "summary": "MTIA 300, Meta'nın kendi geliştirdiği eğitim ve inference hızlandırıcı ailesinin, **sıralama ve öneri modellerini eğitmeye** göre optimize edilmiş ilk üyesi. Yazının çıkış noktası şu gözlem: öneri modelleri büyük dil modellerinden farklı olarak devasa kayan nokta işlem gücüne değil, **hızlandırıcılar arası hızlı ve verimli iletişime** muhtaç. Gömme tabloları (embedding tables) modelin parametrelerinin %99'undan fazlasını tutabiliyor; bu da yüzlerce hızlandırıcı arasında sık AllReduce, AllToAll ve AllGather işlemleri gerektiriyor.\n\nGPU'larda bu iletişim işlemleri (NCCL gibi kütüphanelerle) eğitim hesabıyla **aynı kaynakları** (streaming multiprocessor'ları) paylaşıyor; ikisi birlikte koşunca ikisi de yavaşlıyor ve pahalı donanım boşta kalıyor. Meta'nın çözümü iki katmanlı. Birincisi: ağ arayüzünü çip paketinin içine koymak: iki ağ chiplet'i, toplam 12 adet 800 Gbps RDMA NIC ile **1,2 TB/s G/Ç bant genişliği** sağlıyor ve PCIe'ye hiç çıkmıyor. Aynı 12 NIC hem rack içi (16 node, 1 TB/s'ye kadar) hem raflar arası (200 GB/s) iletişim için esnekçe bölünebiliyor. İkincisi: iletişimi hesap ızgarasından ayırmak. Çip, 12×6'lık işlem elemanı ızgarasının yanında iletişimi bağımsız yürüten 16 ayrı **mesaj motoru** taşıyor.\n\nDonanımla birlikte yazılım da (HCCL iletişim kütüphanesi) sıfırdan, donanımla birlikte tasarlanmış.",
        "key_points": [
            "Darboğazı tanımak her şeyin başı: öneri modellerinde sorun FLOPS değil, iletişim.",
            "İletişim ve hesap aynı kaynağı paylaşırsa birbirini yavaşlatır; ayırmak ikisini de hızlandırır.",
            "Ağ yapılandırması yeniden ayarlanarak rack içi/rack arası bant dengesi donanımı değiştirmeden uyarlanabiliyor.",
            "Donanım ve iletişim kütüphanesinin birlikte tasarlanması (co-design) ana strateji."
        ],
        "why_it_matters": "Genel amaçlı donanım her iş yükünde iyi olmak zorundadır; belirli bir iş yükü için tasarım yapınca kaynak çakışmalarını mimariyle ortadan kaldırabilirsin. Bu ilke yazılımda da geçerli: hesabı ve I/O'yu aynı thread havuzunda yarıştırma.",
        "for_you": "Donanım tasarlamayacaksın ama aynı deseni bir Spring Boot servisinde tanırsın: CPU ağırlıklı işi ve ağ bekleyen işi aynı thread havuzuna koyarsan biri diğerini aç bırakır. Ayrı havuzlar (`@Async` ile ayrı executor) ya da sanal thread'ler bu ayrımı yapar. Daha genel ders: “yavaş” dediğin sistemde önce hangi kaynağın paylaşıldığını bul.",
        "terms": [
            {
                "en": "collective communication",
                "tr": "collective communication",
                "definition": "AllReduce, AllToAll gibi, birçok hızlandırıcının birlikte katıldığı veri paylaşım işlemleri."
            },
            {
                "en": "RDMA",
                "tr": "RDMA",
                "definition": "Veriyi işlemciyi yormadan bir makinenin belleğinden diğerinin belleğine taşıyan ağ tekniği."
            },
            {
                "en": "embedding table",
                "tr": "embedding table",
                "definition": "Kategorik varlıkların (kullanıcı, reklam) vektörlerini tutan büyük arama tablosu."
            },
            {
                "en": "co-design",
                "tr": "co-design",
                "definition": "Donanımı ve onu kullanan yazılımı birbirine göre aynı anda tasarlama yaklaşımı."
            }
        ]
    },
    {
        "url": "https://engineering.fb.com/2026/08/24/networking-traffic/metaroce-rdma-transport-ai-ethernet/",
        "slot": "brief",
        "title_tr": "Sıra bozukluğunu hata değil normal saymak: MetaRoCE",
        "difficulty": "ileri",
        "tags": [
            "networking",
            "protocol",
            "open source",
            "AI infrastructure"
        ],
        "summary": "Meta, yapay zekâ iş yükleri için sıfırdan tasarlanmış, ticari Ethernet üzerinde çalışan bir RDMA taşıma protokolü olan **MetaRoCE**'yi tanıttı ve spesifikasyonunu, referans yazılım uygulamasını ve uyumluluk test paketini Open Compute Project'e açtı.\n\nStandart RoCE ağın her çerçeveyi **sırayla** teslim etmesini bekler ve bunun için PFC gibi mekanizmalara dayanır; bu da çok düzlemli büyük ağlarda performans getiren packet spraying’i (packet spraying) caydırır. MetaRoCE'nin temel fikri tek cümlede: **“Ağ paketleri görür, NIC niyeti görür.”** Zekâyı anahtarlardan uca (NIC'e) taşıyor. Paketler birçok yol üzerinden serpiştiriliyor ve **sırasız varış tasarım gereği normal**; her paket kendi hedef adresini taşıdığı için veri doğrudan son bellek konumuna yazılıyor.",
        "key_points": [
            "Ağ sırayı garanti etmek zorunda değilse, ağ çok daha basit ve çok yollu çalışabilir.",
            "Yol başına gerçek zamanlı telemetri (RTT, ECN, doluluk) uç noktada toplanıp rota kararına dönüşüyor."
        ],
        "for_you": "‘Sırasız gelmesini normal say’ fikri distributed yazılımda da çok kullanışlı: message queue’larda sırayı garanti etmek pahalıdır; consumer’larını **idempotent** ve sıradan bağımsız yazarsan sistem hem ölçeklenir hem basitleşir. Olayları timestamp’le sıralayıp geç gelenleri doğru yere yerleştirmek, sıralı teslimata güvenmekten daha sağlamdır.",
        "terms": [
            {
                "en": "packet spraying",
                "tr": "packet spraying",
                "definition": "Bir bağlantının paketlerini birden fazla yol üzerinden dağıtarak ağı daha verimli kullanma."
            },
            {
                "en": "out-of-order delivery",
                "tr": "out-of-order delivery",
                "definition": "Paketlerin gönderildikleri sırayla değil, farklı sırayla varması."
            },
            {
                "en": "ECMP",
                "tr": "ECMP",
                "definition": "Aynı hedefe giden birden çok eşit yol arasında trafiği dağıtan yönlendirme tekniği."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
