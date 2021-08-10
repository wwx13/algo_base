import torch
from torch import tensor

def mask_last_dim(valid_length, output: tensor, max_min="max"):
    """
    对倒数第一个维度取最， 并在倒数第二个维度设置步长有效索引。
    valid_length: batch * seq
    output: batch * seq * hidden
    ~ 按位取反 与 正负数的补码关系
    https://blog.csdn.net/oAlevel/article/details/79267644

    return: batch * seq_len
    """
    print(output.max(dim=-1)[0], ~valid_length + 2)
    return output.max(dim=-1)[0].masked_fill((~valid_length + 2).to(dtype=torch.bool), -1e9)

# res = mask_last_dim(torch.tensor([[1,1,1,1],[1,1,1,0],[1,1,0,0]]), torch.ones((3,4,5)))


def mask_time_pooling(valid_length, output: tensor, max_min="max"):
    """
    按照时间步取pooling, 并在倒数第二个维度设置步长有效索引。
    valid_length: batch * seq
    output: batch * seq * hidden

    在每个输出通道维度上，判定此时的时间步是否大于有效长度，并mask相应值。
    return: batch * hidden
    """
    if max_min == "avg":
        padding = 0
    elif max_min == "max":
        padding = -1e20
    elif max_min == "min":
        padding = 1e20
    else:
        raise Exception("Unknow arg valus: max_min must be one of {avg/max/min} !")

    # print("input: |\n {} |\n".format(output))
    transposed = output.transpose(2, 1)
    shape_t = transposed.shape
    sum_valid = valid_length.sum(dim=-1)
    valid_length = sum_valid.reshape(shape_t[0], 1, 1).repeat(1, shape_t[1], shape_t[2])
    length_tensor = torch.arange(1, shape_t[-1]+1).repeat(shape_t[0], shape_t[1], 1)
    # batch * hidden* seqlen

    # print(valid_length)
    # print(length_tensor)
    # print(length_tensor > valid_length)
    mask_neg_inf = length_tensor > valid_length

    if max_min == "max":
        return transposed.masked_fill(mask_neg_inf, padding).max(dim=-1)[0]
    elif max_min == "min":
        return transposed.masked_fill(mask_neg_inf, padding).min(dim=-1)[0]
    elif max_min == "avg":
        return transposed.masked_fill(mask_neg_inf, padding).sum(dim=-1) / sum_valid.unsqueeze(dim=-1)
    else:
        raise Exception("Unknow arg valus: max_min must be one of {avg/max/min} !")


res = mask_time_pooling(torch.tensor([[1,1,1,1],[1,1,1,0],[1,1,0,0]]), torch.randn((3,4,5)), max_min="avg")
print(res)

# print(res)