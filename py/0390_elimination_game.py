"""
There is a list of sorted integers from 1 to n. 
Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""

class Solution(object):
    def last_remaining(self, n: int) -> int:
        """
        l => odd
        1 2 3 4 5 6 7 8 9
          2   4   6   8  
          2       6 
                  6
        """
        if not n:
            return None
        if len(n) == 1:
            return n[0]
        cnt = 0
        index = 0
        rnd = 1
        l2r = True
        while cnt < len(n) - 1:
            if l2r:
                while index < len(n):

