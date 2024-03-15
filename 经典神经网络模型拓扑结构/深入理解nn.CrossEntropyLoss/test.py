import torch
from torch import nn

loss = nn.CrossEntropyLoss()
inp = torch.randn(3, 5, requires_grad=True)
# print(inp)
target = torch.empty(3, dtype=torch.long).random_(5)
# print(target)
print(loss(inp, target))
softmax = nn.Softmax(dim=1)
# print(softmax(inp))
print(torch.log(softmax(inp)))
print(target)
print(nn.NLLLoss()(nn.LogSoftmax(dim=1)(inp), target))

