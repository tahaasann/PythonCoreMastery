# Sözlükler (dictionaries): bilgiyi anahtarla bul
# Listede bir öğeyi çoğunlukla konumuna göre bulursun.
# Sözlükte (dictionary / dict) bir değeri anlamlı bir anahtarla (key) bulursun.

# 1. Anahtar-değer modeli (key-value model)
# Bir ürünün rengi, bedeni ve fiyatı farklı türlerde veridir. Bunları sıradan bir listede saklarsan, her alanın hangi konumda olduğunu hatırlaman gerekir. Sözlükte her değere bir ad olan anahtarla ulaşırsın.

# "color" (anahtar(key)) -> "green" (değer(value)) -> ürün bilgisi (alan(field))


product = {
    "name": "Willow Ballet Flat",
    "color": "green",
    "size": 36,
    "price_usd": 54.50,
}

print(product["color"])
print(product["price_usd"])
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# green
# 54.5

# Beklenen çıktı green ve 54.5 olur. Köşeli parantez içindeki metin anahtardır. Bu metin tırnaklıdır; product[color] yazarsan Python sözlük anahtarı yerine color adlı değişkeni arar.

# Sözlükte anahtarlar benzersizdir. Aynı anahtara yeniden değer atarsan, yeni bir çift oluşturmazsın; mevcut anahtarın değerini değiştirirsin.
example = {"color": "green", "color": "olive"}
print(example)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# {'color': 'olive'}

# Bu sözlükte son değer tutulur: {'color': 'olive'}. Bu nedenle aynı anahtarı iki kez yazmak genellikle bir yazım hatasını saklayabilir.

# Liste (list): product[0] gibi sayısal konumdan (index) erişirsin. Öğelerin anlamı konuma bağlıdır.
# Sözlük (dict): product["color"] gibi alanın adından (anahtar (key)) erişirsin. Anlamı anahtar açıklar.

# Boş yapı ayrımı: {} boş sözlük oluşturur. Boş küme (empty_set) oluşturmak için set() gerekir.

empty_thing = {}
empty_different_thing = set()
print(type(empty_thing))
print(type(empty_different_thing))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# <class 'dict'>
# <class 'set'>

print("-------------------------------------------------")


# 2. Değere eriş, ekle ve güncelle
# Bir anahtar zaten varsa ona yeni değer atamak güncellemedir. Anahtar yoksa atama yeni alan ekler. Yazım biçimi ikisinde de aynıdır.

product = {"name": "Willow Ballet Flat", "price_usd": 54.50}

# Var olan alanı güncelle
product["price_usd"] = 49.99

# Yeni alan ekle
product["in_stock"] = True

print(product["price_usd"])
print(product["in_stock"])
print(len(product))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# 49.99
# True
# 3

# Tahmin et: product["price_usd"] = 49.99 satırından sonra len(product) neden iki artmıyor?
# Cevabım: Çünkü aynı "price_usd" anahtarından hali hazırda product sözlüğünde zaten var. Bundan dolayı sadece "price_usd"'nin eski değeri olan 54.50 değerini yeni değer olan 49.99'a çevirir. Çift sayısı değişmez yani.


# Bir alanı kaldırma (deletion)
del product["in_stock"]
print("in_stock" in product)  # False
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# False

# Beklenen sonuç False.
# del, anahtar-değer çiftini sözlükten kaldırır.
# Silinecek anahtarın var olduğundan emin değilsen, önce üyeliğini denetlemek gerekir.

print("-------------------------------------------------")

# 3. Olmayan anahtar: hata mı, varsayılan mı?
# Köşeli parantezle olmayan bir anahtarı istemek, programın beklediği kaydın bulunmadığını gösteren KeyError hatası üretir.

product = {"name": "Willow Ballet Flat"}
# print(product["brand"])
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\02_data_structures\agent_search_request.py", line 93, in <module>
#     print(product["brand"])
#           ~~~~~~~^^^^^^^^^
# KeyError: 'brand'

# Bu örnek KeyError: 'brand' ile durur. Hata vermek her zaman kötü değildir: Bir alanın kesinlikle bulunması gerekiyorsa eksik veriyi erken fark ettirir.

# Alan isteğe bağlıysa veya henüz gelmemiş olabiliyorsa get() kullanabilirsin:

product = {"name": "Willow Ballet Flat"}

print(product.get("brand"))
print(product.get("brand", "Marka belirtilmedi"))
# Terminal Çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# None
# Marka belirtilmedi

# İlk çağrı varsayılan olarak None verir. İkinci çağrı verdiğin varsayılan metni döndürür. get(), anahtar bulunmadığında sözlüğü değiştirmez ve hata üretmez.

# Bir anahtarın bulunup bulunmadığını yalnızca sınamak istiyorsan in kullan:

print("name" in product)
print("brand" in product)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# True
# False

# Sözlükte "name" in product anahtarların arasında arama yapar; değerlerin arasında değil.

# None ayrıntısı: get(key) anahtar eksikken None döndürür; ama anahtar mevcut olup değeri gerçekten None ise de aynı sonuç görünür. Bu iki durumu ayırmak gerekiyorsa key in dictionary ile varlığı ayrıca kontrol et.

print("-------------------------------------------------")

# 4. Sözlükte gezinme (iteration)
# Sözlük üzerinde doğrudan for döngüsü kurduğunda Python anahtarları sırayla verir. Anahtar ve değerleri birlikte almak için .items() kullanılır.

product = {"color": "green", "size": 36, "price_usd": 54.50}

for key in product:
    print(key)

for key, value in product.items():
    print(key, "=", value)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# color
# size
# price_usd
# color = green
# size = 36
# price_usd = 54.5

# Döngüler sözlüğün eklendiği sırada gezer. Python sözlüklerinde ekleme sırası dil garantisidir (Python 3.7+). Bu, sözlüğün sıra numarasıyla erişildiği anlamına gelmez: product[0] “ilk alan” demek değildir. Alanı yine anahtarıyla seçersin.

# .keys() anahtarları, .values() değerleri verir.

print("-------------------------------------------------")


# 5. Sözlük değiştirilebilir (mutable)
# Liste gibi sözlük de değiştirilebilir (mutable): nesne aynı kalırken içindeki anahtar-değer çiftlerini ekleyebilir, güncelleyebilir veya silebilirsin.

preferences = {"color": "green"}
same_preferences = preferences

same_preferences["size"] = 36

print(preferences)
print(preferences is same_preferences)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# {'color': 'green', 'size': 36}
# True

# İlk çıktı {'color': 'green', 'size': 36}; ikinci çıktı True olur. İki ad da aynı sözlük nesnesine bağlıdır. Bu, listelerde gördüğün ad eşlemesi (aliasing) davranışının sözlükteki karşılığıdır.

# Bir sözlüğü başka bir ada atamak, kopya oluşturmaz.

print("-------------------------------------------------")

# Yeni problem laboratuvarı: agent arama isteği

search_request = {
    "query_text": "green ballet flat",
    "size": 36,
    "max_price_usd": 60.00,
    "include_used_items": None,
}

print(search_request["query_text"])
print(search_request["size"])
print(search_request["max_price_usd"])
print(
    search_request.get("include_used_items", "Tercih belirtilmedi")
)  # Ben Tercih belirtilmedi diye çıktı vereceğini sanıyordum fakat None çıktısını verdi.
print("include_used_items" in search_request)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# green ballet flat
# 36
# 60.0
# None
# True


new_search_request = {
    "query_text": "green ballet flat",
    "size": 36,
    # "max_price_usd": 60.00,  # max_price_usd olmadan deneme
    "include_used_items": None,
}

print(new_search_request["query_text"])
print(new_search_request["size"])
print(new_search_request.get("max_price_usd", 60.00))
print(
    new_search_request.get("include_used_items", "Tercih belirtilmedi")
)  # Ben Tercih belirtilmedi diye çıktı vereceğini sanıyordum fakat None çıktısını verdi. Sebebini üstteki max_price_usd yokmuş gibi yaptığım denemeden anladım. Çünkü eğer sözlükte değer yoksa default değer atanabiliyor. Fakat bunda None değeri var.
print("include_used_items" in new_search_request)
print(
    "max_price_usd" in new_search_request
)  # "alan yok" ile "alan var ve değeri None" aynı şey değildir.
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# green ballet flat
# 36
# 60.0
# None
# True
# False


for key, value in search_request.items():
    print(key, " = ", value)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_search_request.py
# query_text  =  green ballet flat
# size  =  36
# max_price_usd  =  60.0
# include_used_items  =  None


# 7. Geçiş Kapısı

# 1. Liste öğesini indeks numaralarıyla bulunabilir, sözlük değerini bulmak için anahtar kelimeyi söylemek gerekir. Örneğin: list[0] -> dict["anahtar"]

# 2. Anahtar'ı saklamak için yazdığımız unique isimlerdir. Değer de anahtar ile bulunan değerlerdir. Örneğin birisi beden bilgisini saklamak için "size" anahtar kelimesini ve mesela 36 değerini yazarak bir sözlük oluşturabilir. {} kullanılmalı tabii ki.

# 3. Hayır sadece o anahtarın değerini günceller. Çünkü sözlükteki anahtarlar unique olmalı.

# 4. KeyError verir. olmayan anahtarı print ile okuyamazsın.

# 5. get() erişimi sadece eğer anahtar-değer çifti yoksa None verir, ve istersen None vermesi yerine not ekleyebilirsin, ama hali hazırda bir anahtar atadıysan ve değerini None atadıysan not ekleyemezsin, çıktı hep none olur.

# 6. "size" anahtar kelimesinin search_request sözlüğü içinde bulunup bulunmadığını kontrol eder.

# 7. Hayır, o anahtar sözlükte vardır, sadece değeri None'dır.

# 8. Diğerinde de o eklenen alan görünür. Tıpkı liste gibi, iki değişken aynı sözlüğe bağlıysa, sadece o değişkenlere o sözlük nesnesi atanmış olur. biri değişirse diğeri de değişir.

# 9. Kendime puanım 5
