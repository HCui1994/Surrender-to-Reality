"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3

Explanation: 
The repeated subarray with maximum length is [3, 2, 1].

Note:
1.  1 <= len(A), len(B) <= 1000
2.  0 <= A[i], B[i] < 100

"""
import numpy as np


class Solution:
    def find_length_dp(self, arr1, arr2):
        """
        与 LCS 问题不同的是，subarray 要求连续
        尝试沿用 LCS 的思路，创建 memo.shape = (len(A), len(B)) 的备忘
        memo[i][j] 代表 以 A[i], B[j] 结尾的最长公共子串的长度

        dynamic programming 通用解法，速度比较慢 22.60%
        """
        if not arr1 or not arr2:
            return 0
        memo = [[0 for _ in range(len(arr2) + 1)]
                for _ in range(len(arr1) + 1)]
        max_length = 0
        for i in range(len(arr1)):
            memo_i = i + 1
            for j in range(len(arr2)):
                memo_j = j + 1
                if arr1[i] == arr2[j]:
                    memo[memo_i][memo_j] = memo[memo_i - 1][memo_j - 1] + 1
                    max_length = max(max_length, memo[memo_i][memo_j])
                else:
                    # 注意这里与 LCS 的区别
                    memo[memo_i][memo_j] = 0
        print(np.array(memo))
        return max_length


    def find_length_dp_mem_opt(self, arr1, arr2):
        """
        在 dp 递推过程中当前的 memo[i][j] 只与 memo[i - 1][:] 有关
        可以将空间复杂度降到 O(min(m, n))
        """
        if not arr1 or not arr2:
            return 0
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        max_length = 0
        memo = [0 for _ in range(len(arr2) + 1)]
        for i in range(len(arr1)):
            temp_memo = [0 for _ in range(len(arr2) + 1)]
            for j in range(len(arr2)):
                if arr1[i] == arr2[j]:
                    temp_memo[j + 1] = memo[j] + 1
                    max_length = max(temp_memo[j + 1], max_length)
            memo = temp_memo
        print(memo)
        return max_length

    def find_length_binary_search(self, arr1, arr2):
        """
        Intuition
        如果 arr1 arr2 有长度为 k 的公共子串，则有长度为 j <= k 的公共子串
        定义函数 check(length) of Boolean
        Let check(length) be the answer to the question "Is there a subarray with length length, common to A and B?" This is a function with range that must take the form [True, True, ..., True, False, False, ..., False] with at least one True. We can binary search on this function.

        Algorithm

        Focusing on the binary search, our invariant is that check(hi) will always be False. We'll start with hi = min(len(A), len(B)) + 1; clearly check(hi) is False.

        Now we perform our check in the midpoint mi of lo and hi. When it is possible, then lo = mi + 1, and when it isn't, hi = mi. This maintains the invariant. At the end of our binary search, hi == lo and lo is the lowest value such that check(lo) is False, so we want lo - 1.

        As for the check itself, we can naively check whether any A[i:i+k] == B[j:j+k] using set structures.
        """
        def check(length):
            seen = set(tuple(arr1[i : i + length]) for i in range(len(arr1) - length + 1))
            return any(tuple(arr2[j : j + length]) in seen for j in range(len(arr2) - length + 1))

        lo, hi = 0, min(len(arr1), len(arr2)) + 1
        while lo < hi:
            mi = (lo + hi) / 2
            if check(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo - 1


    def test(self):
        A = [3,2,1]
        B = [3,2,1,4,7]
        ans = self.find_length_dp_mem_opt(A, B)
        print(ans)


soln = Solution()
soln.test()