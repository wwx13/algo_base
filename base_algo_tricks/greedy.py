

# https://leetcode-cn.com/submissions/detail/182964523/
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        if not ratings:
            return []
        if len(ratings) == 1:
            return 1
        base = [1] * len(ratings)
        data = ratings
        for i in range(1, len(data)):
            if data[i - 1] < data[i]:
                base[i] = base[i - 1] + 1

        for i in range(len(data) - 2, -1, -1):
            if data[i] > data[i + 1]:
                if base[i] > base[i + 1]:
                    continue
                else:
                    base[i] = base[i + 1] + 1
        return sum(base)