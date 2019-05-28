class Transcator(object):
    def max_profit(self, prices):
        # corner case
        if len(prices) < 2:
            return 0
        # how many states?
        # idle1 (buy) hold1 (sell) cooldown (wait) idle2
        # init
        idle = 0
        hold = -prices[0]
        cooldown = -float("inf")
        max_profit = max(idle, hold, cooldown)
        
        for price in prices[1:]:
            idle_temp = max(idle, cooldown)
            hold_temp = max(hold, idle - price)
            cooldown_temp = hold + price
            max_profit = max(idle_temp, hold_temp, cooldown_temp)
            idle, hold, cooldown = idle_temp, hold_temp, cooldown_temp

        return max_profit


if __name__ == "__main__":
    prices = [1, 2, 3, 0, 2]
    transactor = Transcator()
    transactor.max_profit(prices)