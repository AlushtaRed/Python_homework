# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = [1, 3, 1, 3, 1, 3, 1]


def result(list_x):
    count = 0
    for i in range(1, len(list_x)-1):
        if list_x[i] > list_x[i-1] and list_x[i] > list_x[i+1]:
            count = count + 1
    return count


print(result(list_1))
print(result(list_2))
