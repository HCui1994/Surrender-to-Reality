import collections


def merge_intervals(intervals):
    if not intervals:
        return None
    intervals.sort()
    res = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1], end)
        else:
            res.append([start, end])
    print(res)
    return res


merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
