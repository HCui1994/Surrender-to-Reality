"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
# Definition for an interval.


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals: [Interval], new_interval: Interval):
        if not intervals:
            return [new_interval]

        i = 0
        new_start, new_end = new_interval.start, new_interval.end

        while i < len(intervals):
            start, end = intervals[i].start, intervals[i].end
            if new_start > start:
                i += 1
                continue
            break

        former = intervals[:i]
        latter = intervals[i:]

        if not former:
            former = [new_interval]
        else:
            if new_start < former[-1].end:
                former[-1].end = max(new_end, former[-1].end)
            else:
                former += [new_interval]

        i = 0
        while i < len(latter):
            start, end = latter[i].start, latter[i].end
            if start < former[-1].end:
                former[-1].end = max(former[-1].end, end)
                i += 1
                continue
            break

        return former + latter[i:]
