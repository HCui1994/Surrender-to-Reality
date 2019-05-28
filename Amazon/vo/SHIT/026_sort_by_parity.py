class Sort(object):
    @ staticmethod
    def parity_sort(arr):
        evenpos, oddpos = 0, 1
        i = 0
        while i < len(arr):
            print(arr, i, oddpos, evenpos)
            if i & 1 == arr[i] & 1:
                i += 1
            elif i & 1 and not arr[i] & 1:
                # index odd, arr[i] even 
                arr[evenpos], arr[i] = arr[i], arr[evenpos]
                evenpos += 2
            elif not i & 1 and arr[i] & 1:
                # index even
                arr[oddpos], arr[i] = arr[i], arr[oddpos]
                oddpos += 2
        print(arr)


Sort.parity_sort([3, 4])
