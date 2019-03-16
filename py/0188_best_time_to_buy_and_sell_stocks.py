"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""


class Solution(object):
    def max_profit(self, prices, k):
        """
        MLE
        """
        if not prices:
            return 0
        # init
        # at most k transactions
        # idle  1 2 3 ... k-1 k k+1
        # hold  1 2 3 ... k-1 k
        idle = [-float("inf") for _ in range(k + 2)]
        hold = [-float("inf") for _ in range(k + 1)]
        idle[1] = 0
        hold[1] = -prices[0]
        max_profit = 0
        for day, price in enumerate(prices[1:]):
            hold[1] = max(hold[1], idle[1] - price)
            for state in range(2, k + 1):
                idle[state] = max(idle[state], hold[state - 1] + price)
                hold[state] = max(hold[state], idle[state] - price)
            idle[k + 1] = max(idle[k + 1], hold[k] + price)
        print(max(idle + hold))

    def max_profit_mem_opt(self, prices, k):
        """
        markov chain，可以改良空间到 O(1)
        """
        if len(prices) < 2 or k == 0:
            return 0
        idle1 = 0
        hold1 = -prices[0]
        max_profit = 0
        idle2 = idle3 = hold2 = -float("inf")
        for price in prices[1:]:
            hold1 = max(hold1, idle1 - price)
            max_profit = max(max_profit, hold1)
            for _ in range(2, k + 1):
                idle2 = max(idle2, hold1 + price)
                hold2 = max(hold2, idle2 - price)
                max_profit = max(max_profit, idle2, hold2)
            idle3 = max(idle3, hold2 + price)
            max_profit = max(max_profit, idle3)
        print(max_profit)

