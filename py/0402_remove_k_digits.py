"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
1.  The length of num is less than 10002 and will be ≥ k.
2.  The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

class Solution:
    # def remove_k_digits(self, num, k):
    #     """
    #     one pass
    #     从最高位开始，找k个最大的数
    #     如果 num[i:j] 递增，而 num[j] < num[j - 1], 删除　num[j - 1]
    #     如果 num[i:-1] 全递增，但还剩 kk 个需要删除，删除最后 kk 个
    #     如果 num[i:-1] 全递减，但还剩 kk 个需要删除，删除最前 kk 个
    #     """
    #     sentinal_num = [0] + [int(digit) for digit in num] + [float("inf")]
    #     for ik in range(k):
    #         idx = 1
    #         while num[idx] > num[idx - 1] and idx < len(sentinal_num) + 1:
    #             idx += 1
    #         if idx == len(sentinal_num):
    #             break
    #         sentinal_num.pop(idx)

    #     # while idx in range
    #     return sentinal_num

    def remove_k_digits(self, num, k):
        """
        using stack
        """
        if len(num) == k:
            return "0"
        stack = ['0']
        idx = 0
        while k > 0 and idx < len(num):
            print(k, idx, stack)
            if num[idx] >= stack[-1]:
                stack.append(num[idx])
                idx += 1
            elif num[idx] < stack[-1]:
                stack.pop()
                k -= 1
        # print(stack)
        if k > 0:
            res =  "".join((stack + list(num[idx:])))[:-k]
        else:
            res = "".join((stack + list(num[idx:])))
        return str(int(res))
                
        

    def test(self):
        num = "10200"
        k = 1
        print(self.remove_k_digits(num, k))


Solution().test()


        