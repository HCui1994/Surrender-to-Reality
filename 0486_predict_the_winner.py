"""
Given an array of scores that are non-negative integers. 
Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. 
Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. 
The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False

Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.

Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Note:
1. 1 <= length of the array <= 20.
2. Any scores in the given array are non-negative integers and will not exceed 10,000,000.
3. If the scores of both players are equal, then player 1 is still the winner.
"""
import numpy as np
class Solution:
    def predict_the_winner(self, nums):
        """
        dynamic ptogramming
        """
        if not len(nums):
            return True
        # memo[i][j][0] 表示 在数列 nums[i:j] 上先手可获得最大值
        # memo[i][j][1] 表示 数列 nums[i:j] 的和
        memo = [[[0, 0] for _ in range(len(nums) + 1)] for _ in nums]
        # 初始化， 只有一个数字的时候，player 1 总获胜
        for i in range(len(nums)):
            memo[i][i + 1] = [nums[i], nums[i]]
        print(np.array(memo).shape)
        for l in range(2, len(nums) + 1, +1):
            for i in range(0, len(nums) - 1, +1):
                j = i + l
                # print(i, j)
                if j > len(nums):
                    break
                # 此时，memo[i:j] 表示 player1 在数列nums[i:j]上 先手能否获胜
                # 子问题：在数列[i:j-1] 和 memo[i+1:j]，
                # 表示 player2 先手时，player2能否获胜
                # 如果两种情况 player2都能够获胜，则 player1 在数列 nums[i:j]上无法获胜
                # player1 从左侧取
                left, right = nums[i], nums[j - 1]
                # 如果player1从左侧取，可得到的值为，left + sum(nums[i+1:j] - player2_val)
                pick_from_left = left + (memo[i + 1][j][1] - memo[i + 1][j][0])
                # 从右侧取，同理
                pick_from_right = right + (memo[i][j - 1][1] - memo[i][j - 1][0])
                # player1 取到最大值
                memo[i][j][0] = max(pick_from_left, pick_from_right)
                memo[i][j][1] = nums[i] + memo[i + 1][j][1]
        player1, summation = memo[0][len(nums)]
        if player1 >= summation / 2:
            return True
        else:
            return False
        

        

    def test(self):
        nums = [1, 5, 233, 7]
        ans = self.predict_the_winner(nums)
        print(ans)


soln = Solution()
soln.test()