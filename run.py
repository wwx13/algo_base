
"""二叉树"""
from binary_tree.visit import (
    preorder_visit_none_recur, BTTree,
    midorder_visit_none_recur, preorder_visit_recur,
    lastorder_visit_none_recur, level_vist_norecur,
    level_vist_recur
)
from binary_tree.visiual import draw

l = [40, 20, 30, 70, 60, 75, 71, 74]

tree = BTTree(l)
# tree.insert(*l)

# draw(tree.root)
# lastorder_visit_none_recur(tree.root)
# preorder_visit_recur(tree.root)
# midorder_visit_none_recur(tree.root)
level_vist_recur([tree.root])
# level_vist_norecur(tree.root)
