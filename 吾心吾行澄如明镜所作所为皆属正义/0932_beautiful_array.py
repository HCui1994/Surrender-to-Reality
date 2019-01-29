"""
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:
For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].
Given N, return any beautiful array A.  (It is guaranteed that one exists.)

Example 1:
Input: 4
Output: [2,1,4,3]

Example 2:
Input: 5
Output: [3,1,2,5,4]
 
Note:
1 <= N <= 1000
"""


class Solution:
    def beautiful_array(self, N):
        memo = {1: [1]}
        def f(N):
            print(N)
            if N not in memo:
                odds = f((N + 1) // 2)
                evens = f(N // 2)
                memo[N] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return memo[N]

        f(N)
        print(memo)
        return memo[N]
    
    def test(self):
        self.beautiful_array(5)



Solution().test()