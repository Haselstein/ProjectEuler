#Сумма цирф числа 100! (сто факториал)
import time

start_time = time.time()

def Fact (x):
    if (x == 1):
        return 1
    else:
        return x * Fact(x-1)

A = []
S = Fact(100)
Sum = 0
while S > 0:
    S //= 10
    Sum += S%10
print(Sum)

print("--- %s seconds ---" % (time.time() - start_time))