import time
start = time.time()
# print(start)
res = []
for i in range(10000000):
    res.append(i * 2)
# print(res)
print(time.time() - start)

