# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Введите трехзначное число: "))
if num > 99 and num < 1000:
    print(f"{num} -> {(num//100)+(num//10%10)+(num%10)}")
else:
    print("Ошибка! Введите трехзначное число: ")