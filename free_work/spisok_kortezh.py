value = "1,2,3,4,5,6,7,8"
print(value)
ints_as_string = value.split(',')

ints = map(int, ints_as_string)

spisok = list(ints)
kortezh = tuple(spisok)
print(spisok)
print(kortezh)
