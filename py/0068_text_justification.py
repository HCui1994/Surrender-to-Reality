"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

class Solution(object):
    def fully_justify(self, words, max_width):
        res = []
        idx = 0
        while idx < len(words):
            line_words = [words[idx]]
            line_len = len(words[idx])  # 初始化一个新行
            idx += 1
            while idx < len(words) and line_len + 1 + len(words[idx]) <= max_width:
                # 当前行可以容纳一个space与下一个word
                line_len += 1 + len(words[idx])
                line_words.append(words[idx])
                idx += 1
            # 行填满，开始justify
            num_break = len(line_words) - 1
            if num_break == 0:
                # 如果某一行只有一个单词， 不做justify
                line_str = line_words[0] + " " * (max_width - line_len)
                res.append(line_str)
            else:
                # 如果某一行有超过一个单词
                space_remain = max_width - line_len  # 剩余的空格数
                quotient, remainder = divmod(space_remain, num_break)
                # 每个间隔添加 quotient个空格，前remainder个间隔额外添加一个空格
                line_str = ""
                for word in line_words[:-1]:
                    line_str += word
                    line_str += " "
                    line_str += " " * quotient
                    if remainder:
                        line_str += " "
                        remainder -= 1
                line_str += line_words[-1]
                res.append(line_str)
        last_line = res.pop().split(" ")
        last_line_str = ""
        for word in last_line:
            if word:
                last_line_str += word + " "
        last_line_str += " " * (max_width - len(last_line))
        return res


if __name__ == "__main__":
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    soln = Solution()
    soln.fully_justify(words, 20)
