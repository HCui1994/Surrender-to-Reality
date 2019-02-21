"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
"""


class Solution:

    def num_trees(self, n):
        """
        因为是二叉搜索树，在根节点位置确定时，子问题便是左子树和右子树分别有多少种可能性
        num nodes       num trees           (root num sub trees)
        0               0
        1               1
        2               2
        3               5                   (1 => 2) (2 => 1 * 1) (3 => 2)
        4               14                  (1 => 5) (2 => 1 * 2) (3 => 2 * 1) (4 => 5)
        """
        if not n:
            return 0
        memo = [0 for _ in range(n + 1)]
        memo[0], memo[1] = 0, 1
        # print(memo)
        for i in range(2, n + 1, +1):
            for root in range(1, i + 1, +1):
                print(root, i, memo[i - 1])
                if root == 1 or root == i:
                    memo[i] += memo[i - 1]
                else:
                    memo[i] += memo[root - 1] * memo[i - root]
        # print(memo)
        return memo[-1]

    def test(self):
        n = 4
        ans = self.num_trees(n)
        print(ans)


soln = Solution()
soln.test()
        