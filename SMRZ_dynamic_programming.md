# Dynamic Programming Summary

----

## 1. 序列

dp[i]包括了前i-1个子问题的解，i=0表示不取任何元素

### House Robber

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

#### 滚动指针的空间优化

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

### House Robber II

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
**Follow up: House Robber II**
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

### Maximum Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

什么是子问题？
将一个点作为**某个正方形的右下角**。 该点的左侧，上侧，左上侧，三点为右下角形成的三个正方形的大小，决定了以该点为右下角的正方形的大小。

<pre><code>
class Solution
    def maximum_square_dp(self, matrix):
        """
        dp solution
        若某个点是一个正方形的右下角，则其 1.左侧 2.上侧 3.左上侧 三个点一定也是某个正方形的右下角
        初始化就是matrix自身
        """
        matrix = [[int(element) for element in row] for row in matrix]
        # print(matrix[1][3])
        num_row = len(matrix)
        if not num_row:
            return 0
        num_col = len(matrix[0])
        for row in range(1, num_row, +1):
            for col in range(1, num_col, +1):
                if matrix[row][col] == 1:
                    #                   左上                            左                     上                  当前
                    matrix[row][col] = min(matrix[row - 1][col - 1], matrix[row][col - 1], matrix[row - 1][col]) + 1
        # print(matrix)
        max_edge = 0
        for row in range(num_row):
            for col in range(num_col):
                if matrix[row][col] > max_edge:
                    max_edge = matrix[row][col]
        return max_edge ** 2  
</code></pre>

### Follow up: Maximum Square II

Given a 2D binary matrix filled with 0’s and 1’s, find the largest square which diagonal is all 1 and others is 0.

Notice

Only consider the main diagonal situation.

For example, given the following matrix:

1 0 1 0 0
1 0 0 1 0
1 1 0 0 1
1 0 0 1 0

Return 9

子问题：将一个点作为**某个正方形的右下角**，改点数字代表了符合条件的正方形的对角线长度。 若想将该点纳入正方形，进行扩张，则

1. diagnal_length = 左上的点的值
2. 从该点向左数diagnal_length个点，以这些店为右下角的正方形，必须对角线全部为0
3. 向上同理

<pre><code>
class Solution:
    def maximum_square(self, matrix):
        num_row = len(matrix)
        if not num_row:
            return 0
        num_col = len(matrix[0])
        for row in range(1, num_row, +1):
            for col in range(1, num_col, +1):
                if matrix[row][col] == 1 and matrix[row - 1][col - 1] != 0:
                    diag_length = matrix[row - 1][col - 1]
                    extend_flag = True
                    for idx in range(1, diag_length + 1, +1):
                        if matrix[row][col - idx] != 0 or matrix[row - 1][col] != 0:
                            extend_flag = False
                            break
                    if extend_flag:
                        matrix[row][col] = matrix[row - 1][col - 1] + 1
        max_diagnal = 0
        for row in matrix:
            for element in row:
                max_diagnal = max(max_diagnal, element)
        return max_diagnal ** 2
</code></pre>

## 2. 记忆化搜索

实现方式：从小到大的递推，从大到小的搜索

### Longest Increasing Continuous Subsequence

Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right. Indices of the integers in the subsequence should be continuous.

O(n) time and O(1) extra space.

Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.

简单难度的问题，简单在于，求解的是**连续**子序列

1. 如果当前数小于等于前一个，递增被打断，长度状态重置为 1  
2. 如果当前数大于前一个，处于递增，长度状态为前一个状态 加1  

### Follow up: Longest Increasing subsequence IIs

Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).

Example
Given a matrix:

[
[1 ,2 ,3 ,4 ,5],
[16,17,24,23,6],
[15,18,25,22,7],
[14,19,20,21,8],
[13,12,11,10,9]
]
return 25

当前状态的子状态可能来自于 上 下 左 右 四个方向，转移方程不具有顺序性，难以描述。初始状态也不好找，比如此题目中，不知道应该从哪个坐标开始数子序列。
DFS由于其 深度优先 的性质，可以优先找到最小的子问题，一旦子问题的解确定下来便不再改变（该节点已访问，不会再做修改）

<pre><code>
class Solution:
    def __init__(self):
        self._memo = None
        self._visited = None
        self._matrix = None
        self._num_row = 0
        self._num_col = 0

    def longest_inc_cont_subseq(self, matrix):
        if not matrix:
            return 0
        self._num_row = len(matrix)
        self._num_col = len(matrix[0])
        self._visited = [[False for _ in range(self._num_col)] for _ in range(self._num_row)]
        self._memo = [[1 for _ in range(self._num_col)] for _ in range(self._num_row)]
        self._matrix = matrix
        max_length = 0
        for i in range(self._num_row):
            for j in range(self._num_col):
                max_length = max(self._dfs(i, j), max_length)
        print(np.array(self._memo))
        return max_length

    def _dfs(self, i, j):
        if self._visited[i][j]:  # 每个节点仅被访问一次
            return self._memo[i][j]
        current_max = 1
        di = [1, -1, 0, 0]
        dj = [0, 0, -1, 1]
        for idx in range(4):
            ii = i + di[idx]
            jj = j + dj[idx]
            if ii >=0 and ii < self._num_row and jj >=0 and jj < self._num_col:
                if self._matrix[ii][jj] > self._matrix[i][j]:
                    current_max = max(current_max, self._dfs(ii, jj) + 1)
        # 第一个完成访问的节点，必然是拥有最大值的节点，因为其“最深”
        self._visited[i][j] = True
        self._memo[i][j] = current_max
        print(self._matrix[i][j])
        return current_max
</code></pre>

### Follow up: Coins in a Line 记忆化搜索与博弈

There are **n** coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?

Example
n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true.
n = 5, return true.

## 3. 背包

**所有的背包问题都可以转换为01背包**
01背包当前状态计算与子问题的考量：
当前考虑将第 i 个物品放入 体积为 V 的背包，有两种选择

1. 放入第 i 个物品，则前 i-1 个物品只能放入 V-v[i] 容量的背包  
2. 不放第 i 个物品，则前 i-1 个物品可以放入 V 容量的背包  

哪个选择可以带来最大的收益？就是当前问题的解

其余的背包问题都沿用与01背包同样的子问题，不同之处在于如何转换为01背包
将物品复制的时候，可以考虑 2 的幂次。**所有整数都可以表达为 2 的幂数列的线性组合。**
<pre><code>
import numpy as np
import time
class BKPK:
    @staticmethod
    def optimization_on_01_and_complete(stuff_volume, stuff_value, backpack_volume):
        pass

    @staticmethod
    def backpack_01(stuff_volume, stuff_value, backpack_volume):
        """ 
        N个物品，背包容量V，放入第i件物品消耗G[i]，得到价值W[i]，每个物品只能放入一件，放入哪些物品使得总价值最大？
        Args: 
            stuff_vol: [vol0, vol1, ...] of Integer
            stuff_value: [val1, val2, ...] of Integer
            backpack_vol: total volume of backpack of Integer
        """
        stuff_num = len(stuff_value)
        memo = np.zeros((stuff_num + 1, backpack_volume + 1))
        memo[0, :] = 0 # 初始化，背包中不放任何物品，价值肯定为0
        for stuff_idx in range(len(stuff_value)):
            memo_stuff_idx = stuff_idx + 1
            for vol in range(stuff_volume[stuff_idx], backpack_volume+1, +1):
                collect = stuff_value[stuff_idx] + memo[memo_stuff_idx - 1, vol - stuff_volume[stuff_idx]]
                uncollect = memo[memo_stuff_idx - 1, vol]
                memo[memo_stuff_idx, vol] = max([collect, uncollect])
        print(memo)
        print(memo[memo.shape[0]-1, memo.shape[1]-1])

    @staticmethod
    def backpack_01_memory_optimze(stuff_volume, stuff_value, backpack_volume):
        """
        collect = stuff_value[stuff_idx] + memo[memo_stuff_idx - 1, vol - stuff_vol[stuff_idx]]
        uncollect = memo[memo_stuff_idx - 1, vol]
        计算memo[memo_stuff_idx, :]一行，只需要memo[memo_stuff_idx-1, :]一行
        不需要保存所有子问题解
        """
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = stuff_value[stuff_idx] + memo[vol - stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])

    @staticmethod
    def backpack_complete(stuff_volume, stuff_value, backpack_volume):
        """ 
        N个物品，背包容量V，放入第i件物品消耗G[i]，得到价值W[i]，每个物品可以无限次放入，放入哪些物品使得总价值最大？
        如何将完全背包问题褪化为01背包？
        第i物品最多可以放入 backpack_volume // stuff_volume[i] 次，
        将第i物品复制出为 backpack_volume // stuff_volume[i] 件相同的物品
        之后运行backpack_01
        """
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_volume)):
            num_of_duplicate = backpack_volume // stuff_volume[i]
            for _ in range(num_of_duplicate):
                duplicate_stuff_volume.append(stuff_volume[i])
                duplicate_stuff_value.append(stuff_value[i])
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])

    @staticmethod
    def backpack_complete_optimized(stuff_volume, stuff_value, backpack_volume):
        """
        更高效的转化方法:
        把第 i 种物品复制成为费用为 stuff_volume[i] * 2 ** k, 价值为 stuff_value[i] * 2 ** k 的若干件物品, 
        其中 k 取遍满足stuff_volume[i] * 2 ** k <= backpack_volume 的非负整数。任何数量的同种物品可以作为上述复制品的线性组合
        如此不再需要 backpack_volume // stuff_volume[i] 的复制品
        而仅需要 log(backpack_volume) // log(stuff_volume[i]) 的复制品
        """
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_value)):
            k = 0
            while stuff_volume[i] * 2 ** k <= backpack_volume:
                duplicate_stuff_value.append(stuff_value[i] * 2 ** k)
                duplicate_stuff_volume.append(stuff_volume[i] * 2 ** k)
                k += 1
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])

    @staticmethod
    def backpack_multiple(stuff_volume, stuff_value, stuff_multiple, backpack_volume):
        """
        有 N 种物品和一个容量为 backpack_volume 的背包
        第 i 种物品最多有 stuff_multiple[i] 件可用, 
        每件耗费的空间 stuff_volume[i]
        价值 stuff_value[i]
        求解将哪些物品装入背包可使这些物品的耗费的空间总和不超过背包容量,且价值总和最大。
        Args:
            stuff_multiple: [num_of_stuff1, num_of_stuff2, ...]
        """
        # 可以像完全背包一样，将所有复制物品放入 duplicate_stuff_value, duplicate_stuff_volume
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_multiple)):
            for _ in range(stuff_multiple[i]):
                duplicate_stuff_value.append(stuff_value[i])
                duplicate_stuff_volume.append(stuff_volume[i])
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol] 
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])

    @staticmethod
    def backpack_mixed(stuff_type, stuff_volume, stuff_value, stuff_multiple, backpack_volume):
        """
        有 N 种物品和一个容量为 backpack_volume 的背包
        第 i 种物品可能只有一个，可能有无限多，也可能最多有 stuff_multiple[i] 件可用, 
        每件耗费的空间 stuff_volume[i]
        价值 stuff_value[i]
        求解将哪些物品装入背包可使这些物品的耗费的空间总和不超过背包容量,且价值总和最大。
        Args:
            stuff_type ["01", "multiple", "complete", ...]
        """
        # 按照每种物品的类别创建 duplicate_stuff_volume 和 duplicate_stuff_value
        pass

    @staticmethod
    def backpack_2d(stuff_volume_1, stuff_volume_2, stuff_value, backpack_volume_1, backpack_volume_2):
        """
        对于每件物品,具有两种不同的费用,选择这件物品必须同时付出这两种费用。
        对于每种费用都有一个可付出的最大值(背包容量)。怎样选择物品可以得到最大的价值。
        设第 i 件物品价值 stuff_value[i], 所需的两种费用分别为 stuff_volume_1[i] 和 stuff_volume_2[i]
        两种费用可付出的最大值(即两种背包容量)分别为 backpack_volume_1 和 backpack_volume_2 。
        """
        # 为memo增加一个维度
        num_of_stuff = len(stuff_value)
        memo = np.zeros((num_of_stuff + 1, backpack_volume_1 + 1, backpack_volume_2 + 1))
        for stuff_idx in range(num_of_stuff):
            memo_stuff_idx = stuff_idx + 1
            for vol1 in range(stuff_volume_1[stuff_idx], backpack_volume_1 + 1, +1):
                for vol2 in range(stuff_volume_2[stuff_idx], backpack_volume_2 + 1, +1):
                    collect = stuff_value[stuff_idx] + memo[memo_stuff_idx - 1, vol1 - stuff_volume_1[stuff_idx], vol2 - stuff_volume_2[stuff_idx]]
                    uncollect = memo[memo_stuff_idx - 1, vol1, vol2]
                    memo[memo_stuff_idx, vol1, vol2] = max(collect, uncollect)
        print(memo)
        print(memo[-1, -1, -1])

    @staticmethod
    def backpack_2d_space_optimize(stuff_volume_1, stuff_volume_2, stuff_value, backpack_volume_1, backpack_volume_2):
        memo = np.zeros((backpack_volume_1 + 1, backpack_volume_2 + 1))
        for stuff_idx in range(len(stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume_1 + 1, backpack_volume_2 + 1))
            for vol1 in range(stuff_volume_1[stuff_idx], backpack_volume_1 + 1, +1):
                for vol2 in range(stuff_volume_2[stuff_idx], backpack_volume_2 + 1, +1):
                    collect = stuff_value[stuff_idx] + memo[vol1 - stuff_volume_1[stuff_idx], vol2 - stuff_volume_2[stuff_idx]]
                    uncollect = memo[vol1, vol2]
                    current_stuff_memo[vol1, vol2] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1, -1])


    @staticmethod
    def backpack_group():
        pass
    
    def backpack_dependency():
        pass
<code><pre>

