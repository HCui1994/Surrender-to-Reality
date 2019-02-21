"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2, 1, 5, 6, 2, 3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10

SCORE:
1255 -> 1325 （TLE）largest_rectangle_area_dp
1348 -> 1426 (38) largest_rectangle_area_prune_opt
    AC, 4.25%
1429 ->  largest_rectangle_area_prune_opt_stack

"""
import numpy as np
class Solution:
    def largest_rectangle_area_dp(self, heights):
        """
        尝试动态规划 (实际上是 brutal ？)
        memo[i][j] 表示 heights[i:j+1] 中，以 i - j 为底的最大矩形面积

        TLE O(0.5 n^2)
        
        不可能会用到排序，必须找到 O(n) 的解法
        这说明，不能使用二维的 memoization
        """
        if not heights:
            return None
        if len(heights) == 1:
            return heights[0]
        length = len(heights)
        memo = [[None for _ in range(length + 1)] for _ in range(length)]
        for i in range(length):
            memo[i][i + 1] = heights[i]
        # print(np.array(memo))
        max_area = max(heights)
        for l in range(2, length + 1):
            for i in range(length - l + 1):
                j = i + l
                # print(i, j)
                prev_width = l - 1
                prev_height = min(memo[i][j - 1], memo[i + 1][j]) / prev_width
                curr_width = l
                curr_height = min(prev_height, heights[i], heights[j - 1])
                memo[i][j] = curr_width * curr_height
                max_area = max(max_area, memo[i][j])
                # print(curr_width * curr_height)
        return int(max_area)

    def largest_rectangle_area_prune_opt(self, heights):
        """
        从左向右遍历, 每当找到一个局部极大值，便开始向左遍历，计算最大矩形面积
        最大面积必然会包含极大值 bin，右侧的极大值 bin 必然会包含左侧的极大值 bin

        注意，没有考虑到 heights[-1]
        仍然是 O(n^2) 最坏情况
        """
        heights = [0] + heights + [0]
        right_ptr = 0
        max_area = 0
        while right_ptr < len(heights) - 1:
            if heights[right_ptr] > heights[right_ptr + 1]:
                # 寻找局部极大值
                max_area = max(max_area, heights[right_ptr])
                min_height = heights[right_ptr]
                left_ptr = right_ptr - 1
                while left_ptr > 0:
                    min_height = min(min_height, heights[left_ptr])
                    max_area = max(max_area, min_height * (right_ptr - left_ptr + 1))
                    left_ptr -= 1
            right_ptr += 1
        
        # # 额外考虑最后一个 bin
        # max_area = max(max_area, heights[-1])
        # min_height = heights[right_ptr]
        # left_ptr = right_ptr - 1
        # while left_ptr > 0:
        #     min_height = min(min_height, heights[left_ptr])
        #     max_area = max(max_area, min_height * (right_ptr - left_ptr + 1))
        #     left_ptr -= 1
        return max_area

    def largest_rectangle_area_prune_opt_stack(self, heights):
        """
        使用 stack 维护递增序列，寻找局部极大值

        直方图矩形面积要最大，需要尽可能的使得连续的矩形多，并且最低一块的高度要高。
        先处理最高局部极大值，宽度为 1，然后再处理左侧更低的 bin，宽度为 2
        当找到局部极大值，开始出栈，出栈顺序即 bin 从大到小

        ???
        """
        heights += [0]
        max_area = 0
        stack = [0]
        length = len(heights)
        idx = 0
        while idx < length:
            if not stack or heights[idx] > stack[-1]:
                # 寻找局部极大值，若当前 bin 比栈顶小，入栈
                stack.append(idx)
            else:
                # 否则，当前栈顶就是一个局部极大值
                local_peak_idx = stack.pop()
                # 栈顶被弹出了。。。
                if not stack:
                    # 如果 stack 为空, 说明只有一个 local max bin
                    max_area = max(max_area, heights[local_peak_idx] * idx)
                else:
                    # 如果 stack 非空，
                    max_area = max(max_area, heights[local_peak_idx] * (idx - stack[-1] - 1))
                    idx -= 1
            idx += 1
        return max_area



    def test(self):
        heights =  [3, 1, 3, 2, 2]
        print(self.largest_rectangle_area_prune_opt(heights))


Solution().test()