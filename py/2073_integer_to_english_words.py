"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


class Solution(object):
    def number_to_words(self, num):
        return " ".join(self.split_title(num))

    def split_title(self, num):
        num_buf = []
        while num:
            num, remiander = divmod(num, 1000)
            num_buf.append(remiander)
        big_title = {0: None, 1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion"}
        res_buf = []
        for i in range(len(num_buf)):
            if num_buf[i] > 0:
                if i == 0:
                    res_buf += self.split_num(num_buf[i])[::-1]
                else:
                    res_buf.append(big_title[i])
                    res_buf += self.split_num(num_buf[i])[::-1]
        return res_buf[::-1]

    def split_num(self, num):
        small_title = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                       10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                       20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        res_buf = []
        num, remainder = divmod(num, 100)
        if num > 0:
            res_buf.append(small_title[num])
            res_buf.append("Hundred")
        if remainder > 0:
            if remainder in small_title:
                res_buf.append(small_title[remainder])
            else:
                num, remainder = divmod(remainder, 10)
                print(num, remainder)
                res_buf.append(small_title[num * 10])
                res_buf.append(small_title[remainder])
        return res_buf


if __name__ == "__main__":
    soln = Solution()
    ans = soln.number_to_words(1000000)
    print(ans)
