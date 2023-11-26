# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
input_list = "a a a b c a a d c d d"
user_list = input_list.split()

result_list = []

for i in range(len(user_list)):
    tmp = user_list[:i].count(user_list[i])
    if tmp >= 1:
        result_list.append(f'{user_list[i]}_{tmp}')
    else:
        result_list.append(user_list[i])
    
print(input_list)
print(" ".join(result_list))