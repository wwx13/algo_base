# 最小生成树

from stroe_graph import Graph, build_g
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
        self.compare = {
            "min": min,
            "max": max
        }[max_min]
        self.__build__()

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

    def inset_tail(self, val):
        self.heap.append(val)
        self.bubble(len(self.heap)-1)

    def pop_head(self):
        ret = self.heap.pop(0)
        self.heap.insert(0, self.heap[-1])
        self.heap.pop(-1)
        self.down(0)
        return ret

    def get_array_val(self, idx):
        if self.get_val_func:
            return self.get_val_func(self.heap, idx)

        return self.heap[idx]

    def set_get_val_func(self, func):
        self.get_val_func = func


class MinTree(object):
    def __init__(self, graph: Graph):
        """
        :param graph: 通过类实现的邻接表
        """
        self.graph = graph

        pass

    def prim(self, graph: Graph):
        self.father = {}  # 记录一个节点的父节点
        self.dis = Heap([], max_min="min")
        def get_val(objs, idx):
            return objs[idx]["distance"]
        self.dis.set_get_val_func(get_val)

        head = graph.vertexes[0]
        self.father[head.node_id] = {
            "father": head.node_id,
            "distance": 0
        }
        while len(self.father) < graph.vertex_num:
            # for neibor_node_dis_mapper in head.connects:
            # neibor_node_dis_mapper = graph.get_vertex(neibor_node_id)
            for key, val in head.connects.items():
                self.dis.inset_tail(
                    {
                        "node_id": key,
                        "distance": val,
                        "father_id": head.node_id
                     }
                )
            next_head = None
            while self.dis.heap:
                next_head = self.dis.pop_head()
                if next_head["node_id"] not in self.father:
                    break
                next_head = None
            if not next_head:
                return self.father

            self.father[next_head["node_id"]] = {
                "father": next_head["father_id"],
                "distance": next_head["distance"]
            }
            head = graph.get_vertex(next_head["node_id"])

        return self.father

    def kruscal(self, graph: Graph):
        self.dis = Heap([], max_min="min")
        def get_val(objs, idx):
            return objs[idx]["distance"]
        self.dis.set_get_val_func(get_val)

        g_ids = []
        for vertex in graph.vertexes:
            g_ids.append(vertex.node_id)
            for item in vertex.connects:
                self.dis.inset_tail(
                    {
                        "father": vertex.node_id,
                        "distance": item["distance"],
                        "node_id": item["node_id"]
                    }
                )
        self.father = {}
        union = Union(g_ids)

        while len(self.father) < graph.vertex_num - 1:
            if not self.dis:
                raise Exception("有节点无联通")
            pop_head = self.dis.pop_head()
            idx1 = pop_head["father"]
            idx2 = pop_head["node_id"]
            if union.is_connected(idx1, idx2):
                continue
            union.is_connected(idx1, idx2)
            self.father[idx2] = idx1
        return self.father


if __name__ == "__main__":
    gh = build_g()
    mt = MinTree(gh)
    print(mt.prim(gh))