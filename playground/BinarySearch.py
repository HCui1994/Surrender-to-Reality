class BinarySearch(object):
    @staticmethod
    def bs1(array, value, low=0, high="default"):
        if high == "default":
            high = len(array)
        while low < high:
            mid = low + (high - low) // 2  # 防止溢出
            if array[mid] >= value:  # 寻找 第一个 大于等于 value 的下标
                high = mid
            else:
                low = mid + 1
        return low

    @staticmethod
    def bs2(array, value, low=0, high="default"):
        if high == "default":
            high = len(array)
        while low < high:
            mid = low + (high - low) // 2
            if array[mid] > value:  # 寻找 第一个 大于 value 的下标
                high = mid
            else:
                low = mid + 1
        return low

    @staticmethod
    def bs3(array, value):
        low, high = -1, len(array) - 1
        while high > low:
            mid = high - (high - low) // 2
            if array[mid] <= value:  # 寻找 最后一个 小于等于 value 的下标
                low = mid
            else:
                high = mid - 1
        return high

    @staticmethod
    def bs4(array, value):
        low, high = -1, len(array) - 1
        while high > low:
            mid = high - (high - low) // 2
            if array[mid] < value:  # 寻找 最后一个 小于 value 的下标
                low = mid
            else:
                high = mid - 1
        return high


if __name__ == "__main__":
    bisect = BinarySearch()
    print(bisect.bs1([5, 9], 6))  # 第一个 大于等于 value
    print(bisect.bs2([5, 5, 5], 6))  # 第一个 大于 value
    print(bisect.bs3([5, 5, 5], 6))  # 最后一个 小于等于 value
    print(bisect.bs4([5, 5, 5], 6))  # 最后一个 小于 value
