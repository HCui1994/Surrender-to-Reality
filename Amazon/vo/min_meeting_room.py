import collections
import heapq

def minMeetingRooms(intervals):
    """
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
    find the minimum number of conference rooms required.
    Example 1:
    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2

    类似题目：
    给一堆 videos 的起始时间，终止时间，速度， 求最大的 bandwidth
    样例输入:
    intervals = [["1:00", "2:00"], ["1:30", "2:30"]]  band = [10, 5]
    输出: 15
    Leetcode 0253
    Sort + Proirity Queue
    """
    if not intervals:
        return 0

    def key(element):
        return element[0]
    intervals = sorted(intervals, key=key)
    pq = [intervals[0][::-1]]
    meeting_room = 1
    for start, end in intervals[1:]:
        while pq and start > pq[0][0]:
            heapq.heappop(pq)
        heapq.heappush(pq, [end, start])
        meeting_room = max(meeting_room, len(pq))
    print(meeting_room)



minMeetingRooms([[0, 30], [5, 10], [15, 20]])
minMeetingRooms([[7, 10], [2, 4]])