
"""
可以推导出构建一棵树的递归方程是T(n)=2T(n/2)+R
其中R是一个时间常数
可以试着在图上画出这个线段树，可以计算出树的高度是 log2(n)
那么按照常规来,第一个节点的时间是T(n)+R
然后我们再将T(n)分摊给他的两个子节点,可以推出
T(n)=2T(n/2)+R
如此迭代下去，可以推出T(n)

T(n)=R+2R+4R+....+R2x-1

然后这个数列的长度是log2(n)
根据等比数列求和
可以算出T(n)=(n/2-1)R
那么时间复杂度就是O(n)

作者：YellowTag
链接：https://www.jianshu.com/p/fac41cc1f2a6
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
class SegmentTree(object):
    def __init__(self, array, merge_func=None):
        self.array = array
        self.st = self.build_st(array, merge_func)
        self.lazy_tag = [None] * len(self.st)
        self.merge_func = merge_func

    def build_st(self, array, merge_func=None):
        st = [0] * (len(array) * 4)

        def recursive_build(st_idx, l, r):
            print(l, st_idx, r)
            if l == r:
                st[st_idx] = array[l]
                return st[st_idx]
            mid = (l + r) // 2
            left = recursive_build(2 * st_idx + 1, l, mid)
            right = recursive_build(2 * st_idx + 2, mid+1, r)
            if merge_func:
                merged_val = merge_func(left, right)
            else:
                merged_val = sum([left, right])
            st[st_idx] = merged_val

            return merged_val

        recursive_build(0, 0, len(array)-1)
        return st

    def query_or_modify(self, l, r, modify_value=None, merge_func=None):
        """
        l: start
        r: end 不包括.
        """

        def recur_query(
            self, control_l, control_r, st_idx, l, r,
            modify_value,
            merge_func=None
        ):
            if r-1 < control_l or l > control_r:
                if not modify_value:
                    return None
                return self.st[st_idx]
            print("-->",st_idx, control_l, control_r, l, r, self.lazy_tag)
            if control_l >= l and control_r < r:
                if modify_value:
                    if merge_func:
                        self.st[st_idx] = merge_func(
                            modify_value * (control_r-control_l + 1),
                            self.st[st_idx])
                    else:
                        self.st[st_idx] = sum(

                            [modify_value * (control_r - control_l + 1),
                            self.st[st_idx]]
                        )
                    self.lay_tag_next_down(st_idx, modify_value)
                print("low", st_idx, control_l, control_r, self.st[st_idx])
                return self.st[st_idx]
            if self.lazy_tag[st_idx] is not None:   # lazy tag 下放

                self.lay_tag_next_down(st_idx, modify_value)
                if merge_func:

                    self.st[st_idx] = merge_func(
                        self.lazy_tag[st_idx] * (control_r - control_l + 1),
                        self.st[st_idx]
                    )
                else:
                    self.st[st_idx] = sum([
                        self.lazy_tag[st_idx] * (control_r - control_l + 1),
                        self.st[st_idx]])
                self.lazy_tag[st_idx] = None

            mid = (control_l + control_r) // 2

            left = recur_query(self, control_l, mid, 2 * st_idx + 1, l, r,
                               modify_value, merge_func)

            right = recur_query(self, mid + 1, control_r, 2 * st_idx + 2, l, r,
                                modify_value, merge_func)
            print(st_idx, control_l, control_r, left, right,"[pp[")
            if left and right:

                if merge_func:
                    new_val = merge_func(left, right)
                    self.st[st_idx] = new_val
                else:
                    new_val = sum([left, right])
                    self.st[st_idx] = new_val
                    return new_val
            if left:
                self.st[st_idx] = left
                return left
            if right:
                self.st[st_idx] = right
                return right
            return None

        return recur_query(self, 0, len(self.array) - 1, 0, l, r, modify_value,
                           merge_func)

    def lay_tag_next_down(self, st_idx, modify_value):
        if (2 * st_idx + 1) < len(self.st):
            self.lazy_tag[2 * st_idx + 1] = modify_value  # 懒惰标记，向上先更新
        if (2 * st_idx + 1) < len(self.st):
            self.lazy_tag[2 * st_idx + 2] = modify_value