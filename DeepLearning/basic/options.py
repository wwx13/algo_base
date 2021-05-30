#
import torch

# print(torch.empty(5, 2))

x = torch.tensor([5.5, 3])
print(x)

x = x.new_ones(5, 3, dtype=torch.float64)  # 返回的tensor默认具有相同的torch.dtype和torch.device
print(x)

# x = torch.randn_like(x, dtype=torch.float) # 指定新的数据类型
# print(x)