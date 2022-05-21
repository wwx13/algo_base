


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True


        def recur(node):
            if not node:
                return True, node

            is_bst_left, root_l = recur(node.left)
            is_bst_right, root_r = recur(node.right)

            is_bst = False
            if is_bst_left and is_bst_right and is_ordered(root_l, node, root_r):
                is_bst = True
            return is_bst, node

        def is_ordered(l, temp, r):
            if not l and not r:
                return True
            if not l:

