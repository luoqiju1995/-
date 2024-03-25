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
        if random.randint(1, 1000) <= prob[i]:
            if random.randint(0, 1) == 1:
                return i+1
            for j in range(90):
                if random.randint(1, 1000) <= prob[j]:
                    return i+j+2


if __name__ == '__main__':
    N = 100000
    values = np.zeros(180)
    for i in range(N):
        values[chouka()-1] += 1
    print(sum(values[:10]))
    # print(sum(values[11:20]))
    # print(sum(values[21:30]))
    # print(sum(values[31:40]))
    # print(sum(values[41:50]))
    # print(sum(values[51:60]))
    # print(sum(values[61:70]))
    print(sum(values[71:80])/N)
    # print(sum(values[81:90]))
    # print(sum(values[91:100]))
    # print(sum(values[101:110]))
    # print(sum(values[111:120]))
    # print(sum(values[121:130]))
    # print(sum(values[131:140]))
    # print(sum(values[141:150]))
    print(sum(values[151:160])/N)
    # print(sum(values[161:170]))
    # print(sum(values[171:180]))
    draw(values)

    # average_star_prob = []
    # for i in range(N):
    #     average_star_prob.append(chouka())
    # print(sum(average_star_prob)/N)