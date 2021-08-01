#


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.

# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/submissions/
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head

        former_node = ListNode(None)

        temp_node = head
        while temp_node:
            if temp_node.val == former_node.val:
                former_node.next = temp_node.next
            else:
                former_node = temp_node
            temp_node = temp_node.next

        return head


# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/submissions/

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def need_del(root):
            if not root:
                return False, root

            temp_node = root
            if not temp_node.next or temp_node.next.val != temp_node.val:
                return False, temp_node.next
            else:
                while temp_node.next.val == temp_node.val:
                    temp_node = temp_node.next
                    if not temp_node.next:
                        return True, None

                return True, temp_node.next

        temp_node = head
        if not temp_node:
            return temp_node

        former_node = None
        while temp_node:
            need_reaplce, next_node = need_del(temp_node)

            if need_reaplce:
                if former_node:
                    former_node.next = next_node
                else:
                    head = next_node
                temp_node = next_node
            else:
                former_node = temp_node
                temp_node = temp_node.next

        return head


# https://leetcode-cn.com/problems/reverse-linked-list/submissions/
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_node = head
        if not temp_node:
            return head

        former = None
        while temp_node:

            next_ = temp_node.next
            temp_node.next = former
            if not next_:
                break
            former = temp_node
            temp_node = next_

        return temp_node


# https://leetcode-cn.com/problems/linked-list-cycle/submissions/
# 快慢指针，你值得拥有


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return False

        fast = head.next.next
        slow = head.next
        while  fast and slow:
            if fast == slow:
                return True
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return False

# TODO 如何找到环的开始


# 翻转链表
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp_n = head
        former = None
        while temp_n:
            next_n = temp_n.next
            temp_n.next = former
            former = temp_n
            temp_n = next_n
        return former


# 翻转链表的递归解法
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def reverse(head):
            """
            :type head: ListNode
            :rtype: ListNode
            """
            if not head:
                return None, None

            r_h, r_t = reverse(head.next)
            if not r_t:
                return head, head

            r_t.next = head
            head.next = None
            return r_h, head

        return reverse(head)[0]

# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution(object):
    """
    双指针解法
    实际上这道题是滑动窗口标准解法
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        point1 = point2 = 0

        max_len = 0
        # temp_len = 0
        exist = {}
        while point2 < len(s):
            if s[point2] in exist:
                temp_len = point2 - point1
                if temp_len > max_len:
                    max_len = temp_len

                if exist[s[point2]] >= point1:
                    point1 = exist[s[point2]] + 1

            exist[s[point2]] = point2
            point2 += 1

        max_len = max(max_len, point2 - point1)

        return max_len


# TODO
# https://leetcode-cn.com/problems/minimum-window-substring/