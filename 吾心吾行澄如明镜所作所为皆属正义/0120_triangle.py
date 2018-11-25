"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        height = len(triangle)
        bottom = len(triangle[height - 1])
        memo = triangle[-1]
        for h in range(height - 2, -1, -1):
            temp_memo = triangle[h]
            for idx in range(len(triangle[h])):
                temp_memo[idx] += min(memo[idx], memo[idx + 1])
            memo = temp_memo
        return memo[0]


soln = Solution()
triangle = [[2],[3,4]]
ans = soln.minimumTotal(triangle)
print(ans)