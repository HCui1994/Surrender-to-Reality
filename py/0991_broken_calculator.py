class Solution(object):
    def broken_calc(self, x, y):
        if x >= y:
            return x - y
        else:
            if y % 2:
                return self.broken_calc(x, y + 1) + 1
            else:
                return self.broken_calc(x, y // 2) + 1

    def test(self):
        print(self.broken_calc(3, 10))


Solution().test()
