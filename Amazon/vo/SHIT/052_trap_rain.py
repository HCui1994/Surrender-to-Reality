class TrapRain(object):
    def eval(self, arr):
        global_high = -float("inf")
        local_high = arr[0]
        cnt = 0
        for h in arr:
            global_high = max(global_high, h)
            if h <= local_high:
                cnt += local_high - h
            else:
                local_high = h
        arr = arr[::-1]
        local_high = arr[0]
        for h in arr:
            if h <= local_high:
                cnt += local_high - h
            else:
                local_high = h
        return cnt - len(arr) * global_high