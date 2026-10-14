# Kümeler (sets): tekrarları ayıkla, ortakları bul
# Bir ürün kataloğunda veya agent arama sonuçlarında aynı seçenek birden çok kez gelebilir. Küme (set), benzersiz öğeleri saklar ve iki grubun ortak ya da farklı öğelerini bulmanı sağlar.

# 1. Küme (set) hangi problemi çözer?
# Liste (list) aynı değeri birden fazla kez tutabilir ve öğelerin sırasını korur. Küme ise yinelenen (duplicate) öğeleri tekilleştirir; öğeler arasında “birinci, ikinci” sırası tutmaz.


shoe_sizes = [36, 37, 36, 38, 37, 36]
uniques_sizes = set(shoe_sizes)

print(len(shoe_sizes))
print(len(uniques_sizes))
print(36 in uniques_sizes)
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# 6
# 3
# True

# Çıktı sırasıyla 6, 3 ve True olur. Kümede 36, 37 ve 38 sayıları bulunur; tekrarlar tek öğeye iner. Kümenin yazdırdığı öğe sırası sabit değildir.

# Liste (list): Sıralıdır; tekrarları korur. İndeksle (index) erişebilirsin.
# Küme (set): Benzersiz öğeleri tutar; sırasızdır. İndeksle erişemezsin.

# Tahmin et: unique_sizes[0] “kümenin ilk bedenini” verir mi?
# Vermez çünkü unique_sizes bir Küme (set)'dir. Kümelere indeksle erişilemez.

# Boş küme: {36, 37} bir kümedir; fakat {} boş sözlüktür (empty dictionary). Boş küme oluşturmak için set() yaz.

print("------------------------------------")


# 2. Tekrarlanan kayıtları tekilleştir
# Bir listeden kümeye geçmek tekrarları kaldırır. Kaynak listeyi değiştirmez; yeni bir set nesnesi üretir.

seen_merchants = ["shop-a", "shop-b", "shop-a", "shop-c", "shop-b"]
unique_merchants = set(seen_merchants)

print(seen_merchants)
print(len(seen_merchants))
print(len(unique_merchants))
print(sorted(unique_merchants))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# ['shop-a', 'shop-b', 'shop-a', 'shop-c', 'shop-b']
# 5
# 3
# ['shop-a', 'shop-b', 'shop-c']

# Liste beş kayıt içerir, kümede üç benzersiz satıcı bulunur.
# sorted() yeni ve sıralı bir liste döndürür; raporda kararlı (stable) bir görünüm istediğinde kullanabilirsin.

# Kümenin kendisi bir sıra garantisi vermez.
# Programını kümenin yazdırdığı belirli sıraya göre kurma.
# Örneğin küme çıktısı bugün {'shop-a', 'shop-b', 'shop-c'}, başka bir çalıştırmada farklı sırada görünebilir; öğeler aynıysa veri kümesi aynıdır.

print("------------------------------------")

# 3. Üyelik testi ve küme güncelleme
# in bir öğenin kümede olup olmadığını sorar.
# add() öğe ekler. Bir öğe zaten varsa tekrar eklemek kümede ikinci bir kopya oluşturmaz.

available_sizes = {36, 37, 38}

print(36 in available_sizes)
print(40 in available_sizes)

available_sizes.add(39)
available_sizes.add(37)
print(sorted(available_sizes))
# Terminal Çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# True
# False
# [36, 37, 38, 39]

# Son satırdaki liste [36, 37, 38, 39] olur. 37 zaten vardı; küme benzersiz öğe kuralını korur.

# discard() öğe varsa kaldırır; yoksa hata vermez.
# remove() ise öğe yoksa KeyError verir. Bu derste güvenli kaldırma için discard() kullan:
available_sizes.discard(36)
available_sizes.discard(99)
# available_sizes.remove(42)
print(sorted(available_sizes))
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\02_data_structures\agent_source_sets.py", line
#  85, in <module>
#     available_sizes.remove(42)
#     ~~~~~~~~~~~~~~~~~~~~~~^^^^
# KeyError: 42
# remove 'KeyError' verdi fakat discard(99) herhangi bir hata vermedi.
#
# Remove'u yorum satırına alınca Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# [37, 38, 39]
# "99" kümede bulunmasa da program durmaz. Üyelik testiyle varlığı ayrıca denetlemek, iş kuralı için gerekebilir.

print("------------------------------------")

# 4. İki grubu karşılaştır: küme işlemleri
# Alışveriş örneğinde kullanıcının istediği bedenler ile mağazada bulunan bedenleri karşılaştıralım. Aynı işlemler agent kaynak grupları için de geçerlidir.
requested_sizes = {36, 37, 38}
in_stock_sizes = {35, 36, 38, 40}

print(sorted(requested_sizes | in_stock_sizes))  # İki küme(set)de de olan sizelar
print(
    sorted(requested_sizes & in_stock_sizes)
)  # sadece requested_sizes ile in_stock_sizes'da ortak olanlar
print(
    sorted(requested_sizes - in_stock_sizes)
)  # requested_sizes'da olup in_stock_sizes'da olmaynlar
print(sorted(requested_sizes ^ in_stock_sizes))  # iki kümede ortak olmayan değerler.
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# [35, 36, 37, 38, 40]
# [36, 38]
# [37]
# [35, 37, 40]

# Birleşim (union) - "|" : İki kümede bulunan tüm benzersiz öğeler:
# {35, 36, 37, 38, 40}

# Kesişim (intersection) - "&": İki kümede de bulunan öğeler:
# {36, 38}

# Fark (Difference) - "-": Soldaki kümede olup sağdakinde olmayanlar.
# {37}

# Simetrik fark (symmetric difference) - "^": Yalnızca kümelerden birinde olan öğeler:
# {35, 37, 40} (ikisinde ortak olanlar dışarıda kalır.)

# Operatörleri karıştırma: & iki kümenin kesişimini bulur. Boolean (bool) işleç olan and ise doğru/yanlış ifadelerini birleştirir. Benzer görünmezler ve aynı işi yapmazlar.

# Tahmin et: Kümelerde çıkarma işlemi yönlü müdür? A - B ile B - A aynı sonucu verir mi?
# Evet yönlüdür, soldan sağa doğru işlenir yani A - B -> A'da olup B'de olmayanlar, B - A -> B'de olup A'da olmayanlar

print("------------------------------------")

# 5. Yeni problem laboratuvarı: agent kaynaklarını birleştir
# Bir agent araması protokol destekleyen kataloglardan ve tarayıcıyla bulunan sayfalardan aday kaynaklar almış olsun.
#  Aynı kaynak iki taraftan gelebilir.
# Görevin yinelenenleri ayıklamak ve hangi kaynakların ortak ya da yalnızca tek tarafta olduğunu bulmak.
protocol_source = [
    "catalog.example",
    "shop-a.example",
    "catalog.example",
    "market.example",
]
browser_source = [
    "shop-a.example",
    "shop-b.example",
    "market.example",
    "shop-b.example",
]

set_protocol_source = set(protocol_source)
set_browser_source = set(browser_source)

print(len(protocol_source))
print(len(browser_source))
print(len(set_protocol_source))
print(len(set_browser_source))

# İlk iki listenin eleman sayısı 4'tür, ardından bunları kümeye(set) çevirince eleman sayıları 3'e düşüyor. Çünkü listede de tekrarlanan değerler var, setlerde hiçbir üye tekrarlanmaz.

print(
    sorted(set_protocol_source | set_browser_source)
)  # ['catalog.example', 'market.example', 'shop-a.example', 'shop-b.example']
print(
    sorted(set_protocol_source & set_browser_source)
)  # ['market.example', 'shop-a.example']
print(sorted(set_protocol_source - set_browser_source))  # ['catalog.example']
print(
    sorted(set_protocol_source ^ set_browser_source)
)  # ['catalog.example', 'shop-b.example']

set_protocol_source.add("shop-c.example")
set_browser_source.discard("market.example")

print(
    sorted(set_protocol_source | set_browser_source)
)  # ['catalog.example', 'market.example', 'shop-a.example', 'shop-b.example', 'shop-c.example']
print(sorted(set_protocol_source & set_browser_source))  # ['shop-a.example']
print(
    sorted(set_protocol_source - set_browser_source)
)  # ['catalog.example', 'market.example', 'shop-c.example']
print(
    sorted(set_protocol_source ^ set_browser_source)
)  # ['catalog.example', 'market.example', 'shop-b.example', 'shop-c.example']

print("shop-a.example" in set_browser_source)  # True
print("catalog_example" in set_browser_source)  # False
print("shop-c.example" in set_protocol_source)  # True
print("shop-b.example" in set_protocol_source)  # False

# 6. Geçiş Kapısı
# 1. Listede istediğin kadar değeri tekrarlayabilir ve elemanlara indeksle erişebilirsin, Küme(set)'de her değer benzersiz ve indeksleme erişileyemen sırasızdır.

# 2. {} boş küme değil bir dictionary yani sözlük oluşturur. Boş küme oluşturmak için set() kullanılmalı.

# 3. Çünkü kümede unique değerler olduğu için birkaç öğe aynı değere sahipse sadece bir tanesi kalır, geri kalanlar yok olur, bu da sıralamayı sürekli değiştirme ihtimali olur. Bundan dolayı indeksleme yapılamaz.
# DÜZELTME: Kümelerde indeksleme yapılamamasının nedeni tekrarların sırayı değiştirmesi değil. Küme, öğelere konum vermez; yani sırasızdır (unordered). Tüm öğeler benzersiz olsa bile my_set[0] kullanılamaz.

# 4. Tekrar etmez, sanki hiç eklenmemiş gibi kalır küme.

# 5. "in" değerin küme içinde olup olmadığını kontrol eder. "add()" kümeye yeni eleman eklemeye yarar, "discard()" kümeden istenilen elemanı silmeye yarar, eğer istenilen eleman kümede yoksa hata vermez, ama remove() KeyError verir.

# 6. Minimum iki küme birleştiğinde tek bir kümede benzersiz, tekrarsız elemanlar birleşir, "|" ile yapılır. Kesişim "&" ile yapılır ve soldaki küme ile sağdaki kümedeki ortak değerleri seçer.

# 7. Çünkü soldan sağa doğru işlem yapılır. İlki A'da olup B'de olmayan, ikincisi B'de olup A'da olmayan değerleri gösterir.

# 8. Hayır kesinlikle yapmaz boolean and doğru/yanlış ifadelerini birleştirir, & iki kümenin kesişimini bulur.

# 9. Kendime 5 puan veriyorum.

# print(set_browser_source[0])
# Terminal çıktısı:
# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/01_syntax_basics/02_data_structures/agent_source_sets.py
# Traceback (most recent call last):
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\01_syntax_basics\02_data_structures\agent_source_sets.py", line
#  218, in <module>
#     print(set_browser_source[0])
#           ~~~~~~~~~~~~~~~~~~^^^
# TypeError: 'set' object is not subscriptable