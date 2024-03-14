import random


li = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(li)
for i in range(length-1):
    j = random.randrange(0, length-1-i)
    li[length-1-i], li[j] = li[j], li[length-1-i]
    print(li)
# print(li)

