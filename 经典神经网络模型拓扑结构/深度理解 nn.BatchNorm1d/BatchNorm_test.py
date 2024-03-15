import torch
from torch import nn


# 1d
# x = torch.randn(4, 5)
# m = nn.BatchNorm1d(5)
# print(m.weight)
# print(m.bias)
# print(x)
# output = m(x)
# print(output)
# print(output.mean(dim=0))
# print(output.std(dim=0))
# print(output.std(dim=0, unbiased=False))
# mean = x.mean(dim=0)
# print(mean)
# std = torch.sqrt(1e-5 + torch.var(x, dim=0, unbiased=False))
# print(std)
# print((x-mean)/std)
# print(output)


# 2d
x = torch.randn(2, 3, 2, 2)
# print(x)
m = nn.BatchNorm2d(3)  # 对齐第一个非批次的维度 2，3，2，2 中第一个2是批次，所以对齐第一个3
print(m.weight)
print(m.bias)
print(m(x))

