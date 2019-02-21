class Solution:
    # insertion sort
    def merge(self, nums1, m, nums2, n):
        if m == 0:
            nums1[m:] = nums2
        for num2 in nums2:
            i = m-1
            while nums1[i] > num2 and i >= 0:
                nums1[i+1] = nums1[i]
                i -= 1
            nums1[i+1] = num2
            m += 1 # 记得m自增！

    # 同理还可以bubblesort
    def merge2(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        for i in range(m, m+n, +1):
            j = i - 1
            while nums1[j] > nums1[j+1] and j >=0 :
                nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
                j -= 1
        



solution = Solution()
nums1 = [0]
m = 0
nums2 = [1]
n = 1
solution.merge(nums1, m, nums2, n)
print(nums1)