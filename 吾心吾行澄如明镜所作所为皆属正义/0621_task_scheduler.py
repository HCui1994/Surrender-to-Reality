"""
Given a char array representing tasks CPU need to do. 
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. 
Each task could be done in one interval. 
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, 
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
1.  The number of tasks is in the range [1, 10000].
2.  The integer n is in the range [0, 100].
"""

import collections
class Solution:
    # def __init__(self):
    #     self._cooldown = None
    #     self._tasks = None

    # def least_interval(self, tasks, n):
    #     """
    #     第一感觉类似于 buy and sell stock with cool down。
    #     问题在于本题中 cooldown 的时间不确定，进程数（状态数）也不确定

    #     尝试遍历到所有的情况，使用 dfs
    #     """
    #     self._cooldown = n
    #     self._task_couter = collections.Counter(tasks)
    #     return self._dfs(cooldown_task=None, cooldown_remain=0, elapse_time=0) + 1

    # def _dfs(self, cooldown_task, cooldown_remain, elapse_time):
    #     """
    #     cooldown_task：正在等待冷却的进程
    #     task_remain：剩余冷却时间
    #     """
    #     print(cooldown_task, cooldown_remain, elapse_time)
    #     no_task_remian = True
    #     min_elapse_time = float("inf")
    #     for task, task_remain in self._task_couter.items():
    #         if task_remain:
    #             # 如果某个进程还有剩余
    #             no_task_remian = False
    #             if cooldown_task == task and cooldown_remain:
    #                 # 如果某个进程正在冷却，进程计数器不自减
    #                 min_elapse_time = min(min_elapse_time, self._dfs(task, cooldown_remain-1, elapse_time+1))
    #             else:
    #                 # 进程没在冷却
    #                 if cooldown_remain == 0:
    #                     cooldown_remain = self._cooldown
    #                 else:
    #                     cooldown_remain -= 1
    #                 self._task_couter[task] -= 1
    #                 min_elapse_time = min(min_elapse_time, self._dfs(task, cooldown_remain, elapse_time+1))
    #                 self._task_couter[task] += 1
    #     if no_task_remian:
    #         # 如果没有剩余的进程了，当前进程结束后全部结束，返回一个时间片
    #         return 1
    #     else:
    #         return min_elapse_time + 1


    

    def test(self):
        tasks = ["A","A","A","B","B","B", "C"]
        n = 2
        print(self.least_interval(tasks, n))

Solution().test()
        