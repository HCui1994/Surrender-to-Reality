class Solution(object):
    def all_paths(self, grid, begin_i, begin_j, end_i, end_j):
        if not grid or not grid[0]:
            return []
        # init
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.end_i, self.end_j = end_i, end_j
        self.visited = set()
        self.paths = []
        self.dfs(begin_i, begin_j, [(begin_i, begin_j)])
        return self.paths
        

    def dfs(self, i, j, path):
        if self.grid[i][j] == "obstacle":
            return
        if (i, j) in self.visited:
            return
        if i == self.end_i and j == self.end_j:
            self.paths.append(path)
            return
        self.visited.add((i, j))
        di, dj = [0, 0, -1, 1], [-1, 1, 0, 0]
        for k in range(4):
            ii = i + di[k]
            jj = j + dj[k]
            if 0 <= ii < self.m and 0 <= jj < self.n:
                self.dfs(ii, jj, path + [(ii, jj)])
        self.visited.remove((i, j))