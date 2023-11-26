def show_all(file_name: str):
    with open (file_name, 'r', encoding='utf-8') as f:
        data =f.readlines()
        # print((list(zip(range(1,len(data)+1), data))))
        x = list(zip(range(1,len(data)+1), data))
        for item in x:
            print(*item)
    

def remove(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    # data = ""
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        s = f"{last_name}, {first_name}, {patronymic}, {phone_number}\n"
        data.remove(s)
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(data)

def modify(file_name: str):
    # print("Введите данные для изменения: ")
    # last_name = input("Введите фамилию: ")
    # first_name = input("Введите имя: ")
    # patronymic = input("Введите отчество: ")
    # phone_number = input("Введите номер телефона: ")
    old_data = find_by_atribute(file_name, True)
    print("Введите новые данные: ")
    last_name_m = input("Введите фамилию: ")
    first_name_m = input("Введите имя: ")
    patronymic_m = input("Введите отчество: ")
    phone_number_m = input("Введите номер телефона: ")
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f"{last_name_m}, {first_name_m}, {patronymic_m}, {phone_number_m}\n"
    with open(file_name, "w", encoding="utf-8") as f:
        f.writelines(data)

def find_by_atribute(file_name: str, option: bool):
    c = input("Введите 1 для поиска по фамилии и 2 для поиска по имени: ")
    opt = 0
    if c =="1":
        opt = 0
    elif c == "2":
        opt = 1
    attr = input("Введите имя\фамилия для поиска: ")
    with open(file_name, "r", encoding="utf-8") as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(", ")[opt] == attr, data))
        # print(list(zip(range(1,len(data)+1), data)))
        x = list(zip(range(1,len(data)+1), data))
        for item in x:
            print(*item)
        
        if option:
            id = input("Введите ID нужного пользователя для изменения: ")
        else :
            id =input("Введите ID нужного пользователя: ")
        return data[int(id)-1]

    



def add_new(file_name: str):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open(file_name, "a", encoding="utf-8") as fd:
        fd.write(f"{last_name}, {first_name}, {patronymic}, {phone_number}\n")

def copy_paste(file_name: str):
    i = find_by_atribute(file_name, False)
    new_file_name = input("Введите имя файла для переноса: ")
    with open(new_file_name, "a", encoding="utf-8") as fd:
        fd.write(i)

def copy_paste_by_index(file_name: str):
    print(show_all(file_name))
    with open (file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        x = int(input("Введите номер строки для переноса: "))
        print(data[x-1])
        new_file_name = input("Введите имя файла для переноса: ")
        with open(new_file_name, "a", encoding="utf-8") as fd:
            fd.write(data[x-1])

    



def main():

    file_name = "homework_phonebook.txt"
    flag_exit = False
    while not flag_exit:
        print("1 - показать все записи")
        print("2 - добавить записи")
        print("3 - удалить запись")
        print("4 - изменить запись")
        print("5 - поиск по имени/фамилии")
        print("6 - перенос по имени/фамилии")
        print("7 - перенос в другой файл по индексу")
        answer = input("Введите операцию или x для выхода ")
        if answer == "1":
            show_all(file_name)
        elif answer == "2":
            add_new(file_name)
        elif answer == "3":
            remove(file_name)
        elif answer == "4":
            modify(file_name)
        elif answer == "5":
            print(find_by_atribute(file_name, False))
        elif answer == "6":
            copy_paste(file_name)
        elif answer == "7":
            copy_paste_by_index(file_name)

        elif answer == "x":
            flag_exit = True
if __name__ == '__main__':
    main()