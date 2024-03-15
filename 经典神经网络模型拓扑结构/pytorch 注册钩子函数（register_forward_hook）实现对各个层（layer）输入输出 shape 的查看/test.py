import timm
import torch
from torch import nn


def print_shape(m, i, o):
    """

    :param m: model
    :param i: input
    :param o: output
    :return:
    """
    print(m, i[0].shape, o.shape)


model_name = 'vgg11'
model = timm.create_model(model_name, pretrained=True)

# print(timm.list_models('vgg*'))


def get_children(model: nn.Module):
    children = list(model.children())
    flatt_children = []
    if children == []:
        return model
    else:
        for child in children:
            try:
                flatt_children.extend(get_children(child))
            except TypeError:
                flatt_children.append(get_children(child))
    return flatt_children


flatt_children = get_children(model)
for layer in flatt_children:
    layer.register_forward_hook(print_shape)


for layer in model.children():
    layer.register_forward_hook(print_shape)

batch_input = torch.randn(4, 3, 299, 299)
model(batch_input)
