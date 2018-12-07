"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

class Solution:
    def majorityElement(self, nums):
        """ 
        思路：摩尔投票升级版，超过n/3的数最多只能有两个；
        先选出两个候选人A,B,遍历数组，如果投A（等于A），则A的票数++;如果投B，B的票数++；
        如果A,B都不投（即与A，B都不相等）,那么检查此时是否AB中候选人的票数是否为0，如果为0,则成为新的候选人；
        如果A,B两个人的票数都不为0，那么A,B两个候选人的票数均--；
        遍历结束后选出两个候选人，但是这两个候选人是否满足>n/3，还需要再遍历一遍数组，找出两个候选人的具体票数
        """
        if not nums:
            return []
        # 选两个候选人
        candidate_a, candidate_b = nums[0], nums[0]
        count_a = count_b = 0
        for num in nums:
            # print(candidate_a, candidate_b, num, count_a, count_b)
            if num == candidate_a:
                # 如果投票给候选人 a
                count_a += 1
            elif num == candidate_b:
                # 如果投票给候选人 b
                count_b += 1
            elif count_a == 0:
                # 如果不给任意候选人投票，且 a 的票数差为 0，则更换候选人
                candidate_a = num
                count_a += 1
            elif count_b == 0:
                candidate_b = num
                count_b += 1
            else:  # candidate_a != num and candidate_b != num
                count_a -= 1
                count_b -= 1
        
        count_a = count_b = 0
        for num in nums:
            if num == candidate_a:
                count_a += 1
            elif num == candidate_b:
                count_b += 1
        res = []
        if len(nums) // 3 < count_a:
            res.append(candidate_a)
        if len(nums) // 3 < count_b:
            res.append(candidate_b) 
        return res