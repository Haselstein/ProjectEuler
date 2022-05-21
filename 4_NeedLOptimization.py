#Наибольшее произведение-палиндром
#Можно оптимизировать, начав поиск полиндрома с конца, то есть с произведения 999 на 999
def Palindrome(x, y):
    S = x*y
    A = []
    while S > 0:
        A.append(S%10)
        S //= 10
    A.reverse()
    if len(A) == 6:
        if A[0] == A[5] and A[1] == A[4] and A[2] == A[3]:
            return True
        else:
            return False
    else:
        if A[0] == A[4] and A[1] == A[3]:
            return True
        else:
            return False
Count = 0
max = 100*100
for x in range(100,999):
    for y in range(100, 999):
        if Palindrome(x, y) == True:
            if x*y > max:
                max = x*y
print(max)