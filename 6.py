#Разность между суммой квадратов и квадратом суммы чисел от 1 до n
def SummKV(n): #Сумма квадратов чисел
    Sum = 0
    for i in range(1, n+1):
        Sum += i*i
    return Sum

def KVSumm(n): #Квадрат суммы чисел
    Sum = 0
    for i in range(1, n+1):
        Sum += i
    return Sum*Sum

n = int(input("Введите количество чисел: "))
#print(SummKV(n))
#print(KVSumm(n))
print(abs(KVSumm(n)-SummKV(n)))