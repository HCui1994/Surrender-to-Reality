import collections

class Solution(object):
    def substring_premute(self, string1, string2):
        # corner case
        if len(string2) > len(string1):
            return []  # string2 cannot be a substring of string1
        # preprocess
        template_window = collections.Counter(string2)
        sliding_window = collections.Counter(string1)
        # sliding window init
        left, right = 0, len(string2)
        # core
        res = []
        while right < len(string1):
            if sliding_window == template_window:
                res.append(left)
            left += 1
            right += 1
            if right < len(string1):
                sliding_window[string1[left - 1]] -= 1
                if sliding_window[string1[left - 1]] == 0:
                    del sliding_window[string1[left - 1]]
                sliding_window[string2[right - 1]] += 1
        print(res)

        # analysis    Notations: m - len of string1,  n - len of string2
        # time complexity
        # preprocess: O(m + n)
        # core: O(mn)  pointer goes through string1, each time compares sliding window of size (at maximum) n



if __name__ == "__main__":
    