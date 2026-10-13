r"""
Listeler: sıralı veriyi yönet
Ürün aramasında ürünleri bir arada tutman, tek tek seçmen ve sonuçlara ekleme yapman gerekir. Python listeleri bu işleri yapar.

1. Liste nedir?
Liste (list), birden fazla değeri belirli bir sırayla tutan ve değiştirilebilen bir Python nesnesidir.Listeyi köşeli parantezle yazarsın; öğeleri virgülle ayırırsın.

products = ["green ballet flat", "black boot", "white sneaker"]
Bu listede üç metin vardır. Sıra korunur. Bir listede aynı değerden birden fazla bulunabilir.

Tahmin et: Aşağıdaki listede kaç öğe var ve sırasıyla hangi ürünler var?
products = ["green ballet flat", "black boot", "white sneaker"]
Cevabım: products listesinde 3 tane öğe vardır ve sırayla green ballet flat, black boot, white sneaker ürünleri vardır.

Önemli: iyi veri düzeni: Python listeleri farklı türleri bir arada tutabilir. Ancak bir ürün fiyatları listesinde aynı türden değerleri saklamak, listeyi anlamayı ve işlemeyi kolaylaştırır.
"""

# ----------------------

r"""
2. indeks ve öğe sayısı:
Listedeki konumlara indeks denir. Python indeksleri 0'dan başlatır. Üç öğeli listede geçerli indeksler 0, 1 ve 2'dir.
"""

products = ["green ballet flat", "black boot", "white sneaker"]

print(products[0])  # green ballet flat
print(products[1])  # black boot
print(products[-1])  # - en sondan başlayarak tarar. bundan dolayı white sneaker
print(len(products))  # 3 -> len() listenin öğe sayısını verir.

r"""
Terminal çıktısı:
PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/product_catalog.py
green ballet flat
black boot
white sneaker
3

Son geçerli pozitif indeks, öğre sayısından bir eksiktir.

Sınır dışı indeks: Üç öğreli bir listede 'products[3]' yoktur. Python bunu sessizce 'None' yapmaz.
'IndexError' hatası verir. 

Tahmin et: Dört öğeli bir listede son öğenin indeksi kaçtır? `len(products)` kaç döndürür?
Cevabım: Son öğenin indeksi 3'tür. Çünkü indeksler 0'dan başlar. len(products) 4 döndürür.
"""

# ----------------------

r"""
3. Öğeyi güncelle ve yeni öğe ekle
Liseler değiştirilebilir (mutable). Mevcut öğreyi indeks üzerinden değiştirilebilir, '.append()' ile sona yeni öğe ekleyebilirsin.
"""
products = ["green ballet flat", "black boot"]
products[1] = "black ankle boot"
products.append("white sneaker")

print(products)

r"""
Terminal çıktısı:
PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/product_catalog.py
['green ballet flat', 'black ankle boot', 'white sneaker']

Önemli: 'products.append(...)' listeyi değiştirir. Bu metot yeni liste döndürmek için kullanılmaz. Bu nedenle 'products = products.append("red shoe")' yazma; o durumda 'products' değeri 'None' olur.
"""
# products = products.append("red shoe")
# print(products) # None

r"""
Özel araştırma yaptım:
1. append() Metodu Geriye Hiçbir Şey Döndürmez
Python'da bir fonksiyon ya da metot geriye açıkça bir değer döndürmezse (return veri demezse), Python otomatik olarak o fonksiyonun sonucunu None (boşluk / yokluk) olarak kabul eder.
append() metodu listeyi "yerinde" (in-place) değiştirir. Yani hafızadaki mevcut listenin sonuna yeni elemanı ekler ve işi biter; geriye yeni bir liste vermez. Dönüş değeri None'dır.
Kafanızda şu şekilde canlandırabilirsiniz:
code
Python
# append() metodunun arkasındaki mantık kabaca şöyledir:
def append(self, yeni_eleman):
    # Elemanı bellekteki listeye ekle...
    # (Burada herhangi bir 'return' ifadesi yoktur)
    return None  # Python arka planda bunu döner
2. products = products.append("red shoe") Satırında Ne Olur?
Python bu satırı çalıştırırken sağdan sola doğru ilerler:
Önce sağ taraf çalışır: products.append("red shoe") çağrılır.
Listenin sonuna "red shoe" eklenir.
Ancak bu metodun çalışması bittiğinde ürettiği sonuç None olur.
Sonra atama yapılır (=):
Sağ taraftan dönen None değeri alınır ve products değişkenine atanır.
Yani kod aslında şuna dönüşmüş olur: products = None
Sonuç olarak; elinizdeki liste güncellenmiş olsa bile, siz products değişkeninin içine None atadığınız için eski listeye olan bağlantınızı koparmış olursunuz.
"""

# -----------------

r"""
4. İki ad, tek liste
Değişkenler kutu değildir; nesnelere verilen adlardır. Bir listeyi başka ada atamak, yeni bir liste oluşturmaz. İki ad aynı liste nesnesine bağlanır.
"""
products = ["green ballet flat", "black boot"]
shared_products = products

shared_products.append("white sneaker")
print(products)
print(shared_products)
print(products is shared_products)
r"""
Terminal çıktısı:
PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/product_catalog.py
['green ballet flat', 'black boot', 'white sneaker']
['green ballet flat', 'black boot', 'white sneaker']
True

iki ad da aynı liste nesnesini gösterir. Bu yüzden bir adla yapılan değişiklik, diğer ad üzerinden de görülür.
"""

# Yeni bir üst seviye liste kopyası
independent_products = products.copy()
independent_products.append("red sandal")

print(products)
print(independent_products)
r"""
PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/product_catalog.py
['green ballet flat', 'black boot', 'white sneaker']
['green ballet flat', 'black boot', 'white sneaker', 'red sandal']

'copy()' yeni bir liste oluşturur. Bu örnekte öğeler metin olduğu için sonradan eklene "red sandal" yalnızca kopyada bulunur.
"""

# --------------------------

r"""
5. Listeyi döngüyle tara
'for' döngüsü listedeki değerleri sırayla verir. Değerleri kullanmak için indeks saymak zorunda değilsin.
"""
products = ["green ballet flat", "black boot", "white sneaker"]

for product in products:
    print("Ürün: ", product)
r"""
Terminal çıktısı: 
PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/product_catalog.py

Ürün:  green ballet flat
Ürün:  black boot
Ürün:  white sneaker

Burada 'product' her turda listedeki sıradaki metni alır. Döngü, liste bitince sona erer.
"""

# ----------------------

# 6. Dosya laboratuvarı: küçük ürün kataloğu
products = ["green ballet flat", "black boot", "white sneaker"]

print("İlk ürün:", products[0])
print("Son ürün:", products[-1])
print("Ürün sayısı:", len(products))

products.append("red sandal")
products[1] = "black ankle boot"

products.append("blue flat")

print("Güncel liste:")
for product in products:
    print(product)

shared_products = products
shared_products.append("tan loafer")
print("Asıl listede de görünen ekleme:", products[-1])

independent_products = products.copy()
independent_products.append("navy shoe")
print("Asıl listenin son öğesi:", products[-1])
print("Kopyanın son öğesi:", independent_products[-1])
r"""
Terminal çıktısı:
PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/product_catalog.py
İlk ürün: green ballet flat
Son ürün: white sneaker
Ürün sayısı: 3
Güncel liste:
green ballet flat
black ankle boot
white sneaker
red sandal
blue flat
Asıl listede de görünen ekleme: tan loafer
Asıl listenin son öğesi: tan loafer
Kopyanın son öğesi: navy shoe
"""

products.append("blue flat")
# ilk listenin sonuna "blue flat" ı eğer döngünden sonra eklersem döngü yeni ürünü yazdırmaz.
# döngüden önce yazdırırsam ekler.
# çünkü pythonda kodlar yukarıdan aşağıya doğru çalışır, döngü çalıştıktan sonra sonraki ürünü bilmez.

# products is shared products True döner diye tahmin ediyorum. Çünkü iki isim de aynı liste nesnesini tutar.
# Ama eğer sorulan soru products = shared products satırı yazmadan önce yapılacak bir kontrolse False döner. Çünkü daha önce shared products diye bir liste tanımlamamıştık.
# Düzeltmek gerekiyor:  shared_products henüz tanımlanmadan products is shared_products çalıştırılsaydı
# sonuç False olmazdı. Python shared_products adını bulamadığı için NameError verirdi.
# shared_products = products satırından sonra karşılaştırma True olur.
# shared_products = products.copy() kullanılırsa ayrı liste oluşturulduğundan False olur.

r"""
Terminal raporum:
.append() -> listenin sonuna bir değer ekler
indeks -> listenin elemanlarının yerini belirler ve 0'dan başlar.
.len() -> bir listedeki eleman sayısını döndürür. Düzeltme: len fonksiyon olarak çağırılır. .len() olarak çağırılmaz. len(products) olarak çağrılır. products.len() diye bir liste metodu yoktur.
eğer liste1 = liste2 yi birbirine bağlarsak ikisi de aynı liste nesnesini tutar ve hangisi değiştirirsek değiştirelim, diğeri de değişir.
.copy() -> sadece listeyi kopyalar, bu sayede iki liste birbirinden bağımsız olur, yazdığın uyarıya göre tam olarak bağımsız olmazmış bir sonraki derste göreceğiz.
"""

r"""
7. Geçiş kapısı
1- Python listesindeki ilk öğrenin indeksi 0'dır. Dört öğeli bir listenin son indeksi 3'tür.

2- len(products) products listesindeki eleman sayısını verir. Çünkü indeks 0'la başlar ve biz eleman saymaya 1 ile başlarız, o yüzden len sayısının bir eksiği son indeksi verir.

3- products listesinin sonuna "new_item" adında bir değer ekler.

4- çünkü shared_products ve products sadece bir değişkendir, ikisi de = atama operatörüyle aynı listeyi tutar, bundan dolayı birini değiştirirsek diğeri de değişir. birbirinden bağımsız değildir.

5- atama operatörü yerine copy kullanmak listeleri bağımsızlaştırır. biri değiştiğinde diğeri de değişmez. Yeni kopyayı .copy() oluşturur; = tek başına kopyalama yapmaz. Örneğin independent_products = products.copy() satırında .copy() yeni listeyi üretir, = de bu listeyi yeni ada bağlar. (yerine yazmak yerine yanlışlıkla yeni yazmışım)

6- product her turda products listenin sıradaki öğesini tutar.

kendime puanım: 5
"""
