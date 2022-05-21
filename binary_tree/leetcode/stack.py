"""
栈的后进先出特点可以用于解决匹配任务。
常见如括号匹配。
https://leetcode.cn/problems/longest-valid-parentheses/
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []

        max_len = 0
        former_ed = {}
        for idx, val in enumerate(s):
            if val == "(":
                stack.append(idx)
            else:
                ed = idx
                if not stack:
                    continue
                st = stack.pop(-1)
                if st-1 in  former_ed:
                    max_len = max(max_len, former_ed[st-1]+ed-st+1)
                    former_ed[ed] = former_ed[st-1]+ed-st+1
                else:
                    max_len = max(ed - st+1, max_len)
                    former_ed[ed] = ed-st+1
                # print(former_ed)
        return max_len