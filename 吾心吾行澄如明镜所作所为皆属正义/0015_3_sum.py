"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution(object):
    def three_sum(self, nums):
        """
        三个数必定有正有负，可以先将数组排序，以此来去重
        8 WA, 1TLE
        大失败！
        """
        nums = sorted(nums)
        # print(nums)
        length =len(nums)
        # print(nums)
        a_plus_b_dict = {}
        for ia in range(length - 2):
            if nums[ia] > 0:
                # 如果第一个数大于 0，之后的数一定也大于 0，直接 break
                break
            for ib in range(ia + 1, length - 1):
                if nums[ia] + nums[ib] > 0:
                    # 如果前两个数之和大于 0，即 b 大于 0，则 c 一定也大于 0，直接 break
                    break
                # c 的起始位置不确定！
                a_plus_b = nums[ia] + nums[ib]
                
                if a_plus_b not in a_plus_b_dict.keys():
                    # 直接赋值，由于数组经过排序，不会导致疏漏某种情况
                    a_plus_b_dict[a_plus_b] = set([(ia, ib)])
                    # print(a_plus_b_dict)
                else:
                    # print(a_plus_b_dict)
                    a_plus_b_dict[a_plus_b].add((ia, ib))
        # print(a_plus_b_dict)
        res = set()
        for ic, c in enumerate(nums[::-1]):
            # print(ic, c)
            # c 的其实位置不确定，但一定是正值
            if c < 0:
                # 一旦遇到 c 小于 0，直接 break
                break
            if -c in a_plus_b_dict.keys():
                for ia, ib in a_plus_b_dict[-c]:
                    # print(ia, ib)
                    if length - ic - 1 <= ib:
                        continue
                    # print(ia, ib, ic)
                    res.add((nums[ia], nums[ib], nums[length - ic - 1]))
        return list(res)


        

    def test(self):
        nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
        print(self.three_sum(nums))


Solution().test()

        