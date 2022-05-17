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
        原
        因是， 只有移动高度低的才有提升容量的希望。
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

# https://leetcode-cn.com/problems/subarrays-with-k-different-integers/submissions/
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        转化问题为 >= K 个不同整数的子数组 减去 >=（K+1）的子数组
        >= K 个不同整数的子数组可以安装滑动窗口累积计算
        """
        def get_num(nums, k):
            dist_dict = {}
            base_left = 0
            base_right = 0
            dist_num = 0
            nums_res = 0

            while base_right < len(nums) and base_left < len(nums):
                temp_val = nums[base_right]
                if dist_num < k:
                    if temp_val not in dist_dict:
                        dist_dict[temp_val] = 1
                        dist_num +=1

                    else:
                        dist_dict[temp_val] +=1
                if dist_num == k:
                    # print(k,base_right, dist_dict)
                    nums_res += max(0, len(nums) - base_right)
                    dist_dict[nums[base_left]] -= 1
                    if dist_dict[nums[base_left]] < 1:
                        dist_dict.pop(nums[base_left])
                        dist_num -= 1
                        base_right += 1

                    base_left += 1
                else:
                    base_right += 1
            return nums_res
        big_eq_k = get_num(nums, k)
        big_eq_k_1 = get_num(nums, k+1)
        # print(big_eq_k, big_eq_k_1)
        # return sum([max(0, big_eq_k[i]-big_eq_k_1[i]) for i in range(len(nums))])
        return max(0, big_eq_k-big_eq_k_1)


# https://leetcode-cn.com/problems/wildcard-matching/submissions/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        引理： 如果从左到右匹配过程中，发现当前字符无法和当前正则字符匹配，则只需要调整最近前面的那个*，如果调整不成功则匹配就失败了。
        证明： 证明主要集中在为什么最近那个通配符而不是靠前的。因为，如果倒数第二个通配符需要匹配更多字符，那么完全也可以由倒数第一个
        通配符去完成。因为，倒数第二个本来和介于倒数第一个通配符之间的正则可以匹配原串，此时倒数第一个通配符就可以完成匹配之后更多对的字符，

        因此我们调整匹配过程，只需要关注在无法匹配时，能不能调整最近通配符贪婪的字符串个数。从少到多的尝试。
        """
        matched_s_ix = 0
        real_matched_s_ix = None
        temp_p_ix = 0
        pointer_star_ix = None

        while matched_s_ix < len(s):
            # print(temp_p_ix)
            if temp_p_ix < len(p) and p[temp_p_ix] != "*" and (s[matched_s_ix] == p[temp_p_ix] or p[temp_p_ix] == "?"):
                matched_s_ix += 1
                temp_p_ix += 1
            elif  temp_p_ix < len(p) and p[temp_p_ix] == "*":
                if temp_p_ix == len(p)-1:
                    return True
                pointer_star_ix = temp_p_ix
                temp_p_ix += 1
                real_matched_s_ix = matched_s_ix
            else:
                if pointer_star_ix is None:
                    return False
                temp_p_ix = pointer_star_ix + 1
                matched_s_ix = real_matched_s_ix + 1
                real_matched_s_ix += 1

            # if temp_p_ix >= len(p) and matched_s_ix <= len(s)-1:
                # return False
        last = p[temp_p_ix:]
        if not last:
            return True
        else:
            return all([i=="*"  for i in last])
