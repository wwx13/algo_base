import torch

"""二叉树"""
from binary_tree.visit import (
    preorder_visit_none_recur, BTTree,
    midorder_visit_none_recur, preorder_visit_recur,
    lastorder_visit_none_recur, level_vist_norecur,
    level_vist_recur, merge_sort, quick_sort
)
from binary_tree.visiual import draw

# l = [40, 20, 30, 70, 60, 75, 71, 74]
# l2 = [4, 8, 1, 9]
#
# tree = BTTree(l)
# tree.insert(*l)

# draw(tree.root))
# lastorder_visit_none_recur(tree.root)
# preorder_visit_recur(tree.root)
# midorder_visit_none_recur(tree.root)
# level_vist_recur([tree.root])
# level_vist_norecur(tree.root)_
# print(merge_sort(l))
# print(quick_sort(l2))

# binary search
# from divide_and_conquer.binary_search import binary_search
# res = binary_search([1,2,3,4], 3)
# print(res)

# n queens
from recursive_and_trackback.n_queens import n_queens
print(n_queens(4))

# 其他
# print(torch.ones([10,1]))