# Fonksiyon girdilerini doğru ver
# Bir fonksiyonun parametresi, hangi bilgiyi beklediğini söyler. Çağrıdaki argüman ise o parametreye gerçek değeri verir.

# 1. Parametre ile argüman aynı şey değildir
# Şu fonksiyona bak:


def delivery_note(city):
    return "Teslimat şehri: " + city


message = delivery_note("Boston")

# def delivery_note(city) satırındaki city, fonksiyonun tanımında bulunan bir parametredir (parameter). Çağrıda yer alan "Boston" ise gönderilen bir argümandır (argument).

# Tanım (city) Parametre ←- Fonksiyon çağrısı (delivery_note("Boston")) -> Çağrıdaki değer "Boston" Argüman

# Fonksiyon çağrıldığında Python, verilen argümanı ilgili parametreyle eşleştirir. Fonksiyon gövdesinde artık city adı, bu çağrıdaki "Boston" değerini temsil eder.

# Kısa tahmin: delivery_note("Seattle") çağrısında parametre hangisidir? Argüman hangisidir?
# Cevabım: bu çağrıdaki parametre fonksiyon tanımlamasında kullandığımız "city" dir. Argüman ise function call aşamasında yazdığımız "Seattle" dır.

# 2. Argümanı konumla veya adıyla gönder
# Konumsal gönderim (positional argument)
# Konumsal gönderimde (positional argument), değerler parametrelerle soldan sağa eşleşir.


def make_label(product, size):
    return str(product) + " / beden " + str(size)


print(make_label("Trail shoe", 38))
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# Trail shoe / beden 38

# İlk argüman product parametresine, ikinci argüman size parametresine gider. Bu nedenle sıralama önemlidir.

# Tahmin et: Aşağıdaki çağrı ne yazar? Değerler yanlış parametreye gittiği için hata verir mi?
# print(make_label(38, "Trail shoe"))
# Cevabım: Aşağıdaki çağrının çıktısı "38 / beden Trail shoe" yazar, ilk argüman product'a, ikinci argüman size'a bağlanır.
print(make_label(38, "Trail shoe"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# 38 / beden Trail shoe

# Adla gönderim (keyword argument)
# Adla gönderimde (keyword argument), her değeri parametre adıyla eşleştirirsin. Okuyan kişi, her değerin ne anlama geldiğini daha kolay görür.
print(make_label(size=38, product="Trail shoe"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# Trail shoe / beden 38
#
# Adla verilen argümanların sırası değişebilir. size önce yazılsa da doğru parametreye bağlanır.
#
# İki gönderim biçimini birlikte kullan
print(make_label("Trail shoe", size=38))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# Trail shoe / beden 38
# İlk argüman konumla gider; size ise adıyla verilir. Birlikte kullanırken önce konumsal argümanlar, sonra adla verilen argümanlar gelir.
# print(make_label(size=38, "Trail shoe"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\04_functions\delivery_quote.py", line 57
#     print(make_label(size=38, "Trail shoe"))
#                                           ^
# SyntaxError: positional argument follows keyword argument

# Yaygın hata: Aynı parametreye iki kez değer verme.
# make_label("Trail shoe", product="Boot") çağrısında product hem konumla hem adıyla verilmiştir.
# Python bu çağrıyı kabul etmez.
# Tanımda olmayan bir parametre adı kullanmak da çağrı hatası üretir.
# print(make_label("Trail shoe", product="Boot"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\04_functions\delivery_quote.py", line 69, in <module>
#     print(make_label("Trail shoe", product="Boot"))
#           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: make_label() got multiple values for argument 'product'
#
# Parametre adı anlam taşıyorsa, adla gönderim çoğu zaman çağrıyı daha okunur yapar.
# Özellikle benzer birkaç sayı kullanıldığında adlar karışıklığı azaltır

print("------------------------------------")


# 3. Varsayılan değer (default value)
# Bazı girdiler çoğu çağrıda aynı olur.
# Böyle bir parametreye varsayılan değer verebilirsin.
# Çağrı o argümanı sağlamazsa Python varsayılan değeri kullanır.
def make_search_link(query, country="US"):
    return "https://" + country.lower() + ".example/search?q=" + query


print(make_search_link("green flats"))
print(make_search_link("green flats", "CA"))
print(make_search_link("green flats", country="CA"))


# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# https://us.example/search?q=green flats
# https://ca.example/search?q=green flats
# https://ca.example/search?q=green flats
#
# İlk çağrıda country verilmediği için "US" kullanılır.
# İkinci ve üçüncü çağrılarda "CA" açıkça gönderilir; varsayılan değer kullanılmaz.
# Çağrıdaki durum	        | Python ne yapar?
# Argüman verilmez	        | Varsayılan değer kullanılır.
# Argüman açıkça verilir	| Verilen değer kullanılır.
# None açıkça verilir	    | None kullanılır; varsayılan değer kullanılmaz.
#
#
# “Argüman verilmedi” ile “None verildi” farklı durumlardır.
# Varsayılan değer yalnızca argüman atlandığında kullanılır.
def describe_search(query, country="US"):
    return (query, country)


print(describe_search("ballet flats"))
print(describe_search("ballet flats", None))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# ('ballet flats', 'US')
# ('ballet flats', None)
#
# Tanım sırası: Varsayılan değeri olan parametreler, varsayılanı olmayan parametrelerden sonra yazılır.
# def f(country="US", query): geçerli değildir; zorunlu query parametresi önce gelmelidir.
# def f(country="US", query): # SyntaxError: parameter without a default follows parameter with a default
#     return (country, query)

# print(f("ballet flats"))
# print(f("ballet flats", None))
# Terminal Çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\04_functions\delivery_quote.py", line 121
#     def f(country="US", query):
#                         ^^^^^
# SyntaxError: parameter without a default follows parameter with a default

print("------------------------------------")

# 4. Değiştirilebilir varsayılan değer tuzağı
# Metin ve sayılar gibi değiştirilemeyen (immutable) varsayılan değerler çoğu basit kullanımda güvenlidir. Liste (list) ve sözlük (dictionary) ise değiştirilebilir (mutable) nesnelerdir. Bu fark varsayılan argümanlarda önemlidir.


# Şu fonksiyonda varsayılan değer olarak boş liste kullanılmış:
def add_filter(filter_name, filters=[]):
    filters.append(filter_name)
    return filters


first_call = add_filter("green")
second_call = add_filter("size 36")

print(first_call)
print(second_call)
print(first_call == second_call)


# Önce tahmin et: İki ayrı, tek öğeli liste mi çıkar? Yoksa ikinci çağrı ilk çağrının listesini de etkiler mi?
# Cevabım: bence filters listesi parametre olarak konulduğu için iki ayrı, tek öğeli liste çıkar.
# Yanıldım ve şaşırdım, iki öğeli aynı liste çıktı.
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# ['green', 'size 36']
# ['green', 'size 36']
# True # first_call ile second_call aynı listeye bakıyor, çünkü kendi listemizi vermedik default değeri kullandık.
#
# filters=[] ifadesi her fonksiyon çağrısında yeniden çalışmaz.
# Python varsayılan listeyi fonksiyon tanımlanırken bir kez oluşturur.
# Bu yüzden iki çağrı da aynı liste nesnesini kullanır.
# İlk çağrı listeye "green" ekler.
# İkinci çağrı aynı listeye "size 36" ekler.
# first_call ve second_call aynı liste nesnesine başvurur.
# İkinci çağrı bu listeyi değiştirdiği için ilk adla tuttuğun sonuç da güncel listeyi gösterir.
# Bu davranış çoğu zaman istenmez.
#
#  Güvenli desen: varsayılan olarak None
def add_filter_safely(filter_name, filters=None):
    if filters is None:
        filters = []  # filters None olduğu için her function call'da yeni bir liste olur. Ortak liste yok.

    filters.append(filter_name)
    return filters


first_call = add_filter_safely("green")
second_call = add_filter_safely("size 36")

print(first_call)
print(second_call)
print(first_call == second_call)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# ['green']
# ['size 36']
# False
#
# Her çağrıda filters atlanmışsa, fonksiyon gövdesinde yeni bir liste oluşturulur.
# Böylece iki bağımsız çağrı birbirinin listesini değiştirmez.
# Bu derste önemli kural: Çağrılar arasında paylaşılmasını özellikle istemiyorsan, liste veya sözlüğü doğrudan varsayılan değer yapma.
# Varsayılanı None yap ve yeni nesneyi fonksiyonun içinde oluştur.
# Bu desen, None “bu çağrıda liste verilmedi” anlamına geldiğinde uygundur.
# Eğer None ayrıca geçerli bir kullanıcı verisiyse, daha sonra ayrı bir işaretçi (sentinel) nesnesi kullanmayı öğreneceğiz.

print("------------------------------------")

# 5. Yeni problem laboratuvarı: teslimat teklifi
# Bu kez bir arama isteğini değil, bir teslimat ücretini modelle.
# Fonksiyonun gerekli girdileri ve varsayılan hızlandırılmış teslimat seçeneği olsun.
# Aynı sonucu farklı çağrı biçimleriyle elde et.
# ----- SÖZLEŞME (CONTRACT) -----
# Girdiler: weight_kg (kargonun ağırlığı float), zone_fee_usd (bölge fiyatlandırması float), express (hızlı kargo istenmesi bool, default=False)
# İşlev: Temel ağırlık ve bölge ücretine göre teslimat tutarını (base_price float) hesaplar, express ise 8 USD ekler.
# Çıktı: base_price değerini döndürür yani toplam teslimat ücreti
# Yan etkisi: yok (ekrana yazmaz, dış veriyi bilmez)


def calculate_delivery_fee(weight_kg, zone_fee_usd, express=False):
    base_price = weight_kg * 1.50 + zone_fee_usd

    if express:
        base_price = base_price + 8.00

    return base_price


first_positional = calculate_delivery_fee(2.0, 4.00)
first_name = calculate_delivery_fee(weight_kg=2.0, zone_fee_usd=4.00)

print("Konumsal argümanlarla sonuç ($): ", first_positional)
print("Adla verilen argümanlarla sonuç ($)", first_name)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# Konumsal argümanlarla sonuç ($):  7.0
# Adla verilen argümanlarla sonuç ($) 7.0

first_positional_express = calculate_delivery_fee(2.0, 4.00, express=True)
first_name_express = calculate_delivery_fee(
    weight_kg=2.0, zone_fee_usd=4.00, express=True
)

print("Express ile karışık çağrı (konumsal ve ad ile verilen) argümanlar ile fiyatlandırma", first_positional_express)
print("Express ile adla verilen argümanlar ile fiyatlandırma", first_name_express)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# Express ile karışık çağrı (konumsal ve ad ile verilen) argümanlar ile fiyatlandırma 15.0
# Express ile adla verilen argümanlar ile fiyatlandırma 15.0

# Tahminlerimi yazmadım ama sonuçları doğru bildim.


def add_note(note, notes=None):
    if notes is None:
        notes = []

    notes.append(note)
    return notes


print(add_note("hello"))
print(add_note("world"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/delivery_quote.py
# ['hello']
# ['world']


# 6. Geçiş kapısı
# 1. Fonksiyon tanımlamada fonksiyon isminden sonra gelen parantez içerisindeki değerlere parametre denir. Burada amaç fonksiyonun çalışması için gereken değerleri almaktır fonksiyon tanımındaki isimler parametredir, fonksiyon tanımlandıktan sonra fonksiyonun çağırılması gerektiği zamanda fonksiyona verilen değerlere argüman denir.
# Düzeltme: Parametre, fonksiyon tanımındaki isimdir; argüman ise çağrıda gönderilen değerdir. 

# 2. make_label fonksiyonunu şöyle tanımlamıştık "def make_label(product, size):", fonksiyon çağrısında konumsal argüman verme kullanılmış, buradan "Trail shoe" değerinin product parametresine verilecek olan argüman olduğunu ve 38 değerinin de "size" parametresine verilecek olan bir argüman olduğunu anlayabiliriz.

# 3. Konumsal argüman, parametrelerin tanımlanma sırasına göre soldan sağa doğru function callda verilen argümanlardır. konumsal argümanlarda aynı sıra olmak zorundadır, yoksa python hata vermese de yanlış çıktı alabiliriz. Anahtar sözcüklü argüman(keyword argument) ise istenilen sırada yazılabilen parametre anahtar kelimelerini birebir kullanarak hangi argümanın hangi parametreye gideceğini net bir şekilde belirleyen yöntemdir. Daha güvenlidir. Tek kural: Konumsal argümanlar her zaman anahtar sözcüklü argümanlardan önce yazılmalıdır.

# 4. Aynı parametreye iki dez değer verilirse bu hatayı alırız "TypeError: got multiple values for argument " ve program durur. Bir parametreye hem konumsal hem de adıyla (veya iki kez adıyla) değer verilemez, her parametre çağrı başına yalnızca bir değer alabilir.

# 5. Fonksiyon çağırılırken o argüman kullanıcı tarafından hiç verilmezse (atlanırsa) devreye girer. Açıkça None gönderirse varsayılan değer devreye girmez, parametreye None değeri verilmiş şekilde işlem devam eder.

# 6. Çünkü python'da def satırı yani fonksiyon tanımı fonksiyon her çağrıldığında değil, kod ilk çalıştırıldığında sadece bir kez çalışır. Python o anda hafızada tek bir liste nesnesi oluşturur ve bunu fonksiyon tanımına bağlar. Sonraki her çağrıda hafızadaki aynı liste nesnesini tekrar tekrar kullanır.

# 7. Bu sayede fonksiyon çalıştırıldığı zaman otomatik olarak bir liste nesnesi üretilmez. her çağrıda yeni bir liste üretilir ve notes=None iken fonksiyon içindeki "if" her çağrıda yeni bir liste oluşturur; sonucu bir değişkene atamak listenin oluşması için gerekli değildir.

# 8. Anahtar sözcüklü (keyword) çağrı biçimi (weight_kg=2.0, express=True) daha kolay okunur. Hangi sayının kiloyu, hangi boolean değerin neyi temsil ettiği doğrudan çağrı satırından (kendini açıklayan kod - self-documenting code) net şekilde anlaşılır.

# 9. Kendime 5 puan veriyorum.
