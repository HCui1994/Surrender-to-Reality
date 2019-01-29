"""
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"
 

Note:

0 <= A <= 100
0 <= B <= 100
It is guaranteed such an S exists for the given A and B.
"""

class Solution(object):
    def str_without_aaa_bbb(self, a, b):
        res = ""
        if a == b:
            for _ in range(a):
                res += "ab"
        elif a > b:
            diff = a - b
            if diff <= b:
                for _ in range(diff):
                    res += "aab"
                for _ in range(b - diff):
                    res += "ab"
            else:
                for _ in range(b):
                    res += "aab"
                res += "a" * (diff - b)
        else:
            diff = b - a
            if diff <= a:
                for _ in range(diff):
                    res += "bba"
                for _ in range(a - diff):
                    res += "ba"
            else:
                for _ in range(a):
                    res += "bba"
                res += "b" * (diff - a)
        # print(res)
        return res

    def test(self):
        A = 2
        B = 6
        self.str_without_aaa_bbb(A, B)
    
Solution().test()