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

class Solution:
    def __init__(self):
        self._cooldown = None
        self._tasks = None

    def least_interval(self, tasks, n):
        """
        第一感觉类似于 buy and sell stock with cool down。
        问题在于本题中 cooldown 的时间不确定，进程数（状态数）也不确定

        尝试遍历到所有的情况，使用 dfs

        WA
        """
        import collections
        self._cooldown = n
        self._task_couter = collections.Counter(tasks)
        # self._memoization = {}
        return self._dfs(cooldown_task=None, cooldown_remain=0, elapse_time=0, task_seq=[])

    def _dfs(self, cooldown_task, cooldown_remain, elapse_time, task_seq):
        """
        cooldown_task：正在等待冷却的进程
        task_remain：剩余冷却时间
        """
        # print(cooldown_task, cooldown_remain, elapse_time)
        no_task_remian = True
        min_elapse_time = float("inf")
        for task, task_remain in self._task_couter.items():
            if task_remain:
                # 如果某个进程还有剩余
                no_task_remian = False
                if cooldown_task == task and cooldown_remain:
                    # 如果某个进程正在冷却，进程计数器不自减
                    min_elapse_time = min(min_elapse_time, self._dfs(task, cooldown_remain-1, elapse_time+1, task_seq + ["#"]))
                else:
                    # 进程没在冷却
                    if cooldown_remain == 0:
                        cooldown_remain = self._cooldown
                    else:
                        cooldown_remain -= 1
                    self._task_couter[task] -= 1
                    min_elapse_time = min(min_elapse_time, self._dfs(task, cooldown_remain, elapse_time+1, task_seq + [task]))
                    self._task_couter[task] += 1
        if no_task_remian:
            # 如果没有剩余的进程了，当前进程结束后全部结束，返回一个时间片
            print(task_seq)
            return 0
        else:
            return min_elapse_time + 1


    def least_interval_2(self, tasks, n):
        """
        由于每两个相同进程之间需要冷却，优先考虑数量最多的进程，按照间隔 n 排列
        贪心？
        先确定好高频进程的

        """
        import collections
        tasks_counter = collections.Counter(tasks)
        majority_task = None    # 数量最多的某个进程
        majority_num = 0        # 数量最多的进程个数
        majority_dup = 0        # 有多少个数量最多的进程
        for task, task_num in tasks_counter.items():
            if task_num > majority_num:
                task_num = majority_num
                majority_task = task
        for task, task_num in tasks_counter.items():
            if task_num == majority_num:
                majority_dup += 1
        part_count = majority_num - 1
        part_length = n - (majority_dup - 1)
        empty_slots = part_count * part_length
        tasks_left = len(tasks) - majority_num * majority_dup
        idles = max(0, empty_slots - tasks_left)
        return len(tasks) + idles



    

    def test(self):
        tasks = ["A","A","A","B","B","B"]
        n = 2
        print(self.least_interval_2(tasks, n))

Solution().test()
        