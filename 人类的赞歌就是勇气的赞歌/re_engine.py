"""
利用 nfa 实现正则表达式引擎
"""


class State(object):
    counter = 0

    def __init__(self, entry, next1=None):
        self._num = State.counter
        self.entry = entry
        self.next1 = next1
        State.counter += 1

    def __repr__(self):
        return "(No. {}: {})".format(self._num, self.entry)


_SPLIT = "SPLIT"
_MERGE = "MERGE"


class SplitState(State):
    def __init__(self, next1, next2):
        super(SplitState, self).__init__(_SPLIT, next1)
        self.next2 = next2


class Fragment(object):
    def __init__(self, begin, end=None):
        self.begin = begin
        self.end = end if end else begin

    def __repr__(self):
        return "Frag[{} -> {}]".format(self.begin, self.end)