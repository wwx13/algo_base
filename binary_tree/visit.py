# encoding: utf-8
from typing import List


class Tree(object):
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class BTTree(object):
    def __init__(self, seq):
        self.root = None
        self.insert(*seq)

    def insert(self, *args):
        # 二叉索引树构建
        if not args:
            return
        if not self.root:
            self.root = Tree(args[0])
            args = args[1:]
        for i in args:
            seed = self.root
            while True:
                if i > seed.value:
                    if not seed.right:
                        node = Tree(i)
                        seed.right = node
                        break
                    else:
                        seed = seed.right
                else:
                    if not seed.left:
                        node = Tree(i)
                        seed.left = node
                        break
                    else:
                        seed = seed.left


def visit(tree):
    print(tree.value)


def preorder_visit_recur(tree: Tree):
    """先序递归遍历"""
    if not tree:
        return
    # visit(tree)
    preorder_visit_recur(tree.left)
    visit(tree)
    preorder_visit_recur(tree.right)


def preorder_visit_none_recur(tree: Tree):
    """先序非递归"""
    stack = []

    temp_node = tree
    while stack or temp_node:
        visit(temp_node)
        stack.append(temp_node)
        temp_node = temp_node.left
        while not temp_node and stack:
            temp_node = stack.pop()
            temp_node = temp_node.right


def midorder_visit_none_recur(tree: Tree):
    """中序非递归"""
    stack = []

    temp_node = tree
    while stack or temp_node:
        stack.append(temp_node)
        temp_node = temp_node.left
        while not temp_node and stack:
            temp_node = stack.pop()
            if temp_node:   # 相比于先序只是移到这里
                visit(temp_node)
            temp_node = temp_node.right


def lastorder_visit_none_recur(tree: Tree):
    """中序非递归"""
    stack = []

    temp_node = tree
    while stack or temp_node:
        stack.append((temp_node, 1))
        temp_node = temp_node.left
        while not temp_node and stack:
            # 相比于前序、中序，需要额外的信号
            # pop第一次时再压入栈等待下次访问,直接访问右子树; pop第二次时再访问。
            temp_node, time = stack.pop()
            if time == 1:
                stack.append((temp_node, time + 1))
                temp_node = temp_node.right
            else:
                visit(temp_node)
                temp_node = None


def level_vist_norecur(tree: Tree):
    """队列(非递归）实现层次遍历"""
    if not tree:
        return None
    queue = [tree]

    while queue:
        temp_node = queue.pop(0)
        visit(temp_node)
        if temp_node.left:
            queue.append(temp_node.left)
        if temp_node.right:
            queue.append(temp_node.right)


def level_vist_recur(trees: List[Tree]):
    """递归实现层次遍历"""
    next_layer_trees = []
    if not trees:
        return
    for tree in trees:
        visit(tree)
        if tree.left:
            next_layer_trees.append(tree.left)
        if tree.right:
            next_layer_trees.append(tree.right)
    level_vist_recur(next_layer_trees)


def merge_sort(data: List[int]):
    pass