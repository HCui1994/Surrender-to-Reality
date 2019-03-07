import collections


class FirstNonDup(object):
    def __init__(self, *args, **kwargs):
        self.dq = collections.deque()
        self.cnt = collections.Counter()
        return super().__init__(*args, **kwargs)

    def income(self, val):
        self.cnt[val] += 1
        self.dq.append(val)
        while self.dq and self.cnt[self.dq[0]] >= 2:
            self.dq.popleft()
        print(self.dq)
        if self.dq:
            return self.dq[0]
        else:
            return None


fnd = FirstNonDup()
for val in [0, 1, 0, 3, 1, 4, 5]:
    print(fnd.income(val))
