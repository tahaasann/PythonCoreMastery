# Tahmin et: `60.00 <= 60.00` hangi değeri üretir? Peki `61.00 <= 60.00`?
# Cevap: ilk ifade True üretir çünkü küçük ve eşit operatörü (<=) kullanılmış. İkinci ifade False üretir çünkü 61.00 60.00'dan büyüktür.

# Tahmin et: Fiyat 55, bütçe 60, renk yeşil, numara 37 ise tüm koşulların `and` ile bağlandığı ifade `True` mu, `False` mu?
# Cevap: price <= budget_usd -> true olur, color == "green" -> true olur, fakat size 37 olduğu için koşulu sağlamaz false olur. Bundan dolayı and operatörü kullanıldığı için tek bir false sonucu false yapmaya yeter.


# `==` eşit mi? iki değerin eşit olup olmadığını sorar.
# 36 == 36 # True

# `!=` farklı mı? İki değerin farklı olup olmadığını sorar.
# "green" != "blue" # True

# `<` ve `>` Sırasıyla küçük mü ve büyük mü diye sorar.
# 59.99 < 60.00 # True

# `<=` ve `>=` Eşitlik durumunu da kabul eder.
# 60.00 <= 60.00 # True

# Dikkat!: `=` atama yapar: `budget = 60.00`. `==` karşılaştırma yapar: `budget == 60.00`. Bu iki işaret farklı iş yapar.


# Koşulları birleştir:
# Bir ürünün uygun olması için birden fazla kural gerekebilir. Python'da bu kuralları `and`, 'or', 'not' ile birleştirirsin.

# 'and' - hepsi doğru: iki koşul da doğruysa sonuç doğrudur.
# price <= budget_usd and color == "green"

# 'or' - en az biri doğru: Koşullardan biri doğruysa sonuç doğrudur.
# color == "green" or color == "olive"

# 'not' - tersini al: Doğruyu yanlış, yanlışı doğru yapar.
# not is_sold_out


# 'if' ile bir karar ver
# Karşılaştırma tek başına bir cevap üretir. 'if' ise bu cevaba göre hangi kodun çalışacağını seçer.

# price = 55.00
# budget_usd = 60.00

# if price <= budget_usd:
#     print("Bütçeye uygun")
# else:
#     print("Bütçeyi aşıyor")

# Syntax ipuçları: 'if' satırının sonunda ':' vardır. İçindeki satırlar girintilidir. Python'da girinti yalnızca görünüş değildir; hangi satırların karar bloğuna ait olduğunu belirtir. Genellikle dört boşluk kullanılır.

# Birden fazla olasılık için elif kullanılır.


include_used_items = None
if include_used_items is None:
    print("Kullanıcıdan tercih alınmadı")
elif include_used_items is True:
    print("ikinci el seçeneklere izin ver")
else:
    print("ikinci el seçenekleri çıkar.")

# 'is None' kalıbı, değerin gerçekten 'None' olup olmadığını denetlemek için kullanılır. 'is' nesne kimliğini karşılaştırır. Normal sayısal veya metinsel eşitlik için '==' kullanılır.
# Önemli ayrım: `None` Python’da koşul içinde yanlış (falsey) kabul edilir.
# Bu nedenle `if include_used_items:` yazarsan hem `False` hem `None` aynı dala girer.
# “Kullanıcı hayır dedi” ile “kullanıcı karar vermedi” durumlarını ayırman gerekiyorsa önce `is None` kontrolü yap.

price = 58.00
budget_usd = 60.00
color = "green"
size = 36
include_used_items = None

matches_request = price <= budget_usd and color == "green" and size == 36  # True

print(matches_request)
if matches_request and include_used_items is None:
    print("Ürün isteğe uyuyor; ikinci el tercihi bilinmiyor")
elif matches_request and include_used_items is True:
    print("Ürün isteğe uyuyor; ikinci el seçeneklere izin var")
elif matches_request:
    print("Ürün isteğe uyuyor; ikinci el seçeneklere izin yok")
else:
    print("Ürün temel isteğe uymuyor")


# 1- matches_request içindeki tüm koşullar True olduğu ve and operatörü ile bağlandığı için True değerini alır
# 2- İlk if dalı çalışır çünkü matches_request True alır ve include_uset_items'ı None olarak belirledik.
# 3- Eğer False olur 3. sıradaki elif dalı çalışır çünkü sadece matches_request koşulu sağlanıyor.
# 4- matches_request False olur bundan dolayı else dalı çalışır.


# Dosya Laboratuvarı: Kodu sen yaz örneği
price = 58.00
budget_usd = 60.00
color = "green"
size = 36
include_used_items = None
# include_used_items = False # False olduğu için 3. sıradaki elif dalı çalışır.

matches_request = price <= budget_usd and color == "green" and size == 36  # True

print("Bütçeye uygun:", price <= budget_usd)
print("Temel isteğe uyuyor:", matches_request)

if matches_request and include_used_items is None:
    print("İkinci el tercihi: Henüz seçilmedi")
elif matches_request and include_used_items is True:
    print("İkinci el tercihi: İkinci el seçeneklere izin var")
elif matches_request:
    print("İkinci el tercihi: İkinci el seçeneklere izin yok")
else:
    print("Sonuç: Ürün isteğe uymuyor")

# 1. include_used_items = False yapılırsa 3. sıradaki elif dalı çalışır.
# 2. price = 60.01 4. sıradaki else dalı çalışır çünkü matches_request False döner
# 3. rengi "blue" yaparsak 4. sıradaki else dalı çalışır çünkü marches_request False döner


# 1- `price <= budget_usd` ne üretir? Sonucun anlamı nedir?
# True üretir, price 58.00 ve budget_usd 60.00 olduğu için küçük eşittir koşulu tutuyor (<=)

# 2- `=` ile `==` arasındaki fark nedir?
# = atama operatörüdür, bir değeri bir değişkene atarız. == karşılaştırma operatörüdür, iki değerin birbirine eşit olup olmadığını kontrol eder.

# 3- `and` ile bağlanmış üç koşuldan biri `False` ise tüm ifade ne olur? Neden?
# Tüm koşulun sonucu False olur. Çünkü and koşulu olduğu yerde True almak için hepsinin True olması şarttır.

# 4- `if`, `elif` ve `else` ne zaman çalışır?
# ilk koşul if'dir, if'in koşulu false dönerse, sırasıyla aşağısındaki eliflerin koşulları kontrol edilir, bütün elifler false ise else koşulu zorunlu olarak çalıştırılır. Bundan önceki if ve elif koşullarındaki ilk True sonucun dalı çalıştırılır ve diğerlerine bakılmaz.

# 5- Neden `include_used_items is None` kontrolünü, `if include_used_items:` kontrolünden ayrı tutuyoruz?
# Çünkü None, True veya False gibi bir Boolean değeri değildir. NoneType tipinde bir değerdir. Ama koşula yazarsak is None olmadan False kabul edilebilir

# 6- Şu durumda hangi metin yazdırılır: fiyat 60, bütçe 60, renk yeşil, numara 36, tercih `None`?
# İkinci el tercihi: Henüz seçilmedi yazdırılır.


# Kendime puanım 5
