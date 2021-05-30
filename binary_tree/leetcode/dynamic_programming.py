# encoding: utf-8


# https://leetcode-cn.com/problems/house-robber/submissions/
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return max(dp)

        for temp in range(2, len(nums)):
            dp[temp] = max(dp[temp - 1], dp[temp - 2] + nums[temp])

        return dp[-1]
