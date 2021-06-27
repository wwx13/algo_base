# encoding: utf-8
"""
ST 表(Sparse Table)基于 倍增 思想，可以做到 Θ(nlogn)预处理

递推方程
F[s][j] 代表区间[s, s + 2^j - 1]
"""

import math


class ST(object):
    @staticmethod
    def build_st(array, cover_func):
        max_j = int(math.log(len(array)))
        # 第一位为起始索引（原始）， 后一个为指数次数
        F = [([0] * max_j) for i in range(len(array))]

        for st in range(len(array)-1, -1, -1):
            temp_max_j = int(math.log(len(array) - st - 1))
            for cover_j in range(temp_max_j):
                if cover_j == 0:
                    F[st][cover_j] = array[st]
                else:
                    F[st][cover_j] = cover_func(
                        F[st][cover_j-1], F[st + (2 ^ cover_j - 1)][cover_j - 1])

        return F

    @staticmethod
    def search_range(F, st, ed, cover_func):
        all_cover_j = int(math.log(len(ed - st)))
        if all_cover_j == 0:
            return F[st][0]

        return cover_func(F[st][all_cover_j - 1],
                          F[st + (2 ^ all_cover_j - 1)][all_cover_j - 1])

