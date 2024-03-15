from scipy import stats
import numpy as np
import torch

p = 0.43
dist = stats.bernoulli(p)
xs = dist.rvs(3000)
# print(xs)
# print(np.mean(xs))

xs_tensor = torch.from_numpy(xs).type(torch.FloatTensor)
# print(xs_tensor)
p_est = torch.rand(1, requires_grad=True)
print(p_est)
lr = 1e-5

p_est = torch.rand(1, requires_grad=True)
for epoch in range(300):
    NLL = -torch.sum(xs_tensor * torch.log(p_est) + (1-xs_tensor) * torch.log(1-p_est))
    NLL.backward()

    if epoch % 20 == 0:
        print(f'p_pst:{p_est.data.numpy()}, NLL:{NLL.data.numpy()}')
        print('\t', torch.sum(xs_tensor)/p_est.data.numpy() - torch.sum(1-xs_tensor)/(1-p_est.data.numpy()))

    p_est.data = p_est.data - lr*p_est.grad.data
    p_est.grad.data.zero_()
