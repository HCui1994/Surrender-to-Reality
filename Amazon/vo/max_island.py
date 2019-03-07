def max_island(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1
        di, dj = [1, -1, 0, 0], [0, 0, 1, -1]
        for k in range(4):
            ii, jj = i + di[k], j + dj[k]
            if 0 <= ii < m and 0 <= jj < n:
                area += dfs(ii, jj)
        return area

    max_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area
