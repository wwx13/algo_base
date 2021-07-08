"""
递归与回溯
"""

# https://leetcode-cn.com/problems/eight-queens-lcci/
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def is_valid(former, temp):
            for idx, val in enumerate(former):
                if val[1] == temp[1] or (
                        abs(temp[1] - val[1]) == abs(temp[0] - val[0])):
                    return False
            return True

        all_res = []
        temp_route = []
        temp_idx = []

        def dfs(level):
            if level == n:
                all_res.append([i for i in temp_route])
                return None

            for i in range(n):
                if is_valid(temp_idx, (level, i)):
                    temp_route.append("." * i + "Q" + "." * (n - i - 1))
                    temp_idx.append((level, i))
                    dfs(level + 1)
                    temp_route.pop(-1)
                    temp_idx.pop(-1)

        dfs(0)
        return all_res