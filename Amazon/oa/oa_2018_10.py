#coding: utf-8
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = self.random = None


class Solution:
    def modernLudo(self, length, connections):
        """
        有一个一维的棋盘，起点在棋盘的最左侧，终点在棋盘的最右侧，棋盘上有几个位置是跟其他的位置相连的，
        即如果A与B相连，则当棋子落在位置A时, 你可以选择是否不投骰子，直接移动棋子从A到B。
        并且这个连接是单向的，即不能从B移动到A，现在给定这个棋盘的长度length和位置的相连情况connections，
        你有一个六面的骰子(点数1-6)，最少需要丢几次才能到达终点。
        """
        # build connectiosn
        import collections
        connect_dict = collections.defaultdict(set)
        for fr, to in connections:
            connect_dict[to].add(fr)
        dp = [float("inf") for _ in range(length + 1)]
        dp[1] = 0
        for i in range(2, length + 1):
            # 掷骰子
            for dice in range(1, 7):
                dp[i] = min(dp[i], dp[i - dice])
            dp[i] += 1
            # 直接飞
            for fr in connect_dict[i]:
                dp[i] = min(dp[i], dp[fr])
        return dp[-1]

    def isInterval(self, intervalList, target):
        """
        给定一个包含若干个区间的List数组, 区间的长度是 1000, 例如 [500,1500], [2100,3100].
        给定一个 number, 请问number是否在这些区间内.返回 True 或 False.
        """
        for left, right in intervalList:
            if left <= target <= right:
                return True
        return False

    def logSort(self, logs):
        """
        给出一个由List < String > 组成的日志，每个元素代表一行日志。
        每行日志信息以第一个空格分隔成两个字符串，分割后的前面部分的字符串为日志的ID，
        后面部分的字符串为日志内容(日志的内容也可能包括空格字符)。
        组成日志内容的字符串有以下两种类别：
        1.全部由字母和空格组成。
        2.全部由数字和空格组成。
        现在对日志进行了排序，要求类别1日志按照内容的字典编排的顺序排序并放在顶部，类别2的日志应放在底部并按输入顺序输出
        注意，除第一个以外的空格字符也属于内容，并且当类别1的词典顺序相等时，根据日志ID的字典顺序排序，并且ID一定不重
        """
        def cmp(a, b):
            idxA = a.find(" ")  # find the first blank
            titleA = a[:idxA]  # split title and content
            conA = a[idxA + 1:]
            idxB = b.find(" ")
            titleB = b[:idxB]
            conB = b[idxB + 1:]
            if conA != conB:
                # compare according to content lex-order
                return -1 if conA < conB else 1
            return -1 if titleA < titleB else 1
        sorted_log = sorted(logs, cmp=cmp)
        res = []
        for log in sorted_log:
            # put all type 1 log at head with defined sequence
            idx = log.find(" ")
            if log[idx + 1].isalpha():
                res.append(log)
        for log in logs:
            # put type 2 log at tail with original sequence
            idx = log.find(" ")
            if not log[idx + 1].isalpha():
                res.append(log)
        return res

    def reachEndpoint(self, map):
        """
        可否到达终点？
        给一个大小为 m*n 的map，1 代表空地，0 代表障碍物，9代表终点。从 (0, 0) 开始能否到达终点？
        """
        if not map or not map[0]:
            return False
        visited = set()

        def dfs(i, j):
            if (i, j) in visited or map[i][j] == 0:
                return False
            if map[i][j] == 9:
                return True
            visited.add((i, j))
            di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
            for direct in range(4):
                ii, jj = i + di[direct], j + dj[direct]
                if ii >= 0 and jj >= 0 and ii < len(map) and jj < len(map[0]):
                    if dfs(ii, jj):
                        return True
            visited.remove((i, j))
            return False

        return dfs(0, 0)

    def shortestPath(self, targetMap):
        """
        给定表示地图上坐标的2D数组，地图上只有值0,1,2.
        0表示可以通过，1表示不可通过，2表示目标位置。
        从坐标[0,0]开始，你只能上，下，左，右移动。
        找到可以到达目的地的最短路径，并返回路径的长度。
        """
        memo = {}

        def walker(i, j):
            if (i, j) in memo:
                return memo[i, j]
            if targetMap[i][j] == 1:  # obstacle, unreachable
                return float("inf")
            if targetMap[i][j] == 2:  # reach target
                return 0
            di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]  # define directions
            memo[i, j] = float("inf")  # dp memo init
            for idx in range(4):
                ii, jj = i + di[idx], j + dj[idx]
                if ii >= 0 and jj >= 0 and ii < len(targetMap) and jj < len(targetMap[0]):
                    memo[i, j] = min(memo[i, j], walker(ii, jj))
            memo[i, j] += 1
            return memo[i, j]

        walker(0, 0)
        return memo[0, 0] if memo[0, 0] != float("inf") else -1

    def nearestRestaurant(self, restaurants, n):
        """
        给出一个List，里面的数据代表每一个餐厅的坐标[x, y]。
        顾客的坐标处于原点[0, 0]。
        先找出n家离顾客位置最近的餐厅，然后取 n 家先出现在List中且与顾客的距离不超过 n 家离顾客最近的餐厅的最长距离。
        返回这 n 家餐厅的坐标序列，按输入数据原始的顺序。
        """
        import heapq
        if len(restaurants) < n or not restaurants:
            return []
        pq = []
        for x, y in restaurants:
            # first loop: find max(min(distance)
            heapq.heappush(pq, - (x**2 + y**2))
            if len(pq) > n:  # keep heap size at n
                heapq.heappop(pq)  # pop restaurant too far
        max_dist = -heapq.heappop(pq)
        res = []
        for x, y in restaurants:
            # second loop: get n restaurants with original seq
            if x**2 + y ** 2 <= max_dist and n > 0:
                res.append([x, y])
                n -= 1
        return res

    def bstDistance(self, numbers, node1, node2):
        """"""
        dummy_head = TreeNode(float("inf"))
        paths = []  # store paths from root to node1 and node2, if exist
        for num in numbers:
            path = []
            node = dummy_head
            while node:
                parent = node
                if num < node.val:
                    node = node.left
                    path.append(0)  # 0: left child
                else:
                    node = node.right
                    path.append(1)  # 1: right child
            if path[-1] == 0:  # insert new leaf according to parent
                parent.left = TreeNode(num)
            else:
                parent.right = TreeNode(num)
            if num == node1 or num == node2:
                # find one of two target nodes, save path
                paths.append(path)
            if len(paths) == 2:
                # find both two nodes
                path1, path2 = paths[0][::-1], paths[1][::-1]
                while path1 and path2:
                    if path1[-1] == path2[-1]:
                        # pop the shared path
                        path1.pop()
                        path2.pop()
                    else:
                        break
                # both two nodes found, return result directly
                return len(path1) + len(path2)
        return -1  # node1 or node2 or both are not in numbers

    def frequentWord(self, string, excludewords):
        """
        给出一个字符串s，表示小说的内容，再给出一个list表示这些单词不参加统计
        求字符串中出现频率最高的单词(如果有多个，返回字典序最小的那个)
        """
        import collections
        excludewords = set(excludewords)
        words_dict = collections.Counter()
        i = 0
        while i < len(string):
            # collect all words while counting frequency
            word = ""
            while i < len(string) and string[i] in "qwertyuiopasdfghjklzxcvbnm":
                word += string[i]
                i += 1
            if word and word not in excludewords:
                # don't collect if exclusive
                words_dict[word] += 1
            i += 1
        max_freq = -float("inf")  # init max frequency
        for word, freq in words_dict.items():
            if freq > max_freq:
                res = word
                max_freq = freq
            elif freq == max_freq:
                res = min(res, word)
        return res

    def uniqueSubstring(self, s, k):
        """
        给出一个字符串 s，找出所有的不同的长度为 k 的它的子串，并将结果按照字典序排序
        """
        res = set()
        left = 0
        right = left + k
        while right <= len(s):
            res.add(s[left:right])
            left += 1
            right += 1
        return sorted(list(res))

    def findSubstring(self, string, k):
        """
        给定长度k，找出字符串str里面所有长为k的子串。
        子串的字符不能重复，输出满足这样条件的子串数量 (子串相同的只算1个)。
        """
        import collections
        if len(string) < k:
            return 0  # corner case
        res = set()
        left, right = 0, k
        counter = collections.Counter(string[left: right])  # sliding window init
        if len(counter) == k:  # check the first sliding window
            res.add(string[left: right])
        for left in range(1, len(string) - k + 1):
            right = left + k
            letter_left, letter_right = string[left - 1], string[right - 1]
            counter[letter_left] -= 1
            if counter[letter_left] == 0:
                del counter[letter_left]  # delete if no same letter in window
            counter[letter_right] += 1
            if len(counter) == k:
                res.add(string[left: right])
        return len(res)

    def twoSum5(self, nums, target):
        """
        给定一个整数数组，找出这个数组中 有多少对 的和是小于或等于目标值。返回对数。
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        cnt = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                cnt += right - left  # num of pairs (X, right)
                left += 1
            else:
                right -= 1  # narrow down window
        return cnt

    def copyRandomList(self, head):
        """
        给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点, 
        返回一个深拷贝的链表, 使用O(1)的空间
        """
        if not head:
            return None
        old_node = head
        while old_node:
            old_next = old_node.next
            new_node = RandomListNode(old_node.label)
            old_node.next = new_node
            new_node.next = old_next
            old_node = old_node.next.next
        old_node = head
        while old_node:
            if old_node.random:
                old_node.next.random = old_node.random.next
            old_node = old_node.next.next
        old_node = head
        new_head = head.next
        while old_node:
            new_node = old_node.next
            old_node.next = old_node.next.next
            new_node.next = new_node.next.next if new_node.next else None
            old_node = old_node.next
        return new_head

    def copyRandomListDic(self, head):
        """
        给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点, 
        返回一个深拷贝的链表, 使用O(n)的空间
        """
        if not head:
            return None
        mapping = {}
        node = head
        while node:
            mapping[node] = RandomListNode(node.label)
            node = node.next
        node = head
        while node:
            if node.random:
                mapping[node].random = mapping[node.random]
            mapping[node].next = mapping[node.next] if node.next else None
            node = node.next
        return mapping[head]

    def maxSlidingWindow(self, nums, k):
        """
        给出一个可能包含重复的整数数组，和一个大小为 k 的滑动窗口, 
        从左到右在数组中滑动这个窗口，找到数组中每个窗口内的最大值。
        """
        import collections
        if not nums or not k:
            return []
        res = []
        dq = collections.deque([])
        for i in range(len(nums)):
            if dq and dq[0] == i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            print(dq)
            if i >= k - 1:
                res = nums[dq[0]]
        return res

    def minimumDifference(self, array):
        """
        给出一个 n * m 的二维数组，数组每一行的元素都是排序的，每一行选择 1 个数，
        总共选择 n 个数，这 n 个数的 diff 为 maximum-minimum，求最小的diff
        """
        import heapq
        if not array or not array[0]:
            return 0
        # init
        max_val = -float("inf")
        min_diff = float("inf")
        minheap = []
        m, n = len(array), len(array[0])
        for i in range(m):
            heapq.heappush(minheap, (array[i][0], i, 0))
            max_val = max(max_val, array[i][0])
        while True:
            min_val, row, col = heapq.heappop(minheap)
            min_diff = min(min_diff, max_val - min_val)
            if col == n - 1:  # 某一行已经没有元素
                return min_diff
            replace_val = array[row][col + 1]
            max_val = max(max_val, replace_val)
            heapq.heappush((replace_val, row, col + 1))


soln = Solution()
soln.modernLudo(length=10, connections=[[2, 10]])
soln.maxSlidingWindow([1, 2, 7, 7, 2], 1)
