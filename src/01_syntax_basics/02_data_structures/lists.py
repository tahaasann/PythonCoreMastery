# Durum 1: Doğrudan atama aynı nesneyi işaret eder
original_list: list[int] = [1, 2, 3]
shared_list: list[int] = original_list
shared_list.append(4)
print(original_list)  # [1, 2, 3, 4]: Ana liste de değişti, çünkü shared list ve original list bellekte aynı nesneyi işaret eder.

# Durum 2: copy() kullanımı bağımsız yeni liste üretir
independent_list: list[int] = original_list.copy()
independent_list.append(99)
print(original_list)  # [1, 2, 3, 4]: original list değişmedi, çünkü independent list bağımsız bir nesne
print(independent_list)  # [1, 2, 3, 4, 99]: independent list değişti, çünkü bağımsız bir nesne

# Not: Bir listeyi başka değişkene atayınca yeni bir kopya oluşmaz, aynı nesneyi işaret eder. Ana liste kalsın yeni bir kopya oluşturmak için copy() kullanılmalıdır.

print("\n--------------------------------\n")

# ---- örnek 1 ----
scores: list[int] = [10, 20, 30]
cloned_scores: list[int] = scores.copy()
cloned_scores.append(40)
print(scores)  # [10, 20, 30]: scores listesi değişmedi, çünkü cloned_scores bağımsız bir nesne
print(cloned_scores)  # [10, 20, 30, 40]: cloned_scores listesi değişti, çünkü bağımsız bir nesne
print(id(scores))
print(id(cloned_scores))