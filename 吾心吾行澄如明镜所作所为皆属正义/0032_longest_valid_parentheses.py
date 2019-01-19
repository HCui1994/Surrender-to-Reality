"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

class Solution(object):
    def longest_valid_parentheses_brutal(self, string):
        """
        合法的括号串长度一定是偶数
        TEL O(n^3)
        """
        length = 0
        for start in range(len(string) - 1):
            if string[start] == ")":
                continue
            for end in range(start + 2, len(string) + 1, +2):
                if (end - start) % 2:
                    continue
                # print(string[start: end])
                stack = [string[start]]
                print(string[start: end])
                is_valid = True
                for par in string[start + 1: end]:
                    if par == "(":
                        stack.append(par)
                    elif not stack:
                        is_valid = False
                        break
                    else:
                        stack.pop()
                if not stack and is_valid:
                    length = max(length, end - start)
        # print(length)
        return length
                

    def longest_valid_parentheses_dp(self, string):
        """
        dp[i] 代表以为 string[i] 结尾的合法串长度
        case1：string[i] = "(" 合法串长度必然为 0 
        case2：string[i] = ")"
            pattern1 ( pattern2 )
            pattern ( )

        """
        string_len = len(string)
        dp = [0 for _ in range(string_len + 1)]
        for i in range(1, string_len):
            dpi = i + 1
            if string[i] == "(": # case1
                continue
            if string[i] == ")": # case2
                if string[i - 1] == "(":
                    # pattern ( )
                    dp[dpi] = 2 + dp[dpi - 2]
                else:
                    # pattern1 ( pattern2 )
                    if dp[dpi - 1]:
                        # pattern2 is valid
                        pattern2_len = dp[dpi - 1]
                        if i - pattern2_len - 1 >= 0 and string[i - pattern2_len - 1] == "(":
                            dp[dpi] = 2 + pattern2_len + dp[dpi - pattern2_len - 1 - 1]
        print(dp)
        return max(dp)


    def longest_valid_parentheses_stack(self, string):
        """ 
        wrong answer
        """
        stack = ['#']
        length = 0
        max_length = 0
        for par in string:
            print(stack)
            if par == "(":
                stack.append(par)
            else:
                stack.pop()
                length += 2
            if not stack:
                max_length = max(max_length, length - 2)
                length = 0
                stack.append('#')
        max_length = max(max_length, length)
        # print(max_length)
        return max_length


    def longest_valid_parentheses_stack_2(self, string):
        stack = [-1]
        max_length = 0
        for idx, par in enumerate(string):
            print(stack)
            if par == "(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    max_length = max(max_length, idx - stack[-1])
        print(max_length)
        return max_length









    def test(self):
        string = "())()"
        self.longest_valid_parentheses_stack_2(string)


Solution().test()