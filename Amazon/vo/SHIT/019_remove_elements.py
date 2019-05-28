class Remover(object):
    def remove(self, arr, target):
        remove_cnt = 0
        valid_idx = 0
        for i, num in enumerate(arr):
            if num == target:
                remove_cnt += 1
            else:
                arr[valid_idx] = arr[i]
                valid_idx += 1
        print(arr)
            