


# 反向邻接链表
# 头是入度节点， 内容为 出度的各节点
# https://leetcode-cn.com/problems/course-schedule/submissions/
def build_adj_linked_list(G, req):
    reversed_G = {}
    for i in req:
        G[i[0]].append(i[1])
        if i[1] not in reversed_G:
            reversed_G[i[1]] = [i[0]]
        else:
            reversed_G[i[1]].append(i[0])
    return G, reversed_G


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        sorted_nodes = []
        init_graph = {i: [] for i in range(numCourses)}
        G, reversed_G = build_adj_linked_list(init_graph, prerequisites)
        only_out_nodes = []
        for i in G:
            if not G[i]:
                only_out_nodes.append(i)
        if len(only_out_nodes) > numCourses:
            return True
        while len(sorted_nodes) < numCourses:
            if only_out_nodes == []:
                return False
            temp = only_out_nodes.pop(-1)
            sorted_nodes.append(temp)
            if temp not in reversed_G:
                continue
            for n in reversed_G[temp]:
                G[n].remove(temp)
                if not G[n]:
                    only_out_nodes.append(n)
        return True


