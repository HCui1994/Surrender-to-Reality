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


class Solution(object):
    def get_permutation(self, n, k):
        """
        1 2 3 4 
        1 2 4 3 
        1   3 2 4
        1   3 4 2
        1       4 2 3
        1       4 3 2

        2 1 3 4
        2 1 4 3
        2 3 1 4 
        2 3 4 1
        2 4 1 3
        2 4 3 1

        3 1 2 4
        3 1 4 2
        3 2 1 4
        3 2 4 1
        3 4 1 2
        3 4 2 1

        4 1 2 3
        4 1 3 2
        4 2 1 3
        4 2 3 1
        4 3 1 2
        4 3 2 1
        """
        fact = lambda x: 1 if x == 0 or x == 1 else fact(x - 1) * x
        n_comb = fact(n)
        k %= n_comb
        res = ""
        pos = n
        digit_set = list(range(1, n + 1))
        while pos >= 0:
            quotient, remainder = divmod(n_comb, pos)
            

            


Solution().get_permutation(4,15)