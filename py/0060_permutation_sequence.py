"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
"""

# import bisect


class Solution(object):
    def __init__(self):
        self.fact_memo = {}
        self.fact_memo[1] = 1
        self.fact_memo[0] = 1

    def fact(self, x):
        if x in self.fact_memo:
            return self.fact_memo[x]
        return x * self.fact(x - 1)

    def get_permutation(self, n, k):
        digits = list(range(1, n + 1))
        print("all digits", digits)
        res = ""
        for i in range(n - 1, 0, -1):
            quotient, remainder = divmod(k, self.fact(i))
            k -= quotient * self.fact(i)

            idx = quotient
            if remainder == 0:
                idx -= 1
            # print(idx)

            candidate = digits[idx]
            res += str(candidate)
            digits.remove(candidate)
        
        res += str(digits[0])
        print(res)

Solution().get_permutation(3, 3)
