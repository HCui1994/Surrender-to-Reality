"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""


class NumArray:

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
