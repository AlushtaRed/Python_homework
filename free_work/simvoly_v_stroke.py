string = "ЦСКА всегда будет первым"
string.lower()
n = "е"
# count = 0
# for i in string.lower():
#     if i == n:
#         count = count + 1
count_ = string.lower().count(n)
print(f' буква {n} встречается в строке {count_} раз')
