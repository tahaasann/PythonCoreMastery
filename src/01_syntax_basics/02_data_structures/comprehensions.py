"""
List Comprehensions (Liste üreteçleri):
- Liste üreteçleri, mevcut bir koleksiyondan tek satırda yeni bir liste türetmeyi sağlayan kompakt sözdizimidir.

Mekanizması:
1. Köşeli parantez içinde [ifade for eleman in koleksiyon] şeklinde yazılır.
2. Klasik for döngüsüne göre işlemci seviyesinde daha hızlı çalışır.
3. Sona eklenen if ifadesi ile elemanlar seçilerek filtrelenebilir.
4. Orjinal listeyi değiştirmez; bellekte bağımsız yeni bir liste nesnesi üretir.
5. Yalnızca yeni bir liste inşa etmek amacıyla kullanılmalıdır.
"""

# Durum 1: Kompakt filtreleme ve dönüştürme
numbers: list[int] = [1, 2, 3, 4, 5]
squared_evens: list[int] = [n * n for n in numbers if n % 2 == 0]
print(squared_evens) # [4, 16]: Çiftlerin karesi alındı.

# Durum 2: Yan etki için liste üreteci kullanmak (Hatalı pratik)
# [print(n) for n in numbers]  # Bellekte gereksiz [None, None, ...] listesi üretir

print("\n--------------------------------\n")

# ---- örnek 1 ----
words: list[str] = ["apple", "banana", "cherry", "date"]
filtered_words: list[str] = [word.upper() for word in words if len(word) > 4]
print(words)
print(filtered_words)