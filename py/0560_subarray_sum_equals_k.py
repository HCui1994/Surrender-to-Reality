"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
1.  The length of the array is in range [1, 20000].
2.  The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

SCORE:
2046 -> 2058 (dp, TLE)

2101 ->
"""

class Solution:
    def subarray_sum_brutal(self, nums, k):
        """
        滑动窗口, 还是动态规划(实为暴力)？
        注意：range of numbers in the array is [-1000, 1000]，滑窗似乎不好处理

        果然 tle...
        """
        if not nums:
            return 0
        if len(nums) == 1 and nums[0] == k:
            return 1
        length = len(nums)
        memo = [[None for _ in range(length + 1)] for _ in range(length)]
        count = 0
        # 初始化
        for i in range(length):
            if nums[i] == k:
                count += 1
            memo[i][i + 1] = nums[i]
        for l in range(2, length + 1):
            for i in range(length - l + 1):
                j = i + l
                memo[i][j] = memo[i][j - 1] + nums[j - 1]
                if memo[i][j] == k:
                    count += 1
        return count

    def subarray_sum_dfs(self, nums, k):
        """
        对于一个子串 nums[i:j]，会产生几个分支？这个解法应该等价于 dp
        nums[i-1:j]， nums[i+1:j], nums[i:j-1], nums[i:j+1]
        """
        pass

    def _dfs(self, nums, k, i, j, visited):
        pass

    def subarray_sum_dp(self, nums, k):
        """
        http://www.cnblogs.com/grandyang/p/6810361.html
        肯定得想办法把复杂度降到 O(n)
        遍历数组中的数字，用 summation 来记录到当前位置的累加和
        建立哈希表为了可以快速查找 连续子数组的和为 summation - k
        如果存在的话，那么和为 k 的子数组一定也存在

        a0  a1  a2  a3  a4  a5  a6  a7  a8  a9
                      s3                      s9
        假设 s9 - s3 == k, 则 a4 + a5 + a6 + a7 + a8 + a9 == k
        如果 记录中存在 s9 - k, 即记录中存在 s3, 则计数器将自增

        a0  a1  a2  a3  a4  a5  a6  a7  a8  a9
                      s3          s6          s9
        假设，如果 s6 == s3，则 a4 + a5 + a6 + a7 + a8 + a9 == a7 + a8 == k
        ==>  sum_counter[summation] 代表 累加和为 summation 的字数列有多少个
        计数器自增量即为 sum_counter[summation - k]

        核心思路：将数列看成两个部分，第一部分 [a0, aj] 和 (aj, ak]
        若 sum([a0, aj]) == sum([a0, ak]) - k
        则 sum((aj, ak]) == k
        """
        import collections
        summation = 0
        count = 0
        sum_counter = collections.Counter()
        sum_counter[0] = 1
        # print(sum_counter)
        for num in nums:
            summation += num # summation 记录了 sum(nums[:i+1]), i 为当前下标
                             # summation - k 代表了什么？
            count += sum_counter[summation - k]
            sum_counter[summation] += 1
        print(sum_counter)
        return count



        

    def test(self):
        nums = [100,1,2,3,4]
        k = 6
        print(self.subarray_sum_dp(nums, k))
    

Solution().test()

            