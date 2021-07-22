# encoding: utf-8

from typing import List, Set, Dict
# 邻接链表

"""simple
{
    "node ida": {
        "node_idb": weight,
        ...
    } // node a connect with node b(directed a->b) with weight num.
}

"""


""" complex



"""


class Vertex(object):
    def __init__(self, node_id, connects: dict):
        self.node_id = node_id
        self.connects = connects
        self.min_cost = None    # 最小花费，例如最小生成树中的到已入树的集合的最近距离
        """
        {
            node_id； val,
            ...
        }
        """

    def add_conncet(self, to_node, weight):
        if to_node in self.connects:
            print("node：{}已经在联调节点中了， 强制替换".format(to_node))
        self.connects[to_node] = weight


class Graph(object):
    def __init__(self, vertexs: List[Vertex]):
        self.vertexes: List[Vertex] = []
        self.vertex_mapper = {vec.node_id: vec for vec in vertexs}
        self.vertex_num = len(self.vertexes)

    def add_vertex(self, a_vertex: Vertex):
        self.vertexes.append(a_vertex)

    def update(self):
        self.vertex_num = len(self.vertexes)

    def get_vertex(self, node_id):
        return self.vertex_mapper.get(node_id, None)


