"""
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.


Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""


class Solution(object):
    def min_cost_memoization(self, days, costs):
        self.memo = {days[-1]: min(costs)}
        self.costs = costs
        self.scheduler(days)
        print(self.memo[days[0]])
        return self.memo[days[0]]

    def scheduler(self, days):
        if not days:
            return 0
        if days[0] in self.memo:
            return self.memo[days[0]]
        # 1d
        one_day = self.scheduler(days[1:]) + self.costs[0]
        # 7d
        idx = 1
        while idx < len(days) and days[idx] < days[0] + 7:
            idx += 1
        seven_day = self.scheduler(days[idx:]) + self.costs[1]
        # 30d
        idx = 1
        while idx < len(days) and days[idx] < days[0] + 30:
            idx += 1
        thirdy_day = self.scheduler(days[idx:]) + self.costs[2]
        self.memo[days[0]] = min(one_day, seven_day, thirdy_day)

        return self.memo[days[0]]

    def min_cost_dp(self, days, costs):
        first_day, last_day = days[0], days[-1]
        days = set(days)
        dp = [[float("inf")] * 3 for _ in range(last_day + 2)]
        dp[-1] = [0, 0, 0]
        for day in range(last_day, first_day - 1, -1):
            if day not in days:
                dp[day] = dp[day + 1]
                continue
            # 1d pass
            dp[day][0] = min(dp[day + 1]) + costs[0]
            # 7d pass
            dp[day][1] = min(dp[last_day + 1 if day + 7 > last_day else day + 7]) + costs[1]
            # 30d pass
            dp[day][2] = min(dp[last_day + 1 if day + 30 > last_day else day + 30]) + costs[2]
        print(dp[first_day])
        return min(dp[first_day])

    def test(self):
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        # self.min_cost_memoization(days, costs)
        self.min_cost_dp(days, costs)


Solution().test()
