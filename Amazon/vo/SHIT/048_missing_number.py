class MissingNumber(object):
    def find(self, arr):
        # preprocess
        n = len(arr)
        return (0 + n) * (n + 1) // 2 - sum(arr)