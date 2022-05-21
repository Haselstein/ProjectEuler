#Дружественные числа
#Если d(n) = b, а d(b) = n, то такие числа называются дружественными
###Делается полторы секунды, можно оптимизировать
import math
import numpy as np
import time

start_time = time.time()

def d (n): #поиск делителей числа n
    A = [1] #Массив делителей числа
    for i in range(2, int(math.sqrt(n))):
        if (n%i == 0):
            A.append(int(i))
            A.append(int(n/i))
    return np.sum(A)

#print(d(220))
#print(d(220))
Sum = 0
for i in range(1, 10000):
    n = np.sum(d(i))
    if ((d(i) == n) and (d(n) == i) and (i != n)):
        Sum += d(i)
        #print(d(i))

print(Sum)

print("--- %s seconds ---" % (time.time() - start_time))