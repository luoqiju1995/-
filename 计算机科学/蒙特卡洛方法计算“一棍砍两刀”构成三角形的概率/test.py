"""
0 < a < b < 1
a + (b-a) > (1-b)
a + (1-b) > (b-a)
(b-a) + (1-b) > a
"""
import random


total = 0.0
vic = 0.0
for i in range(1000000):
    a = random.random()
    b = random.random()
    if a < b:
        total += 1
        if (a + (b-a) > (1-b)) and (a + (1-b) > (b-a)) and ((b-a) + (1-b) > a):
            vic += 1


print(vic/total)

