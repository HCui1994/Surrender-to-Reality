"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. 
Arguments are always wrapped with a list, even if there aren't any.
"""


class Solution(object):
    def __init__(self, weights):
        self.segment = []
        for weight in weights:
            self.segment.append(weight if not self.segment else weight + self.segment[-1])
        print(self.segment)

    def pick_index(self):
        import random
        if not self.segment:
            return None
        weighted_pos = random.randint(1, self.segment[-1])
        index = self.upper_bound(weighted_pos)
        print(weighted_pos, index)

    def upper_bound(self, target):
        low, high = -1, len(self.segment) - 1
        while low < high:
            mid = high - (high - low) // 2
            if self.segment[mid] >= target:
                high = mid - 1
            else:
                low = mid
        return low + 1


def test():
    soln = Solution([1])
    soln.pick_index()
    soln.pick_index()


if __name__ == "__main__":
    test()
