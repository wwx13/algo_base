#

def binary_search(order_data, element):
    if not order_data:
        return None

    if len(order_data) == 1:
        if order_data[0] >= element:
            return 0
        return 1

    mid = len(order_data) // 2

    if order_data[mid] >= element:
        return binary_search(order_data[: mid], element)

    return mid + binary_search(order_data[mid: ], element)


# https://leetcode-cn.com/problems/longest-increasing-subsequence/submissions/
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def binary_search(order_data, element):
            if not order_data:
                return None

            if len(order_data) == 1:
                if order_data[0] >= element:
                    return 0
                return 1

            mid = len(order_data) // 2

            if order_data[mid] >= element:
                return binary_search(order_data[: mid], element)

            return mid + binary_search(order_data[mid:], element)

        if not nums or len(nums) == 1:
            return len(nums)

        upper_seq = []
        for i in nums:
            if not upper_seq:
                upper_seq.append(i)

            elif i > upper_seq[-1]:
                upper_seq.append(i)
            else:
                index = binary_search(upper_seq, i)
                upper_seq[index] = i
        return len(upper_seq)


