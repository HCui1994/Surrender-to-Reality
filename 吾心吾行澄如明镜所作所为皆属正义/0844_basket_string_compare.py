"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1.  1 <= S.length <= 200
2.  1 <= T.length <= 200
3.  S and T only contain lowercase letters and '#' characters.
"""


class Solution(object):
    def backspace_compare_stack(self, s, t):
        """
        trivial 第一想到的肯定是使用 stack
        """
        stack_s, stack_t = [], []
        for ele in s:
            if ele == '#':
                if not stack_s:
                    continue
                else:
                    stack_s.pop()
            else:
                stack_s.append(ele)
        for ele in t:
            if ele == '#':
                if not stack_t:
                    continue
                else:
                    stack_t.pop()
            else:
                stack_t.append(ele)
        print(stack_s, stack_t)
        if stack_s == stack_t:
            return True
        else:
            return False

    def backspace_compare_two_pointers(self, s, t):
        """
        尝试双指针降低空间复杂度
        """
        s, t = s[::-1], t[::-1]
        ptr_s, ptr_t = len(s) - 1, len(t) - 1
        while ptr_s > 0 or ptr_t > 0:
            if 

    def test(self):
        s = "a##c"
        t = "#a#cbb"
        print(self.backspace_compare_stack(s, t))



Solution().test()