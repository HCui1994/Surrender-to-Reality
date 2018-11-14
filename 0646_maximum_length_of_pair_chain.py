"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""

class Solution:
    def find_longest_chain(self, pairs):
        def key(element):
            return element[1]
        pairs = sorted(pairs, key=key)
        print(pairs)
        memo_num_pairs = [None for _ in pairs]
        memo_max_end = [None for _ in pairs]
        memo_num_pairs[0], memo_max_end[0] = 1, pairs[0][1]
        for i in range(1, len(pairs), +1):
            if pairs[i][0] > memo_max_end[i - 1]:
                memo_num_pairs[i] = memo_num_pairs[i - 1] + 1
                memo_max_end[i] = pairs[i][1]
            else:
                memo_num_pairs[i], memo_max_end[i] = memo_num_pairs[i - 1], memo_max_end[i - 1]
        print(memo_num_pairs)
        return memo_num_pairs[-1]

    
    def test(self):
        pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]
        ans = self.find_longest_chain(pairs)
        print(ans)


soln = Solution()
soln.test()