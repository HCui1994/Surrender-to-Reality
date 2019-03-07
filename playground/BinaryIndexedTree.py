class BinaryIndexedTree(object):
    """
    A Fenwick tree or binary indexed tree is a data structure that can efficiently update elements and calculate prefix sums in a table of numbers.
    树状数组：一种用于高效处理对一个存储数字的列表进行更新及求前缀和的数据结构。
    可在 O(log n) 时间内得到任意前缀和，并且支持在 O(log n) 时间内动态单点修改
    """

    def __init__(self, nums):
        self.__nums = [0] * (len(nums) + 1)
        self.__fenwick = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def get_nums(self):
        return self.__nums[1:]

    def get_fenwick(self):
        return self.__fenwick[1:]

    def update(self, i, val):
        """
        更新原数组中下标为 i 的元素为 val
        """
        i += 1
        delta = val - self.__nums[i]
        if delta == 0:
            return
        self.__nums[i] = val
        while i < len(self.__fenwick):
            self.__fenwick[i] += delta
            i += i & (-i)

    def query(self, i, j=None):
        """
        返回原数组闭区间 [0, i] 或 [i, j] 的区间和
        """
        res = 0
        if not j:
            i += 1
            while i > 0:
                res += self.__fenwick[i]
                i -= i & (-i)
        else:
            j += 1
            if i == j:
                return self.__nums[j]
            while i > 0:
                res -= self.__fenwick[i]
                i -= i & (-i)
            while j > 0:
                res += self.__fenwick[j]
                j -= j & (-j)
        return res


if __name__ == "__main__":
    operations = ["NumArray", "update", "update", "update", "sumRange", "update", "sumRange", "update", "sumRange", "sumRange", "update"]
    parameters = [[7, 2, 7, 2, 0], [4, 6], [0, 2], [0, 9], [4, 4], [3, 8], [0, 4], [4, 1], [0, 3], [0, 4], [0, 4]]
    for i in range(len(operations)):
        opera = operations[i]
        param = parameters[i]
        if opera == "NumArray":
            bit = BinaryIndexedTree(param)
            print(bit.get_nums())
            print(bit.get_fenwick())
            print("==============")
        elif opera == "update":
            bit.update(param[0], param[1])
            print(bit.get_nums())
            print(bit.get_fenwick())
            print("==============")
        else:
            print(bit.query(param[0], param[1]))
            print("==============")


    
