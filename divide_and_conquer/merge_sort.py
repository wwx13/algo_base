
# https://leetcode.cn/problems/count-of-smaller-numbers-after-self/submissions/

class Node():
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        不好做的题目
        思路1： 插入排序理论上平均情况下可以过，但是我超时了。因为O(nlogn)里的logn是平均查询情况，n是固定的。最坏情况退化o(n**2)。
        思路2：归并排序， O(nlogn)是严格的复杂度
            1. 左右子序列已经降序排列，并且已知子序列原顺序下的向右关系
            2. 按照双指针归并排序时，同时进行左子序列的右关系更新（根据当前要移动的左指针对应有序列剩余元素个数）
            3. 特别注意，要求的结果顺序是和原序列顺序一致的，不是排序顺序。
        """

        def merge(left, right, update_res):
            l, r = 0, 0
            lg_l = len(left)
            lg_r = len(right)
            new = []

            while l < lg_l and r < lg_r:
                if left[l].val > right[r].val:
                    new.append(left[l])
                    # print(l, lg_l, lg_r, left, right, update_left)
                    update_res[left[l].idx].val += lg_r - r
                    l += 1
                else:
                    new.append(right[r])
                    r += 1

            if l < lg_l:
                new = new + left[l:]
            if r < lg_r:
                new = new + right[r:]
            return new

        def merge_sort(nums, res):
            if not nums or len(nums) == 1:
                return nums
            length = len(nums)

            mid = length // 2

            left_nums = merge_sort(nums[:mid], res)
            right_nums = merge_sort(nums[mid:], res)
            if not left_nums:
                return right_nums
            elif not right_nums:
                return left_nums
            else:
                new = merge(left_nums, right_nums, res)
                return new

        res_nodes = [Node(0, idx) for idx, val in enumerate(nums)]
        merge_sort([Node(val, idx) for idx, val in enumerate(nums)], res_nodes)
        res = [0] * len(nums)
        for n in res_nodes:
            res[n.idx] = n.val
        return res