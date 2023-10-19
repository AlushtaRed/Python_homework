import random
import os

os.system("cls")

N = int(input("Введите число N рассматриваемых дней (1 ≤ N ≤ 100): "))
summ = 0
count = 0
# listtemp = [-36, -45, -25, 11, 49, 49]
for i in range(N):
    t = random.randint (-50, 50)
    if t > 0:
        count+=1
    else: 
        if count > summ:
            summ = count
        count=0
    print(t, end=' ')
print()
if count > summ:
    summ = count
print("Наибольшее кол-во дней оттепели равно ", summ)