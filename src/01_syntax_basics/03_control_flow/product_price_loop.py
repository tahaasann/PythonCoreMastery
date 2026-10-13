# Bir alışveriş aramasında çok sayıda ürünü tek tek kontrol etmen gerekir. Döngüler, aynı kuralı her ürün için tekrar yazmadan uygulamanı sağlar.

# 1. Birden fazla değeri bir arada tut
# prices = [24, 65, 39, 60]
# Tahmin et: Bir program bu fiyatları sırayla ekrana yazdırırsa hangi sayı ilk, hangisi son görünür?
# Cevabım: ilk olarak 24 sayısı, son olarak 60 sayısı görünür, soldan sağa doğru sayıları terminale yazdırır.


prices = [24, 65, 39, 60]

for price in prices:  # Burada 'price' her turda farklı değer alır. Dört elemen olduğu için gövde dört kez çalışır.
    print(price)

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# 24
# 65
# 39
# 60


# ---------------------------

# Bir 'if' koşulunu döngü içine koyarsan aynı kural her fiyat için değerlendirilir:
budget_usd = 60

for price in prices:
    if price <= budget_usd:
        print("Bütçeye uygun: ", price)
    else:
        print("Bütçeyi aşıyor: ", price)


# 2. 'for': listedeki her değer için
# Tahmin et: Bu örnekte `if` koşulu kaç kez kontrol edilir? Kaç ürün bütçeye uygundur?
# Cevabım: Listede 4 tane sayı değeri olduğu için for 4 kez çalışır ve bu sayede de 4 tane if koşulu kontrolü yapılır.
# 24, 39, 60 olan ürünler Bütçeye uygun olur, geriye kalan 65 olan ürün bütçeyi aşar.


# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# Bütçeye uygun:  24
# Bütçeyi aşıyor:  65
# Bütçeye uygun:  39
# Bütçeye uygun:  60


# ---------------------------


# 3. 'range': belirli sayıda tur
# Bir sayı aralığında dönmek için 'range()' kullanılır. Bitiş sayısı aralığa dahil değildir.
# for attempt in range(1, 4):
#     print("Deneme: ", attempt)

# 'range(1, 4)' 1'den başlar ve 4'e ulaşmadan durur. Yani 1, 2 ve 3 değerlerini verir.

# Sık karışan nokta: 'range(3)' üç tur yapar ve değerleri 0, 1, 2 olur. 'range(1, 4)' de üç tur yapar ama değerleri 1, 2, 3 olur.


for attempt in range(1, 4):
    print("Deneme: ", attempt)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# Deneme:  1
# Deneme:  2
# Deneme:  3


# ---------------------------

for price in prices:
    if price > budget_usd:
        continue
    print("Uygun: ", price)

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# Uygun:  24
# Uygun:  39
# Uygun:  60


for price in prices:
    if price > budget_usd:
        break
    print(price)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# 24


# 4. Döngünün akışını değiştir
# 'continue' - bu turu atla: O anki değerin geri kalanını atlar ve sonraki değerlere geçer.
# for price in prices:
#     if price > budget_usd:
#         continue
#     print("Uygun: ", price)

# 'break' - döngüyü bitir: Döngüyü o noktada tamamen sona erdirir.
# for price in prices:
#     if price > budget_usd:
#         break
#     print(price)

# Tahmin et: `continue` örneği hangi fiyatları yazar? `break` örneği hangi fiyatı gördüğünde durur?
# Cevabım: 24'ü yazar, 65 gelince budget_usd'den fazla olduğu için if dalına girer ve continue komutunu görünce işlem yapmadan yeni değer yani 39'a geçer, 39 ve 60'ı yapar yani 24, 39, 60.

# 'break' örneğinde ise 24ü yazar 65 olduğunda breaki görüp döngüyü durdurur bu yüzden sadece 24 yazar.


# ---------------------------


# 5. 'while': koşul doğru kaldığı sürece
# 'while', listedeki elemanları otomatik olarak dolaşmaz. Koşulunu kontrol eder; koşul `True` ise gövdeyi çalıştırır ve sonra koşulu yeniden kontrol eder.

remaining_attempts = 3

while remaining_attempts > 0:
    print("Kalan deneme: ", remaining_attempts)
    remaining_attempts = remaining_attempts - 1

print("Denemeler bitti")

# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# Kalan deneme:  3
# Kalan deneme:  2
# Kalan deneme:  1
# Denemeler bitti

# Sonsuz döngü riski: Döngü koşulu hep doğru kalırsa program tekrar etmeye devam eder.
# Bu  örnekte sayacı azaltan satır kaldırılırsa 'remaining_attempts' hiç değişmez.
# 'while' kullanırken "koşulu hangi satır değiştirecek?" sorusunu önceden cevapla.

# 6. Dosya laboratuvarı: fiyatları tara
prices = [24, 65, 39, 60]
budget_usd = 60

print("Bütçeye uyan fiyatlar: ")
for price in prices:
    if price > budget_usd:
        continue
    print(price)

remaining_attempts = 3
while remaining_attempts > 0:
    print("Kalan deneme: ", remaining_attempts)
    remaining_attempts = remaining_attempts - 1

print("Tarama tamamlandı")


# 1- Bütçeyi budget_usd = 38 yapıp tekrar çalıştırırsak, sadece 24 değerini yazdırır, çünkü diğer 3 sayı 38den büyüktür ve döngüde o sayı price ile alındığında if dalına girer ve continue ile o adım print ile yazdırılmadan atlanır. 39 ve 60 38'den büyük olduğu için yazdırılmaz.

# budget_usd 38 iken çıkan terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/03_control_flow/product_price_loop.py
# Bütçeye uyan fiyatlar:
# 24
# Kalan deneme:  3
# Kalan deneme:  2
# Kalan deneme:  1
# Tarama tamamlandı


# For döngüsü 4 kere çalışır çünkü listemizde 4 eleman var. continue if bloğunun koşulunu sağlayan değerleri atlar diğer değerle devam eder. while koşulunu kontrol eder, eğer koşulu sağlanmazsa çalışmaz, eğer koşul sağlanırsa çalışır.


# 7. Geçiş Kapısı Sorularına Cevaplarım:
# 1- bu for döngüsü prices adındaki listedeki elemanları 0. indeksinden başlayarak her bir değeri price değişkenine atar ve for içindeki talimatlar gerçekleşir, ardından diğer indekse geçer aynı işlemler devam eder, sonuncu indekse kadar bu devam eder. Not: for listedeki sıradaki değeri alır. Listede bu sıra indeks sırasına denk gelir; ama for her zaman indeks kullanarak çalışmaz.

# 2- range(1, 4) 1 ile başlar 4'e kadar devam eder ama 4'ü dahil etmez. yani 3 tur çalışır ve 1, 2, 3 değerlerini üretir

# 3- continue döngüyü bitirmez sadece mevcut sayı için çalışmayı atlar döngüdeki bir sonraki değeri çalışmasını ister, break o anda bütün döngüyü durdurur.

# 4- while döngüsünün sonra ermesi için örnekte remaining_attempts değeri değişir

# 5- sonsuz döngüye geçebilir ve bu da kaynak tüketimini gereksiz yere arttırabilir. ram şişebilir. Not: RAM değil CPU meşgul edilir.

# 6- Sadece 24 yazdırır, diğerleri 38'den büyük olduğu için if dalı girer ve if dalında continue olduğu için işlem yapılmadan sonraki liste elemanına geçilir.


# Kendime 5 puan veriyorum. Sadece range eğer çok önemliyse bir tekrar edilebilir.
