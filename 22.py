#Высчитывание "очков имени", чем дальше буква в алфавите от его начала, тем больше очков за неё
#Далее "очки имени" умножаются на позицию имени в списке
#A-1|B-2|C-3|D-4|E-5|F-6|G-7|H-8|I-9|J-10|K-11|L-12|M-13|N-14
#O-15|P-16|Q-17|R-18|S-19|T-20|U-21|V-22|W-23|X-24|Y-25|Z-26
import math
import numpy as np
import time

start_time = time.time()

GetValue = {
    'A': int(1),
    'B': int(2),
    'C': int(3),
    'D': int(4),
    'E': int(5),
    'F': int(6),
    'G': int(7),
    'H': int(8),
    'I': int(9),
    'J': int(10),
    'K': int(11),
    'L': int(12),
    'M': int(13),
    'N': int(14),
    'O': int(15),
    'P': int(16),
    'Q': int(17),
    'R': int(18),
    'S': int(19),
    'T': int(20),
    'U': int(21),
    'V': int(22),
    'W': int(23),
    'X': int(24),
    'Y': int(25),
    'Z': int(26),
}

def NameScore (s): #Нахождение суммы очков имени
    Sum = 0
    for i in range(len(s)):
        if (s[i] == '"'):
            continue
        Sum += GetValue[s[i]]
    return Sum



Names = []
f = open('p022_names.txt')

lines = f.read().split('","')
for i in range(len(lines)):
    #print(NameScore(lines[i]))
    print(NameScore(lines[i])*(i+1)) #Умножить "очки имени" на позицию имени в списке

f.close()

print("--- %s seconds ---" % (time.time() - start_time))