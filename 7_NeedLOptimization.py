#10001-е простое число
'''def Prime(n):
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
n = int(input("До какого значения искать простые числа?"))
print(Prime(n))'''

def Prime(n):
    n = n-1
    S = [2, 3] #Массив простых чисел
    #n = 100
    k = 0
    i = 3
    while len(S)<=n:
        i += 1 #Как можно изменить шаг?
        for j in S:
            if i%j == 0:
                k += 1
                break
        if k == 0: #Можно избавиться от лишних условий
            S.append(i)
        else:
            k = 0 
    return S[n]
n = int(input("Номер простого числа: "))
print(Prime(n))