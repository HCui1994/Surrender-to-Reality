"""
You are given K eggs, and you have access to a building with N floors from 1 to N. 
Each egg is identical in function, and if an egg breaks, you cannot drop it again.
You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, 
    and any egg dropped at or below floor F will not break.
Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 
Your goal is to know with certainty what the value of F is.
What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

Example 1:
Input: K = 1, N = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

Example 2:
Input: K = 2, N = 6
Output: 3

Example 3:
Input: K = 3, N = 14
Output: 4
 
Note:
1 <= K <= 100
1 <= N <= 10000
"""


class Solution(object):
    def super_egg_drop_dp_brutal(self, k, n):
        """
        k: num of eggs
        n: num of floors

        动态规划与二分查找
        dp[k][n] 表示，有 k 个鸡蛋，进行 n 层楼的测试，最坏情况下需要多少 move

        初始化：
        只有 1 个鸡蛋，进行 n 层楼的测试，最坏情况下一定需要 n move （从第一层，一直测试到最后一层，直到鸡蛋被摔破）
        有 k 个鸡蛋，进行 1 层楼的测试，只需要一次move

        状态转移：
        给定 k 个鸡蛋和 n 层楼，在 n//2 层楼测试
        case1：在 n//2 摔破了，则还剩 k-1 个鸡蛋，并且在 [1 .. n//2-1] 楼层中测试
        case2：没有摔破，则还剩 k 个鸡蛋，并且在 [n//2+1 .. n] 楼层中测试
        最坏情况下，是二者中的最大值
        """
        self.dp = {}
        # init
        for ki in range(1, k + 1):
            self.dp[(ki, 0)] = 0  # 0 层楼，不需要 move
            self.dp[(ki, 1)] = 1  # 1 层楼，move 一次
        for ni in range(1, n + 1):
            self.dp[(0, ni)] = ni
            # 只有 1 个鸡蛋，move 次数即为楼层数：需要从第一层一直进行测试，直到鸡蛋破碎，最坏情况下，需要测试所有楼层
            self.dp[(1, ni)] = ni
        # return self.super_egg_drop_dp_binary_search_helper(k, n)
        return self.super_egg_drop_brutal_dp_helper(k, n)

    def super_egg_drop_brutal_dp_helper(self, k, n):
        if (k, n) in self.dp:
            return self.dp[(k, n)]
        res = float("inf")
        for test_floor in range(1, n + 1):  # 遍历测试楼层
            # 如果鸡蛋摔破了，剩余的鸡蛋数量为 k - 1，剩余需要测试的楼层数为 test_floor - 1
            broken = self.super_egg_drop_helper(k - 1, test_floor - 1)
            # 如果鸡蛋没有摔破，剩余的鸡蛋数量任然为 k，剩余需要测试的楼层数为 n - test_floor
            unbroken = self.super_egg_drop_helper(k, n - test_floor)
            print(k, n, test_floor, broken, unbroken)
            res = min(max(broken, unbroken) + 1, res)
        self.dp[(k, n)] = res
        return self.dp[(k, n)]

    def super_egg_drop_binary_search_dp(self, neggs, nfloors):
        self.memo = {}
        return self.binary_dp_helper(neggs, nfloors)

    def binary_dp_helper(self, neggs, nfloors):
        if (neggs, nfloors) in self.memo:
            return self.memo[(neggs, nfloors)]
        if nfloors == 0:
            return 0
        elif neggs == 1:
            return nfloors
        bottom_floor, top_floor = 1, nfloors
        while bottom_floor < top_floor:
            test_floor = (top_floor + bottom_floor) // 2
            test_broken = self.binary_dp_helper(neggs - 1, test_floor - 1)
            # 在测试楼层摔破，则应继续在更低楼层测试
            test_unbroken = self.binary_dp_helper(neggs, nfloors - test_floor)
            # 在测试楼层没摔破，则应在更高楼层测试
            if test_broken < test_unbroken:
                # 如果在更低楼层测试需要的步数少于在更高楼层测试的步数
                bottom_floor = test_floor
            elif test_broken > test_unbroken:
                top_floor = test_floor
            else:
                top_floor = bottom_floor = test_floor
        self.memo[(neggs, nfloors)] = min(
            max(self.binary_dp_helper(neggs - 1, bottom_floor - 1),
                self.binary_dp_helper(neggs, nfloors - bottom_floor)),
            max(self.binary_dp_helper(neggs - 1, top_floor - 1),
                self.binary_dp_helper(neggs - 1, nfloors - top_floor))) + 1
        return self.memo[(neggs, nfloors)]

    def test(self):
        k, n = 2, 6
        print(self.super_egg_drop_binary_search_dp(k, n))


Solution().test()
