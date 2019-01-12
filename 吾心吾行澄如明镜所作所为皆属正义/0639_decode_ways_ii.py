"""
A message containing letters from A-Z is being encoded to numbers using the following mapping way: 
'A' -> 1
'B' -> 2
...
'Z' -> 26

Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9. 
Given the encoded message containing digits and the character '*', return the total number of ways to decode it. 
Also, since the answer may be very large, you should return the output mod 109 + 7. 

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:
Input: "1*"
Output: 9 + 9 = 18

Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
"""

class Solution(object):
    def num_decodings_recursive(self, encode):
        """
        先尝试使用递归解法，构造一个有穷自动机
        """
        return self.nfa(encode)

    def nfa(self, encode):
        """
        case1：编码长度为 0，nfa 识别了整个编码串，是一个有效的解码，返回 1
        case3：若编码的第一位为 '0'，是一个无效的编码，返回 0
        case2：若编码长度为 1，（已经判断第一位不是 '0'），nfa 识别了整个编码串，返回 1  （也可以继续创建唯一分支，交给 case1 来处理）
        case4：若编码长度大于等于 2 （已经判断第一位不是 '0'）：
            case4.1：一位编码：
                case4.1.1：若 encode[0] in {1 .. 9}，产生 1 种解码方式
                case4.1.2：若 encode[0] = '*'，产生 9 种解码方式
            case4.2：两位编码：
                case4.2.1：若 encode[0] = '*', encode[1] = '*': 产生 {11 .. 19, 21 .. 26} 共 15 种解码
                case4.2.2：若 encode[0] = '*'，encode[1] in {0 .. 6}，产生 {10，11，12，13，14，15，16，20，21，22，23，24，25，26} 共14 种解码
                case4.2.3：若 encode[0] = '*'，encode[1] in {7, 8, 9}，产生 {17，18，19} 共3种解码
                case4.2.4：若 encode[1] = '*'，encode[0] = '1'：产生 {11，12，13，14，15，16，17，18，19} 9 种解码
                case4.2.5：若 encode[1] = '*'，encode[0] = '2'：产生 6 种解码
                case4.2.4：若 encode[:2] 代表的数字 in {10 .. 26}: 产生 1 种解码方式
                case4.2.5：否则，是无效的两位编码
        """
        if not encode:
            return 1
        elif encode[0] == '0':
            return 0
        elif len(encode) == 1:
            if encode == "*":
                return 9
            else:
                return 1
        else:
            if encode[0] == "*":
                one_bit_decode = self.nfa(encode[1:]) * 9
            else:
                one_bit_decode = self.nfa(encode[1:]) * 1
            if encode[0] == '*' and encode[1] == '*':
                two_bit_decode = self.nfa(encode[2:]) * 15
            elif encode[0] == '*' and encode[1] in ['0', '1', '2', '3', '4', '5', '6']:
                two_bit_decode = self.nfa(encode[2:]) * 14
            elif encode[0] == '*' and encode[1] in ['7', '8', '9']:
                two_bit_decode = self.nfa(encode[2:]) * 3
            elif encode[0] == '1' and encode[1] == '*':
                two_bit_decode = self.nfa(encode[2:]) * 9
            elif encode[0] == '2' and encode[1] == '*':
                two_bit_decode = self.nfa(encode[2:]) * 7
            elif encode[0] != '*' and encode[1] != '*' and int(encode[:2]) <= 26 and int(encode[:2]) >= 10:
                two_bit_decode = self.nfa(encode[2:]) * 1
            else:
                two_bit_decode = 0
            print(one_bit_decode, two_bit_decode)
            return one_bit_decode + two_bit_decode


    def test(self):
        encode = "1*"
        print(self.num_decodings_recursive(encode))
            
Solution().test()