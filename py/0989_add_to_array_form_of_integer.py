class Solution:
    def addToArrayForm(self, A: 'List[int]', k: 'int') -> 'List[int]':
        a = 0
        for num in A:
            a *=10
            a += num
        # print(a)
        res = []
        a += k
        if a == 0:
            return [0]
        while a > 0:
            a, b = divmod(a, 10)
            res.append(b)
        # print(res[::-1])
        return res[::-1]
    

    def test(self):
        print(self.addToArrayForm([ 0], 0))


Solution().test()
