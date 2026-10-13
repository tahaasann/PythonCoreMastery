print("Merhaba, Python")

# REPL tek satırlık denemeler için terminalde kullanılan python konsoludur. Dosya(IDE), tekrar çalıştırabileceğin program içindir.

# print("Merhaba)

# Çalışma kuralımız: Hata mesajının tamamını kopyalamak yerine önce "hangi dosya, hangi satır, hangi hata adı?" sorularını cevapla. Sonra değişikliği dene.

# PS C:\Users\tahaa\Desktop\python-core-mastery> python src/00_getting_started/hello.py
#   File "C:\Users\tahaa\Desktop\python-core-mastery\src\00_getting_started\hello.py", line 5
#     print("Merhaba)
#           ^
# SyntaxError: unterminated string literal (detected at line 5)


# Kendi cevaplarım Çıktıyı önce tahmin et ve sonra kontrol et.
# 1- print(4 + 6)  -> Çıktı: 10 çünkü parantez içindeki 4 ve 6 toplanıyor, ikisi de sayı formunda yani integer olarak verilmiş.
# 2- hello.py dosyasına ideler yani editörler üzerinden yazarız. Yorumlayıcı olan repl'a terminalden erişiriz. Git'e de terminalden erişiriz.
# 3- Tek satırlık hızlı deneme için en uygun yer Terminalden eriştiğimiz REPL'dir.

# editör: IDE olarak geçen, kodlarımızı yazdığımız, proje klasörlerimizi istiflediğimiz yerdir.
# Python yorumlayıcısı: Python'a kod olarak verdiğimiz talimatlarımızı okur ve uygular.
# .py dosyası: Python kodu içeren dosyadır.
# terminal: Komutlarımızı yazdığım komut ekranı.

budget = 60.00
saved_budget = budget
budget = 75.00

print(saved_budget)
print(budget)
