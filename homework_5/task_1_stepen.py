# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def degree(a,b):
    if b==0:
        return 1
    if b == 1:
        return a
    else:
        return a*degree(a,b-1)

print(degree(2,4))