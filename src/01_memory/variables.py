# Durum 1: İki etiket aynı bellek adresini işaret eder
first_box: int = 1000
second_box: int = first_box
print(first_box is second_box)  # True: Adresler aynıdır

# Durum 2: Değeri değiştirmek etiketi yeni bir adrese taşır
first_box = first_box + 1
print(first_box is second_box)  # False: first_box yeni adrese geçti
print(first_box)
print(second_box)


print("\n--------------------------------\n")

#---- örnek 1 ----
base_score: int = 500
current_score: int = base_score
print(base_score is current_score) 

base_score = base_score + 50

print(base_score is current_score) 
print(base_score)
print(current_score)
print(id(base_score))
print(id(current_score))