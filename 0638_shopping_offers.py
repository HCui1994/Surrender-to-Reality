"""
In LeetCode Store, there are some kinds of items to sell. Each item has a price.

However, there are some special offers, and a special offer consists of one or more different kinds of items with a sale price. 

You are given the each item's price, a set of special offers, and the number we need to buy for each item. 
The job is to output the lowest price you have to pay for exactly certain items as given, where you could make optimal use of the special offers.

Each special offer is represented in the form of an array, the last number represents the price you need to pay for this special offer, 
    other numbers represents how many specific items you could get if you buy this offer.

You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
"""
import numpy as np


class Solution:
    def shopping_offers_backpack(self, price, specials, needs):
        """
        dynamic programming, backpack
        先筛选出合法的特价组合：如果组合中某中物品的数量大于需求，则该特价无法使用
        如何转化为背包问题？
        需要买多少个物品，就有多少个背包，每个背包的容量就是对该物品的需求，并且需要装满所有背包
        同时还需要维护价格memo？
        """
        pass
        # total_item_combine = []
        # # 转化特价组合的可用购买数量
        # for special in specials:
        #     max_available_use_time = float("inf") # 该特价组合最多可用多少次？
        #     for i in range(len(needs)):
        #         if special[i] == 0:
        #             continue
        #         elif needs[i] >= special[i]: # 如果需求大于组合中该物品的数量，则可用
        #             max_available_use_time = min(max_available_use_time, needs[i] // special[i])
        #         else:   # 否则不可用，因为会超出需求数量
        #             max_available_use_time = 0
        #             break
        #     for i in range(max_available_use_time):
        #         total_item_combine.append(special)
        # # 转化单件的可用购买数量
        # for item_idx in range(len(needs)):
        #     single_item_need = needs[item_idx]
        #     combine_item = [0 for _ in specials[0]]
        #     combine_item[item_idx] = 1
        #     combine_item[-1] = price[item_idx]
        #     for _ in range(single_item_need):
        #         total_item_combine.append(combine_item)
        # # 每个物品组合都有用和不用两种选择，问题在于如何同时维护多个背包？由于needs长度是动态的，将其扩展为6维度
        # # 多维背包问题：有多少个背包，就使用多少维度的 memo
        # dims = [need + 1 for need in needs]
        # dims += [0 for _ in range(6 - len(needs))]
        # # memory optimized multi-dimension backpack
        # memo = [[[[[[
        #                         [None for _ in range(dims[5])]
        #                     ] for _ in range(dims[4])
        #                 ] for _ in range(dims[3])
        #             ] for _ in range(dims[2])
        #         ]for _ in range(dims[1])
        #     ] for _ in range(dims[0])
        # ]
        # # 如何初始化？？？？？使用物品的单价进行初始化
        # for vol1 in range(dims[0]):
        #     for vol2 in range(dims[1]):
        #         for vol3 in range(dims[2]):
        #             for vol4 in range(dims[3]):
        #                 for vol5 in range(dims[4]):
        #                     for vol6 in range(dims[5]):
        #                         # memo[vol1][vol2][vol3][vol4][vol5][vol6] = vol1 *
        #                         pass
        # for stuff_idx in range(len(total_item_combine)):
        #     memo_idx = stuff_idx + 1
        #     for vol1 in range(len(needs[0] + 1)):
        #         for vol2 in range(len(needs[1] + 1)):
        #             for vol3 in range(len(needs[2] + 1)):
        #                 for vol4 in range(len(needs[3] + 1)):
        #                     for vol5 in range(len(needs[4] + 1)):
        #                         for vol6 in range(len(needs[5] + 1)):
        #                             # 如果放入物品 i
        #                             #
        #                             pass

    def shopping_offers_dp(self, prices, specials, needs):
        """ WA ??!! """
        import numpy as np
        # 物品数量是动态的，而最多有6件物品
        num_items = len(prices)
        # 将物品价格和对应需求补齐
        prices += [0 for _ in range(6 - num_items)]
        needs += [0 for _ in range(6 - num_items)]
        # 将 special offer 做对应的补齐，注意筛选合法的 special offer
        temp_specials = []
        for special in specials:
            valid_flag = True
            for i in range(len(special) - 1):
                if special[i] > needs[i]:
                    valid_flag = False
                    break
            if valid_flag:
                temp_specials.append(special[:-1] + [0 for _ in range(6 - num_items)] + [special[-1]])
        specials = temp_specials
        # dynamic programming，创建备忘
        memo = np.zeros(np.array(needs) + 1)
        # memo[n0, n1, n2, n3, n4, n5] 表示 6种物品的需求分别为 n0 ... n5 时的最小花费
        # 按照单价购买进行初始化，由于使用 special offer 不一定划算
        for n0 in range(needs[0] + 1):
            for n1 in range(needs[1] + 1):
                for n2 in range(needs[2] + 1):
                    for n3 in range(needs[3] + 1):
                        for n4 in range(needs[4] + 1):
                            for n5 in range(needs[5] + 1):
                                memo[n0, n1, n2, n3, n4, n5] = n0 * prices[0] + n1 * prices[1] + n2 * prices[2] + n3 * prices[3] + n4 * prices[4] + n5 * prices[5]
        # 开始自底向上动态规划
        for special in specials:
            for n0 in range(needs[0] + 1):
                for n1 in range(needs[1] + 1):
                    for n2 in range(needs[2] + 1):
                        for n3 in range(needs[3] + 1):
                            for n4 in range(needs[4] + 1):
                                for n5 in range(needs[5] + 1):
                                    use_special = memo[n0 - special[0], n1 - special[1], n2 - special[2], n3 - special[3], n4 - special[4], n5 - special[5]] + special[-1]
                                    not_use_special = memo[n0, n1, n2, n3, n4, n5]
                                    memo[n0, n1, n2, n3, n4, n5] = min(use_special, not_use_special)
        return int(memo[-1, -1, -1, -1, -1, -1])
    
    def get_key(self, needs):
        # 将需求序列转换为 int 型
        num_items = len(needs)
        key = 0
        for i in range(num_items - 1, -1, -1):
            key += needs[i] * 10 ** (num_items - i - 1)
        return key

    def shopping_offers_recursion_with_memoization(self, prices, specials, needs):
        num_items = len(needs)
        num_specials = len(specials)
        pay = 0
        memo = {}
        key = self.get_key(needs)
        if key in memo.keys():
            return memo[key]
        # 初始化，全部单件购买
        for i in range(num_items):
            pay += prices[i] * needs[i]
        for special in specials:
            temp_needs = [_ for _ in needs]
            valid_flag = True
            for i in range(num_items):
                temp_needs[i] = needs[i] - special[i]
                if temp_needs[i] < 0:
                    valid_flag = False
                    break
            if valid_flag:
                pay = min(pay, special[-1] + self.shopping_offers_recursion_with_memoization(prices, specials, temp_needs))
        memo[key] = pay
        return pay

    def test(self):
        # price = [2, 3, 4]
        # special = [[1, 1, 0, 4], [2, 2, 1, 9]]
        # needs = [0, 0, 0]
        prices = [4,3,2,9,8,8]
        specials = [[1,5,5,1,4,0,18],[3,3,6,6,4,2,32]]
        needs = [6,5,5,6,4,1]
        # self.get_key(needs)
        ans = self.shopping_offers_recursion_with_memoization(prices, specials, needs)
        print(ans)


soln = Solution()
soln.test()