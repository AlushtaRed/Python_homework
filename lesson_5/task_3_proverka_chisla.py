n = int(input("Введите число "))
res = n
count = 0
while res != 0:
    if n % res == 0:
        count += 1
        res -= 1
    else:
        res -= 1
    
if count <= 2:
    print("число простое")
else:
    print("число сложное")


# def prime_num(n, i = None):
#     if i is None:
#         i = n-1
#     if i == 1:
#         return "Yes"
#     if (n <= 1) or (n % i == 0):
#         return "No"
    
#     return prime_num(n, i-1)
    

# print(prime_num(-1))