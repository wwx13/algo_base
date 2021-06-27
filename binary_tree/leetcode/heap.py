# encoding: utf-8

"""
堆的操作元素使用自定义的Node类型，这样方便实际套用，因为实际使用中，经常需要排序元素和自带的属性一起
随着数据结构变化。
"""


class Node(object):
    def __init__(self, val):
        # define any other attrs in val.
        # val = {"name1":, "name2":}
        self.val = val


class Heap(object):
    def __init__(self, array, compare_key):
        # max_heap
        # [like Node instance]
        self.array = array
        self.compare_key = compare_key
        self.heap = self.build_heap(self.array)

    def bubble(self, idx, heap=None):
        if heap is None:
            heap = self.heap
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[parent].val[self.compare_key] < heap[idx].val[self.compare_key]:
                temp = heap[idx]
                heap[idx] = heap[parent]
                heap[parent] = temp
                idx = parent
            else:
                break

    def down(self, idx, heap=None):
        if heap is None:
            heap = self.heap
        while idx < len(heap):
            child_idx_l = 2 * idx + 1
            child_idx_r = 2 * idx + 2
            if child_idx_l < len(heap) and child_idx_r < len(heap):
                max_val = max(heap[idx].val[self.compare_key],
                              heap[child_idx_r].val[self.compare_key],
                              heap[child_idx_l].val[self.compare_key])
                if max_val == heap[idx].val[self.compare_key]:
                    break
                else:
                    if max_val == heap[child_idx_l].val[self.compare_key]:
                        swap = heap[child_idx_l]
                        heap[child_idx_l] = heap[idx]
                        heap[idx] = swap
                        idx = child_idx_l
                    else:
                        swap = heap[child_idx_r]
                        heap[child_idx_r] = heap[idx]
                        heap[idx] = swap
                        idx = child_idx_r
            elif child_idx_l < len(heap):
                max_val = max(heap[idx].val[self.compare_key],
                              heap[child_idx_l].val[self.compare_key])
                if max_val == heap[idx].val[self.compare_key]:
                    break
                else:
                    swap = heap[child_idx_l]
                    heap[child_idx_l] = heap[idx]
                    heap[idx] = swap
                    idx = child_idx_l
            else:
                break

    def pop_head(self):
        head = self.heap.pop(0)
        if self.heap:
            self.heap.insert(0, self.heap[-1])
            self.heap.pop(-1)
            self.down(0)
        return head

    def insert_tail(self, val):
        idx = len(self.heap)
        self.heap.append(val)
        self.bubble(idx)
        pass

    def sort(self):
        max_min_order = []
        while self.heap:
            max_min_order.append(self.pop_head())
        return max_min_order

    def build_heap(self, array):
        for i in range(len(array)//2, -1, -1):
            self.down(i, array)
        return array

# https://leetcode-cn.com/problems/car-pooling/
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """

        """
         双堆
            1.先使用左起点建立小顶堆，后期使用右下车点建立小顶堆。
            2.对于对堆弹出的节点，使用右端点入第二个小顶堆。
            3.第一个小顶堆出堆的条件
                判断当前节点的起始时刻是否大于第二个小顶堆的顶的下车时刻
                    如果大于，则第二个大顶堆出堆顶，循环直到堆空或者不满足大于。累计释放的座位。
                    如果不大于第二个堆顶，则直接判定当前的需要作为和剩余座位情况，如果允许则出第一个堆顶，
                    入第二个堆底并调整堆。
        复杂度 nlogn
        """

        class Node(object):
            def __init__(self, val):
                self.val = {
                    "nums": val[0],
                    "up": val[1],
                    "down": val[2]
                }

        nodes = []
        for item in trips:
            nodes.append(Node(item))
        self.start_heap = Heap(nodes, compare_key="up")
        self.down_heap = Heap([], compare_key="down")
        self.capacity = capacity

        def down_car(up_time):
            # if self.down_heap.heap:
            # print(self.down_heap.heap[0].val["down"] ,"||", up_time)
            while self.down_heap.heap and self.down_heap.heap[0].val[
                "down"] <= up_time:
                self.capacity += self.down_heap.pop_head().val["nums"]

        while self.start_heap.heap:
            st_head = self.start_heap.pop_head()
            up_time = st_head.val["up"]
            # print(st_head.val, self.capacity)
            down_car(up_time)
            # print("--", self.capacity)
            if st_head.val["nums"] > self.capacity:
                return False

            self.capacity -= st_head.val["nums"]
            self.down_heap.insert_tail(st_head)

        return True

# https://leetcode-cn.com/problems/ugly-number-ii/submissions/
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        class Node():
            def __init__(self, val):
                self.val = {
                    "num": val
                }

        alread = set([])
        min_heap = Heap([Node(1)], "num")

        pop = 0
        while pop < n:
            h_ = min_heap.pop_head()
            pop += 1
            for i in [2, 3, 5]:

                tp = (h_.val["num"]) * i
                if tp not in alread:
                    alread.add(tp)
                    min_heap.insert_tail(Node(tp))

        return h_.val["num"]
