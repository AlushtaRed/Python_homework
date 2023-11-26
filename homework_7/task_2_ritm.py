stroka = "пара-ра-рва мрам-пам-папам па-ра-па-дам"
slova = stroka.split()
vowels = "уеыаоэяию"
find_vowels = []
for i in slova:
    count = 0
    for j in i:
        if j in vowels:
            count += 1
    find_vowels.append(count)
if len(slova) > 1:
    if len(set(find_vowels)) == 1:
        print("Парам пам-пам")
    else:
        print("Пам парам")
else:
    print("Количество фраз должно быть больше одной!")
