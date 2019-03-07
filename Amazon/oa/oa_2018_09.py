class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def dotProduct(self, A, B):
        """
        点积
        """
        if not A or not B:
            return -1
        if len(A) != len(B):
            return -1
        summation = 0
        for i in range(len(A)):
            summation += A[i] * B[i]
        return summation

    def reachEndpoint(self, targetMap):
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

    def closestTargetValue(self, target, array):
        """
        给出一个数组，在数组中找到两个数，使得它们的和最接近目标值但不超过目标值，返回它们的和
        """
        array.sort()
        left, right = 0, len(array) - 1
        max_sum = -float("inf")  # init max_sum
        while left < right:
            if array[left] + array[right] > target:  # exceed target
                right -= 1  # narrow down window from right side for smaller pair
            else:
                max_sum = max(array[left] + array[right], max_sum)  # refresh res
                left += 1  # narrow down window from left side for larger pair
        return -1 if max_sum == -float("inf") else max_sum

    def insert(self, head, insert_val):
        """
        给一个来自已经排过序的循环链表的节点，写一个函数来将一个值插入到循环链表中，并且保持还是有序循环链表。给出的节点可以是链表中的任意一个单节点。返回插入后的新链表。
        """
        if not head:
            head = ListNode(insert_val)
            head.next = head
            return head
        curr, next = head, head.next
        while head != next:
            # if head == next, all elements are the same, cannot find left right bound nodes
            # find the node after which to insert the new node
            if curr.val <= insert_val <= next.val:
                # trivial
                break
            if curr.val > next.val >= insert_val:
                # curr is the largest, next is the smallest
                # insert smaller or equal to next
                # insert is the first node
                break
            if insert_val >= curr.val > next.val:
                # curr is the larget, next is the smallest
                # insert greater or equal to curr
                # insert is the last node
                break
            curr, next = curr.next, next.next
        curr.next = ListNode(insert_val, next)
        return curr.next

    def searchMatrix(self, matrix, target):
        """
        Write an efficient algorithm that searches for a value in an m x n matrix.
        This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row
        """
        if not matrix or not matrix[0]:
            return False
        r = self.upper_bound([row[0] for row in matrix], target)
        c = self.upper_bound(matrix[r], target)
        return matrix[r][c] == target

    def upper_bound(self, arr, target):
        """
        return the first x index, st. x<=target
        """
        high, low = len(arr) - 1, -1
        while low < high:
            mid = high - (high - low) // 2
            if arr[mid] <= target:
                low = mid
            else:
                high = mid - 1
        return high

    def lower_bound(self, arr, target):
        """
        返回 arr 中第一个 x >= target 的值的位置
        """
        low, high = 0, len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

    def reverseWords(self, string):
        string = string.split(" ")
        print(string)

    def searchMatrix2(self, matrix, target):
        """
        写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。
        这个矩阵具有以下特性：
            每行中的整数从左到右是排序的。
            每一列的整数从上到下是排序的。
            在每一行或每一列中没有重复的整数。
        """
        def biserach(arr):
            # bi search target lower bound
            low, high = 0, len(arr)
            while low < high:
                mid = low + (high - low) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return 0 if low == len(arr) or arr[low] != target else 1

        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        cnt = 0
        for i in range(m):
            # search according to diagnal
            if matrix[i][i % n] > target:
                cnt += biserach(matrix[i][:i % n])
            else:
                cnt += biserach(matrix[i][i % n:])
        return cnt

    def doOverlap(self, l1, l2, r1, r2):
        """
        给定两个矩形，判断这两个矩形是否有重叠。
        """
        x1, y1 = l1.x, l1.y
        x2, y2 = r1.x, r1.y
        x3, y3 = l2.x, l2.y
        x4, y4 = r2.x, r2.y
        if x3 > x2:
            return False
        if x4 < x1:
            return False
        if y4 > y1:
            return False
        if y3 < y2:
            return False
        return True

    def winSum(self, nums, k):
        """
        给你一个大小为n的整型数组和一个大小为k的滑动窗口，将滑动窗口从头移到尾，输出从开始到结束每一个时刻滑动窗口内的数的和。
        """
        if k > len(nums) or not nums or not k:
            return []
        res = [sum(nums[: k])]
        left, right = 1, k + 1
        while right <= len(nums):
            res.append(res[-1] - nums[left - 1] + nums[right - 1])
            left += 1
            right += 1
        return res

    def secondMax(self, nums):
        """
        找到数组中第二大的数
        """
        import heapq
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        heapq.heappop(nums)
        return -heapq.heappop(nums)

    def climbStairs2(self, n):
        """
        一个小孩爬一个 n 层台阶的楼梯。他可以每次跳 1 步， 2 步 或者 3 步。实现一个方法来统计总共有多少种不同的方式爬到最顶层的台阶。
        """
        memo = {}

        def climb(x):
            if x == n:
                return 1
            if x > n:
                return 0
            if x in memo:
                return memo[x]
            memo[x] = sum([climb(x + dx) for dx in range(1, 4)])
            return memo[x]

        return climb(0)

    def compress(self, origin):
        """
        设计一种方法，通过给重复字符计数来进行基本的字符串压缩。
        例如，字符串 aabcccccaaa 可压缩为 a2b1c5a3 。而如果压缩后的字符数不小于原始的字符数，则返回原始的字符串。
        可以假设字符串仅包括 a-z 的字母。
        """
        origin += "#"
        compress = ""
        i = 0
        while i < len(origin) - 1:
            char = origin[i]
            cnt = 1
            while origin[i] == origin[i + 1]:
                cnt += 1
                i += 1
            compress += char
            compress += str(cnt)
            i += 1
        origin = origin[:-1]
        return compress if len(compress) < len(origin) else origin

    def anagram(self, s, t):
        """
        写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串
        """
        import collections
        counter = collections.Counter(s)
        for char in t:
            if counter[char] == 0:
                return False
            counter[char] -= 1
        return True

    def firstUniqChar(self, string):
        """
        给出一个字符串，找出第一个只出现一次的字符。
        """
        import collections
        counter = collections.Counter(string)
        for i, char in enumerate(string):
            if counter[char] == 1:
                return char
        return '0'

    def minimumSum(self, root):
        """
        给一棵二叉树，找到从根节点到叶子节点的最小路径和
        """
        if not root.left and not root.right:
            return root.val
        elif root.left and not root.right:
            return self.minimumSum(root.left) + root.val
        elif not root.left and root.right:
            return self.minimumSum(root.right) + root.val
        else:
            return min(self.minimumSum(root.left), self.minimumSum(root.right)) + root.val

    def twoSum6(self, nums, target):
        if len(target) < 2:
            return 0
        nums.sort()
        left, right = 0, len(nums)
        cnt = 0
        while left < right:
            if nums[left] + nums[right] == target:
                cnt += 1
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
            else:
                right -= 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1
        return cnt

    def reverseWords(self, s):
        """
        给定一个字符串，逐个翻转字符串中的每个单词。
        """
        words = s.split(' ')
        res = ""
        for word in words:
            if word:
                res += word[::-1] + " "
        return res[:-1][::-1]