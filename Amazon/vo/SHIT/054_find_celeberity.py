def knows(a, b):
    return True


class Solution(object):
    def find_celeberity(self, n):
        self.n = n
        self.not_celebrity = set()
        self.visited = set()
        for i in range(n):
            if i not in self.visited:
                self._dfs(i)

    def _dfs(self, v):
        if v in self.visited:
            return 
        self.visited.add(v)
        for u in range(self.n):
            if knows(v, u):
                self.not_celebrity.add(u)
                self._dfs(u)