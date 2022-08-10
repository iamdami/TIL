import torch

x = torch.rand(3, 1, 20, 128)
print(x)
x1 = x.squeeze() #[3, 1, 20, 128] -> [3, 20, 128]
print(x1)


# x = torch.rand(3, 20, 128)
# print(x)
# x1 = x.unsqueeze(dim=1) #[3, 20, 128] -> [3, 1, 20, 128]
# print(x1)
