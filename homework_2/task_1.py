import random
coins = []
heads = 0
tails = 0

for i in range(1000):
    coins.append(random.randint(0,1))
    if coins[i]==0:
        tails=tails+1
    else: heads=heads+1    
print(coins)
if tails<heads:
    print(tails)
else:
    print(heads)



