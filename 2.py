###Четные числа Фибоначчи
def Fibonachi(n): #Числа Фибоначчи, не превышающие параметра n
    F1 = 1
    F2 = 2
    FTemp = 0
    S = [F1, F2] #Список чисел фибоначчи
    F3 = F1 + F2
    while F3 <= n:
    #for i in range(2, n):
        FTemp = F2
        F2 += F1
        F1 = FTemp
        S.append(F2)
        F3 = F1 + F2 #Избавиться от лишних переменных
        #print(S)
    return S

n = int(input("До какого числа суммировать? "))
S = Fibonachi(n)
#Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
Sum = 0
for i in S:
    if i%2 == 0:
        Sum += i
print(Sum)