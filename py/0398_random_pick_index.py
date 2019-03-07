"""
Given an array of integers with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""
import collections
import random


class SpecialList:

    def __init__(self, nums):
        self.slist = collections.defaultdict(set)
        for i, num in enumerate(nums):
            self.slist[num].add(i)
        self.nums = nums

    def remove(self, target):
        if target not in self.slist:
            return
        target_idx = random.sample(self.slist[target], 1)[0]
        last = self.nums[-1]
        last_idx = len(self.nums) - 1
        self.nums[last_idx], self.nums[target_idx] = self.nums[target_idx], self.nums[last_idx]
        self.nums.pop()
        self.slist[last].remove(last_idx)
        self.slist[last].add(target_idx)
        self.slist[target].remove(target_idx)
        if not self.slist[target]:
            del self.slist[target]

    def add(self, target):
        self.nums.append(target)
        self.slist[target].add(len(self.nums) - 1)

    def inspect(self):
        print(self.nums)
        print(self.slist)

    def pick(self, target) -> int:
        if target not in self.slist:
            return None
        return random.sample(self.slist[target], 1)[0]
        # Your Solution object will be instantiated and called as such:
        # obj = Solution(nums)
        # param_1 = obj.pick(target)


if __name__ == "__main__":
    special_list = SpecialList([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
    special_list.remove(1)
    special_list.add(999)
    special_list.inspect()
    for _ in range(10):
        print(special_list.pick(5))
