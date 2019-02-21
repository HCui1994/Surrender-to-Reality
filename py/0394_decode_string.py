"""
Given an encoded string, return it's decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


"""

class Solution:
    def __init__(self):
        self._string = None
        self._ptr = 0
        self._length = 0
        self._result = ""

    def decode_string(self, s):
        """
        上下文无关文法。
        语法分析，我tm全忘了
        LL(1) 文法：叶节点从左到右即为分析后的文法
        LL(1): 从左向右扫描，产生最左推导
        
        本题不是LL(1)文法？<string> -> number [ <string> ] 产生了一个右推导

        注意点：要么全都 return，要么全都直接打印， 

        # <string> -> <string> <string>  错误的语法设计，产生了左侧递归
        <string> -> number [ <string> ] <string>
        <string> -> word <string>
        <string> -> epsilon
        """
        self._string = s
        self._length = len(s)
        while self._ptr < self._length:
            self._result += self._parser()
        return self._result

    def _parser(self):
        if self._ptr == self._length or self._string[self._ptr] == ']':
            self._ptr += 1
            return ""
        if self._string[self._ptr] >= "0" and self._string[self._ptr] <= "9":
            num = ""
            while self._string[self._ptr] >= "0" and self._string[self._ptr] <= "9":
                num += self._string[self._ptr]
                self._ptr += 1
            num = int(num)
            self._ptr += 1 # 跳过 '['
            string1 = self._parser()
            string2 = self._parser()
            return num * string1 + string2
        elif (self._string[self._ptr] >= "a" and self._string[self._ptr] <= "z") or (heself._string[self._ptr] >= "A" and self._string[self._ptr] <= "Z"):
            word = ""
            while self._ptr < self._length and ((self._string[self._ptr] >= "a" and self._string[self._ptr] <= "z") or (self._string[self._ptr] >= "A" and self._string[self._ptr] <= "Z")):
                word += self._string[self._ptr]
                self._ptr += 1
            string = self._parser()
            return word + string

    # def _decode_string_iterative(self, s):
    #     """
    #     尝试递推求解
    #     """
    #     number_stack = []
    #     string_stack = []
    #     number = 0
    #     string = ""
    #     self._string = s
    #     self._length = len(s)
    #     while self._ptr < self._length:
    #         if self._string[self._ptr] >= '0' and self._string[self._ptr] <= '9':
    #             num = ""
    #             while self._string[self._ptr] >= '0' and self._string[self._ptr] <= '9':
    #                 num += self._string[self._ptr]
    #                 self._ptr += 1
    #             number = int(num)
    #         elif self._string[self._ptr] == '[':
    #             number_stack.append(number)
    #             string_stack.append(string)
    #             number = 0
    #             string = ""
    #             self._ptr += 1
    #         elif self._string[self._ptr] == ']':
    #             string += number_stack.pop() * string_stack.pop()
    #             self._ptr += 1
    #         else:
    #             string += self._string[self._ptr]
    #             self._ptr += 1
    #     print(string)
    #     print(string_stack.pop())
                




        
            
            

    def test(self):
        s = "2[abc]3[cd]ef"
        print(self._decode_string_iterative(s))


Solution().test()
