class BinarySearch(object):
    @staticmethod
    def lower_bound(array, value, low=0, high="default"):
        """
        返回 [low, high) 左闭右开区间中，以 value 作为下界的值的最小值的下标
        """
        if high == "default":
            high = len(array)
        while low < high:
            mid = low + (high - low) // 2  # 防止溢出
            if array[mid] < value:
                low = mid + 1
            else:
                high = mid
        return low  # return last 亦可

    @staticmethod
    def upper_bound(array, value, low=-1, high="default"):
        """
        返回 (low, high] 左开右闭区间中，以 value 作为上界的最大值的下标
        """
        if high == "default":
            high = len(array) - 1
        while high > low:
            mid = high - (high - low - 1) // 2
            if array[mid] > value:
                high = mid - 1
            else:
                low = mid
        return high

bisearch = BinarySearch()
a = [1, 2, 2, 3, 4, 4, 4, 6, 6, 6, 7, 8, 9]
print(bisearch.lower_bound(a, 6))
print(bisearch.upper_bound(a, 6))

import bisect
print(bisect.bisect_left(a, 6))
print(bisect.bisect_right(a, 6))