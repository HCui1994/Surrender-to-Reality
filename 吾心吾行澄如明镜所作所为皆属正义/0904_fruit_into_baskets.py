"""
In a row of trees, the i-th tree produces fruit with type tree[i].
You start at any tree of your choice, then repeatedly perform the following steps:
Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: 
    you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
You have two baskets, and each basket an carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
What is the total amount of fruit you can collect with this procedure?

Example 1:
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Example 2:
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Example 3:
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Example 4:
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 
Note:
1.  1 <= tree.length <= 40000
2.  0 <= tree[i] < tree.length
"""


class Solution(object):
    def total_fruit_queue(self, tree):
        """
        求一个数组的最长连续子数组的长度，
        子数组最多有两个不同的数字
        尝试使用队列，使用 idx 遍历 tree 数列
        1.  如果 tree[idx] == queue[-1]，queue[-1] 计数器自增
        2.  如果 tree[idx] != queue[-1]，且 tree[idx] != queue[-2]，
            出队直到 len(queue) == 1
            tree[idx] 入队
        3.  如果 tree[idx] != queue[-1]，且 tree[idx] == queue[-2]
            tree[idx] 入队
        4.  如果 tree[idx] != queue[-1]，且当前队列长度仅为 1 
            tree[idx] 入队

        TLE
        """
        if len(tree) <= 2:
            return len(tree)
        queue = [{"type": tree[0], "counter": 1}, ]
        idx = 1
        max_fruit = 1
        while idx < len(tree):
            if tree[idx] == queue[-1]["type"]:
                queue[-1]["counter"] += 1
                idx += 1
            else:
                if len(queue) == 1:
                    queue.append({"type": tree[idx], "counter": 1})
                    idx += 1
                elif tree[idx] == queue[-2]["type"]:
                    temp_num_fruits = 0
                    for q in queue:
                        temp_num_fruits += q["counter"]
                    max_fruit = max(max_fruit, temp_num_fruits)
                    queue_length = len(queue)
                    # for _ in range(queue_length - 2):
                    #     queue.pop(0)
                    queue.append({"type": tree[idx], "counter": 1})
                    idx += 1
                elif tree[idx] != queue[-2]["type"]:
                    temp_num_fruits = 0
                    for q in queue:
                        temp_num_fruits += q["counter"]
                    max_fruit = max(max_fruit, temp_num_fruits)
                    queue_length = len(queue)
                    for _ in range(queue_length - 1):
                        queue.pop(0)
                    queue.append({"type": tree[idx], "counter": 1})
                    idx += 1
        temp_num_fruits = 0
        for q in queue:
            temp_num_fruits += q["counter"]
        max_fruit = max(max_fruit, temp_num_fruits)
        return max_fruit

    def total_fruit_two_pointers(self, tree):
        """
        队列求解的思想其实类似于双指针，但是 TLE
        https://blog.csdn.net/XX_123_1_RJ/article/details/82828570 
        获取 tree[] 其中的一个最长子序列，而且这个子序列，只有两种水果。
        解题思路：
        （1）使用双指针法或者是滑动窗口法，遍历整个 tree[] ，找到一个小区间内只有两个水果，而且，这个区间的长度是所有子区间最长的。
        （2）可以使用 cnt = {} 来保存一个区间的元素统计数，用i表示这个滑动窗口的左端，j表示换的窗口的右端，j随着遍历tree[] 一直向右端走。
        （3）每次遍历一个元素，就要更新 cnt = {} 并判断长度是否超过了2，如果超过了，此时就开始处理左端点i，i开始向右移动，同时更新 cnt = {}，直到 cnt = {} 的长度小于等于2，并更新保留一次最优的结果。
        """
        # cnt = {}
        # i = res = 0
        # for j, v in enumerate(tree):
        #     cnt[v] = cnt.get(v, 0) + 1  # cnt.get(v, 0) 从字典里获取一个数，如果不存在就默认为 0
        #     while len(cnt) > 2:  # 如果字典中的元素大于 2
        #         cnt[tree[i]] -= 1
        #         if cnt[tree[i]] == 0:
        #             del cnt[tree[i]]
        #         i += 1
        #     res = max(res, j - i + 1)  # 结束一个区间，更新一次最优结果
        # return res

        import collections
        counter = collections.Counter()
        left = res = 0
        for right, fruit_type in enumerate(tree):
            counter[fruit_type] += 1
            while len(counter) > 2:
                # 循环条件：counter 中统计了超过两个数字
                counter[tree[left]] -= 1
                if counter[tree[left]] == 0:
                    del counter[tree[right]]
                print(counter)
                left += 1
            res = max(res, right - left + 1)
        return res

    def test(self):
        tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
        self.total_fruit_two_pointers(tree)


Solution().test()
