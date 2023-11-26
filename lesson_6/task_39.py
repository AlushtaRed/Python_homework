# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
import random
number = 10
array_1 = [random.randint(-5,5) for _ in range(number+1)]
array_2 = [random.randint(-5,5) for _ in range(number+1)]
print(array_1)
print(array_2)
def filter_list(array1, array2):
    res_array = []
    for i in array1:
        if i not in array2:
            res_array.append(i)
    return res_array
print(filter_list(array_1,array_2))