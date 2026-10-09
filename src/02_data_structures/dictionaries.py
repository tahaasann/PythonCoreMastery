"""
SÖZLÜK: 
- Sözlük, verileri benzersiz anahtarlar ve bunlara karşılık gelen değerler halinde saklayan değiştirilebilir bir koleksiyondur.

Mekanizması:
1. Süslü parantezler {} kullanılarak anahtar: değer çiftleri şeklinde tanımlanır.
2. Değerlere sıra numarası ile değil, doğrudan ilişkili anahtar ismi ile erişilir.
3. Anahtarlar benzeriz ve değiştirilemez (immutable) veri türünde olmak zorundadır.
4. Değerler her tür veriyi içerebilir ve doğrudan güncellenebilir.
5. Olmayan bir anahtarı aramak "KeyError" hatası fırlatır ve program çöker. ".get()" yöntemi ise varsayılan değerle güvenli okuma sağlar.
"""

# Durum 1: Güvenli sözlük kullanımı ve erişim
product: dict [str, str | float] = {"title": "Mouse", "price": 49.90}
print(product["title"]) # Mouse: Anahtar ile doğrudan erişim
print(product.get("stock", 0)) # 0: Olmayan anahtar için varsayılan değer döner


# Durum 2: Hatalı anahtar sorgusu ve geçersiz anahtar tipi
# print(product["stock"]) # KeyError: 'stock' anahtarı mevcut değil, program çöker

# Değiştirilebilir listeler anahtar yapılamaz
#bad_dict: dict[list[int], str] = {[1, 2]: "gecersiz"}  # TypeError: unhashable type

print("\n--------------------------------\n")

# ---- örnek 1 ----
hardware: dict[str, str | float] = {"brand": "Apple", "price": 1000.00}
print(hardware.get("warranty_months", 24))
hardware["price"] = 1500.00
print(hardware)