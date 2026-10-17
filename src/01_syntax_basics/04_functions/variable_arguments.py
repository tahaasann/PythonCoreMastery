
# Değişken sayıda argümanları topla ve aç
# Bir fonksiyon bazen kaç ürün fiyatı, arama terimi veya seçenek alacağını önceden bilemez. Python, ek konumsal argümanları *args ile tuple içinde; ek anahtar sözcüklü argümanları **kwargs ile sözlük içinde toplamana izin verir. Aynı yıldızlar çağrı sırasında bir koleksiyonu argümanlara açmak için de kullanılabilir.

# Yıldızın anlamını bağlam belirler:
# Tanımda (*args) fazla konumsal argümanları toplar 
# ->
# Fonksiyonun içinde args bir tuple'dır, kwargs bir dict'tir 
# -> 
# Çağrıda (*values/**options) koleksiyondaki değerleri açar

# 1. *args: ek konumsal argümanları tuple'da topla
# Fonksiyon imzasında bir parametrenin başındaki *, o noktadan sonra gelen fazla konumsal argümanları tek bir tuple'da toplar. Yaygın ad args'tır; bu ad özel değildir. *prices veya *terms gibi amaca uygun isimler de kullanabilirsin.

def cart_subtotal(*prices_usd):
    print(prices_usd)
    print(type(prices_usd))
    return sum(prices_usd)

print(cart_subtotal(19.99, 24.50, 10.00))
print(cart_subtotal())
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# (19.99, 24.5, 10.0)
# <class 'tuple'>
# 54.489999999999995
# ()
# <class 'tuple'>
# 0
# İlk çağrıda fonksiyonun içindeki prices_usd değeri (19.99, 24.50, 10.0) olur. İkinci çağrıda boş tuple () olur; sum(()) sonucu 0 verir.
# 
# Tahmin et: cart_subtotal(12.0) içindeki prices_usd tek sayı mı, tuple mı olur? Fonksiyonun toplamı ne döndürür?
# Cevabım: tuple olur. anladığım kadarıyla parametre olarak *args verdiğimiz zaman program çalıştırılıp fonksiyon tanımlandığı anda *args gördüğü gibi otomatik olarak boş bir tuple (12.0, ) oluşturulur. Fonksiyonun toplamı 12.0 döndürür.
# DÜZELTME: Tuple her çağrıda o çağrının argümanlarından oluşur. cart_subtotal(12.0) için Python önceden boş bir tuple oluşturup içine değer eklemez; prices_usd doğrudan (12.0,) olur. Argüman gönderilmezse () olur.

# İsim sihirli değil: *args yazımındaki args, parametrenin adıdır. 
# Özel davranışı veren şey baştaki yıldızdır. 
# Bu yüzden gövdede ismi args olarak kullanmak zorunda değilsin; imzada seçtiğin ismi kullanırsın.

print("-----------------------------")

# 2. **kwargs: ek anahtar sözcüklü argümanları sözlükte topla
# İmzada bir parametrenin başındaki çift yıldız **, ayrıca tanımlanmamış anahtar sözcüklü argümanları bir sözlükte toplar. 
# Yaygın ad kwargs'tır; yine, özel olan ad değil ** sözdizimidir.
def describe_search(**filters):
    return filters

print(describe_search(color="green", size=36))
print(describe_search(country="US"))
print(describe_search())
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# {'color': 'green', 'size': 36}
# {'country': 'US'}
# {}
# Her anahtar sözcüğün adı sözlük anahtarı, gönderilen değer de o anahtarın değeri olur.
# 
# Tahmin et: describe_search(color="green", size=36) içinde filters["size"] hangi değeri verir? type(filters) ne gösterir?
# Cevabım: filters["size"] değeri 36 değerini verir. type(filters) <class 'dict'> cevabını yani bir sözlük olduğunu gösterir.
# 
# Tasarım uyarısı: **kwargs kullanınca fonksiyon çok sayıda seçeneği kabul edebilir; 
# bu, her seçeneğin geçerli olduğu anlamına gelmez. 
# Sözlüğün anahtarlarını kontrol etmek ve desteklenmeyen seçenekleri belirlemek uygulamanın sorumluluğundadır.

print("-----------------------------")

# 3. Çağrıda koleksiyonları argümanlara aç
# Fonksiyon çağrısında tek yıldız bir iterable'ın (ör. liste veya tuple) elemanlarını ayrı konumsal argümanlar olarak açar. 
# Çift yıldız bir sözlüğün anahtar-değer çiftlerini ayrı anahtar sözcüklü argümanlar olarak açar.
def show_delivery(item, country, express=False):
    return item, country, express

delivery_vaules = ("ballet flat", "US")
print(show_delivery(*delivery_vaules))

delivery_options = {"express": True}
print(show_delivery("trail shoe", "CA", **delivery_options))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# ('ballet flat', 'US', False)
# ('trail shoe', 'CA', True)
# 
# Tahmin et: colors = ["green", "olive"] iken describe_search(*colors) hangi iki argümanı yollar? Peki filters = {"size": 36} iken describe_search(**filters) nasıl çağrıya dönüşür?
# Cevabım: "green" ve "olive" argümanlarını tek bir tuple halinde yollar describe_search("green", "olive"). {"size": 36} sözlüğü şeklinde **filtersa yollar.
# Düzeltme: İlk çağrı describe_search("green", "olive") olur; bu örnekte fonksiyonun yalnızca **filters parametresi olduğu için bu iki konumsal değer kabul edilmez ve TypeError oluşur. İkinci çağrı describe_search(size=36) olur ve {"size": 36} döndürür.
# 
# Açma her imzada çalışmaz: 
# Açılan değerlerin sayısı ve adları fonksiyon imzasına uymalıdır. 
# Aynı parametreyi hem konumla hem adıyla iki kez vermek veya sözlükte eşleşmeyen anahtar kullanmak TypeError oluşturabilir.

print("-----------------------------")

# Birleşik fonksiyon imzasında yıldızları oku
def search_catalog(query, /, *terms, country="US", **preferences):
    return {
        "query": query,
        "terms": terms,
        "country": country,
        "preferences": preferences,
    }

request = search_catalog(
    "ballet flat",
    "green",
    "leather",
    country="US",
    size=36,
    include_used=False,
)

print(request)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# {'query': 'ballet flat', 'terms': ('green', 'leather'), 'country': 'US', 'preferences': {'size': 36, 'include_used': False}}
# Burada:

# query, Ders 12'deki / nedeniyle yalnızca konumsal verilir.
# terms, *terms nedeniyle ek konumsal argümanları tuple olarak toplar.
# country, *terms'ten sonra yazıldığı için anahtar sözcüklü verilir. Varsayılanı "US" olduğu için atlanabilir.
# preferences, **preferences nedeniyle kalan anahtar sözcüklü argümanları sözlük olarak toplar.
# Bu örneğin terms değeri ("green", "leather"); preferences değeri {"size": 36, "include_used": False} olur.
# +----------------+------------------------------------------+------------------------+
# | İmza Parçası   | İşlev                                    | Fonksiyon İçindeki Tür |
# +----------------+------------------------------------------+------------------------+
# | query, /       | yalnızca konumsal                        | tek değer              |
# | *terms         | fazla konumsal argümanları toplar        | tuple (demet)          |
# | country="US"   | anahtar sözcüklü, varsayılanlı           | tek değer              |
# | **preferences  | fazla anahtar sözcüklü argümanları toplar| dict (sözlük)          |
# +----------------+------------------------------------------+------------------------+
# 
# Parametre sırası için sezgi: 
# Önce zorunlu konumsal bilgi, 
# sonra *args, 
# sonra anahtar sözcüklü seçenekler, 
# en sonda **kwargs gelir. 
# Bu derste geçerli biçim def f(required, /, *items, option=True, **extras): şeklindedir.

print("-----------------------------")

# 5. Laboratuvar: agent arama isteği ve sepet fiyatı
# Argümanları toplama(packing), dışarıdan parça parça gelen bir sürü veriyi tek bir paketin içine toplar. Eğer tek yıldız (*args) koyarsan gelen dağınık değerleri bir tuple(demet) paketinde toplar. Eğer çift yıldız (**kwarhs) koyarsan gelen isim=değer şeklindeki dağınık çiftleri bir dict (sözlük) paketinde toplar.
# Argümanları açma(unpacking), fonksiyon çağrılırken, mevcut bir listenin (*) veya sözlüğün (**) başına yıldız konularak elemanlarının tek tek bağımsız argümanlara dönüştürülüp fonksiyona aktarılmasıdır. 
# Değişken konumsal argüman (variable positional argument - *args / *terms): Fonksiyona kaç tane konumsal argüman geleceği bilinmediğinde kullanılır. Gelen tüm fazla konumsal argümanları fonksiypn içinde bir TUPLE(demet) olarak saklar.
# Değişken Anahtar Sözcüklü Argüman (Variable keyword argument - **kwargs / **preferences): Fonksiyona kaç tane veya hangi isimde adlandırılmış argüman geleceği bilinmediğinde kullanılır. Gelen tüm 'anahtar=değer' çiftlerini fonksiyon içinde bir DICT (sözlük) olarak saklar.

def cart_subtotal(*prices_usd):
    # print(prices_usd) -> Tuple'ın nasıl göründüğünü terminalde doğrulamak için yaptım. ancak daha önce üzerine çalıştığımız gibi "hesaplama fonksiyonlarında yan etki (print) olmamalı, sadece return olmalı" kuralı gereği bu satırı yorum içerisine aldım.
    # DÜZELTME: print() kullanımı mutlak biçimde yasak değildir. Saf hesaplama fonksiyonu sonucu return eder; print() ise gözlemlenebilir yan etkidir. Ekrana yazdırmak fonksiyonun amacıysa print() kullanılabilir; hesaplamayı ve gösterimi ayrı tutmak çoğu zaman daha uygundur.
    return sum(prices_usd)

print(cart_subtotal())
print(cart_subtotal(5))
print(cart_subtotal(5, 10, 15))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# ()
# 0
# (5,)
# 5
# (5, 10, 15)
# 30
# Tam da tahmin ettiğim gibi her function callda sıfır bir tuple üretiliyor ve çağrının içindeki değerler tuple'a ekleniyor

def describe_search(**filters):
    return filters

print(describe_search(color="green", size=36))
print(describe_search())
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# {'color': 'green', 'size': 36} -> function callda verilen girdiler bir sözlükte toplanmış ve anahtar-değer çiftine dönüştürülmüştür.
# {}

selected_prices = [10, 15, 20]
print(cart_subtotal(*selected_prices))

selected_filters = {"color": "green", "size": 36, "best_price": True}
print(describe_search(**selected_filters))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# (10, 15, 20)
# 45
# {'color': 'green', 'size': 36, 'best_price': True}
# Tek Yıldız (*): Listeyi patlatır ve içindeki elemanları tek tek konumsal argümanlara (positional arguments) dönüştürür. (Yani cart_subtotal(10, 15, 20) yazmışsınız gibi davranır).
# Çift Yıldız (**): Sözlüğü patlatır ve anahtar-değer çiftlerini anahtar sözcüklü argümanlara (keyword arguments) dönüştürür. (Yani describe_search(color="green", size=36, best_price=True) yazmışsınız gibi davranır).

def search_catalog(query, /, *terms, country="US", **preferences):
    return {
        "query": query,
        "terms": terms,
        "country": country,
        "preferences": preferences,
    }

print(search_catalog("ballet flat", "green", "leather", country="US", size=36))
print(search_catalog("green shoes", country="TR"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/variable_arguments.py
# {'query': 'ballet flat', 'terms': ('green', 'leather'), 'country': 'US', 'preferences': {'size': 36}}
# {'query': 'green shoes', 'terms': (), 'country': 'TR', 'preferences': {}} -> *terms için sadece boş bir tuple, **preferences için ise sadece boş bir sözlük oluşturdu.
# NOT: cart_subtotal, describe_search, search_catalog adlarıyla ikince kez fonksiyon tanımladık. Bu geçerlidir: Python aynı ada yeni fonksiyonu bağlar: sonraki çağrılar en son tanımı kullanır.

print("-----------------------------")

# 6. Geçiş kapısı
# 1. items tuple türünde olur. hiç argüman verilmese dahi boş bir tuple oluşturulur.

# 2. options dictionaries türünde olur. hiç argüman verilmese dahi boş bir sözlük oluşturulur.

# 3. hayır özel değildir. özel olan '*' dır. '*' sembolünü görünce bunun bir variable positional argument olacağını anlarız,
# DÜZELTME: Yıldızın anlamı bağlama göre değişir. “* sembolünü görünce variable positional argument olduğunu anlarız” doğru değil. Tek başına *, imzada keyword-only parametrelerin sınırını koyar; *items, fazla konumsal argümanları toplar; çağrıdaki *values ise iterable’ı açar. **options tanımda ek anahtar sözcüklü argümanları sözlüğe toplar, çağrıda sözlüğü açar.

# 4. Tanımdaki '*items' toplar(packing): fonksiyon tanımlanırken paranteze yazılır. Dışarıdan virgülle gelen dağınık değerleri alır ve fonksiyonun içinde tek bir tuple paketi haline getirir.
# Çağrıdaki '*values' dağıtır/açar (unpacking): fonksiyon çağrılırken argümanın önüne yazılır. Elimizdeki mevcut bir listeyi/tuple'ı patlatıp, elemanlarını sanki tek tek virgülle yazmışız gibi dışarıya ayrı ayrı konumsal argümanlar olarak döker.

# 5. f(**options) yazmak; options sözlüğündeki anahtar-değer çiftlerini patlatıp, onları fonksiyona "anahtar1=deger1", "anahtar2=deger2" şeklinde adlandırılmış (keyword) argümanlar olarak aktarır.

# 6. country *terms'den sonra geldiği için Python kuralları gereği '*args' veya tek başına '*' işaretinden sonra gelen Her şey yalnızca anahtar sözcüklü (keyword-only) olmak zorundadır. Konumsal verilemez. Yani country="TR" şeklinde mutlaka adıyla verilmelidir. 
# filters: fonksiyon tanımında açıkça yazılmayan, dışarıdan fazladan gönderilen tüm anahtar=deger çiftlerini içine alan bir dict (sözlük) olur.

# 7. Anahtarlar mutlaka string olmalıdır. Çünkü sözlük patlatıldığında anahtarlar birer parametre adına dönüşür (ad="Ahmet" gibi). Python'da değişken ve parametre adları sayı olamaz, sadece metin olabilir.
# İmzayla uyuşmak zorundadır, çünkü sözlükteki her bir anahtar, fonksiyondaki bir parametre adıyla birebir eşleşir. Eğer sözlüğünüzde fonksiyonda hiç tanımlanmamış bir anahtar varsa (ve fonksiyonda **kwargs gibi bir esneklik yoksa) Python TypeError: got an unexpected keyword argument hatası vererek çöker.

# 8. Kendime puanım 5