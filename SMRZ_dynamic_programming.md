## Dynamic Programming Summary
----
### 1.  序列
dp[i]包括了前i-1个子问题的解，i=0表示不取任何元素
#### House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Given [3, 8, 4], return 8.

分析：
到第i家商店，可以选择   
1. 不抢 
2. 抢  
         
如果不抢，则可能抢了i-1，也可能不抢i-1
如果抢了i，必然不抢i-1

采用二维数组存储子问题解，dp[i][0]不抢i，dp[i][1]抢i
 <pre><code>
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        """
        用二维数组存储子问题解
        dp[i][0], 不抢劫商店i；dp[i][1]抢劫商店i
        """
        dp = [[0, 0] for _ in range(len(nums)+1)]
        # 初始化
        dp[1][0] = 0
        dp[1][1] = nums[0]
        for i in range(2, len(dp), +1):
            """不抢商店i，可以抢i-1，也可以不抢i-1"""
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            """抢了商店i，一定没有抢i-1"""
            dp[i][1] = dp[i-1][0] + nums[i-1]
        return max(dp[-1])

nums = [2,1,1,2]
soln = Solution()
print(soln.rob(nums))
</code></pre>
**滚动指针的空间优化**
<pre><code>
class Solution:
    def rob_space_opt(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        """商店i处的收益仅和i-1的收益相关"""
        """只需要存储i，i-1"""
        dp = [[0,       0], 
              [0, nums[0]]
        ]
        for i in range(1, len(nums), +1):
            rob_current = dp[0][0] + nums[i]
            not_rob_current = max(dp[0][1], dp[1][1])
            dp = [[dp[1][0], dp[1][1]], [not_rob_current, rob_current]]
        return max(rob_current, not_rob_current)
</code></pre>

#### House Robber II
Same as House Robber I, but all houses form a circle. **循环数组**。
将数组分裂，产生1错位，分别进行一次计算，返回最大值
<pre><code>
"""Previouely House Robber I: 0189"""
"""循环数组，错一位，求两个解"""
class Solution:
    def rob(self, nums):
        def rob_space_opt(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0, nums[0]]
            for i in range(1, len(nums), +1):
                rob_current = dp[0] + nums[i]
                not_rob_current = max(dp[0], dp[1])
                dp = [not_rob_current, rob_current]
            return max(rob_current, not_rob_current)
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        return max(rob_space_opt(nums[:-1]), rob_space_opt(nums[1:]))

soln = Solution()
nums = [1,2,3,1]
print(soln.rob(nums))
</code></pre>
**Extension**
#### House Robber II 
(don't think this is a dp problem)
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
<pre><code>
"""0337"""
class Solution:
    def rob(self, root):
        return max(self.postorder_rob(root))
    def postorder_rob(self, node):
        if not node:
            return [0, 0]
        # 依旧，考虑抢左节点，和不抢左节点
        rob_left, not_rob_left = self.postorder_rob(node.left)
        rob_right, not_rob_right = self.postorder_rob(node.right)
        # 如果抢当前节点，必定不能抢左右节点
        rob_current = not_rob_left + not_rob_right + node.val
        # 如果不抢当前节点，左右均可抢可不抢
        not_rob_current = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        print(rob_current, not_rob_current)
        return rob_current, not_rob_current
</code></pre>