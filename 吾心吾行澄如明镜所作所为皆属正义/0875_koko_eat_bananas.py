"""
Koko loves to eat bananas. There are N piles of bananas, the i-th pile has piles[i] bananas. The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K. Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  
If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.

Example 1:
Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], H = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], H = 6
Output: 23

Note:

1.  1 <= piles.length <= 10^4
2.  piles.length <= H <= 10^9
3.  1 <= piles[i] <= 10^9
"""

class Solution:
    def min_eating_speed_brutal(self, piles, h):
        """
        brutal 
        得到了最小速度和最大速度，暴力求解
        """
        max_speed = max(piles)
        min_speed = sum(piles) // h
        # print(max_speed, min_speed)
        for speed in range(min_speed, max_speed + 1, +1):
            time_req = 0
            for pile in piles:
                if pile % speed:
                    time_req += pile // speed + 1
                else:
                    time_req += pile // speed
            # print(speed, time_req)
            if time_req <= h:
                return speed
        return max_speed

    def min_eating_speed_binary_search(self, piles, h):
        """
        类似于“在一个给定区间中找一个值”的问题，尝试 binary search
        """
        max_speed = max(piles)
        total_bananas = sum(piles)
        if total_bananas % h:
            min_speed = total_bananas // h + 1
        else:
            min_speed = total_bananas // h
        print(max_speed, min_speed)
        while min_speed < max_speed:
            
            speed = (min_speed + max_speed) // 2
            if self._check_valid(piles, h, speed):
                max_speed = speed
            else:
                min_speed = speed + 1
                speed += 1
        return speed

    def _check_valid(self, piles, h, speed):
        time_req = 0
        for pile in piles:
            if pile % speed:
                time_req += pile // speed + 1
            else:
                time_req += pile // speed
        # print(speed, time_req)
        if time_req <= h:
            return True
        else:
            return False

    

    def test(self):
        piles = [30,11,23,4,20]
        h = 5
        ans = self.min_eating_speed_binary_search(piles, h)
        print(ans)


soln = Solution()
soln.test()