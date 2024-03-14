import random


li = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(li)
for i in range(n - 1):
    j = random.randrange(0, n - 1 - i)
    li[n - 1 - i], li[j] = li[j], li[n - 1 - i]
    print(li)
# print(li)

