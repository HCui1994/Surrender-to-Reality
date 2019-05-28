"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  
Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
"""
import collections


class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        time = [t % 60 for t in time]
        songs = collections.defaultdict(set)
        for i, d in enumerate(time):
            songs[d].add(i)
        cnt = 0
        print(songs)
        for t in songs.keys():
            comp_t = (60 - t) % 60
            s = songs[t]
            if comp_t in songs:
                print(s, songs[comp_t])
                comp_s = songs[comp_t]
                for i in s:
                    for j in comp_s:
                        if i < j:
                            cnt += 1
        return cnt


print(Solution().numPairsDivisibleBy60([60, 60, 60]))
