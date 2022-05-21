#Сумма цифр числа 2^1000
import math
import numpy
import time

start_time = time.time()
A = []
S = int(math.pow(2, 1000))

while S > 0:
    A.append(S%10)
    S //= 10
A.reverse()
#Sum = 0
#for i in A:
#    Sum += i
#print(Sum)
print(numpy.sum(A))
print("--- %s seconds ---" % (time.time() - start_time))