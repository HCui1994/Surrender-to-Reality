"""
Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, 
count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. 
No jumps through non selected key is allowed.
The order of keys used matters.

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Invalid move: 4 - 1 - 3 - 6 
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

Example:

Input: m = 1, n = 1
Output: 9
"""

class Soltion:
    def __init__(self):
        self.visited = [False for _ in range(10)]
        self.jumps = [[None for _ in range(10)] for _ in range(10)]
        self.jumps[1][3] = self.jumps[3][1] = 2;
        self.jumps[4][6] = self.jumps[6][4] = 5;
        self.jumps[7][9] = self.jumps[9][7] = 8;
        self.jumps[1][7] = self.jumps[7][1] = 4;
        self.jumps[2][8] = self.jumps[8][2] = 5;
        self.jumps[3][9] = self.jumps[9][3] = 6;
        self.jumps[1][9] = self.jumps[9][1] = self.jumps[3][7] = self.jumps[7][3] = 5;
        self.m = self.n = 0

    def num_of_patterns_dfs(self, m, n):
        """
        这种问题，第一想到的应该还是，深度优先搜索
        """
        self.m = m
        self.n = n
        # self.visited = [False for _ in range(10)]
        res_1_3_7_9 = self.dfs_visit(num=1, len=1, res=0)
        # self.visited = [False for _ in range(10)]
        res_2_4_6_8 = self.dfs_visit(num=2, len=1, res=0)
        # self.visited = [False for _ in range(10)]
        res_5 = self.dfs_visit(num=5, len=1, res=0)
        return res_1_3_7_9 * 4 + res_2_4_6_8 * 4 + res_5

    def dfs_visit(self, num, len, res):
        """
        Args:
            num: 当前滑到的数字
            len: 到当前数字划过了多少数字
            res: 到当前数字 之前 有多少种滑法
        """
        # 只有在滑动长度大于 m 的时候，统计画法
        if len >= self.m:
            res += 1
        # 滑动到下一个数字，长度加 1 
        len += 1
        # 如果下一个数字长度超过范围，直接返回当前的画法数量
        if len > self.n:
            return res
        # 如果没有超过范围，设置当前数字已经滑过
        self.visited[num] = True
        for next_num in range(1, 10, +1):
            pass_by = self.jumps[num][next_num]
            if pass_by and not self.visited[pass_by]:
                # 如果从当前数字滑动到下一个数字，需要经过某个数字，且这个数字之前没有被滑到过，则是一个无效的滑法，跳过
                continue
            if self.visited[next_num]:
                # 如果下一个数字已经被滑过，则是一个无效的画法，跳过
                continue
            # 创建分支，去下一个数字
            # 下一个数字会继承当前的参数 len res，所以不是 res += dfs_visit(...), 每走到一个新的，范围内的节点，统计数就会 +1
            res = self.dfs_visit(num=next_num, len=len, res=res)
        # 离开当前分支的时候，设置已访问为 false，因为其父节点的其他分支与当前分支无关
        self.visited[num] = False
        return res

    def num_of_patterns_dfs_2(self, m, n):
        self.m = m
        self.n = n
        res_1_3_7_9 = self.dfs_visit_2(current_num=1, prev_len=1) * 4
        res_2_4_6_8 = self.dfs_visit_2(current_num=2, prev_len=1) * 4
        res_5 = self.dfs_visit_2(current_num=5, prev_len=1)
        return res_1_3_7_9 + res_2_4_6_8 + res_5
    
    def dfs_visit_2(self, current_num, prev_len):
        """ 
        WA 
        似乎无法用自底向上的方法来统计
        在该方法中，只能统计到从长度 m 到长度 n 有多少种走法
        但是题目的要求是，长度 m 到 m+1, m+2, ..., n
        可以想办法改正吗？
        """
        # 到达 dfs 搜索树的叶节点
        current_len = prev_len + 1
        self.visited[current_num] = True
        if current_len > self.n:
            self.visited[current_num] = False
            return 1
        res = 0
        for next_num in range(1, 10, +1):
            by_pass = self.jumps[current_num][next_num]
            if by_pass and not self.visited[by_pass]:
                continue
            if self.visited[next_num]:
                continue
            res += self.dfs_visit_2(next_num, current_len)
        print(res, current_len, current_num)
        if current_len < self.m:
            # 如果当前长度不足 m，当前数字不在统计范围内
            return res
        else:
            return res + 1

    def test(self):
        m, n = 3, 3
        ans1 = self.num_of_patterns_dfs(m, n)
        ans2 = self.num_of_patterns_dfs_2(m, n)
        print(ans1, ans2)

    
soln = Soltion()
soln.test()


