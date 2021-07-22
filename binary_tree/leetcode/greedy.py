
# https://leetcode-cn.com/problems/non-overlapping-intervals/submissions/
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        res = sorted(intervals, key=lambda x:x[1])
        small = None

        skip = 0
        for i in res:
            if small is None:
                small = i[1]
                continue
            if small is not None:
                if i[0] < small:
                    # print(small, i)
                    skip += 1
                else:
                    small = i[1]
        return skip


#
class Solution(object):
    # TIME OUT
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        print(s,p)
        if not s and p =="*"*len(p):
            return True
        if (not s and p) or (not p and s):
            return False
        if not s and not p:
            return True
        pass_id = 0
        for ix, i in enumerate(s):
            # print(pass_id, p)
            if p[pass_id] != "*":
                if p[pass_id] == "?" or p[pass_id] == i:
                    pass_id += 1
                    if pass_id == len(p):
                        if ix == len(s) - 1:
                            return True
                        return False
                else:
                    return False
            else:
                print("??")
                if pass_id == len(p) - 1: return True
                for j in range(pass_id + 1, len(p)):
                    if p[j] not in ["*"]:
                        pass_id = j
                        break
                if pass_id < j:
                    return True
                for next_s_id in range(ix, len(s)):
                    if s[next_s_id] == p[pass_id] or p[pass_id] == "?":
                        res = self.isMatch(s[(next_s_id + 1):], p[(pass_id + 1):])
                        if res:
                            return True
        # print(p[pass_id:])
        if p[pass_id:] == "*"*(len(p)-pass_id):
            return True
        return False

# https://leetcode-cn.com/problems/wildcard-matching/
class Solution(object):
    # 记忆化搜索勉强过
    def __init__(self):
        self.mem = {}

    def add(self, s, p, res):
        if s in self.mem:
            if p not in self.mem[s]:
                self.mem[s][p] = res
        else:
            self.mem[s] = {p: res}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s in self.mem:
            if p in self.mem[s]:
                return self.mem[s][p]

        if not s and p == "*" * len(p):
            self.add(s, p, True)
            return True
        if (not s and p) or (not p and s):
            self.add(s, p, False)
            return False
        if not s and not p:
            self.add(s, p, True)
            return True
        pass_id = 0
        for ix, i in enumerate(s):
            if p[pass_id] != "*":
                if p[pass_id] == "?" or p[pass_id] == i:
                    pass_id += 1
                    if pass_id == len(p):
                        if ix == len(s) - 1:
                            self.add(s, p, True)
                            return True
                        self.add(s, p, False)
                        return False
                else:
                    self.add(s, p, False)
                    return False
            else:
                if pass_id == len(p) - 1: return True
                for j in range(pass_id + 1, len(p)):
                    if p[j] not in ["*"]:
                        pass_id = j
                        break
                if pass_id < j:
                    self.add(s, p, True)
                    return True
                for next_s_id in range(ix, len(s)):

                    if s[next_s_id] == p[pass_id] or p[pass_id] == "?":
                        res = self.isMatch(s[(next_s_id + 1):], p[(pass_id + 1):])
                        if res:
                            self.add(s, p, True)
                            return True
            if p[pass_id:] == "*" * (len(p) - pass_id):
                self.add(s, p, True)
                return True
        self.add(s, p, False)
        return False
s="adceb"
p="*a*b"
s="acbcb"
p="a*c?b"
s="abcabczzzde"
p="*abc???de*"
s="c"
p="*?*"
r = Solution().isMatch(s=s, p=p)
print(r)