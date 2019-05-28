class MaxProduct(object):
    def max_product(self, arr):
        if not len(arr):
            return 0
        global_max = local_max = local_min = arr[0]
        for num in arr[1:]:
            local_max_tmp = max(local_max, local_max * num, num)
            local_min_tmp = min(local_min, local_max * num, num)
            local_max, local_min = local_max_tmp, local_min_tmp
            global_max = max(global_max, local_max)
        return global_max