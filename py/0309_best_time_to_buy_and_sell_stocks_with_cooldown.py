"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
class Solution:
    def maxProfit(self, prices):
        """ 
        每一天有几种状态？持有，闲等，冷却
        持有 卖出 冷却
        持有 等待 持有
        冷却 等待 闲等
        闲等 等待 闲等
        闲等 购入 持有
        """
        if len(prices) < 2:
            return 0
        profit_hold = [None for _ in prices]
        profit_cool = [None for _ in prices]
        profit_idle = [None for _ in prices]
        # init: 第一天买入
        profit_hold[0] = 0 - prices[0]
        # init: 第一天不可能冷却
        profit_cool[0] = 0
        # init: 第一天闲等
        profit_idle[0] = 0
        for idx in range(1, len(prices), +1):
            # 在满足当前天是最优解的条件下，算到所有情况
            # 从第二天起计算状态
            hold_sell_cool = prices[idx] + profit_hold[idx - 1]
            hold_wait_hold = profit_hold[idx - 1]
            cool_wait_idle = profit_cool[idx - 1]
            idle_wait_idle = profit_idle[idx - 1]
            idle_buy_hold  = profit_idle[idx - 1] - prices[idx]
            profit_hold[idx] = max(hold_wait_hold, idle_buy_hold)
            profit_cool[idx] = hold_sell_cool
            profit_idle[idx] = max(cool_wait_idle, idle_wait_idle)
        print("prices:", prices)
        print("profit_cool\t", profit_cool)
        print("profit_idle\t", profit_idle)
        print("profit_hold\t", profit_hold)

        return max([profit_cool[-1], profit_hold[-1], profit_idle[-1]])

soln = Solution()
prices = [4,1]
soln.maxProfit(prices)
            

        