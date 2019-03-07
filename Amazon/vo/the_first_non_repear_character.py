import collections

def first_non_repeat(string):
    cnt = collections.Counter(string)
    for c in string:
        if cnt[c] == 1:
            return c
    return None