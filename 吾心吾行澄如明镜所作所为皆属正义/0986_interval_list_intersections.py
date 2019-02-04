
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        if not A or not B:
            return []
        ia = ib = 0
        res = []
        while ia < len(A) and ib < len(B):
            a_start, a_end = A[ia].start, A[ia].end
            b_start, b_end = B[ib].start, B[ib].end
            if a_end < b_start:
                ia += 1
                continue
            if b_end < a_start:
                ib += 1
                continue
            if a_start < b_start:
                if a_end < b_end:
                    res.append(Interval(b_start, a_end))
                    ia += 1
                else:
                    res.append(Interval(b_start, b_end))
                    ib += 1
            else:
                if a_end < b_end:
                    res.append(Interval(a_start, a_end))
                    ia += 1
                else:
                    res.append(Interval(a_start, b_end))
                    ib+=1
        return res