class Solution:
    def minDominoRotations(self, A, B):
        sets = [set([a, b]) for a, b in zip(A, B)]
        temp = set(range(1, 7))
        for ss in sets:
            temp &= ss
        if not temp:
            return -1
        min_cnt = float("inf")
        for maintain in temp:
            cnt_a = cnt_b = 0
            for a, b in zip(A, B):
                if a == maintain and b == maintain:
                    continue
                if a == maintain and b != maintain:
                    cnt_b += 1
                    continue
                if a != maintain and b == maintain:
                    cnt_a += 1
                    continue
            min_cnt = min(min_cnt, cnt_a, cnt_b)
        return min_cnt


soln = Solution()
soln.minDominoRotations([2, 3, 2], [3, 2, 3])
