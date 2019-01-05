# def fourSum(self, nums, target):
#     def findNsum(l, r, target, N, result, results):
#         # early termination
#         if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
#             return
#         if N == 2:  # two pointers solve sorted 2-sum problem
#             while l < r:
#                 s = nums[l] + nums[r]
#                 if s == target:
#                     results.append(result + [nums[l], nums[r]])
#                     l += 1
#                     while l < r and nums[l] == nums[l-1]:
#                         l += 1
#                 elif s < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else:  # recursively reduce N
#             for i in range(l, r+1):
#                 if i == l or (i > l and nums[i-1] != nums[i]):
#                     findNsum(i+1, r, target-nums[i],
#                              N-1, result+[nums[i]], results)

#     nums.sort()
#     results = []
#     findNsum(0, len(nums)-1, target, 4, [], results)
#     return results


def n_sum(nums, n, target):
    def find_n_sum(left, right, target, n, result, results):
        print(result, left, right)
        if right - left + 2 < n:
            return
        if n < 2:
            return
        if target < nums[left] * n:
            return
        if target > nums[right] * n:
            return
        if n == 2:
            while left < right:
                sub_target = nums[left] + nums[right]
                if sub_target == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # right -= 1
                    # while right > left and nums[right] == nums[right + 1]:
                    #     right -= 1
                elif sub_target < target:
                    left += 1
                elif sub_target > target:
                    right -= 1
        else:
            for i in range(left, right + 1, +1):
                if i > left and nums[i] == nums[i - 1]:
                    continue
                find_n_sum(i + 1, right, target -
                           nums[i], n - 1, result + [nums[i]], results)
    nums.sort()
    results = []
    find_n_sum(0, len(nums) - 1, target, n, [], results)
    # return results
    print(results)


n_sum([-1, 0, -5, -2, -2, -4, 0, 1, -2], -9, 4)
