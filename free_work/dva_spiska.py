# Напишите программу, которая принимает два списка 
# и выводит все элементы первого, которых нет во втором.
list_1=[1,2,3,3,4,5,6]
list_2 =[5,3,6,7,8,9]
# set_1 =set(list_1)
# set_2 = set(list_2)
result = set(list_1).difference(set(list_2))
print(result)