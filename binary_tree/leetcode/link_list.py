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