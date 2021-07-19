# encoding: utf-8


# var
# isVisit
# map[int]
# 保留已经得到的结果，该结构相当于一个备忘录
# 记忆化搜索函数调用者
# 模板
def memorySearchCaller():
    # {
    #  * 1.
    #       进行一些预处理
    #  * 2.
    #   开始调用记忆化搜索函数，返回记忆化搜索结果
    # }
    pass

 # 记忆化搜索函数
def memorySearch():
    # 3.
    #   判断是否需要返回结果以及进行一些剪枝(特殊情况处理)
    #   如果该问题已经求解过了，那么直接返回结果
    if x, ok := isVisit[key]:
        return x

    # 4.
    #   如果没求解，则继续调用记忆化搜索函数，得出结果(一般情况处理)
    #   记录该问题的结果，加入备忘录
    isVisit[key] = ans
    return ans

# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row_n = len(matrix)
        col_n = len(matrix[0])
        mt = [[-1] * len(matrix[0]) for _ in range(len(matrix))]

        # mt[0][0] = 1
        def dfs(i, j):
            if not (0 <= i < row_n and 0 <= j < col_n):
                return None
            if mt[i][j] != -1:
                return mt[i][j]

            for direct in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                next_row = i + direct[0]
                next_col = j + direct[1]
                next_val = dfs(next_row, next_col)
                if mt[i][j] == -1:
                    mt[i][j] = 1
                if 0 <= next_row < row_n and 0 <= next_col < col_n and next_val and \
                        matrix[i][j] > matrix[next_row][next_col]:
                    mt[i][j] = max(mt[i][j], next_val + 1)
            return mt[i][j]

        return max(dfs(i, j) for i in range(row_n) for j in range(col_n))

"""
记忆化搜索的特点：
    1. 函数承载了递推的作用，递推值需要单独记录，但是缓存可以帮助我们不反复递归。

"""
# T5
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/submissions/
#


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = [([i] + ([-1] * len(word2))) for i in range(len(word1) + 1)]
        mem[0] = [i for i in range(len(word2) + 1)]

        def dfs(i, j):
            if mem[i][j] != -1:
                return mem[i][j]
            res = None
            res = min(dfs(i - 1, j) + 1, dfs(i, j - 1) + 1, dfs(i - 1, j - 1) + 2)
            if word1[i - 1] == word2[j - 1]:
                res = min(res, dfs(i - 1, j - 1))

            mem[i][j] = res
            return res

        return dfs(len(word1), len(word2))
        # return r
