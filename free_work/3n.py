# При заданном целом числе n посчитайте n + nn + nnn.
n = 3
print(f'n = {n}')
str_n = str(n)
# print(type(str_n))
nn = str_n*2
nnn = str_n*3
print(f'n + nn + nnn = {n + int(nn) + int(nnn)}')