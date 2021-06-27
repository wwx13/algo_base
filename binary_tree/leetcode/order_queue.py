

# https://leetcode-cn.com/problems/sliding-window-maximum/submissions/
# https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/submissions/
class OrderQueue(object):
    """
    单调队列实现:
        此处的队列是可以在队尾出队和入队， 可以从队头出队，
        这也是和单调栈的区别
    """

    @staticmethod
    def slide_window_get_max_k(array, slide_sep_k):
        dequeue = []

        max_k = []
        st_counter = 0  # 当前考虑比较的k个数的开头

        for idx, val in enumerate(array):
            if dequeue:
                while dequeue and dequeue[-1][0] <= val:
                    dequeue.pop(-1)

            dequeue.append((val, idx))
            if idx - st_counter == (slide_sep_k-1):
                max_k.append(dequeue[0][0])
                if dequeue[0][1] <= st_counter:
                    dequeue.pop(0)

                st_counter += 1
        return max_k

nums = [1,3,-1,-3,5,3,6,7]
k = 3

res = OrderQueue().slide_window_get_max_k(nums, k)
print(res)