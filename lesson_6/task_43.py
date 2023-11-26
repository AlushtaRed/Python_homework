# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
import random

len_list = int(input("Введите длинну массива: "))

def create_random_list(number):
    return [random.randint(0,7) for _ in range(number)]

def find_couple(list_x : list):
    
    count_of_couple = 0
    for i in set(list_x):
        count_of_couple += list_x.count(i)//2   
    return count_of_couple


user_array = create_random_list(len_list)
print(user_array)
print(find_couple(user_array))