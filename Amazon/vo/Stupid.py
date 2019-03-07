import collections

class Stupid(collections.deque, collections.Counter):
    def __init__(self, iterable, maxlen):
        return super().__init__(iterable, maxlen)

