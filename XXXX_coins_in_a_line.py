"""
There are **n** coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.
Could you please decide the first play will win or lose?
Example
n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true.
n = 5, return true.
"""


class Solution:
    """ THIS DOES NOT WORK ... WHY ? """
    def __init__(self):
        self._memo = {}
        self._memo[1] = self._memo[2] = True

    def win_or_lose(self, coins):
        player = True
        if self._pick(coins - 2, not player) and self._pick(coins - 1, not player):
            self._memo[coins] = False
        else:
            self._memo[coins] = True
        print(self._memo)
    
    def _pick(self, coins, player):
        """
        Args:
            coins: number of coins remaining of Integer
            player: currently who is mastering this branch of Boolean, True = self, False = rival
        Returns:
            status: win or lose when first pick at this branch
        """
        if coins in self._memo.keys():
            if player:  # 当前为自己取子
                return self._memo[coins]
            else:       # 当前为对手取子
                return not self._memo[coins]
        if player:  # 如果当前是自己取子，下一轮对手取子，两个分支有一个不能取胜即可
            if self._pick(coins - 2, not player) and self._pick(coins - 1, not player):
                self._memo[coins] = False
                return False
            else:
                self._memo[coins] = True
                return True
        else:       # 如果当前是对手取子，下一轮为自己取子，两个分支必须全部能够获胜
            if self._pick(coins - 2, not player) and self._pick(coins - 1, not player):
                return False
            else:
                return True

    def win_or_lose_2(self, coins):
        """ 无法理解 """
        # memo[i]: i 个硬币，先手取，是输还是赢？
        memo = [False for _ in range(coins + 1)]
        memo[0] = False
        memo[1] = memo[2] = True
        memo[3] = False
        for i in range(4, coins + 1, +1):
            # 先手取 一个硬币 和 两个硬币 的分支
            # 轮到对手，取一个和取两个，如果对手的两个分支都保证获胜，则自己负
            # pick_one = not(memo[i - 1 - 1] and memo[i - 1 - 2])  # 为什么不用取反？如果对方起手的两个情况都获胜，自己就输了
            # pick_two = not(memo[i - 2 - 1] and memo[i - 2 - 2])  # 应该至少对手的两个情况中有一个会输，自己才能获胜
            pick_one = memo[i - 1 - 1] and memo[i - 1 - 2]
            pick_two = memo[i - 2 - 1] and memo[i - 2 - 2]
            memo[i] = pick_one or pick_two
        print(memo)
        return memo[-1]

    def win_or_lose_3(self, coins):
        memo = [None for _ in range(coins + 1)]
        return self._mem_search(coins, memo)
    
    def _mem_search(self, coins, memo):
        if memo[coins] is not None:
            return memo[coins]
        if coins == 0:
            memo[coins] = False
        elif coins == 1:
            memo[coins] = True
        elif coins == 2:
            memo[coins] = True
        elif coins == 3:
            memo[coins] = False
        else:
            # still not clear ???????
            pick_one = self._mem_search(coins - 2, memo) and self._mem_search(coins - 3, memo)
            pick_two = self._mem_search(coins - 3, memo) and self._mem_search(coins - 4, memo)
            memo[coins] = pick_one or pick_two
        return memo[coins]

    def _win_or_lose_4(self, coins):
        """ 方法4类似方法1 """
        memo = [None for _ in range(coins + 1)]
        self._mem_search_2(coins, memo)
        print(memo)
        return(memo[-1])

    def _mem_search_2(self, coins, memo):
        if memo[coins] is not None:
            return memo[coins]
        if coins == 0:
            memo[coins] = False
        elif coins == 1:
            memo[coins] = True
        else:
            memo[coins] = not self._mem_search_2(coins - 1, memo) or not self._mem_search_2(coins - 2, memo)
            # 我的两个选项：拿走一个硬币，和拿走两个硬币
            # 切换到对手视角，如果我的两个选项之后，对手都能获得成功，则我的两个选项都无法使我胜利
            # 如果对手有一个方法会失败，则我会成功
        return memo[coins]




soln = Solution()
nums = 10
soln._win_or_lose_4(nums)
