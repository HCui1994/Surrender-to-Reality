"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""

import numpy as np

class Solution(object):
    def convert(self, string, num_row):
        num_letters_one_zigzag = 2 * num_row - 2
        # print(num_letters_one_zigzag)
        num_zigzag = len(string) // num_letters_one_zigzag + 1
        num_col_per_zigzag = num_letters_one_zigzag - num_row + 1
        num_col = num_col_per_zigzag * num_zigzag

        zigzag = [['#' for _ in range(num_col)] for _ in range(num_row)]
        row, col = 0, 0
        direction = "down"
        for letter in string:
            zigzag[row][col] = letter
            if direction == "down":
                row += 1
                if row == num_row:
                    direction = "topright"
                    row -= 2
                    col += 1
            else:
                row -= 1
                col += 1
                if row == -1:
                    direction = "down"
                    row += 2
                    col -= 1
        res = ""
        for row in range(num_row):
            for col in range(num_col):
                if zigzag[row][col] != '#':
                    res += zigzag[row][col]
        return res


    def test(self):
        s = "PAYPALISHIRING"
        numRows = 4
        self.convert(s, numRows)


Solution().test()