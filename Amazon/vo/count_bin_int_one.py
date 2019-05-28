class Solution(object):
    def count_one(self, num):
        # convert decimal into binary
        # during the procedure, count how many 1
        cnt = 0
        while num:
            num, remainder = divmod(num, 2)
            cnt += remainder
        return cnt


if __name__ == "__main__":
    soln = Solution()
    print(soln.count_one(15))  # 101