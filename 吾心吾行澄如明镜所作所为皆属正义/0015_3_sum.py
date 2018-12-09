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
        TLE

        mgj，想死
        """
        nums = sorted(nums)
        if len(nums) < 3 or nums[0] > 0 or nums[-1] < 0:
            return []
        length = len(nums)
        ci_start = 2
        res = set()
        print(nums)
        # case 1: a, b <= 0, c > 0
        a_plus_b_dict = {}
        for ai in range(length - 2):
            if nums[ai] > 0:
                # c 从第一个正数开始找
                ci_start = ai
                break
            for bi in range(ai + 1, length - 1):
                if nums[bi] > 0:
                    break
                a_plus_b = nums[ai] + nums[bi]
                if a_plus_b not in a_plus_b_dict.keys():
                    a_plus_b_dict[a_plus_b] = set([(ai, bi)])
                else:
                    a_plus_b_dict[a_plus_b].add((ai, bi))
        for ci in range(ci_start, length):
            if nums[ci] <= 0:
                # 如果 c 不是正数，跳过
                continue
            if -nums[ci] in a_plus_b_dict.keys():
                for ai, bi in a_plus_b_dict[-nums[ci]]:
                    res.add((nums[ai], nums[bi], nums[ci]))

        # case 2: a, b >= 0, c < 0
        nums = nums[::-1]
        a_plus_b_dict = {}
        for ai in range(length - 2):
            if nums[ai] < 0:
                ci_start = ai
                break
            for bi in range(ai + 1, length - 1):
                if nums[bi] < 0:
                    break
                a_plus_b = nums[ai] + nums[bi]
                if a_plus_b not in a_plus_b_dict.keys():
                    a_plus_b_dict[a_plus_b] = set([(ai, bi)])
                else:
                    a_plus_b_dict[a_plus_b].add((ai, bi))
        for ci in range(ci_start, length):
            if nums[ci] >= 0:
                continue
            if -nums[ci] in a_plus_b_dict.keys():
                for ai, bi in a_plus_b_dict[-nums[ci]]:
                    res.add((nums[ci], nums[bi], nums[ai]))

        for i in range(length - 2):
            if (nums[i], nums[i + 1], nums[i + 2]) == (0, 0, 0):
                res.add((0, 0, 0))


        return list(res)


    def three_sums_2(self, nums):
        """
        http://www.cnblogs.com/grandyang/p/4481576.html
        我们对原数组进行排序，然后开始遍历排序后的数组，这里注意不是遍历到最后一个停止，而是到倒数第三个就可以了。
        这里我们可以先做个剪枝优化，就是当遍历到正数的时候就break，为啥呢，因为我们的数组现在是有序的了，如果第一个要fix的数就是正数了，那么后面的数字就都是正数，就永远不会出现和为0的情况了。
        然后我们还要加上重复就跳过的处理，处理方法是从第二个数开始，如果和前面的数字相等，就跳过，因为我们不想把相同的数字fix两次。
        对于遍历到的数，用0减去这个fix的数得到一个target，然后只需要再之后找到两个数之和等于target即可。
        我们用两个指针分别指向fix数字之后开始的数组首尾两个数，如果两个数和正好为target，则将这两个数和fix的数一起存入结果中。然后就是跳过重复数字的步骤了，两个指针都需要检测重复数字。
        如果两数之和小于target，则我们将左边那个指针i右移一位，使得指向的数字增大一些。
        """
        import collections
        res = set()
        nums = sorted(nums)
        if not nums or nums[0] > 0 or nums[-1] < 0:
            return []
        nums_counter = collections.Counter(nums)
        nums_set = list(nums_counter.keys())[::-1]
        print(nums_set)
        # print(nums_counter)
        if nums_counter[0] >= 3:
            res.add((0, 0, 0))
        for a in nums:
            if a >= 0:
                break
            for c in nums_set:
                if c < 0:
                    break
                b = -(a + c)
                # print(a, b, c)
                if (a == b and nums_counter[a] > 1) or (b == c and nums_counter[c] > 1) or (nums_counter[b] > 0 and a != b and b != c):
                    # print("1===", a, b, c)
                    res.add(tuple(sorted([a, b, c])))
        return list(res)
        

    def test(self):
        nums = [-1,0,1,2,-1,-4]
        print(self.three_sums_2(nums))


Solution().test()

        