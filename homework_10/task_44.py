import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
# new_list = []
# r = 1
# h = 0
# for i in lst:
#     if i == 'robot':
#         new_list.append([r, h])
#     else:
#         new_list.append([h, r])
new_list = [[1,0]  if i == 'robot' else [0,1] for i in lst]

data = pd.DataFrame({'whoAmI': lst})
new_data = pd.DataFrame(new_list, columns=['robot', 'human'])
# data.head()
print(data)
print(new_data)
