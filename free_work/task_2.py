# Напишите проверку на то, является ли строка палиндромом. 
# Палиндром — это слово или фраза, 
# которые одинаково читаются слева направо и справа налево.
x = "ghhя"
print (x[::-1])
print (x==x[::-1])