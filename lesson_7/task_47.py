values = [2, 3, 5, 7, 11, "dfdrr", 17, 19, 23, 29]
transormed_values = list(map(lambda x: x, values))
print(transormed_values)
if values == transormed_values:
    print("ok")
else:
    print("fail")

