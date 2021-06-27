

class UnionSet(object):
    def __init__(self, array):
        self.father = list(range(len(array)))  # father store idx of origin array
        self.array = array

    def find(self, idx):
        """给定一个索引查询其父节点在原array idx"""
        if self.father[idx] != idx:
            self.father[idx] = self.find(self.father[idx])

        return self.father[idx]

    def union(self, idx1, idx2):
        """给定任意两点，联通它们，通过其所属根节点"""
        left_idx = self.find(idx1)
        right_idx = self.find(idx2)
        self.father[left_idx] = right_idx
        return None

# https://leetcode-cn.com/problems/number-of-provinces/
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        num = len(isConnected)
        mask_special = [set() for i in range(num)]
        ust = UnionSet(list(range(num)))
        for idx, row in enumerate(isConnected):
            for ijx, col in enumerate(row[(idx+1):]):
                ijx = ijx + idx + 1
                if ijx in mask_special[idx]:
                    continue
                if col == 1:
                   ust.union(idx, ijx)
                   mask_special[ijx].add(idx)
        real_root = set()
        for i in set(ust.father):
            r = ust.find(i)
            if r not in real_root:
                real_root.add(r)
        return len(real_root)

# https://leetcode-cn.com/problems/longest-consecutive-sequence/
class Union(object):
    def __init__(self, length):
        self.father = list(range(length))

    def query(self, idx):
        if self.father[idx] != idx:
            self.father[idx] = self.query(self.father[idx])
        return self.father[idx]

    def union(self, idx1, idx2):
        root1 = self.query(idx1)
        root2 = self.query(idx2)
        self.father[root1] = root2
        return None


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        row_n = len(nums)
        nums = list(set(nums))
        exist_key_idx = {}
        un = Union(row_n)

        for idx, val in enumerate(nums):
            exist_key_idx[val] = idx
            if val - 1 in exist_key_idx:
                merge_idx = exist_key_idx[val - 1]
                un.union(merge_idx, idx)
            if val + 1 in exist_key_idx:
                un.union(exist_key_idx[val + 1], idx)
        consec = {}
        for idx in un.father:
            root = un.query(idx)
            if root not in consec:
                consec[root] = 1
            else:
                consec[root] += 1
        max_ = 0
        for key, value in consec.items():
            if value > max_:
                max_ = value

        return max_
