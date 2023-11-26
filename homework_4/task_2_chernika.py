arr = [5, 8, 6, 4, 9, 2, 7, 3]
for i in range(2):
    arr.append(arr[i])
# print(arr)
result = 0
sum = 0
for i in range(1, len(arr)-1):
    sum = arr[i]+arr[i-1]+arr[i+1]
    if sum > result:
        result = sum
print(result)
# arr_count = list()
# print(arr_count)
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(arr_count)
# Вывод максимальной урожайности, которую может собрать собирающий модуль
# print(max(arr_count))