"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. 
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973

Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

class Solution:
    def maximum_swap_brutal(self, num):
        """ 
        先从暴力求解开始考虑
        从后往前找最大的，从前往后找最小的 
        """
        num_str = list(str(num))
        length = len(num_str)
        max_num = num
        for i in range(length - 1):
            for j in range(length - 1, i, -1):
                num_str[i], num_str[j] = num_str[j], num_str[i]
                max_num = max(max_num, self.list_to_int(num_str))
                num_str[i], num_str[j] = num_str[j], num_str[i]
        return max_num

    def list_to_int(self, l):
        i = 0
        for d in l:
            i = i * 10 + int(d)
        return i

    def maximum_swap_greedy(self, num):
        """
        总共只有十个数，从后开始先找 target = 9，再找 8, 7, 6,...
        从末位找第一个等于 target 的低位数字，找到后，从首位找第一个小于 target 的高位数字,
        找到后直接 swap，return
        """
        num_str = list(str(num))
        length = len(num_str)
        for target in range(9, 0, -1):
            print(num_str)
            for back in range(length - 1, 0, -1):
                if int(num_str[back]) == target:
                    print(target, back)
                    for front in range(back):
                        if int(num_str[front]) < target:
                            num_str[back], num_str[front] = num_str[front], num_str[back]
                            return self.list_to_int(num_str)
        return num        


    def test(self):
        num = 99901
        print(self.maximum_swap_greedy(num))

    
Solution().test()
            