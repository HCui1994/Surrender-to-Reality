def quickselect(arr, k):
    return _quickselect(arr, 0, len(arr), k)


def _quickselect(arr, low, high, k):
    if high - low > 1:
        mt, ht = _partition_three_way(arr, low, high)
        if k < mt:
            return _quickselect(arr, low, mt, k)
        elif k < ht:
            return arr[mt]
        else:
            return _quickselect(arr, ht, high, k)
    elif low == k:
        return arr[low]
    elif high == k:
        return arr[high - 1]


def _partition_three_way(arr, low, high):
    pivot = arr[low]
    mt, ht = low, high  # mt: begin index of inerval equal to pivot
    # ht: begin index of interval greater than pivot
    i = low + 1
    while i < ht:
        if arr[i] == pivot:
            i += 1
        elif arr[i] < pivot:
            arr[mt], arr[i] = arr[i], arr[mt]
            mt += 1
            i += 1
        else:
            arr[i], arr[ht - 1] = arr[ht - 1], arr[i]
            ht -= 1
    return mt, ht


# def quicksort(arr):
#     _quicksort(arr, 0, len(arr))


# def _quicksort(arr, low, high):
#     if high - low > 1:
#         mt, ht = _partition_three_way(arr, low, high)
#         print(mt, ht)
#         _quicksort(arr, low, mt)
#         _quicksort(arr, ht, high)


arr = [7, 10, 4, 3, 20, 15]
k = 4
print(quickselect(arr, k - 1))

