# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
numbers = [1, 3, 3, 3, 4]
def change_num(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    for n in range(len(numbers)):
        if numbers[n] == max_num:
           numbers[n] = min_num
           
change_num(numbers)
print(*numbers)

vas_marks = [1, 3, 3, 3, 4]
print([min(vas_marks) if i == max(vas_marks) else i for i in vas_marks])