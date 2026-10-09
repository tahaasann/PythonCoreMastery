"""
SET (Küme):
- Küme, yinelenen (tekrarlanan) verileri otomatik olarak eleyen ve sırasız eleman tutan değiştirilebilir bir koleksiyondur.

Mekanizması:
1. Süslü parantezler {} veya "set()" kurucusu ile tanımlanır.
2. Kümeler asla aynı elemanı birden fazla saklamaz; kopyalar anında silinir.
3. Elemanlar sırasız saklanır; bu nedenle indeks numarası ile elemana erişilemez.
4. Sadece değiştirilemez (immutable) türdeki veriler küöe elemanı olabilir.
5. Boş bir küme tanımlamak için süslü parantez {} değil, set() yazılmalıdır.
"""

# Durum 1: Tekrarların elenmesi ve eleman ekleme
tags: set[str] = {"python", "kod", "python"}
tags.add("veri")
print(tags) # {"python", "kod", "veri"}: Tekrarlar ayıklandı

# Durum 2: Boş küme yanılgısı ve indeks hatası
empty_wrong = {} # Sözlük oluşturur! Küme değildir
print(type(empty_wrong)) # <class 'dict'>

# print(tags[0]) # TypeError: 'set' object does not support indexing

print("\n--------------------------------\n")

# ---- örnek 1 ----
raw_tags: list[str] = ["python", "kod", "python", "kod", "c++", "python"]
unique_tags: set[str] = set(raw_tags)
unique_tags.add("java")
print(unique_tags)

# Boş küme oluştururken {} yazmak default olarak sözlük oluşturur, bu yüzden set() yazılmalıdır.