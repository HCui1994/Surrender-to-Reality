# one pass 最优解
class OnePass:
    def nextPermutation(self, nums):
        i = len(nums) - 2 # 下标从最后开始向前递增
        # 如果前一个大于等于后一个，下标向前推进，不做互换
        # 如果前一个小于后一个，记前一个的下标为i-1，后一个下标为 j=i，此时需要互换
        while i >= 0 and nums[i+1] <= nums[i]:  
            i -= 1
        # nums[i-1] 必将被向后换，但是要换到什么位置？   
        # nums[i:] 递减，如果要找到下一个最大排列，相当于发生了进位 
        # 既然是进位，就需要找到比 nums[i-1] 更大的最小元素
        # 下表j向后推进，直到 nums[j] > nums[i-1] and nums[j+1] <= nums[i-1]
        # 此时将 nums[i-1] 和 nums[j] 互换
        # 注意，此时仍有 nums[j] > nums[j+1], 即nums[i:]仍是非递增的
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i] , nums[j] = nums[j], nums[i]
        # 由于相当于发生了进位，nums[i:] 应当非递减
        # 直接倒转 nums[i:]

        # 边界：如果整个数列递减，则直接反转整个数列
        nums[i+1:] = nums[i+1:][::-1]
        return nums
 
    
# nums = [1,0,0]
# one_pass = OnePass()
# print(one_pass.nextPermutation(nums))



# Extension
# 字典序获得全排列
# 对于算法运行时得到的一个排列，如list=[2,4,3,1]，如何得到这个排列的下一个排列呢？
# 由尾部向前寻找第一个满足before<after的元素，并记下其下标low，在本例中即2对应low=0
# 从low的后一个元素开始向后寻找  最后一个  满足list[high]>list[low]的元素，并记下其下标high，在本例中即3对应high=2
# 将list[low]和list[high]对换，得到list=[3,4,2,1]
# 将下标low之后的所有元素翻转，得到list=[3,1,2,4]
class Permutation:
    def permutation(self, list):
        list = sorted(list)
        perm = [[_ for _ in list]]
        while True:
            low_index = len(list) - 1 - 1
            while low_index > 0 and list[low_index] >= list[low_index+1]:
                low_index -= 1
            if low_index == 0:
                break
            high_index = low_index + 1
            while high_index < len(list) and list[high_index] > list[low_index]:
                high_index += 1
            high_index -= 1
            list[low_index], list[high_index] = list[high_index], list[low_index]
            list[low_index+1:] = list[low_index+1:][::-1]
            perm.append([_ for _ in list])
        return perm



# permutation = Permutation()
# list = [1,3,2,4,3,5]
# print(permutation.permutation(list))


