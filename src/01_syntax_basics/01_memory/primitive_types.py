# Durum 1: Doğru tip belirteçleri ile standart atama
user_age: int = 25
account_balance: float = 150.75
user_name: str = "Deniz"
is_active: bool = True

# Durum 2: Tip belirtecine uymayan atama (Python engellemez)
counter: int = 10
print(type(counter))
counter = "on"  # Tip uyarısı verir ancak program çökmeksizin devam eder
print(type(counter))  # <class 'str'>: Bellekteki yeni nesnenin tipi baskın gelir

print("\n--------------------------------\n")

# ---- örnek 1 ----
sayi: int = 20
print(type(sayi))
yazi: str = "20"
print(type(yazi))
kontrol: bool = True
print(type(kontrol))
kesirli: float = 20.5
print(type(kesirli))

kesirli = 10
print(type(kesirli))
