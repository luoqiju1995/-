import random
import matplotlib.pyplot as plt
import numpy as np


def draw(values):
    x = [x for x in range(1, 181)]
    y = values
    plt.bar(x, y)
    plt.show()


def chouka():
    prob = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 66, 126, 186, 246, 306, 366, 426,
            486, 546, 606, 666, 726, 786, 846, 906, 966, 1026]

    for i in range(90):
        if random.random() <= prob[i]/1000:
            if random.randint(0, 1) == 1:
                return i+1
            for j in range(90):
                if random.random() <= prob[j]/1000:
                    return i+j+2


def caculate_prob(num1, num2=0):
    prob = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 66, 126, 186, 246, 306, 366, 426,
            486, 546, 606, 666, 726, 786, 846, 906, 966, 1026]
    flag = True
    res = 1
    if num2 == 0:
        flag = False
    if flag:
        for i in range(num1-1):
            res *= 1-prob[i]/1000
        res *= prob[num1-1] / 1000
        for j in range(num2-1):
            res *= 1 - prob[j] / 1000
        res *= prob[num2-1] / 1000
        return res
    else:
        for i in range(num1-1):
            res *= 1-prob[i]/1000
        res *= prob[num1]
        return res


def main_1():
    N = 50000
    values = np.zeros(180)
    for i in range(N):
        values[chouka() - 1] += 1
    print(sum(values[:10]))
    print(sum(values[70:80]) / N)
    print(sum(values[150:160]) / N)
    # print(sum(values[160:170]))
    print(values[170:])
    print(values[89])
    # draw(values)


def main_2():
    li = []
    for i in range(81, 91):
        for j in range(81, 91):
            # if i + j >= 170:
            #     li.append(caculate_prob(i, j))
            li.append(caculate_prob(i, j))
    print(sum(li))


if __name__ == '__main__':
    random.seed(0)
    main_1()

