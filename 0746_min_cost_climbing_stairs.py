class Solution:
    def minCostClimbingStairs(self, cost):
        """
        Args:
            cost: [stair1, stair2, ...] of Integer
        Returns:
            min_cost: of Integer
        """
        cost += [0]
        memo = [None for _ in cost]
        memo[:2] = cost[:2]
        for idx in range(2, len(cost), +1):
            one_step = cost[idx] + memo[idx - 1]
            two_step = cost[idx] + memo[idx - 2]
            memo[idx] = min(one_step, two_step)
        print(memo)

    def min_cost_mem_opt(self, cost):
        cost += [0]
        memo = cost[:2]
        for idx in range(2, len(cost), +1):
            memo[0], memo[1] = memo[1], min(cost[idx] + memo[1], cost[idx] + memo[0])


cost = [10, 15, 20]
soln = Solution()
soln.minCostClimbingStairs(cost)