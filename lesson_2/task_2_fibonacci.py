import os

os.system("cls")

# 0 1 1 2 3 5 8

n = int(input("Enter number  "))
a = 1
b = 0
i = 1
fibonacci = 0
count = 0

while i <= n + 1:
    # print(fibonacci, end=" ")
    if fibonacci == n:
        # print(f"\nЧисло {n} по счету на {i} месте")
        break
    fibonacci = a + b
    a = b
    b = fibonacci
    i += 1
else:
    i = -1
print(i)