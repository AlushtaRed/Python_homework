def print_operation_table(operation, num_rows, num_columns):
   
    if num_rows >=2:
        for x in range(1, num_rows+1):
            for y in range(1, num_columns+1):
                if x ==1:
                    print(y, end=" ")
                elif y ==1:
                    print(x, end=" ")
                else:
                    print(operation(x, y), end=" ")
            print()
    else:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")


print_operation_table(lambda x, y: (x+y)*2, 5, 5)

def print_operation_table(operation, num_rows, num_columns):
    result_table = []
    if num_rows >=2:
        for x in range(1, num_rows+1):
            for y in range(1, num_columns+1):
                if x ==1:
                    print(y,"", end="")
                elif y ==1:
                    print(x,"", end="")
                else:
                    print(operation(x, y),"", end="")
            print()
    else:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")


print_operation_table(lambda x, y: (x+y)*2, 5, 5)


# num_rows = 5
# num_columns = 5
# for i in range(1, num_columns): 
#     for j in range(1, num_rows):
#         res = i*j
#         print(res, end=" ")
#     print()
