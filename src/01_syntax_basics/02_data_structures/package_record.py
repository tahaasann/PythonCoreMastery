# Tuple (Demetler): Sabit sırayı koru
# Bir tuple, sırası belli ve elemanları sonradan değiştirilemeyen bir gruptur.

# 1. Demet (Tuple) nedir?
# Demet (tuple), birden çok değeri sıralı (ordered) biçimde tutan bir Python nesnesidir. Çoğu zaman parantezle yazılır; değerler virgülle ayrılır.


rgb_color = (40, 120, 200)
print(rgb_color[0])
print(len(rgb_color))

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# 40
# 3

# Liste (list) gibi tupleda da sıra korunur; indeksleme 0'dan başlar ve 'len()' öğe sayısını verir.

# liste -> [...] ile yazılır. Öğreleri ekleyebilir veya değiştirebilirsin.
# Demet -> (...) ile yazılır. Demetin öğe bağları sonradan değiştirilemez.

# Tuple, küçük ve sabit bir grup değeri birlikte taşımak için kullanışlıdır. Değerlerin sırası önemlidir.


# --------------------------

# 2. Tek öğeli demette (single-item tuple) virgül gerekir

one_number = (36)
one_tuple = (36,)

print(type(one_number))
print(type(one_tuple))

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# <class 'int'>
# <class 'tuple'>

# İlk satırdaki parantez matematikteki gibi gruplayıcıdır; 'one_number bir tamsayıdır.' İkinci satırdaki virgül, tek öğeli bir tuple oluşturur.

# Tahmin et: `( "green" )` tuple mıdır? Peki `("green",)`?
# Cevabım: Bence ( "green" ) string'dir, ("green", ) tuple'dır.
# Tuple'ı belirleyen parantez değil, virgüldür.

# --------------------------

# 3. Demet öğeleri sonradan değiştirilemez
# Listeyi indeksle güncelleyebilirdik: items[0] = ...
# Tuple'ı aynı işlem tür hatası (TypeError) verir. Bu, demetin değişmez (immutable) olmasının temel örneğidir.

rgb_color = (40, 120, 200)
# rgb_color[0] = 255  # TypeError: 'tuple' object does not support item assignment

# Rengi değiştirmek istiyorsan yeni tuple oluşturup değişken adını yeni tuple'a bağlayabilirsin:
rgb_color = (40, 120, 200)
new_rgb_color = (255, rgb_color[1], rgb_color[2])

print(rgb_color)
print(new_rgb_color)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# (40, 120, 200)
# (255, 120, 200)

# İlk demet (tuple) aynı kalır. İkinci demet yeni değerleri taşır. Değişken adı yeni nesneye yeniden bağlanabilir (rebind); mevcut demet nesnesinin elemanları değiştirilemez.

# Önemli sınır: Demetin kendisi değişmezdir. İçinde list gibi değiştirilebilir (mutable) nesne varsa, o iç nesnenin içeriği değişebilir. Bu ayrıntıya sonra bakacağız


# --------------------------

# 4. Demeti açma (tuple unpacking)
# Demet açma (unpacking), demet içindeki değerleri birden çok değişkene sırayla bağlar. Değişken sayısı öğre sayısıyla eşleşmelidir.

coordinate = (12, 8)
x, y = coordinate

print("x: ", x)
print("y: ", y)

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# x:  12
# y:  8
# İlk öğe 'x' adına, ikinci öğre 'y' adına bağlanır. İki değişken fakat üç öğre olsaydı Python 'ValueError' verirdi.
# Tahmin et: `first, second = ("A", "B")` sonrasında `second` hangi değeri tutar?
# Cevabım: second B değerini tutar.

package_cm = (30, 20, 10)
length_cm, width_cm, height_cm = package_cm

print("Paket boyutları (cm): ")
print("Uzunluk: ", length_cm)
print("Genişlik: ", width_cm)
print("Yükseklik: ", height_cm)
print("Ölçü sayısı: ", len(package_cm))

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# Paket boyutları (cm):
# Uzunluk:  30
# Genişlik:  20
# Yükseklik:  10
# Ölçü sayısı:  3

# package_cm 30, 20, 10 olunca uzunluk genişlik ve yükseklik değişiyor.
# Eğer tuple'ı iki öğeli yaparsak, Unpacking satırı üç değer beklidiği için TypeError verir,
# çünkü tuple'ın tip kuralları gereyi unpacking aşamasında tupleda kaç değer varsa o sayıda değişkenle unpacking yapılmalı.
# tuple'ı 30, 20 olacak şekilde değiştirdim ve çalıştırıdm ve aldığım hataya çok şaşırdım:
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\02_data_structures\package_record.py", line 94, in <module>
#     length_cm, width_cm, height_cm = package_cm
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ValueError: not enough values to unpack (expected 3, got 2)
# TypeError almayı beklerken ValueError aldım. unpack için yeteri kadar değer yok hatası aldım. Sanırım tuple'ı indeksle değiştirmenin sonucunda alınan TypeError hatasını bu hatayla karıştırdım, benim için iyi oldu. Öğrendim.

# package_cm[0] = 10
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/package_record.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\02_data_structures\package_record.py", line 123, in <module>
#     package_cm[0] = 10
#     ~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# dediğim gibi indeksle değiştirmeye çalışınca tuple type hatası verdi.


# 6. Geçiş kapısı
# 1. Tuple ile listenin temel farkı, liste değiştirilebilirkten tuple değiştirilemezdir. liste [...] şeklinde yazılırken tuple (...,) şeklinde yazılır, ikisi de indeksle çağırılabilir.
# 2. virgül (,) parantez içindeki nesneyi tuple yapar, parantez hiçbir şey ifade etmez. matematik işleminde kullanılan parantez de olabilir.
# 3. Tuple içindeki öğeyi değiştirmeye çalışırsan TypeError alırsın. Çünkü tuplellar değiştirilemezlerdir.
# 4. Eğer eşleşmezlerse ValueError alırlar. tuple'daki öğe sayısı kadar değişken olmalıdır.
# 5. x 12'yi tutar, y 8'i tutar.
# 6. değişmeyecek veriler için uygun olabilir, mesela siparişleri tupleda tutmak mantıklı olabilir, yada gönderilecek ürünün kargo bilgileri gibi değiştirilmemesi gereken bilgiler tuple ile tutulabilir.
