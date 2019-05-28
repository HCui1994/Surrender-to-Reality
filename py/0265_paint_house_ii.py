class Solution(object):
    def min_cost(self, costs):
        nhosue = len(costs)
        ncolor = len(costs[0])
        dp = [[float("inf") for _ in range(ncolor)] for _ in range(nhosue)]
        # init obly paint house 0
        dp[0][:] = costs[0]

        for hi in range(1, nhosue):
            for ci in range(ncolor):
                for prev_ci in range(ncolor):
                    if ci == prev_ci:
                        continue
                    dp[hi][ci] = min(dp[hi][ci], costs[hi][ci] + dp[hi - 1][prev_ci])

        return min(dp[-1])
