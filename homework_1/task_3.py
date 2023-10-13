n = int(input("Введите номер билета "))
sumLeft = 0
sumRight = 0
while 999<n<1000000:
    sumRight = sumRight + n%10
    n = n//10
# print(sumRight)
while 0<n<1000:
    sumLeft=sumLeft+n%10
    n=n//10
# print(sumLeft)
if sumLeft==sumRight:
    print("yes")
else: 
    print("no")