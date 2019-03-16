class Solution(object):
    def two_sum(self, nums, target):
        # corner case
        if len(nums) < 2:
            return []
        # preprocess
        nums.sort()
        # two pointer init
        left, right = 0, len(nums) - 1
        res = []
        # core
        while left < right:
            if nums[left] + nums[right] == target:
                # find two sum == target, record
                res.append((nums[left], nums[right]))
                left += 1  # shrink window from left
                while left < right and nums[left] == nums[left - 1]:
                    # remove duplicate
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1  # need bigger two sum, shink winsow from left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1  # need smaller two sum, shrink window from right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        print(res)

        # time complexity:
        # preprocess - O(n log n) (sorting)
        # core - O(n)
        # total - O(n log n)
        # space complexity: O(1)  (sort could be in place)

    def two_sum_2(self, nums, target):
        import collections
        # corner case
        if len(nums) < 2:
            return []
        # preprocess
        counter = collections.Counter(nums)
        # core
        res = []
        for num in counter.keys():
            another_num = target - num
            if another_num in counter.keys():  # O(1)
                if another_num == num:
                    if counter[num] > 2:
                        res.append([num, another_num])
                else:
                    res.append([num, another_num])
        # remove dup
        res = res[:len(res) // 2 + 1]
        print(res)

        # time complexity:
        # preprocess - O(n) go through all nums
        # core - O(m)  m <=> number of diff nums
        # remove dup - O(1)
        # total - O(n)
        # space complexity
        # counter - O(m)  (number of diff nums)

    def two_sum_helper(self, nums, target):
        left, right = 0, len(nums) - 1
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                # find two sum == target, record
                res.append((nums[left], nums[right]))
                left += 1  # shrink window from left
                while left < right and nums[left] == nums[left - 1]:
                    # remove duplicate
                    left += 1
            elif nums[left] + nums[right] < target:
                left += 1  # need bigger two sum, shink winsow from left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1  # need smaller two sum, shrink window from right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
        return res

    def three_sum(self, nums, target):
        # corner case
        if len(nums) < 3:
            return []
        # preprocess
        nums.sort()
        # core -- a, b, c stands for three different components
        res = []
        ai = 0
        # for ai in range(len(nums) - 2):
        while ai < len(nums) - 2:  # better for removing dup
            a = nums[ai]
            b_plus_c = self.two_sum_helper(nums[ai + 1:], target - a)
            res += [[a, b, c] for b, c in b_plus_c]
            ai += 1
            while nums[ai] == nums[ai - 1]:
                ai += 1  # remove dup
        print(res)

        # time complexity
        # preprocess - O(n log n) (sorting)
        # core - outer while-loop  O(n)
        #        two_sum_helper() O(n)
        #       total - O(n^2)
        # total - O(n^2)
        # space complexity
        # O(1) - sorting in place

    def three_sum_smaller(self, nums, target):
        """
        find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target
        """
        # corner case
        if len(nums) < 3:
            return []
        # preprocess
        nums.sort()
        # core
        cnt = 0
        for ai in range(len(nums) - 2):  # do not need to remove dup
            bi, ci = ai + 1, len(nums) - 1
            while bi < ci:
                if nums[ai] + nums[bi] + nums[ci] < target:
                    cnt += ci - (bi + 1) + 1
                    bi += 1
                else:
                    ci -= 1
        print(cnt)

    def three_sum_closest(self, nums, target):
        # corner case
        if len(nums) < 3:
            return None
        # preprocess
        nums.sort()
        # init
        closest_sum = nums[0] + nums[1] + nums[-1]
        closest_diff = abs(closest_sum - target)
        ai = 0
        # core
        print(nums)
        while ai < len(nums) - 2:
            bi, ci = ai + 1, len(nums) - 1
            while bi < ci:
                diff = nums[ai] + nums[bi] + nums[ci] - target
                if abs(diff) < closest_diff:  # find closer sum, refresh
                    print(nums[ai], nums[bi], nums[ci])
                    closest_sum = nums[ai] + nums[bi] + nums[ci]
                    closest_diff = abs(diff)
                if diff >= 0:  # sum greater than target
                    ci -= 1
                    while bi < ci and nums[ci] == nums[ci + 1]:
                        # remove dup, speed boost
                        ci -= 1
                else:
                    bi += 1
                    while bi < ci and nums[bi] == nums[bi - 1]:
                        bi += 1
            ai += 1
            while ai < len(nums) - 2 and nums[ai] == nums[ai - 1]:
                ai += 1
        print(closest_sum)

    def three_sum_multi(self, nums, target):
        if len(nums) < 3:
            return 0
        nums.sort()
        cnt = 0
        ai = 0
        for ai in range(len(nums) - 2):
            bi, ci = ai + 1, len(nums) - 1
            while bi < ci:
                if nums[ai] + nums[bi] + nums[ci] > target:
                    ci -= 1
                elif nums[ai] + nums[bi] + nums[ci] < target:
                    bi += 1
                else:
                    # count duplicate one time
                    if nums[bi] == nums[ci]:
                        length = ci - bi + 1
                        cnt += length * (length - 1) // 2
                        break
                    else:
                        cnt_bi = cnt_ci = 1
                        bi += 1
                        while nums[bi] == nums[bi - 1]:
                            cnt_bi += 1
                            bi += 1
                        ci -= 1
                        while nums[ci] == nums[ci + 1]:
                            cnt_ci += 1
                            ci -= 1
                        cnt += cnt_bi * cnt_ci
                        continue
        return cnt

    def three_sum_multi_math(self, nums, target):
        import collections

        def _choose(m, n):
            if n == 1:
                return m
            if n == 2:
                return m * (m - 1) // 2
            if n == 3:
                return m * (m - 1) * (m - 2) // 6

        # preprocess
        counter = collections.Counter(nums)
        key_list = sorted(list(counter.keys()))

        MOD = 10 ** 9 + 7

        # core
        cnt = 0
        for ai in range(len(key_list)):
            for bi in range(ai, len(key_list)):
                a, b = key_list[ai], key_list[bi]
                c = target - a - b
                if c not in key_list or c < b or a + b + c != target:
                    continue
                if a != b and b != c:
                    cnt += (_choose(counter[a], 1) * _choose(counter[b], 1) * _choose(counter[c], 1))
                elif a == b and b != c:
                    if counter[a] < 2:
                        continue
                    cnt += (_choose(counter[a], 2) * _choose(counter[c], 1))
                elif a != b and b == c:
                    if counter[b] < 2:
                        continue
                    cnt += (_choose(counter[a], 1) * _choose(counter[b], 2))
                elif a == b and b == c:
                    if counter[a] < 3:
                        continue
                    cnt += _choose(counter[a], 3)
                cnt %= MOD
        return cnt

        # analysis
        # counting Combination - O(1)  (only choose 1 or 2 or 3)
        # preprocess: sorting - O(mlogm)   m -- number of diff nums
        #             counting - O(n)
        # core outer for-loop - m times
        #      inner for-loop - m times
        # total: O(n + mlogm + m^2)



if __name__ == "__main__":
    soln = Solution()
    # soln.two_sum_2([1, 1, 2, 5, 4, 2, 3, 4, 5, 6, 9, 8, 7, 5, 4, 3, 2], 4)
    # soln.three_sum([-1, 0, 1, 2, -1, -4], 0)
    # soln.three_sum_closest([0, 2, 1, -3], 1)
    soln.three_sum_multi_math([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], target=8)
