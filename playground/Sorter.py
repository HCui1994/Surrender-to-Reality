import timeit


class Sorter:

    @staticmethod
    def quicksort(list):
        start = timeit.default_timer()
        Sorter._quicksort_helper(list, 0, len(list)-1)
        end = timeit.default_timer()
        print("Quick sort time elaspe: " + str((end-start)*1000))


    @staticmethod
    def _quicksort_helper(list, first, last):
        if first < last:
            split_point = Sorter._partition(list, first, last)
            Sorter._quicksort_helper(list, first, split_point-1)
            Sorter._quicksort_helper(list, split_point+1, last)


    @staticmethod
    def _partition(list, first, last):
        pivot = list[first]     # 取第 0 元素作为轴，归位
        leftmark = first + 1    # 从第 1 元素到最后 1 元素，需要重新归位到轴两侧
        rightmark = last
        done = False
        while not done:
            # 左mark <= 右mark 且 左mark处元素小于轴
            while leftmark <= rightmark and list[leftmark] <= pivot:
                leftmark += 1 # 下标完成了自增，但此时 list[leftmark] > pivot

            while leftmark <= rightmark and list[rightmark] >= pivot:
                rightmark -= 1 # 下标完成了自减，但此时 list[rightmark] < pivot

            if rightmark < leftmark: 
                done = True
            else: # 直接互换
                list[leftmark], list[rightmark] = list[rightmark], list[leftmark]
        # 由于此时 rightmark < leftmark
        # 故实际上 list[rightmark] < pivot = list[first] < list[leftmark]
        list[first], list[rightmark] = list[rightmark], list[first]

        return rightmark


    @staticmethod
    def bubblesort(list):
        start = timeit.default_timer()
        # 每个pass总能将最大的元素“浮上”数组末尾
        # 下个pass可以少考虑1个元素
        for passnum in range(len(list)-1, 0, -1):
            for i in range(passnum):
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
        end = timeit.default_timer()
        print("Bubble sort time elaspe: " + str((end-start)*1000))

    
    @staticmethod
    def mergesort(list):
        start = timeit.default_timer()
        Sorter._mergesort_helper(list)
        end = timeit.default_timer()
        print("Merge sort time elaspe: " + str((end-start)*1000))


    @staticmethod
    def _mergesort_helper(list):
        # 有多于1个元素等待排序 ，仅1个元素不用排序
        if len(list) > 1:
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]
            # 切分数组进行排序
            Sorter._mergesort_helper(left)
            Sorter._mergesort_helper(right)
            # 归并
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i += 1
                else:
                    list[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                list[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                list[k] = right[j]
                j += 1
                k += 1


    @staticmethod
    def selectionsort(list):
        start = timeit.default_timer()
        # 每次选出最大的元素，与数组最后的元素交换
        # 下次可以少考虑1个元素
        for fillslot in range(len(list)-1, 0, -1):
            max_position = 0
            # 将max_position 置0，position 从数组第1元素开始计
            for position in range(1, fillslot+1):
                if list[position] > list[max_position]:
                    max_position = position
                # 将最大元素与数组末尾元素互换
                list[max_position], list[fillslot] = list[fillslot], list[max_position]
        end = timeit.default_timer()
        print("Selection sort time elaspe: " + str((end-start)*1000))


    @staticmethod
    def insertionsort(list):
        start = timeit.default_timer()
        # 从第1元素开始 
        for index in range(1, len(list)):
            current_value = list[index]
            position = index
            # 如果当前元素比之前相邻的元素小，就互换位置
            # 在保证了当前元素之前的子数组都已经排好序的情况下，将当前元素插入
            # while循环挪动子数组元素
            while position > 0 and list[position-1] > current_value:
                list[position] = list[position - 1]
                position -= 1
            # 插入当前元素
            list[position] = current_value
        end = timeit.default_timer()
        print("Insertion sort time elaspe: " + str((end-start)*1000))



if __name__ == "__main__":
    a = list(range(512, 0, -1))
    Sorter.selectionsort(a)
    print(a)

