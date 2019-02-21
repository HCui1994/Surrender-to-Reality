import numpy as np
class Solution:
    def minCost(self, costs):
        """
        Args:
            costs: [[r1, g1, b1], [r2, g2, b2], ...]
        Returns:
            minimal total cost
        """
        if not costs:
            return 0
        memo = np.zeros((len(costs), 3))
        memo[0, :] = costs[0]
        for idx in range(1, len(costs), +1):
            # paint red
            memo[idx, 0] = costs[idx][0] + min(memo[idx - 1, [1, 2]])
            # paint green
            memo[idx, 1] = costs[idx][1] + min(memo[idx - 1, [0, 2]])
            # paint blue
            memo[idx, 2] = costs[idx][2] + min(memo[idx - 1, [0, 1]])
        print(memo)
        print(min(memo[-1]))
        return min(memo[-1])


    def min_cost_mem_opt(self, costs):
        if not costs:
            return 0
        memo = costs[0]
        for idx in range(1, len(costs), +1):
            memo = [costs[idx][0] + min(memo[1], memo[2]), costs[idx][1] + min(memo[0], memo[2]), costs[idx][2] + min(memo[0], memo[1])]
        print(memo)
        print(min(memo))



costs = [[17,2,17],[16,16,5],[14,3,19]]
soln = Solution()
soln.min_cost_mem_opt(costs)