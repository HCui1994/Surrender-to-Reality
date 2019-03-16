class Solution(object):
    def best_time_to_buy_and_sell(self, prices):
        # three status: idle1 hold idle2
        # two transitions: buy sell
        idle1 = 0
        hold1 = -prices[0]
        idle2 = -float("inf")
        max_profit = 0
        transcaction_day = (-float("inf"), float("inf"))

        for day, price in enumerate(prices[1:]):
    
            hold1 = max(hold1, idle1 - price)
            idle2 = max(idle2, hold1 + price)
        
            max_profit = max(idle1, hold1, idle2)
        print(max_profit)
        print(transcaction_day)


Solution().best_time_to_buy_and_sell([7, 1, 5, 3, 6, 4])
