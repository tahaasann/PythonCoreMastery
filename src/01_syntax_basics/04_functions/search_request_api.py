# Parametre türlerini seç
# Bir fonksiyonu çağırırken bazı değerleri sırayla, bazılarını adıyla gönderebilirsin. Python, fonksiyon tanımında / ve * işaretleriyle bu seçenekleri sınırlamana da izin verir. 

# 1. Standart parametre iki biçimde de kullanılabilir
# Ders 11’de kullandığın biçimde, parametreyi hem konumla hem adıyla gönderebilirsin. Bu tür parametreye konumsal veya adla verilebilen parametre (positional-or-keyword parameter) denir.

def describe_item(name, color="black"):
    return name + " / " + color

print(describe_item("Ballet flat"))
print(describe_item("Ballet flat", "green"))
print(describe_item("Ballet flat", color="green"))
print(describe_item(color="green", name="Ballet flat"))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py         
# Ballet flat / black
# Ballet flat / green
# Ballet flat / green
# Ballet flat / green

# name ve color çağrıda konumla veya adla verilebilir. 
# color için varsayılan değer vardır. 
# Son çağrıda adla verilen argümanların sırası değişmiştir, ancak değerler doğru parametrelere gider.
# Tahmin et: İlk çağrıda neden color eksik argüman hatası oluşturmaz?
# Cevabım: Çünkü color'a zaten default parametre olarak black atanmış. Yani color'ı kullanmadığım için otomatik olarak black değerini parametreye alır.

print("------------------------------")

# 2. / öncesi: yalnızca konumsal
# Fonksiyon tanımındaki / işareti, solunda kalan parametrelerin çağrıda yalnızca konumla verilebileceğini belirtir.

def show_amount(amount_usd, /):
    return "Tutar: " + str(amount_usd)

print(show_amount(24.50))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# Tutar: 24.5
# show_amount(24.50) geçerlidir. 
# show_amount(amount_usd=24.50) çağrısı geçersizdir; 
# çünkü amount_usd yalnızca konumsal parametredir.

# Neden böyle bir seçenek var? 
# Çağıranın parametre adını bilmesine gerek olmayan küçük bir değer, bazen yalnızca konumla verilebilir. 
# Böylece o iç isim, dışarıya sunulan çağrı biçiminin parçası olmaz. 
# Bu özellik her fonksiyona eklenmez; yalnızca tasarım amacına uyuyorsa kullanılır.

# Bu imzada / öncesinde birden fazla parametre de olabilir:
def distance_between(start, end, /):
    return end - start

print(distance_between(4, 11))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# 7
# start ve end değerleri sıralarına göre eşleşir. Bu çağrıda distance_between(start=4, end=11) kullanılamaz.
# 
# def error_distance_between(start, end, /):
#     return end - start

# print(error_distance_between(start=3, end=8))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\04_functions\search_request_api.py", line 60,in <module>
#     print(error_distance_between(start=3, end=8))
#           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
# TypeError: error_distance_between() got some positional-only arguments passed as keyword arguments: 'start, end' 
# 
# Çıktıyı tahmin et: distance_between(11, 4) hangi sayıyı döndürür? Python, değerlerin “start” ve “end” anlamını kontrol eder mi?
# Cevabım: distance_between(11, 4) -7 sayısını döndürür, start 11'i alır, end 4'ü alır. Python değerlerin "start" ve "end" anlamını kontrol etmez.
# Parametre adları işaretin sağında başlıyorsa, 
# bu parametreler konumla veya adla verilebilir. Böylece tek imzada farklı parametre türleri bulunabilir.
def error_distance_between(start, /, end):
    return end - start

print(error_distance_between(5, end=8))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# 3

print("------------------------------")


# 3. Tek başına * sonrası: yalnızca adla
# Fonksiyon tanımında tek başına duran * işareti, sağındaki parametreleri yalnızca adla verilmeye zorlar. 
# Bunlara yalnızca anahtar sözcüklü parametreler (keyword-only parameters) denir.
def delivery_cost(weight_kg, *, express=False):
    total = weight_kg * 1.50

    if express:
        total = total + 8.00

    return total
# weight_kg, varsayılan standart biçimdedir: konumla veya adıyla gönderilebilir. 
# express ise * sağında olduğu için adıyla verilmelidir.
print(delivery_cost(2.0))
print(delivery_cost(2.0, express=True))
print(delivery_cost(weight_kg=2.0, express=True))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# 3.0
# 11.0
# 11.0
# 
# Hızlandırılmış teslimat bir bool değeridir. 
# Çağrıya yalnızca True yazmak yerine express=True demek, bu değerin anlamını görünür kılar.
# Geçerli mi? delivery_cost(2.0, True) çağrısı neden çalışmaz?
# Çünkü fonksiyon tanımlanırken parametrelerde * sembolü kullanıldı ve bu sembolün sağındaki parametreler ad ile atama yapılmalı(keyword-only).
# print(delivery_cost(2.0, True))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\04_functions\search_request_api.py", line 110, in <module>
#     print(delivery_cost(2.0, True))
#           ~~~~~~~~~~~~~^^^^^^^^^^^
# TypeError: delivery_cost() takes 1 positional argument but 2 were given
# 
# ÖNEMLİ NOT: İşaretleri karıştırma: Bu derste tek başına *, parametreleri ayırır. *args ise farklı bir sözdizimidir; fazla konumsal argümanları toplar. **kwargs da farklıdır. İkisini daha sonra işleyeceğiz.

print("------------------------------")

# 4. Üç parametre türünü tek imzada gör
def estimate_delivery(weight_kg, /, zone_fee_usd, *, express=False):
    total = weight_kg * 1.50 + zone_fee_usd

    if express:
        total = total + 8.00
    
    return total

# İmzadaki yer          |  	Parametre türü	                            |   Çağrıda nasıl verilir?
# / öncesi	            |   Yalnızca konumsal (positional-only)	        |   Yalnızca sırayla
# / ile * arası	        |   Konumsal veya adla (positional-or-keyword)	|   Sırayla veya isimle
# Tek başına * sonrası  |	Yalnızca anahtar sözcüklü (keyword-only)    |	Yalnızca isimle
# 
# Bu fonksiyon için çağrılar:
print(estimate_delivery(2.0, 4.00, express=True))
print(estimate_delivery(2.0, zone_fee_usd=4.00, express=True))
print(estimate_delivery(2.0, 4.00, express=False))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# 15.0
# 15.0
# 7.0
# weight_kg konumsal verilmelidir. zone_fee_usd iki biçimde de verilebilir. express mutlaka adıyla verilmelidir.
# Okunabilirlik ilkesi: Değerin anlamı açık değilse, adıyla verilen argüman seç. 
# Özellikle boolean seçenekleri (True/False) adla vermek çağrıyı daha kolay okumaya yardım eder.

# Geçersiz çağrıları tahmin et
# Aşağıdaki örnekleri dosyanda çalıştırma; önce yorum olarak yaz ve neden geçersiz olduklarını açıkla. Hatalı bir çağrı çalışır durumdaki dosyanın yürütülmesini durdurabilir.

# # estimate_delivery(weight_kg=2.0, zone_fee_usd=4.00)
# # weight_kg, / işaretinin solunda; adıyla verilemez. Konumsal adlandırma olmalı bundan dolayı TypeError verir.

# # estimate_delivery(2.0, 4.00, True)
# # express, * işaretinden sonra; yalnızca adıyla verilebilir. express değeri Keyword-only adlandırma olmalı bundan dolayı TypeError verir.

print("------------------------------")

# 5. Laboratuvar: arama isteği fonksiyon arayüzü
# Şimdi bir agent arama isteğini açık bir fonksiyon imzasına dönüştür. Zorunlu sorgu metni yalnızca konumla verilsin. Bölge hem konumla hem adıyla verilebilsin. Sonuç sayısı ve ikinci el tercihi yalnızca adla verilsin.
# ----- SÖZLEŞME (CONTRACT) -----
# Girdiler: query (arama metni), country (ülke isim kısaltması), limit (kaç arama sonucu isteniyor), include_used (ikinci el ürün olsun mu?), query zorunlu parametredir, diğerleri ise varsayılan değere sahip olduğu için isteğe bağlıdır.
# İşlevler: Parametrelerden arama isteğini temsil eden bir sözlük oluşturup döndürür.
# Çıktı: Bu fonksiyon ekrana yazmaz veya dış durumu değiştirmez; girdilerinden bir sözlük üretip return eder. print() ise ekrana çıktı verdiği için gözlemlenebilir bir yan etki oluşturur.

def build_search_request(query, /, country="US", *, limit=5, include_used=None):
    return {
        "query": query,
        "country": country,
        "limit": limit,
        "include_used": include_used,
    }

function_call_1 = build_search_request("how?")
function_call_2 = build_search_request("how many?", "TR", limit=10)
function_call_3 = build_search_request("how much?", country="TR", limit=7, include_used=True)
# print etmeden önce bu çağrıların sonucunu tahmin ediyorum:
# function_call_1 -> {"query": "how?", "country": "US", "limit": 5, "include_used": None}
# function_call_2 -> {"query": "how many?", "country": "TR", "limit": 10, "include_used": None}
# function_call_3 -> {"query": "how much?", "country": "TR", "limit": 7, "include_used": True}
# include_used verilmediğinde None değeri default olarak verilir.
print("Sorgu metni: ", function_call_1["query"], " Ülke/Bölge: ", function_call_1["country"], " Cevap limiti: ", function_call_1["limit"], " 2. el olsun mu?", function_call_1["include_used"])
print("Sorgu metni: ", function_call_2["query"], " Ülke/Bölge: ", function_call_2["country"], " Cevap limiti: ", function_call_2["limit"], " 2. el olsun mu?", function_call_2["include_used"])
print("Sorgu metni: ", function_call_3["query"], " Ülke/Bölge: ", function_call_3["country"], " Cevap limiti: ", function_call_3["limit"], " 2. el olsun mu?", function_call_3["include_used"])
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/04_functions/search_request_api.py
# Sorgu metni:  how?  Ülke/Bölge:  US  Cevap limiti:  5  2. el olsun mu? None
# Sorgu metni:  how many?  Ülke/Bölge:  TR  Cevap limiti:  10  2. el olsun mu? None
# Sorgu metni:  how much?  Ülke/Bölge:  TR  Cevap limiti:  7  2. el olsun mu? True

# build_search_request(query="bu nedir?") # TypeError verir; çünkü query parametresi '/' işaretinden önce olduğu için adıyla verilemez.
# build_search_request("bu nedir?", "TR", 10, False) # TypeError verir; çünkü include_used parametresi '*' işaretinden sonra olduğu için konumla verilemez, keyword-only'dir.

print("------------------------------")

#  6. Geçiş kapısı
# 1. İşaret olmayan standart bir parametre hem konumsal(positional) olarak hem de adlandırma ile verilebilir.

# 2. / işaretinin solunda bulunan tüm parametreler, çağrı sırasında konumlarıyla verilmelidir.

# 3. Tek başına * ile verilen sağında bulunan tüm parametrelerin, çağrı sırasında keyword-only olarak değerleri verilmeli.

# 4. item'ın çağrı biçimi konumsal olmak zorundadır, 
# count hem konumsal hem adsal olabilir detailed adsal olmak zorundadır. 
# ayrıca buradaki tek zorunlu parametre item'dır. 
# diğerlerine default değer atandığı için opsiyoneldir.

# 5. Evet geçerlidir, 
# "shoe" item'ın konumuna göre doğru yere yazılmıştır, 
# 8 count için konumsal olarak adlandırılmak tercih edilmiştir ve detailed adsal olarak verilmiştir.

# 6. Çünkü item parametresi positional olarak atanması gerekir 
# çünkü /'den önce yer alıyor. TypeError verir. 

# 7. Konumsal verildiğinde  True/False ne anlama geldiği dışarıdan anlaşılmaz ve kafa karıştırır. 
# Adıyla verildiğinde kod kendini açıklar fonksiyonun tanımına gerek kalmadan o ayarın ne işe yaradığını hemen anlaşılır.

# 8. Tek başına '*' bir değişken/parametre değildir. 
# Sadece bir sözdizimi ayracıdır(sınır çizgisi). 
# Hiçbir veri tutmaz, görevi yalnızca kendisinden sonraki parametreleri adıyla verilmeye zorlamaktır. 
# '*args' gerçek bir parametredir. 
# Fonksiyona gönderilen sınırsız/sayısı belirsiz konumsal argümanları bir tuple(demet) içinde toplayıp fonksiyon içine aktarır. 

# 9. Kendime puanım 5