# Напишите программу, которая принимает текст и 
# выводит два слова: наиболее часто встречающееся и самое длинное.
stroka = "лошадь конь конь овца курица скумбрия"
list_ = list(stroka.split())
longest = max(list_, key = len)

print(list_)
print(longest)