#Неизбыточные суммы
#Совершенное число - число, состоящее из суммы его делителей. Когда сумма больше - избыточное. Меньше - недостаточное.
#Поиск в числах 24:28123
#Найти сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел
#Задания:
#1) Содать список избыточных чисел
#2) Проверять все числа на сумму чисел из массива
#3) Если не равен сумме - то что нужно искать

import math
import numpy as np


def multipliers(n): # Раскладывает число на множители
    A = [1] # Массив делителей числа
    for i in range(2, int(math.sqrt(n)+1)):
        if (n%i == 0):
            A.append(int(i))
            A.append(int(n/i))
    B = list(set(A))
    return np.sum(B) # Возвращает сумму делителей числа

def excess(n): # Проверка на избыточное число
    if n < multipliers(n):
        return True
    else:
        return False

A = [12] # Список избыточных чисел

for n in range(13, 14056):
    if excess(n):
        A.append(n)

# Следующий кусок кода проверить надо!!! Делается оч долго
for m in range(24, 28112):
    flag = 0
    for i in A:
        if flag == 1:
            break
        for j in A:
            if (m == i+j):
                print(m)
                flag = 1
                break

# Есть список избыточных чисел. Осталось добавить проверку на состовление числа из суммы 2-х избыточных
print(A)