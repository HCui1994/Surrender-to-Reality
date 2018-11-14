"""
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. 
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""

class Solution:
    def max_profit(self, prices, fee):
        """
        参考 0309_best_time_to_buy_and_sell_stock_with_cooldown
        有几种状体啊？持有，闲等
        状态之间如何转换？
        闲等，买入，持有
        持有，卖出，闲等（支付额外费用）
        持有，等待，持有
        闲等，等待，闲等
        """
        if len(prices) < 2:
            return 0
        if len(prices) == 2:
            return max(0, prices[1] - prices[0] - fee)
        memo_hold = [0 for _ in prices]
        memo_idle = [0 for _ in prices]
        memo_hold[0] = 0 - prices[0]
        memo_idle[0] = 0
        for i in range(1, len(prices), +1):
            # 注意此处的符号            
            # 由于之前已经减去了购买 price，此处不应用减号，而应该用加号
            #                          *
            hold_sell_idle = prices[i] + memo_hold[i - 1] - fee
            hold_wait_hold = memo_hold[i - 1]
            idle_buy_hold  = memo_idle[i - 1] - prices[i]
            idle_wait_idle = memo_idle[i - 1]
            memo_hold[i] = max(hold_wait_hold, idle_buy_hold)
            memo_idle[i] = max(hold_sell_idle, idle_wait_idle)
        print(memo_hold)
        print(memo_idle)
        return max(memo_hold, memo_idle)[-1]

    def test(self):
        prices = [1, 3, 2, 8, 4, 9]
        fee = 2
        self.max_profit(prices, fee)


soln = Solution()
soln.test()