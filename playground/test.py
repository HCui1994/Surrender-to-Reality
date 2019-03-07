from functools import singledispatch
import collections

od = collections.OrderedDict()

od[1] = 1
od[2] = 2
od[3] = 3
od[4] = 4

print(od)
od.pop(2)
print(od)
od.popitem(last=False)
print(od)
print(od.popitem(last=True))
print(od)