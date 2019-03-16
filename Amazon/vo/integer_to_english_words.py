class Solution(object):
    def int_to_eng(self, num):
        if num > 2 ** 32 - 1:
            return None
        if num == 0:
            return "Zero"
        res = []
        big_title = {0: "", 1: "Thousand", 2: "Million", 3: "Billion"}
        big_key = 0
        while num:
            num, part = divmod(num, 1000)
            part_eng = self.part_to_eng(part)
            print(part_eng)
            if part_eng:
                res = part_eng + [big_title[big_key]] + res
            big_key += 1
        if res[-1] == "":
            res.pop()
        print(res)
        return " ".join(res)

    def part_to_eng(self, part):
        res = []
        small_key, part = divmod(part, 100)
        small_title = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                       10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                       17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
                       60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
        if small_key > 0:
            res.append(small_title[small_key])
            res.append("Hundred")
        if part == 0:
            return res
        if part in small_title:
            res.append(small_title[part])
            return res
        small_key, part = divmod(part, 10)
        res.append(small_title[small_key * 10])
        res.append(small_title[part])
        return res


if __name__ == "__main__":
    soln = Solution()
    soln.int_to_eng(100000)
