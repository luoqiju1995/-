import torch
from torch import nn


# NLP Example
# batch, sentence_length, embedding_dim = 20, 5, 10
# embedding = torch.randn(batch, sentence_length, embedding_dim)
# layer_norm = nn.LayerNorm(embedding_dim)
# # Activate module
# print(layer_norm(embedding))

# Image Example
# N, C, H, W = 20, 5, 10, 10
# input = torch.randn(N, C, H, W)
# layer_norm = nn.LayerNorm([C, H, W])
# output = layer_norm(input)
# print(output)
