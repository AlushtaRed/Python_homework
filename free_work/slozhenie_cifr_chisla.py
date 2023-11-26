n = 123
# sum = 0
# while n > 0:
#     sum = sum + n%10
#     n = n//10
# print(f'сумма цифр в числе = {sum}')
digits = []
for i in str(n):
    digits.append(int(i))
print(sum(digits))