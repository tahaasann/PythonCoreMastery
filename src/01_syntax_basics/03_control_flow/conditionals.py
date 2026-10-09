"""
Koşullu Mantık (if, elif, else):
- Koşullu ifadeler, mantıksal şartların doğruluğuna göre kodun farklı yollardan akmasını sağlayan mekanik karar yapılarıdır.

Mekanizması:
1. "if" ifadesi verilen mantıksal önermenin "True" olup olmadığını denetler.
2. Şart sağlanmazsa sonraki "elif" bloklarına sırayla bakılır.
3. Hiçbir şart sağlanmazsa en sondaki "else" bloğu otomatik çalışır.
4. Boole mantığında "and" iki şartın da varlığını, "or" ise en az bir şartı arar.
5. Python'da dört boşlukluk girintiler kodun hangi bloğa ait olduğunu belirler.
"""

# Durum 1: Birbirine bağlı hiyerarşik karar yapısı
user_role: str = "admin"
is_authenticated: bool = True

if is_authenticated and user_role == "admin":
    print("Yönetici girişi.")
elif is_authenticated:
    print("Standart kullanıcı girişi.")
else:
    print("Erişim engellendi.")

# Durum 2: Birbirini ezen bağımsız blok hatası (Her iki blok da tetiklenir)
# score: int = 85
# if score > 50: print("Geçti.")
# if score > 80: print("Başarılı.") # elif kullanılmadığı için iki kez basar


print("\n--------------------------------\n")

# ---- örnek 1 ----
temperature: float = -15
is_raining: bool = False

if temperature < 0 and is_raining:
    print("Kar yağıyor")
elif temperature >= 0 and is_raining:
    print("Şemsiye al")
else:
    print("Sıkı giyin")