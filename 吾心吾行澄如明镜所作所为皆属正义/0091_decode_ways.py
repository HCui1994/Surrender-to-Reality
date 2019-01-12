"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution(object):
    def num_decodings_recursive(self, encode):
        """
        dfs，从左向右扫描，创建所有可能的分支
        又是一个 nfa dfa 问题：有穷自动机将在不确定出进行猜测，每一种猜测将创建一个不同的分支
        由于 0 的存在，不能保证所有的编码都是合法的
            且由于有 26 个字母，
        => 每次需要考虑两位
        case0：string 的长度为 0 => 一次成功的匹配，返回 1 
        case1：string 的第一位为 0 => 无效的编码，返回 0
        case2：string 的长度为 1 => 返回 1
        case3：string 的长度大于等于 2
            case3.1：string[:2] 代表的数字大于 26，创建一个新分支，继续调用
            case3.2：string[:2] 代表的数字小于等于26：创建两个新分支
        TLE
        nfa <=> RE，正则表达式匹配始终是比较慢的解法
        """
        return self.nfa(encode)

    def nfa(self, encode):
        print(encode)
        if not encode:
            return 1
        elif encode[0] == "0":
            return 0
        elif len(encode) == 1:
            return 1
        else:
            if int(encode[:2]) > 26:
                return self.nfa(encode[1:])
            else:
                return self.nfa(encode[1:]) + self.nfa(encode[2:])


    def num_decoding_dp(self, encode):
        """
        dp[i] 表示：encode[:i] 有多少种解码方式
        """
        if not encode or encode[0] == '0':
            return 0
        dp = [0 for _ in encode]
        dp[0] = dp[-1] = 1 # 初始化
        for i in range(1, len(encode)):
            if encode[i - 1] == '0' and encode[i] == '0':
                # 如果连着两个 0，则是无效的编码，无法解码
                return 0
            two_bit = int(encode[i - 1: i + 1])
            print(two_bit)
            if encode[i] == '0':
                # 如果当前为 0，无法进行一位解码
                if two_bit <= 26:
                    # 如果可以进行两位解码
                    dp[i] = dp[i - 2]
                else:
                    # 否则是无效的编码，无法进行解码
                    return 0
            else:
                # 如果当前位不为 0，可以进行一位解码，可能可以进行两位解码
                one_bit_decode = dp[i - 1]
                if two_bit <= 26 and two_bit >= 10:
                    two_bit_decode = dp[i - 2]
                else:
                    two_bit_decode = 0
                dp[i] = one_bit_decode + two_bit_decode
                print(dp)
        return dp[-1]



    def test(self):
        encode = "101"
        print(self.num_decoding_dp(encode))


Solution().test()