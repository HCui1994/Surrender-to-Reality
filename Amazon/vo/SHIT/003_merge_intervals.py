class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Merger(object):
    def merge(self, intervals):

        def key(element):
            return [element.start, element.end]

        intervals = sorted(intervals, key=key)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval.start <= res[-1].end:
                res[-1].end = max(res[-1].end, interval.end)
            else:
                res.append(interval)
        
        return res