"""9 Ekim 2026 sayısı."""

from pipeline.compose import save_edition

DATE = "2026-10-09"

INTRO = "1 Ekim’de Cloudflare’in decision model Clef’i okumuştun; bir hafta sonra ses ve video da alan sürümü geldi. Yazının ilginç kısmı duyuru değil, eğitim tarifi: omurgayı dondur, küçük adaptörler eğit, olasılıkları kalibre et. Yanında bir satın alma haberi ve ‘platform kilidi’ tartışması var."

DRAFTS = [
    {
        "url": "https://blog.cloudflare.com/clef-faster-cheaper-multimodal/",
        "slot": "cover",
        "title_tr": "Ses ve video için ayrı model zinciri kurma: Clef-omni ve arkasındaki eğitim tarifi",
        "difficulty": "orta",
        "tags": [
            "LLM",
            "multimodal",
            "fine-tuning",
            "open source"
        ],
        "summary": "Cloudflare, geçen hafta yayımladığı açık ağırlıklı karar modelleri Clef ve Clef-flash’ın ardından **Clef-omni**’yi duyurdu: metin ve görselin yanında ses (wav, mp3) ve video (mp4, webm) girdisi alan bir decision model. Aynı yazıda Clef-flash’ın fiyatı düşürüldü ve Clef hızlandırıldı. Ağırlıklar Hugging Face’te açık.\n\nPratik fark şu: konuşmayı önce metne çeviren, videoyu ses ve görüntü kanallarına ayıran **ardışık model zincirleri** kurmak yerine tek bir modele soruyorsun. Yazıdaki örnek bir kurulum denetimi: cihazın bir fotoğrafı, çalışırken alınmış bir ses kaydı ve fanın bir videosu tek istekte gönderiliyor; sorular şema olarak veriliyor (‘etiket fotoğrafta görünüyor mu’, ‘cihaz takırtısız çalışıyor mu’, ‘fan dönüyor mu’) ve her biri tipli bir cevap alıyor.\n\nMimari tarafı öğretici. Clef-omni, zaten metin, görsel, ses ve video işleyebilen Qwen3-Omni-30B-A3B-Instruct adlı bir **mixture of experts (MoE) (MoE)** modelin üzerine kurulu. Clef modelleri çıktı token’ı üretmediği için (LLM gibi metin yazmıyorlar) gelen dosyaları yazıya dökme ya da altyazılama maliyeti ortadan kalkıyor; medya ögeleri doğrudan tek bir dizinin içine yerleşiyor.\n\nEğitim tarifi Clef ile aynı: **omurga donduruluyor**, yalnızca **düşük ranklı adaptörler (LoRA)** eğitiliyor ve standart son-eğitim yaklaşımı uygulanıyor: **etiket yumuşatmalı çapraz entropi** kaybı ile **Brier puanı calibration’ı** birlikte. Calibration bir decision model için kritik: ‘%90 eminim’ dediği kararların gerçekten yaklaşık %90’ı doğru çıkmalı. Yazıya göre yalnızca metin içeren kararlar medyanda yaklaşık 130 ms’de dönüyor. Bir not daha: Clef’in ilk sürümü bir cuma akşamı karar verilip hafta sonu eğitilmiş ve perşembe yayımlanmış.",
        "key_points": [
            "Model zinciri (ses→metin→karar) her halkada gecikme ve hata biriktirir; tek model bunu kaldırır.",
            "Omurgayı dondurup yalnızca LoRA eğitmek, büyük bir modeli günler içinde ve ucuza uyarlamayı sağlar.",
            "Decision model’de doğruluk kadar calibration önemli: güven puanı gerçek isabet oranını yansıtmalı.",
            "Çıktı token’ı üretmemek, gecikmenin en büyük kalemini ortadan kaldırır."
        ],
        "why_it_matters": "Dondurulmuş omurga + LoRA + calibration, bugün küçük bir ekibin açık bir modelden kendi işine özel bir model çıkarmasının en erişilebilir yolu. Yazı ayrıca ‘her şeyi metne çevir, sonra LLM’e sor’ alışkanlığının tek seçenek olmadığını gösteriyor.",
        "for_you": "Ses akışı olan bir uygulamada konuşmayı önce metne çevirip sonra bir LLM’e soruyorsan iki modelin gecikmesini ve iki modelin hatasını topluyorsun. Sorun bir sınıflandırma ise (telaffuz doğru mu, cümle tamamlandı mı) sesi doğrudan alan bir modeli denemeye değer. Calibration’ı da kendi modellerinde ölç: PyTorch’ta bir sınıflandırıcının tahminlerini güven aralıklarına böl (yüzde 80-90, yüzde 90-100) ve her aralıktaki gerçek isabet oranına bak. Model ‘yüzde 95 eminim’ deyip yüzde 70 tutturuyorsa eşik değerlerin anlamsızdır; temperature scaling bunu birkaç satırda düzeltir.",
        "terms": [
            {
                "en": "LoRA (low-rank adaptation)",
                "tr": "LoRA (low-rank adaptation)",
                "definition": "Modelin ağırlıklarını dondurup yalnızca küçük ek matrisleri eğiterek yapılan ucuz fine-tuning."
            },
            {
                "en": "calibration",
                "tr": "calibration",
                "definition": "Modelin bildirdiği güven olasılığının gerçek doğruluk oranıyla örtüşmesi."
            },
            {
                "en": "Brier score",
                "tr": "Brier score",
                "definition": "Tahmin edilen olasılık ile gerçek sonuç arasındaki farkın karesinin ortalaması; düşük olan iyidir."
            },
            {
                "en": "mixture of experts (MoE)",
                "tr": "mixture of experts (MoE)",
                "definition": "Her girdi için yalnızca bir kısmı çalışan alt ağlardan oluşan model mimarisi."
            },
            {
                "en": "multimodal",
                "tr": "multimodal",
                "definition": "Metin, görsel, ses ve video gibi birden çok girdi türünü birlikte işleyebilen."
            }
        ]
    },
    {
        "url": "https://blog.cloudflare.com/deno-joins-cloudflare/",
        "slot": "brief",
        "title_tr": "Deno Cloudflare’e katılıyor: ‘platform kilidi’ tartışmasına bir cevap",
        "difficulty": "başlangıç",
        "tags": [
            "platform",
            "open source",
            "serverless",
            "industry"
        ],
        "summary": "Cloudflare, Deno ekibinin kendisine katıldığını duyurdu ve yazıyı yaygın bir eleştiriye cevap olarak kurdu. Eleştiri şu: Workers diğer bulut platformlarından farklı çalışıyor, özellikle Durable Objects kullanan uygulamalar yalnızca farklı yazılmıyor, farklı tasarlanıyor; dolayısıyla başka yere taşımak zor ve bu bilinçli bir tuzak. Bu bakışa göre Deno’nun ağustosta yayımladığı, Workers ve Durable Objects’in açık kaynak bir uygulaması olan `celld` bir tehditti.\n\nCloudflare’in savunması: Workers farklı çünkü daha iyi bir programlama modeli (yüzlerce konumda çalışan uygulamayı yönetmek, ‘binding’ ile dış kaynaklara hem kolay hem güvenli erişim) ve daha iyi olmak mevcut platformlarla tam uyumlu kalmayı engelliyor. Şirket, kilidin kendisine de zarar verdiğini, çıkış yolu olmasaydı büyük müşterilerin baştan gelmeyeceğini ve bu yüzden açık kaynağa yöneldiğini söylüyor. Bu bir şirketin kendi lehine yazdığı metin; iddiaları o gözle okumak gerekir.",
        "key_points": [
            "Bir platformun sunduğu özel model güç verir ama taşınabilirliği azaltır; bu bir takastır.",
            "Açık kaynak bir uyumlu uygulama, kilit riskini düşüren somut bir çıkış yoludur.",
            "Satıcının kendi yazısındaki gerekçeler tek taraflıdır; bağımsız kaynakla tartmak gerekir."
        ],
        "for_you": "Bir platform seçerken kendine şu soruyu sor: ‘buradan çıkmam gerekirse neyi yeniden yazarım?’ İş mantığını platforma özgü API’lerden ince bir arayüzle ayır (Spring’de bir `StorageService` interface’i, arkasında S3 ya da R2). Bir sağlayıcıya özel özelliği kullanmak yanlış değil; bilinçsizce her yere yaymak yanlış.",
        "terms": [
            {
                "en": "vendor lock-in",
                "tr": "vendor lock-in",
                "definition": "Bir sağlayıcıya özgü teknolojiye bağımlı kalıp başka sağlayıcıya geçmenin pahalı hâle gelmesi."
            },
            {
                "en": "Durable Objects",
                "tr": "Durable Objects",
                "definition": "Cloudflare Workers’da durum tutan, tekil ve adreslenebilir serverless nesneler."
            }
        ]
    }
]

if __name__ == "__main__":
    save_edition(DATE, INTRO, DRAFTS)
