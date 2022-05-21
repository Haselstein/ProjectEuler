#Нахождение простых чисел
def Prime(n):
    S = [2, 3]
    #n = 100
    k = 0
    for i in range(4, n+1):
        for j in S:
            if i%j == 0:
                k += 1
        if k == 0:
            S.append(i)
        else:
            k = 0
    return S

n = int(input("До какого значения искать простые числа?: "))
print(Prime(n))

n = int(input("Введите число, наибольший простой делитель которого нужно найти: "))
count = 2
while 1:
    if n % count == 0:
        n /= count
        if n == 1:
            print(count)
            break
    else:
        count += 1