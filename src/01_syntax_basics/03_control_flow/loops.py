"""
Loops (Döngüler):
- Döngüler, belirli bir kod bloğunu bir veri koleksiyonu üzerinde veya bir koşul sürdükçe tekrarlayan mekanizmalardır.

Mekanizması:
1. "for" döngüsü bir koleksiyonun her elemanını sırasıyla tek tek ziyaret eder.
2. "while" döngüsü tanımlanan mantıksal şart True olduğu sürece çalışmayı sürdürür.
3. "break" ifadesi döngü çalışmasını anında durdurur ve bloktan dışarı çıkar.
4. "continue" ifadesi mevcut turu derhal atlar ve bir sonraki tura geçer.
5. Koşulu güncellenmeyen "while" döngüleri sonsuz döngü oluşurarak programı kilitler.
"""

# Durum 1: for ve break ile kontrollü gezinme
numbers: list[int] = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break  # 3 görüldüğünde döngü durur
    print(num)  # 1, 2


# Durum 2: while döngüsünde adım güncellemeyi unutmak (Sonsuz döngü)
counter: int = 0
# while counter < 3:
#     print(counter)  # counter artırılmazsa Sonsuz döngü, programı kilitler


print("\n--------------------------------\n")


# ---- örnek 1 ----
numbers: list[int] = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 == 1:
        continue
    print(num)


counter: int = 3
while counter > 0:
    print(counter)
    counter -= 1