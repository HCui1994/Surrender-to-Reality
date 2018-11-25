class Solution:
    def numWays(self, n, k):
        """
        Args:
            n: num of fences of Integer
            k: num of colors of Integer
        """
        # Attention:
        # NO MORE THAN TWO adjacent fence posts have the same color.
        if not n or not k:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        num_of_paints = [k, k * k]
        for _ in range(2, n, +1):
            # 如果前两个篱笆颜色相同，则当前篱笆的颜色需要不同于前一个篱笆
            prev_two_same_color = (k - 1) * num_of_paints[1]
            # 如果前两个篱笆颜色不同，则当前篱笆的颜色 ？？？？？？
            prev_two_diff_color = (k - 1) * num_of_paints[0]
            num_of_paints = [num_of_paints[1], prev_two_same_color + prev_two_diff_color]
        return num_of_paints[-1]


soln = Solution()
n = 1
k = 2 
print(soln.numWays(n, k))