strint_part = "a a a b c a a d c d d"
sting_array = strint_part.split()
string_dict = dict()
zero = ""
for i in sting_array:
    if i in string_dict:
        string_dict[i] += 1
        zero += f"{i}_{string_dict[i]} "
    else:
        string_dict[i] = 0
        zero += f"{i} "
print(zero)