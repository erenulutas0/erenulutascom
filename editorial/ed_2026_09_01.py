"""1 Eylül 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-09-01"

INTRO = "Agent geliştiriyorsan bu yazın en önemli protokol haberi: MCP, çıkışından bu yana en büyük revizyonuyla stateless (stateless) oldu. Yani “sticky session” ve ortak oturum deposu ihtiyacı protokol seviyesinde ortadan kalktı."

DRAFTS = [
    {
        "url": "https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/",
        "slot": "cover",
        "title_tr": "MCP stateless oldu: sticky session, oturum deposu ve load balancer ayarlarını silebilirsin",
        "difficulty": "orta",
        "tags": [
            "MCP",
            "agent",
            "architecture",
            "scaling"
        ],
        "summary": "28 Temmuz 2026'da MCP, çıkışından bu yana **en büyük revizyonunu** yayımladı ve protokol çekirdeğini stateless hâle getirdi. `initialize` handshake ve istemcinin sonraki her istekte geri yollamak zorunda olduğu `Mcp-Session-Id` başlığı kalktı. Artık her istek kendi protokol sürümünü ve istemci bağlamını taşıyor; istemcinin ilk mesajı doğrudan araç çağrısı olabiliyor ve **herhangi bir sunucu örneği** cevaplayabiliyor. İstemci sunucunun neleri desteklediğini önceden öğrenmek isterse yeni `server/discover` metodu tek cevapta protokol sürümlerini, yetenekleri ve kimliği dönüyor.\n\nAWS açısından önemi: eski tasarım yatay ölçeklemeyle çatışıyordu. Oturum, onu başlatan örnekte yaşıyordu; birden fazla örnek çalıştırmak ya istemcileri **sticky routing** ile sabitlemek ya da session state’i ortak bir depoya taşımak demekti. İkisi de o protokol için doğruydu; yeni protokolde ikisi de gereksiz. Yazının analojisi güzel: eski protokolde sunucu yüzünüzü hatırlayan bir vale gibiydi (hep aynı valeyle muhatap olmak zorundaydınız); yeni protokolde **numaralı bilet** alıyorsunuz ve herhangi bir görevli yardım edebiliyor.\n\nMimari değişimler: ALB sticky ayarları yerine düz round-robin; DynamoDB ya da ElastiCache oturum deposu yerine sunucunun ürettiği ve araç argümanı olarak taşınan tanımlayıcılar; gövde ayrıştırmadan `Mcp-Method` ve `Mcp-Name` başlıklarıyla yönlendirme ve hız sınırlama; Lambda için “istek gelir, cevap gider” doğal uyumu; araç listeleri için `ttlMs` ve `cacheScope` ile yerleşik cache; W3C Trace Context ile distributed tracing; ve akış devam ettirme (`Last-Event-ID`) yerine **idempotent araçlar**: kopan çağrıyı istemci tekrar gönderiyor.\n\nÖnemli bir uyarı: **eski istemcilere hizmet veriyorsan altyapıyı silme.** Spesifikasyon eski istemciler için geriye uyumlu bir hat taşıyor; sticky kuralları ve oturum deposu, eski sürümdeki trafik sıfıra inene kadar durmalı. Gateway'de istek başına protokol sürümünü logla, eski hat için bir kapatma tarihi koy.",
        "key_points": [
            "Stateless protokol yatay ölçeklemeyi bedavaya getirir: durumu istemciye ya da isteğin kendisine taşırsan her örnek her isteğe bakabilir.",
            "“Stateless” protokol demektir, uygulamanın durumsuz olduğu anlamına gelmez: durum varsa sunucunun ürettiği tanımlayıcıyla taşınır.",
            "Sunucu artık istemciye çağrı ortasında geri istek (onay, örnekleme) atamıyor; bunun yerine `input_required` sonucu ve `requestState` belirteciyle çok turlu istek akışı (MRTR) kullanılıyor.",
            "Yeniden deneme güvenliği için araçları idempotent yaz: kopan çağrı güvenle tekrarlanabilmeli.",
            "Göç sırası: önce protokol sürümünü logla, eski trafik bitince altyapıyı kaldır."
        ],
        "why_it_matters": "Durum, ölçeklemenin en pahalı düşmanıdır. Bir protokol ya da servis durumu istemciye itebiliyorsa, ona ait hiçbir altyapıyı (sticky yönlendirme, ortak depo, oturum temizleme işi) işletmek zorunda kalmazsın. Bu, HTTP'nin kendisinin neden başarılı olduğunun da özeti.",
        "for_you": "Kendi MCP server’ını yazarsan baştan stateless tasarla; Spring Boot’ta bu, `HttpSession` kullanmamak ve her isteği bağımsız ele almak demek. Aynı ilke bugünkü tüm servislerin için bir kontrol: `HttpSession` ya da yerel bellekte tuttuğun her şey, ikinci bir instance açtığın an sorun olur. İkinci pratik beceri **idempotency**: ödeme, abonelik ya da kayıt oluşturan her endpoint’e istemcinin ürettiği bir `Idempotency-Key` kabul ettir; aynı key ikinci kez gelirse işlemi tekrarlama, ilk sonucu dön.",
        "terms": [
            {
                "en": "stateless protocol",
                "tr": "stateless protocol",
                "definition": "Her isteğin kendi başına işlenebildiği, sunucunun önceki istekleri hatırlamasına gerek olmayan protokol."
            },
            {
                "en": "sticky session",
                "tr": "sticky session",
                "definition": "Load balancer’ın bir istemciyi hep aynı sunucu örneğine yönlendirmesi."
            },
            {
                "en": "idempotency",
                "tr": "idempotency",
                "definition": "Aynı isteğin birden çok kez işlenmesinin, bir kez işlenmesiyle aynı sonucu vermesi."
            },
            {
                "en": "W3C Trace Context",
                "tr": "W3C Trace Context",
                "definition": "Dağıtık sistemlerde bir isteğin servisler arasında izlenebilmesi için standart başlık biçimi."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
