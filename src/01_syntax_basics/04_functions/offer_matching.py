# Fonksiyonlar (functions): işi adlandır, tekrar kullan
# Bir ürünün bütçeye uyup uymadığını farklı fiyatlarda tekrar tekrar kontrol etmen gerekebilir. Fonksiyon, bir işi adlandırılmış ve yeniden çağrılabilir bir parçaya dönüştürür.

# 1. Fonksiyon zihinsel modeli
# Fonksiyonu küçük bir görev makinesi gibi düşünebilirsin: çağrıldığında girdileri alır, gövdesindeki (body) talimatları çalıştırır ve gerekiyorsa bir değer döndürür.

# Argümanlar (price=54.50, budget=60) -> Fonksiyon (parametreleri bağla gövdeyi çalıştır) -> Dönüş değeri (True)

# Bir fonksiyonun her çağrısı, tanımladığın işi aynı kurallarla tekrar uygular.
# İşlevin adı ne yaptığını söyler; parametreler hangi veriye ihtiyaç duyduğunu gösterir.

print("-------------------------------------------------")


# 2. Fonksiyon tanımla ve çağır
# def anahtar sözcüğü bir fonksiyon tanımlar. Satırın sonundaki iki nokta ve girintili gövde, Python’ın kod bloğunu tanımasını sağlar.


def show_offer_status():
    print("Teklif kontrol edildi")


print("Program başladı")
show_offer_status()
show_offer_status()
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/offer_matching.py
# Program başladı
# Teklif kontrol edildi
# Teklif kontrol edildi

# Önce Program başladı, sonra aynı mesaj iki kez yazdırılır. Fonksiyon tanımı tek başına gövdeyi çalıştırmaz; çağrı (call) yaptığında çalıştırır.

# Tahmin et: Dosyada yalnızca def show_offer_status(): ve girintili print(...) satırı olsaydı, fonksiyon çağrısı olmadan mesaj görünür müydü?
# Cevabım: Hayır görünmezdi, def show_offer_status(): sadece fonksiyonu tanımlar, aslında tıpkı bir değişken tanımlamak gibidir, eğer o fonksiyon çağırılmazsa, fonksiyon çalışmaz.

# İsim seçimi
# Fonksiyon adları genellikle küçük harfli kelimeler ve alt çizgiyle yazılır: show_offer_status. Ad, yapılan işi anlatmalıdır. do_thing gibi belirsiz adlar kodu anlamayı zorlaştırır.

print("-------------------------------------------------")

# 3. Parametre (parameter) ile argüman (argument)
# Tanımda parantez içine yazdığın ad parametredir. Çağrıda bu parametreye verdiğin gerçek değer argümandır.


def is_within_budget(price_usd, budget_usd):
    return price_usd <= budget_usd


first_result = is_within_budget(54.50, 60.00)
second_result = is_within_budget(72.00, 60.00)

print(first_result)
print(second_result)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/offer_matching.py
# True
# False
#
# Tanımdaki price_usd ve budget_usd parametredir.
# 54.50, 72.00 ve 60.00 çağrılarda aktarılan argümanlardır.
# İlk sonuç True, ikincisi False olur.
#
# Tanım (definition): def is_within_budget(price_usd, budget_usd): Parametre adlarını ve yapılacak işi kurar.
# Çağrı (call): is_within_budget(54.50, 60.00) Argümanları parametrelerle eşleştirir ve gövdeyi çalıştırır.
#
# Değerleri sırayla verince ilk argüman ilk parametreye, ikinci argüman ikinci parametreye bağlanır. Anahtar sözcük argümanları (keyword arguments) adları görünür kılar:
#
# print(is_within_budget(price_usd=54.50, budget_usd=60.00))
# Bu çağrı da True döndürür. Parametre adını yanlış yazarsan Python genellikle TypeError verir. Parametrelerin sırası, anlamı değiştirebileceği için çağrıyı dikkatle oku.

# print(is_within_budget(budget_ud=60.00, price_usd=54.50)) # TypeError: is_within_budget() got an unexpected keyword argument 'budget_ud'. Did you mean 'budget_usd'?

print("-------------------------------------------------")


# 4. return ile print() aynı şey değildir
# print() bir bilgiyi ekrana yazar. return ise fonksiyonun sonucunu çağıran koda verir; bu sonuç değişkene atanabilir, karşılaştırılabilir veya başka bir fonksiyona aktarılabilir.
def calculate_discounted_price(price_usd, discount_usd):
    discounted_price = price_usd - discount_usd
    return discounted_price


final_price = calculate_discounted_price(54.50, 5.00)
print(final_price)
print(final_price <= 60.00)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/offer_matching.py
# 49.5
# True
# Beklenen çıktı 49.5 ve True. Fonksiyon sonucu döndürdüğü için program bu değeri başka bir hesapta kullanabilir.


# Aynı işi yalnızca yazdıran bir fonksiyonla karşılaştır:
def show_discounted_price(price_usd, discount_usd):
    discounted_price = price_usd - discount_usd
    print(discounted_price)


result = show_discounted_price(54.50, 5.00)
print("Fonksiyonun sonucu:", result)
# Terminal Çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/offer_matching.py
# 49.5
# Fonksiyonun sonucu: None
#
# İlk satır 49.5 yazar; ikinci satır Fonksiyonun sonucu: None yazar. Çünkü ilk fonksiyon ekrana yazdırdı, fakat bir değer döndürmedi. Açık bir return yoksa fonksiyon None döndürür.
#
# Kolay karışan nokta: Bir fonksiyonun ekrana bir şey yazması, o değeri çağırana verdiği anlamına gelmez.
# Sonucu başka kodda kullanacaksan return gerekir.
# Python öğreticisi de return olmadan fonksiyonun None döndürdüğünü belirtir.

print("-------------------------------------------------")


# 5. Parametreler ve yerel değişkenler (local variables)
# Fonksiyon içinde tanımlanan parametre ve değişkenler, normalde o fonksiyonun yerel kapsamındadır (local scope). Fonksiyon çağrısı sırasında kullanılabilirler. Bu derste kapsamı yalnızca temel düzeyde inceliyoruz; LEGB kuralı ve kapsamın ayrıntıları daha sonra gelecek.
def make_offer_label(product_name):
    label = product_name + " offer"
    return label


label = make_offer_label("Willow Ballet Flat")
print(label)
# print(product_name)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/offer_matching.py
# Willow Ballet Flat offer
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\04_functions\offer_matching.py", line 116, in<module>
#     print(product_name)
#           ^^^^^^^^^^^^
# NameError: name 'product_name' is not defined
#
# İlk çıktı Willow Ballet Flat offer olur. Son satır ise NameError üretir: product_name fonksiyon içindeki bir parametredir; dışarıda bu adla değişken tanımlamadık.
# Fonksiyondan dışarı çıkması gereken sonucu return ile döndürürüz; fonksiyonun içindeki her adı dışarı açmayız.
#
# Tahmin et: label fonksiyon dışında neden yazdırılabiliyor da product_name yazdırılamıyor?
# Cevabım: Çünkü dışarıdaki label değişkenine fonksiyonun return değerini atadık, product_name sadece bir parametre ve çağrı bittikten sonra bu kapsamın dışından adıyla erişilemez.

print("-------------------------------------------------")

# 6. Yeni problem laboratuvarı: agent teklif eşleştirme fonksiyonu
# Bir agent’ın arama servisi ürün sözlükleri ve kullanıcı isteği alıyor. Bir fonksiyon, teklifin renk, beden ve bütçe koşullarına uyup uymadığını değerlendirsin.

request = {
    "color": "green",
    "size": 36,
    "budget": 60.00,
}

bid_one = {
    "color": "red",
    "size": 36,
    "price": 60.00,
}

bid_two = {
    "color": "green",
    "size": 36,
    "price": 60.00,
}

bid_three = {
    "color": "green",
    "size": 36,
    "price": 70.00,
}


def matches_request(offer, request):
    result = (
        (offer["color"] == request["color"])
        and (offer["size"] == request["size"])
        and (offer["price"] <= request["budget"])
    )
    return result


teklif_bir = matches_request(bid_one, request)
teklif_iki = matches_request(offer=bid_two, request=request)
teklif_uc = matches_request(bid_three, request)
parametreli_teklif_uc = matches_request(request=request, offer=bid_three)

print(
    "Teklif 1: ", teklif_bir
)  # False verir çünkü bid_one'daki color request'teki renge uymuyor.
print("Teklif 2: ", teklif_iki)  # True verir çünkü bid_two ile request tam uyumlu
print(
    "Teklif 3: ", teklif_uc
)  # False verir çünkü bid_three'nun price budget'dan büyük, küçük veya eşit değil.
print(
    "Teklif 3 (parametreli hali): ", parametreli_teklif_uc
)  # False verir çünkü doğru parametreyi doğru argümanla eşleştirdik.
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/offer_matching.py
# Teklif 1:  False
# Teklif 2:  True
# Teklif 3:  False
# Teklif 3 (parametreli hali):  False


# 7. Geçiş kapısı

# 1. Fonksiyon tanımı bir fonksiyonu tanımlamak için yazılan def ile başlayan ardından fonksiyonun işlevini anlat küçük harfli ve altçizgi(_) kullanarak oluşturulan ad ve fonksiyonun iş mantığında kullanacak olan parametrelerin yazıldı ve bu fonksiyonun içindeki iş mantığının belirlendiği yerdir. Fonksiyon çağrısı ise tanımlanan fonksiyonu kullanmak için çağırılmasıdır. birisi fonksiyonu tanımlar diğeri çalıştırır.

# 2. Parametre fonksiyon tanımlama sırasında fonksiyonun hangi değerleri istediğini belirten parantez içerisinde yazılan değerlerdir. Argümanlar ise fonksiyon çağırıldığında (function call) fonksiyona verilmek istenen parametrelerin istediği o değerlerdir. örneğimde: def matches_request(offer, request): fonksiyon tanımlamasında bulunan offer ve request birer parametredir. teklif_bir = matches_request(bid_one, request)'de bulunan bid_one ve request birer argümandır.

# 3. konumsal argümanlar sırası ile bağlanabilir, ama eğer  parametre isimleriyle çağrılırsa o zaman konumun önemi kalmaz, argüman olarak kullanılan iki değerin hangi parametre tarafından seçilmesi gerektiğini fonksiyon anlar.

# 4. print() sadece içine yazılan değeri terminale yazdırmaya yarar, başka bir değişkene değer vermez. return ise fonksiyonun iş mantığının sonucunda dış dünyaya hangi değeri vereciğimizi yazarız bu sayede bir fonksiyon çalıştırıp sonucunu dışarından alıp başka işlemler yazdırabiliriz.

# 5. Kural şudur: Açık return satırı olmayan fonksiyon None değerini döndürür. Çağrılan her fonksiyon geriye mutlaka bir değer döndürmek zorundadır.

# 6. Çünkü fonksiyon içindeki parametreye sadece fonksiyonun içinden erişilebilir, fonksiyonun iş mantığı bittiği an parametreler unutulur, tekrar fonksiyon çağırılana dek bilinmez.
# Düzeltme: 6. yanıt: Parametre adı, fonksiyon çağrısı sürerken yerel kapsamda kullanılabilir; çağrı bitince bu ada fonksiyonun dışından erişemezsin. Ancak argüman olarak verdiğin nesne “unutulmaz”: Örneğin bid_three, fonksiyon çağrısından sonra da değişken olarak duruyor.

# 7. Fonksiyonun her zaman aynı performansı verip vermeyeceğini kontrol edebiliriz. İyi hazırlanmış bir fonksiyon standart cevap kalitesine sahip olmalıdır. Bize bu yararı sağlar.
# Düzeltme: 7. yanıt: Fonksiyon kullanmanın temel faydası performans garantisi vermek değil. Aynı işi kopyalamadan tekrar kullanmak, davranışı tutarlı tutmak ve değişiklik gerektiğinde tek yerde düzenleme yapabilmektir. Ayrıca fonksiyonu ayrı ayrı sınayabilirsin.

# 8. Eksik zorunlu argümanla çağrı yaparsan TypeError alırsın. Function call sırasında parametre sayısında argüman verilmesi gerekir.

# 9. Kendime puanım 5


# print("--------")
# deneme = matches_request(request,)
# print(deneme) # TypeError: matches_request() missing 1 required positional argument: 'request'
