# encoding: utf-8

# https://leetcode-cn.com/problems/connecting-cities-with-minimum-cost
# https://leetcode-cn.com/circle/article/3HR7QC/
# https://leetcode-cn.com/problems/min-cost-to-connect-all-points/
class Union(object):

    def __init__(self, array):
        self.father = list(range(len(array)))
        self.array = array

    def query(self, idx):
        if self.father[idx] != self.array[idx]:
            self.array[idx] = self.query(self.father[idx])
        return self.array[idx]

    def is_connect(self, idx1, idx2):
        if self.query(idx1) == self.query(idx2):
            return True
        return False

    def conncet(self, idx1, idx2):
        self.father[self.query(idx1)] = self.query(idx2)
        return None


class BuildMinTree(object):
    def __init__(self, ):
        pass
    def prim(self):






# copy from blog of csdn
from collections import defaultdict
from heapq import heapify, heappop, heappush


def prim(nodes, edges):
    conn = defaultdict(list)
    for n1, n2, c in edges:
        conn[n1].append((c, n1, n2))
        conn[n2].append((c, n2, n1))

    mst = []
    used = set(nodes[0])
    usable_edges = conn[nodes[0]][:]
    heapify(usable_edges)

    while usable_edges:
        cost, n1, n2 = heappop(usable_edges)
        if n2 not in used:
            used.add(n2)
            mst.append((n1, n2, cost))

            for e in conn[n2]:
                if e[2] not in used:
                    heappush(usable_edges, e)
    return mst


nodes = list("ABCDEFG")
edges = [("A", "B", 7), ("A", "D", 5),
         ("B", "C", 8), ("B", "D", 9),
         ("B", "E", 7), ("C", "E", 5),
         ("D", "E", 15), ("D", "F", 6),
         ("E", "F", 8), ("E", "G", 9),
         ("F", "G", 11)]


# ————————————————
# 版权声明：本文为CSDN博主「wh_springer」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / wh_springer / article / details / 52771813