"""
Tuples:
- Demet, tanımlandıktan sonra elemanları eklenemeyen, silinemeyen ve değiştirilemeyen sabit sıralı bir veri koleksiyonudur.

Mekanizması:
1. Normal parantezler () kullanılarak veya virgülle ayrılarak tanımlanır.
2. DEmetler değiştirilemezdir (immutable); bellekte sabit boyutlu tek parça olarak saklanır.
3. Eleman güncelleme denemeleri çalışma anında tip hatası (TypeError) fırlatır.
4. Değiştirilemez oldukları için listelere göre bellekte daha az yer kaplar.
5. Sabit kalması gereken yapılandırma verilerini ve sistem koordinatlarını güvenle saklamak için kullanılır.
"""

# Durum 1: Değiştirilemez demet tanımı ve güvenli okuma
point_coordinates: tuple[int, int] = (10, 20)
print(point_coordinates[0]) # 10: İndeksle sorunsuz okunur

# Durum 2: Elemanı değiştirme girişimi (Çalışma anında çöker)
#point_coordinates[0] = 100 # TypeError: 'tuple' object does not support item assignment

# İçeriği genişletmek için daima yeni bir demet türetilir
new_coordinates: tuple[int, int, int] = (*point_coordinates, 30)
print(new_coordinates) # (10, 20, 30): Bellekte yeni bir demet oluşturuldu
print(id(point_coordinates))
print(id(new_coordinates))
print(new_coordinates[1])
print(type(new_coordinates))

print("\n--------------------------------\n")

# ---- örnek 1 ----
rgb_color: tuple[int, int, int] = (255, 0, 0)
print(rgb_color[0])
# eğer bu tuple'a .append() yani eleman eklenmeye çalışılırsa TypeError değil AttributeError fırlatır ve program çöker
new_rgb_color: tuple[int, int, int, int] = (*rgb_color, 255)
print(new_rgb_color)