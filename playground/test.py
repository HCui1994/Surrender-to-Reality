from functools import singledispatch


@singledispatch
def to_str(obj):
    print('%r' % (obj))


@to_str.register(int)
def _to_str(obj):
    print('Integer: %d' % (obj))


@to_str.register(str)
def _to_str(obj):
    print('String: %s' % (obj))


@to_str.register(list)
def _to_str(obj):
    print('List: %r' % (obj))


if __name__ == "__main__":
    to_str(1)
    to_str('hello')
    to_str(range(3))
    to_str(object)
