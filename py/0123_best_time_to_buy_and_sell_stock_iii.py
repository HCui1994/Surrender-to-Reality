"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):
    def max_profit(self, prices):
        """
        有状态
        闲置1，持有1，闲置2，持有2，闲置3
        状态转换：
        买入，卖出，等待

        闲置1—等待-闲置1
        闲置1-买入-持有1
        持有1-等待-持有1
        持有1-卖出-闲置2
        闲置2-等待-闲置2
        闲置2-买入-持有2
        持有2-等待-持有2
        持有2-卖出-闲置3
        """
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            else:
                return 0
        days = len(prices)
        dp = {"idle1": [0 for _ in range(days)],
              "hold1": [0 for _ in range(days)],
              "idle2": [0 for _ in range(days)],
              "hold2": [0 for _ in range(days)],
              "idle3": [0 for _ in range(days)]
              }
        # 初始化：
        # 僵尸状态:
        dp["idle2"][0] = dp["hold2"][0] = dp["hold2"][1] = dp["idle3"][0] = dp["idle3"][1] = dp["idle3"][2] = - \
            float("inf")
        # 第一天状态：
        dp["idle1"][0] = 0
        dp["hold1"][0] = -prices[0]

        for day in range(1, days):
            dp["idle1"][day] = dp["idle1"][day - 1]
            dp["hold1"][day] = max(
                dp["idle1"][day - 1] - prices[day], dp["hold1"][day - 1])
            dp["idle2"][day] = max(
                dp["hold1"][day - 1] + prices[day], dp["idle2"][day - 1])
            dp["hold2"][day] = max(
                dp["idle2"][day - 1] - prices[day], dp["hold2"][day - 1])
            dp["idle3"][day] = max(
                dp["hold2"][day - 1] + prices[day], dp["idle3"][day - 1])
        print(max(dp["idle1"][-1], dp["hold1"][-1], dp["idle2"]
                  [-1], dp["hold2"][-1], dp["idle3"][-1]))

    def max_profit_mem_opt(self, prices):
        idle1, hold1 = 0, -prices[0]
        idle2 = hold2 = idle3 = -float("inf")
        for day in range(1, len(prices)):
            idle1 = 0
            hold1 = max(hold1, idle1 - prices[day])
            idle2 = max(idle2, hold1 + prices[day])
            hold2 = max(hold2, idle2 - prices[day])
            idle3 = max(idle3, hold2 + prices[day])
        return max(idle1, hold1, idle2, hold2, idle3)
        
    def test(self):
        prices = [1, 2, 3, 4, 5]
        self.max_profit(prices)


Solution().test()
