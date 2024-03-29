# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

num = input('Введите номер билета: ')
if len(num)==6:
    s1 = int(num[0])+int(num[1])+int(num[2])
    s2 = int(num[-1])+int(num[-2])+int(num[-3])
    if s1 == s2:
        print(f'билет {num} -> счастливый')
    else:
        print(f'билет {num} -> не счастливый')
else:
    print('Неверный номер билета')
