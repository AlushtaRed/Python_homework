import random
sequence = [random.randint(0,20) for _ in range(10)]
print(sequence)
max_value = 0 
found_zero = False

for num in sequence:
    if sequence[0] == 0:
        print("0 находится на 1 месте в последовательности, максимального числа до него нет")
        found_zero = True
        break
    if num == 0:
        print("Наибольшее значение, завершающееся первым встретившимся нулем:", max_value)
        found_zero = True
        break
    elif num > max_value:
        max_value = num

if found_zero == False:
    print("В последовательности нет нуля")