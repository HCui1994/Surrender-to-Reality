class Sort:
    @staticmethod
    def mergesort(arr):
        from copy import deepcopy
        if len(arr) < 2:
            return arr
        temp = deepcopy(arr)
        Sort._mergesort_partition(arr, temp, 0, len(arr))
        for i in range(len(arr)):
            arr[i] = temp[i]
        del temp

    @staticmethod
    def _mergesort_partition(arr, temp, low, high):
        if high - low > 1:
            mid = low + (high - low) // 2
            Sort._mergesort_partition(arr, temp, low, mid)
            Sort._mergesort_partition(arr, temp, mid, high)
            Sort._mergesort_merge(arr, temp, low, mid, high)

    @staticmethod
    def _mergesort_merge(arr, temp, low, mid, high):
        i, j, k = low, mid, low
        while i < mid and j < high:
            if arr[i] < arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        if i == mid:
            temp[k: high] = arr[j: high]
        else:
            temp[k: high] = arr[i: mid]
        arr[low: high] = temp[low: high]

    @staticmethod
    def quicksort(arr):
        if len(arr) < 2:
            return arr
        Sort._quicksort_helper(arr, 0, len(arr))

    @staticmethod
    def _quicksort_partition(arr, low, high):
        pivot = arr[low]
        mt, ht = low, high
        i = low + 1
        while i < ht:
            if arr[i] == pivot:
                i += 1
            elif arr[i] < pivot:
                arr[mt], arr[i] = arr[i], arr[mt]
                i += 1
                mt += 1
            else:
                arr[ht - 1], arr[i] = arr[i], arr[ht - 1]
                ht -= 1
        return mt, ht

    @staticmethod
    def _quicksort_helper(arr, low, high):
        if high - low > 1:
            mt, ht = Sort._quicksort_partition(arr, low, high)
            Sort._quicksort_helper(arr, low, mt)
            Sort._quicksort_helper(arr, ht, high)

    @staticmethod
    def heapsort(arr):
        if len(arr) < 2:
            return arr
        Sort._heapify(arr)
        for endpos in range(len(arr) - 1, 0, -1):
            arr[0], arr[endpos] = arr[endpos], arr[0]
            Sort._sinkdown(arr, 0, endpos - 1)
        arr[:] = arr[::-1]
        

    @staticmethod
    def _sinkdown(arr, pos, endpos):
        while pos * 2 + 1 <= endpos:
            if pos * 2 + 2 > endpos:
                minchild = pos * 2 + 1
            else:
                if arr[pos * 2 + 1] < arr[pos * 2 + 2]:
                    minchild = pos * 2 + 1
                else:
                    minchild = pos * 2 + 2
            if arr[pos] >= arr[minchild]:
                arr[pos], arr[minchild] = arr[minchild], arr[pos]
                pos = minchild
                continue
            break

    @staticmethod
    def _heapify(arr):
        for pos in reversed(range(len(arr) // 2)):
            Sort._sinkdown(arr, pos, len(arr) - 1)


if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    Sort.mergesort(arr)
    print(arr)
    
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    Sort.quicksort(arr)
    print(arr)

    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    Sort.heapsort(arr)
    print(arr)