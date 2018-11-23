"""
An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.

Example 1:
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.

Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.

Note:
1.  intervals will have length in range [1, 3000].
2.  intervals[i] will have length 2, representing some integer interval.
3.  intervals[i][j] will be an integer in [0, 10^8].
"""

import functools

class Solution:
    def interserction_size_two(self, intervals):
        """
        根据区间末尾进行从小到大排序，若区间末尾相同，则按起始从大到小排序：优先考虑靠前的区间，优先考虑短区间
        当前的区间和维护的结果集合 ans 之间有三种可能性： (注意，由于所有区间按照区间末尾进行排序，结果集合应该是递增的)
        1.  如果当前区间起始大于结果集合的最大值，即当前区间与结果集完全没有交集
            将当前区间最后两个数加入结果集
        2.  如果当前区间的起始小于等于结果集和的最大数，但是大于结果集合的次大数，即当前区间中只有一个数在结果集和中
            则当前区间只需加入一个数即可。加入当前区间的末尾
            （由于所有区间按照区间的末尾进行排序，在此情况中，当前区间的末尾必然大于结果集合的最大数，即不在结果集合中）
        3.  如果当前区间的起始小于等于结果集合中次大的数，即当前区间中有至少两个数在结果集合中
            则不做任何操作
        """
        def cmp(a, b):
            if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
                return -1
            elif a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]):
                return 1
            return 0
        key = functools.cmp_to_key(cmp)
        intervals.sort(key=key)
        # 使用一个数组 ans 来维护结果
        # 初始化：
        interval = intervals[0]
        ans = [interval[1] - 1, interval[1]]
        for interval in intervals[1:]:
            print(ans)
            if interval[0] > ans[-1]:
                # 情况 1 ：当前区间起始大于结果集中最大的数
                ans.append(interval[1] - 1)
                ans.append(interval[1])
            elif interval[0] <= ans[-1] and interval[0] > ans[-2]:
                # 如果当前区间起始等于结果集和的最大值，加入当前区间的末尾
                ans.append(interval[1])
            else:
                pass
            
        return len(ans)

    def interserction_size_two_2(self, intervals):
        """
        solution by http://www.cnblogs.com/grandyang/p/8503476.html
        """
        def cmp(a, b):
            if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
                return -1
            elif a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]):
                return 1
            return 0
        key = functools.cmp_to_key(cmp)
        intervals.sort(key=key)
        ans = [-1, -1]
        for interval in intervals:
            print(ans)
            if interval[0] <= ans[-2]:
                # 如果当前区间起始小于结果集合中次大的数，说明当前区间至少包含了结果集中的两个数，当前区间不做任何处理
                pass
            elif interval[0] > ans[-1]:
                # 如果当前区间起始大于结果集合中的最大数，说明当前区间与结果集合没有交集，加入当前区间中最后两个数（注意先添加小的，后添加大的）
                ans.append(interval[1] - 1)
                ans.append(interval[1])
            else:
                # 生于一种情况，当前区间的起始小于结果集中的最大数，但是小于次大数，当前区间只需加入一个数
                ans.append(interval[-1])
        return len(ans) - 2

    def interserction_size_k(self, intervals, k):
        """
        follow up: 要求每个区间和结果集合的交集至少为 k，区间长度也至少为 k
        依然根据原有的排序方法，但是可能性扩展为 k + 1 个：
        交集大小为 0, 1, 2, 3, ...., k

        按照 grandyang 的解法进行修改，其初始化的方法更加先进
        """
        def cmp(a, b):
            if a[1] < b[1] or (a[1] == b[1] and a[0] > b[0]):
                return -1
            elif a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]):
                return 1
            return 0
        key = functools.cmp_to_key(cmp)
        intervals.sort(key=key)
        print(intervals)
        # 使用一个数组 ans 来维护结果
        # 初始化：
        interval = intervals[0]
        ans = [-1 for _ in range(k)]
        for interval in intervals[1:]:
            print(ans)
            for i in range(k):
                # 结果集合从大到小遍历，找到当前区间与结果集合的交集大小是多少
                if interval[0] < ans[-1 - i]:
                    # 如果 当前区间起始小于等于结果集和第 i 大的数，继续遍历
                    # 直到发现当前区间的起始大于等于结果集和中第 i 大的数
                    # 说明当前区间中有 i 个数在结果集合中，需要再加入 k - i 个数
                    break
            print(i)
            temp_ans = []
            for j in range(i):
                print(temp_ans)
                temp_ans.append(interval[1] - i)
            ans += temp_ans[::-1]
        
        return len(ans) - k
                

        

    def test(self):
        intervals = [[12,19],[18,25],[4,6],[19,24],[19,22]]
        # print(self.interserction_size_two(intervals))
        # print(self.interserction_size_two_2(intervals))
        print(self.interserction_size_k(intervals, 2))


soln = Solution()
soln.test()