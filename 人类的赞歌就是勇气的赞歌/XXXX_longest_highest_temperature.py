"""
given a time series that keeps infromation about temperature readings for a city, 
reutrn a time series that tells you, for a given day, how long has its value being the largest running value.
eg: for temperature readings [30, 50, 60, 20, 10, 40, 60, 90]
the transformed time series should be [1,2,3,1,1,3,7,8]
"""

class Solution(object):
    def solution(self, time_series):
        if not time_series:
            return []
        max_days = [[0, 0]] * len(time_series)
        max_days[0] = [time_series[0], 1]
        i = 1
        while i < len(time_series):
            if time_series[i] < time_series[i-1]:
                max_days[i] = [time_series[i], 1]
            else:
                day_count = 1
                curr_temp = time_series[i]
                next_high_temp, _ = max_days[i-1]
                j = i-1
                while j >= 0 and curr_temp > next_high_temp:
                    next_high_temp = max_days[j][0]
                    if curr_temp > next_high_temp:
                        day_count += max_days[j][1]
                    j -= max_days[j][1]
                max_days[i] = [time_series[i], day_count]
            i += 1
        return max_days


solution = Solution()
time_series = [30, 50, 60, 20, 10, 40, 60, 90]
print(solution.solution(time_series))
