"""
n sum 问题通解
"""


def n_sum(nums, target, n):
    def find_n_sum(left, right, target, n, result, results):
        # print(left, right, target, n, result, results)
        if right - left + 1 < n or n < 2 or target < nums[left] * n or target > nums[right] * n:
            return
        if n == 2:
            # 递归出口：2_sum 作为最小子问题
            while left < right:
                sub_target = nums[left] + nums[right]
                if sub_target < target:
                    left += 1
                elif sub_target > target:
                    right -= 1
                else:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left] - 1:
                        left += 1
                    while right > left and nums[right] == nums[right] + 1:
                        right += 1
        else:
            for i in range(left, right + 1, +1):
                if i > left and nums[i] == nums[i - 1]:
                    continue
                find_n_sum(left=i + 1,
                           right=right,
                           target=target - nums[i],
                           n=n - 1,
                           result=result + [nums[i]],
                           results=results)

    nums.sort()
    results = []
    find_n_sum(0, len(nums) - 1, target, n, [], results)
    print(results)


nums = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
target = 0
n = 3
print(n_sum(nums=nums, n=3, target=target))
