# HARD级题目



# 1
def check(tgt, temp):
    """检查目标和当前区间信息是否完全匹配
    这个函数的复杂度较高 0(len(s))
    """
    if len(tgt) != len(temp):
        return False
    for key in tgt:
        if key not in temp or temp[key] < tgt[key]:
            return False
    return True


def add(s, exist):
    """维护存在的频次信息"""
    if s in exist:
        exist[s] += 1
    else:
        exist[s] = 1
    return exist


class Solution(object):

    def minWindow(self, s, t):
        """

        维护两个指针l,r：
        如果当前区间[l,r)的信息和目标值比少，则移动右指针
        如果相同则根据长度是否最短更新结果，然后移动l指针到下一个在t中的字符。
        O(len(s)^2)
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        left = right = 0
        min_len = 999999999999
        st = None
        ed = None
        exist = {}
        tgt = {}
        for i in t:
            if i not in tgt:
                tgt[i] = 1
            else:
                tgt[i] += 1

        while left < len(s) or right < len(s):
            c = check(tgt, exist)
            while not c and right < len(s):
                if s[right] in tgt:
                    exist = add(s[right], exist)
                right += 1
                c = check(tgt, exist)
            temp_len = right - left

            if temp_len < min_len and c:
                min_len = temp_len
                st = left
                ed = right
            elif not c:
                break

            if s[left] in exist:
                exist[s[left]] -= 1
            left += 1
            while left < len(s) and s[left] not in exist:
                left += 1

        if st is None or ed is None:
            return ""
        return s[st:ed]


# 2 更快的方式

def check(tgt, temp):
    """返回还需要匹配的tgt内容
    O(t)
    """
    new_tgt = tgt.copy()
    for key in temp:
        new_tgt[key] -= temp[key]
        if new_tgt[key] <= 0:
            new_tgt.pop(key)
    return new_tgt


def add(s, exist):
    if s in exist:
        exist[s] += 1
    else:
        exist[s] = 1
    return exist


class Solution(object):

    def minWindow(self, s, t):
        """

        维护两个指针l,r：
        如果当前区间[l,r)的信息和目标值比少，则移动右指针
        如果相同则根据长度是否最短更新结果，然后移动l指针到下一个在t中的字符。
        其中， 维护的是区间需要匹配的剩余内容， 这个是通过记录当前区间范围内容包含在tgt中元素的
        数目达到的。

        O(len(s) * len(t) )
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        left = right = 0
        min_len = 9999999
        st = None
        ed = None

        tgt = {}
        for i in t:
            if i not in tgt:
                tgt[i] = 1
            else:
                tgt[i] += 1
        # print(tgt)
        need_next = tgt
        over_n = {}
        while left < len(s) or right < len(s):
            c = need_next

            while c and right < len(s):
                if s[right] in c:
                    c = check(c, {s[right]: 1})
                elif s[right] in tgt:
                    if s[right] not in over_n:
                        over_n[s[right]] = 0
                    over_n[s[right]] += 1
                right += 1

            temp_len = right - left
            if temp_len < min_len and not c:
                min_len = temp_len
                st = left
                ed = right
            elif c:
                break

            if s[left] in tgt and (s[left] not in over_n or over_n[s[left]] < 1):
                need_next = {s[left]: 1}
            else:
                if s[left] in tgt:
                    over_n[s[left]] -= 1
                need_next = {}

            left += 1
            while left < len(s) and s[left] not in tgt:
                left += 1

        if st is None or ed is None:
            return ""
        return s[st:ed]


s = "ADOBECODEBANC"
t = "ABC"
s="acbbaca"
t="aba"
s="ab"
t="b"
s="aaaaaaaaaaaabbbbbcdd"
t="abcdd"
# s="a"
# t="aa"
res = Solution().minWindow(s, t)
print(res)


