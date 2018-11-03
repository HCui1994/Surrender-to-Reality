import numpy as np
import time
class BKPK:
    @staticmethod
    def optimization_on_01_and_complete(stuff_volume, stuff_value, backpack_volume):
        pass


    @staticmethod
    def backpack_01(stuff_volume, stuff_value, backpack_volume):
        """ 
        N个物品，背包容量V，放入第i件物品消耗G[i]，得到价值W[i]，每个物品只能放入一件，放入哪些物品使得总价值最大？
        Args: 
            stuff_vol: [vol0, vol1, ...] of Integer
            stuff_value: [val1, val2, ...] of Integer
            backpack_vol: total volume of backpack of Integer
        """
        stuff_num = len(stuff_value)
        memo = np.zeros((stuff_num+1, backpack_volume))
        memo[0, :] = 0 # 初始化，背包中不放任何物品，价值肯定为0
        for stuff_idx in range(len(stuff_value)):
            memo_stuff_idx = stuff_idx + 1
            for vol in range(stuff_volume[stuff_idx], backpack_volume, +1):
                collect = stuff_value[stuff_idx] + memo[memo_stuff_idx - 1, vol - stuff_volume[stuff_idx]]
                uncollect = memo[memo_stuff_idx - 1, vol]
                memo[memo_stuff_idx, vol] = max([collect, uncollect])
        print(memo)
        print(memo[memo.shape[0]-1, memo.shape[1]-1])

    @staticmethod
    def backpack_01_memory_optimze(stuff_volume, stuff_value, backpack_volume):
        """
        collect = stuff_value[stuff_idx] + memo[memo_stuff_idx - 1, vol - stuff_vol[stuff_idx]]
        uncollect = memo[memo_stuff_idx - 1, vol]
        计算memo[memo_stuff_idx, :]一行，只需要memo[memo_stuff_idx-1, :]一行
        不需要保存所有子问题解
        """
        memo = np.zeros((backpack_volume, ))
        for stuff_idx in range(len(stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume, ))
            for vol in range(stuff_volume[stuff_idx], backpack_volume, +1):
                collect = stuff_value[stuff_idx] + memo[vol - stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                print(collect, uncollect, stuff_idx)
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
            print(memo)
            time.sleep(5)
        print(memo)
        print(memo[-1])
        
    @staticmethod
    def backpack_complete(stuff_volume, stuff_value, backpack_volume):
        """ 
        N个物品，背包容量V，放入第i件物品消耗G[i]，得到价值W[i]，每个物品可以无限次放入，放入哪些物品使得总价值最大？
        如何将完全背包问题褪化为01背包？
        第i物品最多可以放入 backpack_volume // stuff_volume[i] 次，将第i物品转化为 backpack_volume // stuff_volume[i] 件相同的物品
        之后运行backpack_01
        Args: 
            stuff_vol: [vol0, vol1, ...] of Integer
            stuff_value: [val1, val2, ...] of Integer
            backpack_vol: total volume of backpack of Integer
        """
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_volume)):
            num_of_duplicate = backpack_volume // stuff_volume[i]
            for _ in range(num_of_duplicate):
                duplicate_stuff_volume.append(stuff_volume[i])
                duplicate_stuff_value.append(stuff_value[i])
        memo = np.zeros((backpack_volume))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])




"""
test_cases
"""
stuff_volume =   [1, 4, 3, 3]
stuff_value = [3, 5, 10,9]
backpack_volume = 6
BKPK.backpack_01_memory_optimze(stuff_volume, stuff_value, backpack_volume)
