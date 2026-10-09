"""
Fonksiyon ve Tip İmzaları:
- Fonksiyon, belirli bir işi yapmak üzere adlandırılan, girdi kabul eden ve sonuç üreten yeniden kullanılabilir kod bloğudur.

Mekanizması:
1. "def" anahtar kelimesi ile tanımlanır ve çağrılana kadar çalıştırılmaz.
2. Parametreler girdileri temsil eder; beklenen tipler ": type" ile belirtilir.
3. "return" ifadesi üretilen değeri çağrıldığı yere geri verir ve fonksiyonu derhal sonlandırır.
4. Dönüş tipi imzada "-> type" simgesi ile açıkça ilan edilir.
5. "return" yazılmayan fonksiyonlar varsayılan olarak daima "None" nesnesi döndürür.
"""

# Durum 1: Tip imzalı ve dönüş değerli standart fonksiyon
def calculate_vat(price: float, rate: float) -> float:
    return price * rate

total_vat: float = calculate_vat(100.0, 0.20)
print(total_vat)    # 20.0

# Durum 2: return yerine print yanılgısı (Sonuç saklanamaz)
def bad_vat(price: float, rate: float) -> None:
    print(price * rate)

lost_result = bad_vat(100.0, 0.20) # lost_result değeri 20.0 değil None olur.
print(lost_result) # None

print("\n--------------------------------\n")

# ---- örnek 1 ----
def square(number: int) -> int:
    return number * number

result: int = square(4)

print(result)
print(result is not None)