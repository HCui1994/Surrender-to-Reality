"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. 
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. 
It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""


class Solution(object):
    def next_closest_time(self, time):
        digits = set(list(time))
        hour, minute = time.split(":")
        hour, minute = int(hour), int(minute)
        next_hour = prev_hour = hour
        next_minute = prev_minute = minute
        while True:
            next_minute += 1
            if next_minute == 60:
                next_hour += 1
                next_minute = 0
            if next_hour == 24:
                next_hour = 0
            next_time = "{:02d}:{:02d}".format(next_hour, next_minute)
            prev_minute -= 1
            if prev_minute == -1:
                prev_minute = 59
                prev_hour -= 1
            if prev_hour == -1:
                prev_hour = 23
            prev_time = "{:02d}:{:02d}".format(prev_hour, prev_minute)
            is_next_found = True
            for digit in next_time:
                if digit not in digits:
                    is_next_found = False
                    break
            if is_next_found:
                return next_time
            is_prev_found = True
            for digit in prev_time:
                if digit not in digits:
                    is_prev_found = False
            if is_prev_found:
                return prev_time
            print(prev_time, next_time)

    def nextClosestTime(self, time):
        cur = 60 * int(time[:2]) + int(time[3:])
        # print(cur)
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed for block in divmod(cur, 60) for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

    def test(self):
        time = "01:34"
        print(self.next_closest_time(time))
        print(self.nextClosestTime(time))


Solution().test()
