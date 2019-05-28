"""
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). 
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 

Example 2:
Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:
Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""

import numpy as np


class Solution(object):
    def ship_within_days(self, weights, days):
        self.weights = weights
        self.days = days
        self.min_cargo = float("inf")
        self.memo = {}
        self.split(0, 1)
        print(self.memo)

    def split(self, start, day):
        print(start, day)
        if day == self.days:
            return sum(self.weights[start:])
        if (start, day) in self.memo:
            return self.memo[start, day]
        for break_point in range(start + 1, len(self.weights) - day):
            print(break_point)
            self.memo[day][start] = max(self.memo[day][start], sum(self.weights[start:]) + self.split(break_point, day + 1))
        return self.memo[day][start]

Solution().ship_within_days([1, 2, 3, 1, 1],  4)
