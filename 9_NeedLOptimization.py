#Особая тройка Пифагора
#a<b<c, a^2+b^2=c^2
#a+b+c=1000 Найти abc
#a = 1
#b = 2
#c = 3
#n = 1
#a*a + b*b = c*c
import time

start_time = time.time()

flag = 0
for a in range(1, 1000): #Найти оптимальный способ поиска
    if flag == 1:
        break
    for b in range(a, 1000):
        for c in range(b, 1000):
            if a + b + c == 1000 and a*a + b*b - c*c == 0:
            #if 2*(-a*b+2000*(a+b-500)) and a + b + c == 1000 and a < b < c:
                print(a*b*c)
                flag = 1

print("--- %s seconds ---" % (time.time() - start_time))