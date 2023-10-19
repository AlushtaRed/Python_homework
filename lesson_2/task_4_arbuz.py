import random
import os
os.system("cls")

n = 10

arbuzy = []
for i in range(n):
    arbuzy.append(random.randint(5, 20))


print(arbuzy)
min_ = arbuzy[0]
max_ = arbuzy[0]
for i in arbuzy:
    if i>max_:
        max_=i
    if i<min_:
        min_=i
print(f'для тещи {min_} абуз, для себя {max_} арбуз')