list_num = [1, 2, 3, 4, 5]
k = 3

print(list_num)
for i in range(k):
    list_num.insert(0, list_num.pop())

print(list_num)


# list_num = [1, 2, 3, 4, 5]
# k = 3
# print(list_num[:k])
# print(list_num[k:])

# print(list_num[k:] + list_num[:k])