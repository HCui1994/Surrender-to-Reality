"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.
The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"

Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""


class Soltuion(object):
    def neraest_palindromic(self, n):
        length = len(n)
        pre, suf = n[:length // 2], n[::-1][:length // 2]
        
        if pre != suf:
            return pre + pre[::-1]
        else:
            pre_int = int(pre)
            if length % 2 == 0:
            diff = pre_int




if __name__ == "__main__":
    soln = Soltuion()
    soln.neraest_palindromic("123456")
