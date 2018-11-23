import functools

intervals = [[2,10],[3,7],[3,15],[4,11],[6,12],[6,16],[7,8],[7,11],[7,15],[11,12]]

def compare_obj(a, b):
    """Old-style comparison function.
    """
    # print('comparing {} and {}'.format(a, b))
    if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
        return -1
    elif a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]):
        return 1
    return 0

# Make a key function using cmp_to_key()
get_key = functools.cmp_to_key(compare_obj)

def get_key_wrapper(o):
    "Wrapper function for get_key to allow for print statements."
    new_key = get_key(o)
    print('key_wrapper({}) -> {!r}'.format(o, new_key))
    return new_key

intervals = sorted(intervals, key=get_key)
print(intervals)