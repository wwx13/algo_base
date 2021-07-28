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
        # self.vertex_num = len(self.vertexes)

    def add_vertex(self, a_vertex: Vertex):
        self.vertexes.append(a_vertex)

    def update(self):
       return len(self.vertexes)

    def get_vertex(self, node_id):
        return self.vertex_mapper.get(node_id, None)

    @property
    def vertex_num(self):
        return self.update()
        # return self.vertex_num


def build_g():

    def cal_dis(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

    node_info = {}
    for idx, val in enumerate(points):
        if idx not in node_info:
            node_info[idx] = {}
        for idx2, later_val in enumerate(points[(idx + 1):]):
            right_idx = idx + 1 + idx2
            dis = cal_dis(val, later_val)
            node_info[idx][right_idx] = dis

            if right_idx not in node_info:
                node_info[right_idx] = {}
            node_info[right_idx][idx] = dis

    gph = Graph([])
    for node_id, connect in node_info.items():
        vt = Vertex(node_id, connect)
        gph.add_vertex(vt)

    return gph


if __name__ == "__main__":
    def cal_dis(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    print("running ")
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

    node_info = {}
    for idx, val in enumerate(points):
        if idx not in node_info:
            node_info[idx] = {}
        for idx2, later_val in enumerate(points[(idx+1):]):
            right_idx = idx + 1 + idx2
            dis = cal_dis(val, later_val)
            node_info[idx][right_idx] = dis

            if right_idx not in node_info:
                node_info[right_idx] = {}
            node_info[right_idx][idx] = dis
    print(node_info)

    gph = Graph([])
    for node_id, connect in node_info.items():
        vt = Vertex(node_id, connect)
        gph.add_vertex(vt)

    print(gph.vertex_num)
