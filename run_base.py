from binary_tree.leetcode.heap import Heap
from binary_tree.leetcode.segment_tree import SegmentTree

# class Node(object):
#     def __init__(self, val):
#         self.val = val
#
#
# def print_(nodes):
#     print([_.val for _ in nodes])
#
#
# res = Heap([Node({"num":3}),Node({"num":5}),Node({"num":1}),Node({"num":30}),
#             Node({"num":21}),Node({"num":9}),Node({"num":107}),
#             Node({"num":3}),Node({"num":22}),Node({"num":51})],
#             compare_key="num"
#            )
# print_(res.heap)
# res.insert_tail(Node({"num":100}))
# print_(res.heap)
# print_(res.sort())

# print(res.pop_head(), res.heap)


st = SegmentTree(
    [
        1,2,3,4
    ],
    merge_func=min
)
print(st.st)

res = st.query_or_modify(0, 3, modify_value=0, merge_func=min)
print(res, st.st)