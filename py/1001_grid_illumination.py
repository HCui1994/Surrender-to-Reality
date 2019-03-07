"""
On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.  Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].

 

Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation: 
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1
Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1
Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.
 

Note:

1 <= N <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == queries[i].length == 2
"""

import collections


class Solution(object):
    def grid_illumination(self, n, lamps, queries):
        lamps = set(map(tuple, lamps))
        horizontal = collections.Counter()
        vertical = collections.Counter()
        left_oblique = collections.Counter()
        right_oblique = collections.Counter()

        for x, y in lamps:
            horizontal[x] += 1
            vertical[y] += 1
            left_oblique[x + y] += 1
            right_oblique[x - y] += 1

        res = []
        for x, y in queries:
            res.append(1 if x in horizontal or y in vertical or x + y in left_oblique or x - y in right_oblique else 0)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    kill_x, kill_y = x + dx, y + dy
                    if (kill_x, kill_y) in lamps:
                        lamps.remove((kill_x, kill_y))
                        horizontal[kill_x] -= 1
                        vertical[kill_y] -= 1
                        left_oblique[kill_x + kill_y] -= 1
                        right_oblique[kill_x - kill_y] -= 1
                        if horizontal[kill_x] == 0:
                            del horizontal[kill_x]
                        if vertical[kill_y] == 0:
                            del vertical[kill_y]
                        if left_oblique[kill_x + kill_y] == 0:
                            del left_oblique[kill_x, kill_y]
                        if right_oblique[kill_x - kill_y] == 0:
                            del right_oblique[kill_x - kill_y]
        return res

    def test(self):
        N = 5
        lamps = [[0, 0], [4, 4]]
        queries = [[1, 1], [1, 1]]
        self.grid_illumination(N, lamps, queries)


Solution().test()
