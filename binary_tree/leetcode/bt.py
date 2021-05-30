# 二叉树和分治相关的简单题目实现

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/submissions/

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# https://leetcode-cn.com/problems/balanced-binary-tree/submissions/

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import math

        def recur(node):
            if node is None:
                return True, 0
            left = recur(node.left)
            right = recur(node.right)
            return abs(left[1] - right[1]) <= 1 and left[0] and right[0], max(
                left[1], right[1]) + 1

        return recur(root)[0]


# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/submissions/
# TODO 值得做一做的hard题目;思路是 向上固定返回连通的最大路径和；全局固定记录最大的非连通最大路径和

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_num = -999999

        def recur(root):
            if not root:
                return False, -999999

            left_is_connected, left_max_path = recur(root.left)
            right_is_connected, right_max_path = recur(root.right)
            # print(root.val, "{}/{}; {}/{}".format(left_is_connected, left_max_path
            # , right_is_connected, right_max_path))
            if left_is_connected and right_is_connected:
                not_connected = max(left_max_path + root.val + right_max_path,
                                    left_max_path, right_max_path)
            else:
                not_connected = max(left_max_path, right_max_path)

            connected = root.val
            if left_is_connected:
                connected = max(left_max_path + root.val, connected)
            if right_is_connected:
                connected = max(right_max_path + root.val, connected)

            if not_connected > self.max_num:
                self.max_num = not_connected

            return True, connected

        res = recur(root)

        return max(res[1], self.max_num)


# https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.most_close_node = None

        def recur_find_node(node, nodes):

            if not node or not nodes:
                return 0
            if node.val in nodes:
                all_node_num = 1
                if recur_find_node(node.left, nodes) + recur_find_node(node.right,
                                                                       nodes) == 1:
                    all_node_num = 2
                    self.most_close_node = node
            else:
                left_num = recur_find_node(node.left, nodes)
                right_num = recur_find_node(node.right, nodes)
                if left_num == right_num == 1:
                    self.most_close_node = node
                all_node_num = left_num + right_num
            return all_node_num

        recur_find_node(root, [p.val, q.val])
        return self.most_close_node


# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/submissions/

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def visit(node, level, res):
            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)

        def level_vist_norecur(tree):
            """队列(非递归）实现层次遍历"""
            if not tree:
                return []
            queue = [(tree, 0)]
            res = []
            while queue:
                temp_node, level = queue.pop(0)
                visit(temp_node, level, res)
                if temp_node.left:
                    queue.append((temp_node.left, level + 1))
                if temp_node.right:
                    queue.append((temp_node.right, level + 1))
            return res

        return level_vist_norecur(root)


# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def visit(node, level, res):
            if len(res) == level:
                res.insert(0, [node.val])
            else:
                res[0].append(node.val)

        def level_vist_norecur(tree):
            """队列(非递归）实现层次遍历"""
            if not tree:
                return []
            queue = [(tree, 0)]
            res = []
            while queue:
                temp_node, level = queue.pop(0)
                visit(temp_node, level, res)
                if temp_node.left:
                    queue.append((temp_node.left, level + 1))
                if temp_node.right:
                    queue.append((temp_node.right, level + 1))
            return res

        return level_vist_norecur(root)


# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/submissions/

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        def recur_vist(nodes, order="left"):
            if not nodes:
                return [[]]

            res = [[]]
            next_level = []

            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                if order == "left":
                    res[0].append(node.val)
                else:
                    res[0].insert(0, node.val)
            next_order = "left" if order == "right" else "right"
            next_res = recur_vist(next_level, next_order)

            if next_res[0]:
                res.extend(next_res)
            return res

        if not root: return []
        return recur_vist([root])


# https://leetcode-cn.com/problems/validate-binary-search-tree/submissions/
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def recur_visit(node):

            if not node:
                return True, None, None

            left_res = recur_visit(node.left)
            right_res = recur_visit(node.right)
            # print(node.val, left_res, right_res)
            if left_res[0] and right_res[0] and (
                    (left_res[2] < node.val or left_res[2] is None)
                    and (right_res[1] > node.val or right_res[1] is None)):
                is_valid = True
                min_ = max_ = node.val
                if left_res[2]:
                    max_ = max(max_, left_res[2])
                    min_ = min(min_, left_res[1])
                if right_res[2]:
                    max_ = max(max_, right_res[2])
                    min_ = min(min_, right_res[1])

                return is_valid, min_, max_
            return False, None, None

        return recur_visit(root)[0]


# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val is None:
            return root
        if root is None:
            return TreeNode(val)

        def recur(node, val):
            if not node:
                return

            if node.val > val:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    recur(node.left, val)
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    recur(node.right, val)

        recur(root, val)
        return root