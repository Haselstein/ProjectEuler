#Сложение простых чисел
#Начинается с нахождения простых чисел
#На двух миллионах очень долго ищет
'''import math
def prime(n):
    S = [2, 3]
    Sum = 0
    #n = 100
    k = 0
    for i in range(4, n+1):
        for j in S:
            if i%j == 0:
                k += 1
        if k == 0:
            Sum += i
            S.append(i)
            print(i)
        else:
            k = 0
    return Sum'''

'''n = 2000000
sum = 0
for i in range(2, n):
    is_prime = True
    for j in range(2, int(math.sqrt(i)+1)):
        if i % j == 0:
            is_prime = False
    if is_prime:
        sum += i
print(sum)


#n = int(input("До какого значения искать простые числа?: "))
#n = 2000000
#print(prime(n))'''
class prime:
    def finder (self):
        import math
        sum = 0
        n = int(input("До какого значения искать простые числа?: "))
        for i in range(2, n):
            is_prime = True
            if i % 2 == 0:
                is_prime = False
            for j in range(3, int(math.sqrt(i) + 1), 2):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                sum += i
                #print(i)
                #print(sum+2)
        print(sum+2)

prime().finder()