class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:

    def getAns1(self, s, k):
        """
        给定一个包含n个小写字母的字符串s，要求将字符串划分成若干个连续子串，子串中的字母类型相同，同时子串的字母个数不超过k，输出最少划分的子串数量。
        Given a string containing n lowercase letters, the string needs to be divided into several continuous substrings, 
        the letter in the substring should be same, and the number of letters in the substring does not exceed k, and output the minimal substring number meeting the requirement.
        """
        if not s:
            return 0
        seq_len = 1
        res = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                if seq_len == k:  # a max seq, count and reset
                    res += 1
                    seq_len = 1
                else:
                    seq_len += 1
            else:
                res += 1
                seq_len = 1
        return res

    def KSubstring(self, string, k):
        """
        给定字符串S和整数K, 计算长度为K且包含K个不同字符的子串数
        """
        import collections
        if len(string) < k:
            return 0  # corner case
        res = set()
        left, right = 0, k
        counter = collections.Counter(string[left: right])  # sliding window init
        if len(counter) == k - 1:  # check the first sliding window
            res.add(string[left: right])
        for left in range(1, len(string) - k + 1):
            right = left + k
            letter_left, letter_right = string[left - 1], string[right - 1]
            counter[letter_left] -= 1
            if counter[letter_left] == 0:
                del counter[letter_left]  # delete if no same letter in window
            counter[letter_right] += 1
            if len(counter) == k - 1:
                res.add(string[left: right])
        print(res)
        return len(res)

    def kClosest(self, points, origin, k):
        """
        给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。
        按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序
        """
        import heapq

        def dist(x, y):
            return (x - origin.x)**2 + (y - origin.y)**2
        pq = []
        for point in points:
            # x, y 坐标也要按最大堆形式入队
            x, y = point.x, point.y
            heapq.heappush(pq, (-dist(x, y), -x, -y))
            if len(pq) > k:
                heapq.heappop(pq)  # 形成最大堆，每次pop的都是距离最远的
        res = []
        while pq:
            res.append([-x for x in heapq.heappop(pq)[1:]])  # 出队时还原正负号
        return res[::-1]  # 结果还原为最小对 pop 顺序

    def nearestRestaurant(self, restaurants, n):
        """
        给出一个List，里面的数据代表每一个餐厅的坐标[x, y]。顾客的坐标处于原点[0, 0]。
        先找出n家离顾客位置最近的餐厅，然后取 n 家先出现在List中且与顾客的距离不超过 n 家离顾客最近的餐厅的最长距离。
        返回这 n 家餐厅的坐标序列，按输入数据原始的顺序。
        """
        import heapq
        if len(restaurants) < n or not restaurants:
            # 如果餐厅数量小于 n，则直接返回一个空序列
            return []
        pq = []  # 声明最大堆
        for x, y in restaurants:
            heapq.heappush(pq, - (x**2 + y**2))  # 根据距离，按照最大堆入队
            if len(pq) > n:
                heapq.heappop(pq)  # 每次 pop 的都是距离最远的
        max_dist = -heapq.heappop(pq)  # 找到最近的 n 个餐馆中最远的距离
        res = []
        for x, y in restaurants:
            # 遍历餐馆坐标, 按原顺序找到范围内的餐馆
            if x ** 2 + y ** 2 <= max_dist and n > 0:
                res.append([x, y])
                n -= 1
        return res

    def aerial_Movie(self, t, dur):
        """
        为了防止乘客在旅途中过于无聊，LQ航空公司决定在航班飞行过程中播放2部电影。
        由于飞机起降过程中不能播放电影，LQ航空公司必须保证两部电影加起来的时长小于等于飞行时长减去30分钟，
        同时又希望两部电影总长度尽量长。现在给定t代表航班飞行时长(分钟)，一个dur[]数组代表所有电影的时间长度，
        请从小到大分别输出两部电影的时长，如果有多组总时长一样的，选取包含单独最长的电影组. 
        题目保证有解
        """
        if len(dur) < 2:
            return []
        dur.sort()
        if dur[0] + dur[1] > t - 30:
            return []
        left, right = 0, len(dur) - 1
        max_dur = 0
        while left < right:
            movie_1, movie_2 = dur[left], dur[right]
            if movie_1 + movie_2 > t - 30:
                right -= 1
            else:
                if movie_1 + movie_2 > max_dur:
                    max_dur = movie_1 + movie_2
                    res = [movie_1, movie_2]
                left += 1
        return res

    def getAns(self, A, B, x):
        """
        给两个数组，给一个最大值，在这两个数组里各找一个组成一对，求其和最接近最大值，但不大于最大值的所有数对。
        """
        A.sort()
        B.sort()
        max_sum = -float("inf")
        res = []
        ai, bi = 0, len(B) - 1
        while ai < len(A) and bi >= 0:
            # scan A from left to right, scan B from right to left
            if A[ai] + B[bi] <= x:
                if A[ai] + B[bi] > max_sum:
                    res = [[A[ai], B[bi]]]  # refresh result
                    max_sum = A[ai] + B[bi]
                elif A[ai] + B[bi] == max_sum:
                    res.append([A[ai], B[bi]])  # add to current result set
                ai += 1
            else:
                bi -= 1
        return res

    def treeProblem(self, fa, val):
        """
        给定一棵n个结点的树，第i个结点的父亲为fa[i-1]，价值为val[i-1]。
        特别地，1表示根节点, 2 表示第二个节点，以此类推，并且保证根节点的父亲是 -1 即 fa[0] = -1。
        某子树的平均价值为，该子树所有的结点val和除以该子树的结点数。
        求该树的子树最大平均价值的为多少, 返回这颗子树的根节点编号。
        """
        self.fa, self.val = fa, val
        self.tree = self.build_tree()
        self.max_subtree_avg = float("-inf")
        self.max_subtree_root_idx = float("inf")
        self.postorder(-1)
        print(self.max_subtree_root_idx)
        return self.max_subtree_root_idx

    def build_tree(self):
        tree = collections.defaultdict(set)
        for node_idx in range(1, len(self.fa) + 1):
            # use index to represent nodes
            parent_idx = self.fa[node_idx - 1]
            tree[parent_idx].add(node_idx)
        return tree

    def postorder(self, node_idx):
        if node_idx not in self.tree:
            node_cnt = 1.
            val_cnt = self.val[node_idx - 1]
        else:
            node_cnt = 1.
            val_cnt = self.val[node_idx - 1]
            for child_idx in self.tree[node_idx]:
                subtree_node_cnt, subtree_val_cnt = self.postorder(child_idx)
                node_cnt += subtree_node_cnt
                val_cnt += subtree_val_cnt
        if val_cnt / node_cnt == self.max_subtree_avg:  # curr_avg_val == max_avg_val
            self.max_subtree_root_idx = min(self.max_subtree_root_idx, node_idx)  # set new res if curr_idx is smaller
        elif val_cnt / node_cnt > self.max_subtree_avg:  # curr_avg_val > max_avg_val
            self.max_subtree_avg = val_cnt / node_cnt   # set new res as curr_idx
            self.max_subtree_root_idx = node_idx
        return node_cnt, val_cnt

    def ladderLength(self, start, end, word_dict):
        """
        给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列
        """
        letter_bank = set()
        for l in range(ord('a'), ord('z') + 1):
            letter_bank.add(chr(l))
        word_dict = set(word_dict)
        word_len = len(start)
        # double bfs
        path_len = 1
        queue1, queue2 = set([start]), set([end])
        while queue1 and queue2:
            if len(queue1) > len(queue2):  # always execute on shorter queue (speed up)
                queue1, queue2 = queue2, queue1
            temp_queue = set()  # bfs queue for next level
            for word in queue1:
                word_to_list = list(word)
                for i in range(word_len):
                    letter_backup = word_to_list[i]
                    for letter_replace in letter_bank:
                        word_to_list[i] = letter_replace
                        word_next = "".join(word_to_list)
                        if word_next in queue2:  # q1 meets q2, return directly
                            return path_len + 1
                        if word_next in word_dict:
                            temp_queue.add(word_next)
                        else:
                            continue
                    word_to_list[i] = letter_backup
            queue1 = temp_queue
            path_len += 1
        return -1


print(Solution().KSubstring("asdasdsdjsfhjuashduhadufishfsduf", 5))