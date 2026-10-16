# Fonksiyonları birleştir: küçük adımlar, açık sonuçlar
# Bir teklifin son fiyatını hesaplamak ve bütçeye uyup uymadığını kontrol etmek iki ayrı iştir. Bu işleri küçük fonksiyonlara ayırıp birleştireceksin. Aynı tasarım, agent’ın bir ürünü kullanıcı isteğiyle eşleştirmesini de daha anlaşılır ve savunulabilir yapar.

# 1. Büyük işi küçük sorulara ayır
# “Bu ürün alınabilir mi?” sorusu birden fazla kararı içerir. Önce indirimi uygularsın; sonra yeni fiyatı bütçeyle karşılaştırırsın. Her adımı ayrı bir fonksiyona vermek, neyin nerede hesaplandığını görünür kılar.

# Ürün fiyatı (54.50 USD) -> İndirim sonrası fiyat (49.50 USD) -> Bütçe kontrolü (True / False)

# Her kutu ayrı bir işi temsil eder. Bir fonksiyonun adı, o tek işi anlatmalıdır. “Hesapla, kontrol et, yazdır, kaydet” gibi birkaç işi tek gövdede toplamak neyi test edeceğini ve hata çıktığında nerede arayacağını zorlaştırır.

# 2. Fonksiyon sözleşmesi (function contract)
# Sözleşme, fonksiyonun ne beklediğini ve ne vereceğini kısa biçimde tanımlar. Bu derste bunu yorum satırlarında ifade edeceğiz. Type hints, docstring standardı ve otomatik doğrulama daha sonra gelecek.

# Soru	                            | Örnek yanıt
# Bu fonksiyon ne yapar?	            | İndirim sonrası fiyatı hesaplar.
# Hangi girdileri bekler?	            | Fiyat ve indirim; ikisi de USD cinsinden sayı.
# Ne döndürür?	                    | İndirim düşülmüş yeni fiyat.
# Yan etkisi (side effect) var mı?	| Hayır. Ekrana yazmaz ve aldığı veriyi değiştirmez.

# İkinci fonksiyonun sözleşmesi farklıdır: fiyatı ve bütçeyi alır, bütçeye uyup uymadığını True veya False olarak döndürür. Sözleşme, kullanıcının “her şeyi önceden bilmesi” değildir; fonksiyon sınırını açıkça anlatmaktır.

# 3. Fonksiyonları birleştir (compose)
# İlk fonksiyon indirimli fiyatı hesaplar. İkinci fonksiyon bir fiyatın bütçeye uyup uymadığını döndürür. Üst düzeydeki can_buy_after_discount() ilk fonksiyonun sonucunu ikincisine verir.
def apply_discount(price_usd, discount_usd):
    return price_usd - discount_usd


def is_within_budget(price_usd, budget_usd):
    return price_usd <= budget_usd


def can_buy_after_discount(price_usd, discount_usd, budget_usd):
    final_price = apply_discount(price_usd, discount_usd)
    return is_within_budget(final_price, budget_usd)


price_after_discount = apply_discount(54.50, 5.00)
can_buy = can_buy_after_discount(54.50, 5.00, 50.00)

print(price_after_discount)
print(can_buy)
# Terminal Çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/agent_offer_pipeline.py
# 49.5
# True
# Beklenen çıktı 49.5 ve True. Değer akışı:
# apply_discount(54.50, 5.00) 49.50 döndürür -> is_within_budget(49.50, 50.00) True döndürür -> can_buy True olur
# Bu, fonksiyon bileşimidir (function composition): bir fonksiyonun dönüş değeri başka bir fonksiyonun girdisi olur. Kodda bunu açıkça bir ara değişkene atadık; böylece her adımı gözlemek ve hata ayıklamak kolaylaşır.

# Tahmin et: Bütçeyi 49.00 yaparsan indirimli fiyat ve can_buy ne olur?
# Cevabım: Bütçeyi 49.00 yaparsak indirimli fiyat değişmez yine 49.50 olur fakat can_buy false olur çünkü indirimli fiyat yeni bütçeyi aşar.

print("--------------------------------------")

# 4. Hesaplama ile yan etkiyi (side effect) ayır
# Bir fonksiyon yalnızca girdilerinden bir sonuç hesaplayıp döndürüyorsa dışarıda gözle görülen bir değişiklik yapmaz. Aynı girdilerle aynı sonucu verir ve test etmek kolaydır. Bu basit özelliklere sahip fonksiyonlara saf fonksiyon (pure function) denir.

# apply_discount() saf fonksiyona örnektir: fiyat ve indirim alır; bir sayı döndürür; ekrana yazmaz; global bir değişkene bağlı değildir.

# print() ise ekranda çıktı oluşturduğu için gözlemlenebilir bir yan etki yapar. Bu her zaman kötü değildir. Programın sonucu kullanıcıya göstermesi gerekir; yalnızca bu işi hesaplama fonksiyonunun içine karıştırmamak çoğu zaman daha kullanışlıdır.

# Hesaplama: değeri döndürür.
discounted_price = apply_discount(54.50, 5.00)

# Sunum: sonucu ekrana yazar.
print("İndirimli fiyat: ", discounted_price)
# Terminal Çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/agent_offer_pipeline.py
# İndirimli fiyat: 49.5
#
# “Saf” demek “her projede zorunlu” demek değildir.
# Dosya yazmak, log kaydetmek veya ağ isteği göndermek gibi işler doğal olarak yan etki taşır.
# Bu derste amaç, yan etkileri tanımak ve iş kuralını mümkün olduğunca onlardan ayrı tutmaktır.

# Gizli bağımlılıktan kaçın
# Bir fonksiyonun bütçeyi dışarıdaki bir değişkenden gizlice okuması, girdilerini çağrıdan anlamayı zorlaştırır.
# Gerekli veriyi parametreyle vermek sözleşmeyi görünür yapar.
# Açık bağımlılık:
is_within_budget(49.50, 50.00)

# Gizli bağımlılık örneği:
budget_usd = 50.00


def is_within_current_budget(price_usd):
    return price_usd <= budget_usd


# İkinci biçimde hangi bütçenin kullanılacağını çağrıdan göremezsin.
# Global kapsamı henüz derinlemesine işlemiyoruz;
# burada yalnızca fonksiyonun ihtiyaç duyduğu veriyi açıkça argüman olarak verme alışkanlığını kuruyoruz.

print("---------------------------")

# 5. Yeni problem laboratuvarı: agent teklif akışı
request = {
    "color": "green",
    "size": 36,
    "budget_usd": 60.00,
}

product_1 = {
    "merchant": "kardeşler kundura",
    "color": "green",
    "size": 36,
    "price_usd": 80.00,
    "discount_usd": 20.00,
}

product_2 = {
    "merchant": "kardeşler kundura",
    "color": "green",
    "size": 35,
    "price_usd": 70.00,
    "discount_usd": 10.00,
}

product_3 = {
    "merchant": "kardeşler kundura",
    "color": "green",
    "size": 36,
    "price_usd": 100.00,
    "discount_usd": 20.00,
}


def final_price(offer):
    return offer["price_usd"] - offer["discount_usd"]


def is_match(offer, request):
    return (
        (final_price(offer) <= request["budget_usd"])
        and (offer["color"] == request["color"])
        and (offer["size"] == request["size"])
    )


teklif_1 = is_match(product_1, request)
teklif_2 = is_match(product_2, request)
teklif_3 = is_match(product_3, request)

print("1. Teklif:", final_price(product_1), " Eşleşti mi? ", teklif_1)
print("2. Teklif:", final_price(product_2), " Eşleşti mi? ", teklif_2)
print("3. Teklif:", final_price(product_3), " Eşleşti mi? ", teklif_3)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/agent_offer_pipeline.py
# 1. Teklif: 60.0  Eşleşti mi?  True
# 2. Teklif: 60.0  Eşleşti mi?  False
# # 3. Teklif: 80.0  Eşleşti mi?  False

# budget_usd'ı 59.99 yaptıktan sonra Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/agent_offer_pipeline.py
# 1. Teklif: 60.0  Eşleşti mi?  False
# 2. Teklif: 60.0  Eşleşti mi?  False
# 3. Teklif: 80.0  Eşleşti mi?  False

# 6. Geçiş kapısı

# 1. Tek bir büyük fonksiyonda hata çıktığında nerede arayacağımızı bulmak zordur. Küçük fonksyionlara böldüğümüzde ise bir sorun varsa (örneğin indirim mi yanlış hesaplandı, yoksa beden mi tutmadı) hatanın tam olarak hangi fonksiyondan kaynakladığını nokta atışı görebiliriz, 2.si ise okunabilirlikte ve neyin nerede hesaplandığını görünür kılar. Fonksiyonun adı tek bir işi anlatır, farklı işler birbirine karışmaz. kodun ne yaptığı dışarıdan bakıldığında hemen anlaşılır.

# 2. Fonksiyon sözleşmesi fonksiyonun ne beklediğini ve ne vereceğini kısa biçimde tanımlar. "Bu fonksiyon ne yapar?", "Hangi girdileri bekler?", "Ne döndürür?", "Yan etkisi (side effect) var mı?" gibi soruları cevaplar.

# 3. final_price'ın dönüş değeri is_match() içinde adeta bir argümanmış gibi kullanılır, return ile döndürülen değer is_match fonksiyonuna girdi olarak girer. Buna fonksiyon birleşimi (composition) denir.

# 4. saf fonksiyonlar dışarıya hiçbir şey yapmadan bütün işi fonksiyonda halleder mesela final_price bir pure function'dır. print ile kullanıcıya bir etki gösterdiğimiz için bunu yan etki olarak adlandırır. Yani print() fonksiyonun kendi iç dünyasından çıkıp dış dünyada (terminal/konsol ekranlarında) gözlemlenebilir fiziksel bir değişiklik yaratır.

# 5. Saf fonksiyon kendi iç dünyasında gerekli tüm işlemleri yapmasıyla belli olur, fonksiyonun dışına çıkmaz. Aynı girdiler verildiği her zaman aynı çıktıyı üretir (öngörülebilirdir). Hiçbir yan etkisi yoktur. Hayır, şart değildir. Ekrana çıktı vermek, veritabanına sipariş kaydetmek vb. yan etkilidir.
# Düzeltme: Saf fonksiyon “bütün işi kendi içinde halleder” demek değildir. Temel fikir, girdilerinden sonuç hesaplayıp return ile vermesi; ekrana yazma, dosyaya kaydetme veya dış durumu değiştirme gibi gözlemlenebilir bir yan etki (side effect) yapmamasıdır. Aynı girdilerle aynı sonucu üretmesi de önemli bir özelliğidir.

# 6. Fonksiyonu bağımsızlık kılar, dışarıdaki değişkenin adının değişmesinden veya yanlışlıkla silinmesinden etkilenmez. Fonksiyonu çağıran kişi, fonksiyonun çalışmak için neye ihtiyacı olduğunu parantez içine bakarak açıkça görür. Başka bir dosyaya taşındığında da bağımsız bir şekilde tak-çalıştır olarak çalışmaya devam eder.
# Düzeltme: 6. yanıtın doğru yönde, ama “başka dosyaya taşınınca tak-çalıştır olur” kısmı garanti değildir. Gereken verileri argüman olarak vermek fonksiyonun girdilerini görünür kılar, test etmeyi ve yeniden kullanmayı kolaylaştırır. Yine de fonksiyonun çalışması, aldığı verinin beklenen biçimde olmasına ve diğer bağımlılıklarına bağlıdır.

# 7. Bütçe kullanıcının ödemeye razı olduğu üst sınırdır. <= yerine < kullansaydık, bütçemiz 60 usd iken 60 usdlik bir ürün karşımıza çıksaydı bu bütçemize uymuyor diyerek hatalı şekilde reddederdik.

# 8. Eğer sorun fiyatın yanlış hesaplaması ile ilgiliyse doğrudan final_price() fonksiyonuna bakılır. Eğer yanlış ürün seçildiyse is_match() fonksiyonundaki mantıksal ifadelere (and kısımlarına) bakılır.

# 9. Kendime puanım 5.
