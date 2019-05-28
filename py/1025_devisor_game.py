"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        self.memo = {}
        return self.pick(n, True)

    def pick(self, n, player):
        if n == 1:
            return False
        if (n, player) in self.memo:
            return self.memo[n, player]
        self.memo[n, player] = False
        for x in range(n - 1, 0, -1):
            if n % x == 0:
                self.memo[n, player] = self.memo[n, player] or (not self.pick(n - x, not player))
                if self.memo[n, player]:
                    return True
        return False



print(Solution().divisorGame(5))