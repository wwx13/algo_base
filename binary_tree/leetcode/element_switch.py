
# https://leetcode.cn/problems/first-missing-positive/submissions/

"""置换： 置换的特色是对输入变量做原地修改，以减少内存开销。
很多时候我们希望减少内存开销，那么就可以考虑进行元素替换、交换，只修改原变量不引入
更多变量以此达到目的

"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        nums = set(nums)

        nums = [i for i in nums if i > 0]
        pos_len = len(nums)
        # nums = [i for i in nums if i <= pos_len]
        for idx, val in enumerate(nums):
            while val != idx + 1 and val <= len(nums):
                temp = nums[val - 1]
                nums[val - 1] = val
                nums[idx] = temp
                val = nums[idx]
        # print("nes", nums)
        for idx, val in enumerate(nums):
            if idx + 1 != val:
                return idx + 1
        return len(nums) + 1

