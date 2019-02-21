"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped. 

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

SCORE:
divide and conquer
1002 -> 1049 (47)
0 attempt AC
77.95%
"""

class Solution:

    def trap_divide_and_conquer(self, height):
        """
        分治: (brutal)
        寻找最高，从最高开始，
        1. 每次向左寻找次高，计算存水量
        2. 每次向右寻找次高，计算存水量
        O(n^2) in the worst case
        """
        if len(height) < 3:
            return 0
        peak_val = 0
        peak_idx = 0
        for i, h in enumerate(height):
            if h > peak_val:
                peak_val = h
                peak_idx = i
        left = self._divide_and_conquer_left(height, peak_idx) 
        right = self._divide_and_conquer_right(height, peak_idx)
        print(left, right)
        return left + right

    def _divide_and_conquer_left(self, height, peak_idx):
        """
        向左寻找次高，找到后，间隔的每个点计算与次高之间的差值，即为该点上的存水量
        从次高点开始，递归
        返回所有结果的和
        """
        if peak_idx == 0:
            return 0
        next_peak_val = height[peak_idx - 1]
        next_peak_idx = peak_idx - 1
        for idx in range(peak_idx - 1, -1, -1):
            if height[idx] >= next_peak_val:
                # print(next_peak_idx, next_peak_val, height[idx])
                next_peak_idx = idx
                next_peak_val = height[next_peak_idx]
        # print(next_peak_idx, next_peak_val, height[idx])
        trap = 0
        for idx in range(next_peak_idx + 1, peak_idx, +1):
            trap += next_peak_val - height[idx]
        # print(trap)
        return trap + self._divide_and_conquer_left(height, peak_idx=next_peak_idx)

    def _divide_and_conquer_right(self, height, peak_idx):
        if peak_idx == len(height) - 1:
            return 0
        next_peak_val = height[peak_idx + 1]
        next_peak_idx = peak_idx + 1
        for idx in range(peak_idx + 1, len(height), +1):
            if height[idx] >= next_peak_val:
                print(next_peak_idx, next_peak_val, height[idx])
                next_peak_idx = idx
                next_peak_val = height[next_peak_idx]
        print(next_peak_idx, next_peak_val, height[idx])
        trap = 0
        for idx in range(peak_idx + 1, next_peak_idx, +1):
            trap += next_peak_val - height[idx]
        return trap + self._divide_and_conquer_right(height, peak_idx=next_peak_idx)

    def trap_one_pass(self, height):
        """
        one pass
        集合运算：
        1.  从左开始设定一个 high，向右寻找 higher，找到则计算 high 与 higher 之间的存水量
        2.  从右同理
        3.  左右得到结果相加

        beautiful
        """
        length = len(height)
        trap_left = trap_right = 0
        peak_val = 0
        high_idx = 0
        high_val = height[high_idx]
        for idx in range(length):
            if height[idx] <= high_val:
                # 如果向右遍历，没有找到 higher，就计算蓄水量
                trap_left += high_val - height[idx]
            else:
                # 如果找到了 higher, 则更新
                high_val = height[idx]
                high_idx = idx
            peak_val = max(peak_val, height[idx])
        
        high_idx = length - 1
        high_val = height[high_idx]
        omega = 0
        for idx in range(length - 1, -1, -1):
            # 从右向左
            if height[idx] <= high_val:
                trap_right += high_val - height[idx]
            else:
                high_val = height[idx]
            omega += peak_val - height[idx]
        
        # A 交 B = A + B - {全集}
        print(trap_left, trap_right)
        return trap_left + trap_right - omega

    def trap_two_pointers(self, height):
        """
        one pass 的改进型
        one pass 需要遍历两遍，因为需要通过一次遍历找到 peak val
        考虑如何在计算 trap_left 和 trap_right 的同时, 找到 peak_val, 
        找到后直接停止
        """
        left_ptr, right_ptr = 0, len(height) - 1
        left_high, right_high = height[left_ptr], height[right_ptr]
        trap = 0
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                # 如果左侧边界更低，就需要向右找到更高的左边界，使得左指针和右指针能够会和在 peak 处
                left_ptr += 1
                if height[left_ptr] < left_high:
                    trap += left_high - height[left_ptr]
                else:
                    left_high = height[left_ptr]
            else:
                # 否则，向左寻找更高的右边界
                right_ptr -= 1
                if height[right_ptr] < right_high:
                    trap += right_high - height[right_ptr]
                else:
                    right_high = height[right_ptr]
        return trap


            
        
    def test(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        print(self.trap_two_pointers(height))


Solution().test()
