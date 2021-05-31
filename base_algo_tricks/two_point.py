# encoding: utf-8

"""
双指针滑动窗口的经典写法。右指针不断往右移，移动到不能往右移动为止(具体条件根据题目而定)。
当右指针到最右边以后，开始挪动左指针，释放窗口左边界
(from leet code cookbook)
"""


# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        left = right = 0
        max_len = 1
        set_data = {}
        while right < len(s):
            # print(right)
            set_data[s[right]] = right
            right += 1
            if len(s) == right or (s[right] in set_data and set_data[s[right]] >= left):
                max_len = max(max_len, right - left)
                if len(s) == right: break
                left = set_data[s[right]] + 1
                if left > len(s) - 1:
                    break
                set_data[s[right]] = right

        return max_len


# https://leetcode-cn.com/problems/container-with-most-water/
class Solution(object):
    def maxArea(self, height):
        """
        最左边一个指针，最右边一个指针， 选择其中高度更小的指针向中间移动一步；
        原因是， 只有移动高度低的才有提升容量的希望。
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 0:
            return 0

        left = 0
        right = len(height) - 1
        max_w = 0

        while left < right:
            temp = (right - left) * min(height[left], height[right])
            if temp > max_w:
                max_w = temp
            if height[left] < height[right]:
                left += 1
            else:
                right = 1
        return max_w
