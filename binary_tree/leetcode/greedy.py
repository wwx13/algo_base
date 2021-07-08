
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