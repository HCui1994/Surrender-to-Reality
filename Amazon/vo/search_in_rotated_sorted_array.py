class Seacher(object):
    def search_in_rotated_array(self, nums, target):
        # corner case
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left + 1) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                # nums[left: mid + 1] sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            

