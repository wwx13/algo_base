# 最小生成树

from .stroe_graph import Graph
"""
Kruscal 算法

1. 对边排序，按权从小到大
2. 选择最小的边，且该边对应的启动
"""


class Union(object):
    def __init__(self, array):
        self.father = list(range(len(array)))   # 存储索引对应关系
        self.array = array

    def find(self, idx):
        if self.father[idx] != idx:
            father = self.find(self.father[idx])
            self.father[idx] = father

        return self.father[idx]

    def union(self, idx1, idx2):
        self.father1 = self.find(idx1)
        self.father2 = self.find(idx2)

        self.father[self.father1] = self.father2

    def is_connected(self, idx1, idx2):
        self.father1 = self.find(idx1)
        self.father2 = self.find(idx2)
        if self.father1 == self.father2:
            return True
        return False


class Heap(object):
    def __init__(self, array, max_min="min"):
        self.heap = list(range(len(array)))  # 记录在array中的位置
        self.array = array
        self.__build__()
        self.compare = {
            "min": min,
            "max": max
        }[max_min]

    def __build__(self):
        for idx in range(len(self.array)//2 + 1, -1, -1):
            self.bubble(idx)

    def bubble(self, idx):
        if idx == 0:
            return
        father_idx = (idx - 1) // 2

        if self.compare(
                self.get_array_val(self.heap[father_idx]),
                self.get_array_val([self.heap[idx]])
        ) == self.get_array_val(self.heap[idx]):
            self.swap(father_idx, idx)
        self.down(father_idx)

    def down(self, idx):
        l_child_idx = 2 * idx + 1
        r_child_idx = 2 * idx + 2
        l_val = self.get_array_val(l_child_idx)
        r_val = self.get_array_val(r_child_idx)
        temp_val = self.get_array_val(idx)

        if self.compare(
           l_val, r_val
        ) == l_val:
            if self.compare(
                temp_val,
                l_val
            ) == l_val:
                self.swap(l_child_idx, idx)
        else:
            if self.compare(
                temp_val,
                r_val
            ) == r_val:
                self.swap(r_child_idx, idx)

    def swap(self, idx1, idx2):
        i1 = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = i1

    def get_array_val(self, idx):
        return self.array[idx].min_cost


class MinTree(object):
    def __init__(self, graph: Graph):
        """
        :param graph: 通过类实现的邻接表
        """
        self.graph = graph

        pass

    def prim(self, graph: Graph):
        self.father = {}  # 记录一个节点的父节点

        head = graph.vertexes[0]
        self.father[head.node_id] = head.node_id
        for neibor_node_id in head.connects:
            neibor_node = graph.get_vertex(neibor_node_id)

        while len(self.father) < graph.vertex_num and

        pass

