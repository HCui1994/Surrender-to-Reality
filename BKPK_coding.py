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
        memo = np.zeros((stuff_num + 1, backpack_volume + 1))
        memo[0, :] = 0 # 初始化，背包中不放任何物品，价值肯定为0
        for stuff_idx in range(len(stuff_value)):
            memo_stuff_idx = stuff_idx + 1
            for vol in range(stuff_volume[stuff_idx], backpack_volume+1, +1):
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
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = stuff_value[stuff_idx] + memo[vol - stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])
        
    @staticmethod
    def backpack_complete(stuff_volume, stuff_value, backpack_volume):
        """ 
        N个物品，背包容量V，放入第i件物品消耗G[i]，得到价值W[i]，每个物品可以无限次放入，放入哪些物品使得总价值最大？
        如何将完全背包问题褪化为01背包？
        第i物品最多可以放入 backpack_volume // stuff_volume[i] 次，
        将第i物品复制出为 backpack_volume // stuff_volume[i] 件相同的物品
        之后运行backpack_01
        """
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_volume)):
            num_of_duplicate = backpack_volume // stuff_volume[i]
            for _ in range(num_of_duplicate):
                duplicate_stuff_volume.append(stuff_volume[i])
                duplicate_stuff_value.append(stuff_value[i])
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])


    @staticmethod
    def backpack_complete_optimized(stuff_volume, stuff_value, backpack_volume):
        """
        更高效的转化方法:
        把第 i 种物品复制成为费用为 stuff_volume[i] * 2 ** k, 价值为 stuff_value[i] * 2 ** k 的若干件物品, 
        其中 k 取遍满足stuff_volume[i] * 2 ** k <= backpack_volume 的非负整数。任何数量的同种物品可以作为上述复制品的线性组合
        如此不再需要 backpack_volume // stuff_volume[i] 的复制品
        而仅需要 log(backpack_volume) // log(stuff_volume[i]) 的复制品
        """
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_value)):
            k = 0
            while stuff_volume[i] * 2 ** k <= backpack_volume:
                duplicate_stuff_value.append(stuff_value[i] * 2 ** k)
                duplicate_stuff_volume.append(stuff_volume[i] * 2 ** k)
                k += 1
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol]
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])


    @staticmethod
    def backpack_multiple(stuff_volume, stuff_value, stuff_multiple, backpack_volume):
        """
        有 N 种物品和一个容量为 backpack_volume 的背包
        第 i 种物品最多有 stuff_multiple[i] 件可用, 
        每件耗费的空间 stuff_volume[i]
        价值 stuff_value[i]
        求解将哪些物品装入背包可使这些物品的耗费的空间总和不超过背包容量,且价值总和最大。
        Args:
            stuff_multiple: [num_of_stuff1, num_of_stuff2, ...]
        """
        # 可以像完全背包一样，将所有复制物品放入 duplicate_stuff_value, duplicate_stuff_volume
        duplicate_stuff_volume = []
        duplicate_stuff_value = []
        for i in range(len(stuff_multiple)):
            for _ in range(stuff_multiple[i]):
                duplicate_stuff_value.append(stuff_value[i])
                duplicate_stuff_volume.append(stuff_volume[i])
        memo = np.zeros((backpack_volume + 1, ))
        for stuff_idx in range(len(duplicate_stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume + 1, ))
            for vol in range(duplicate_stuff_volume[stuff_idx], backpack_volume + 1, +1):
                collect = duplicate_stuff_value[stuff_idx] + memo[vol - duplicate_stuff_volume[stuff_idx]]
                uncollect = memo[vol] 
                current_stuff_memo[vol] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1])


    @staticmethod
    def backpack_mixed(stuff_type, stuff_volume, stuff_value, stuff_multiple, backpack_volume):
        """
        有 N 种物品和一个容量为 backpack_volume 的背包
        第 i 种物品可能只有一个，可能有无限多，也可能最多有 stuff_multiple[i] 件可用, 
        每件耗费的空间 stuff_volume[i]
        价值 stuff_value[i]
        求解将哪些物品装入背包可使这些物品的耗费的空间总和不超过背包容量,且价值总和最大。
        Args:
            stuff_type ["01", "multiple", "complete", ...]
        """
        # 按照每种物品的类别创建 duplicate_stuff_volume 和 duplicate_stuff_value
        pass

    @staticmethod
    def backpack_2d(stuff_volume_1, stuff_volume_2, stuff_value, backpack_volume_1, backpack_volume_2):
        """
        对于每件物品,具有两种不同的费用,选择这件物品必须同时付出这两种费用。
        对于每种费用都有一个可付出的最大值(背包容量)。怎样选择物品可以得到最大的价值。
        设第 i 件物品价值 stuff_value[i], 所需的两种费用分别为 stuff_volume_1[i] 和 stuff_volume_2[i]
        两种费用可付出的最大值(即两种背包容量)分别为 backpack_volume_1 和 backpack_volume_2 。
        """
        # 为memo增加一个维度
        num_of_stuff = len(stuff_value)
        memo = np.zeros((num_of_stuff + 1, backpack_volume_1 + 1, backpack_volume_2 + 1))
        for stuff_idx in range(num_of_stuff):
            memo_stuff_idx = stuff_idx + 1
            for vol1 in range(stuff_volume_1[stuff_idx], backpack_volume_1 + 1, +1):
                for vol2 in range(stuff_volume_2[stuff_idx], backpack_volume_2 + 1, +1):
                    collect = stuff_value[stuff_idx] + memo[memo_stuff_idx - 1, vol1 - stuff_volume_1[stuff_idx], vol2 - stuff_volume_2[stuff_idx]]
                    uncollect = memo[memo_stuff_idx - 1, vol1, vol2]
                    memo[memo_stuff_idx, vol1, vol2] = max(collect, uncollect)
        print(memo)
        print(memo[-1, -1, -1])

    @staticmethod
    def backpack_2d_space_optimize(stuff_volume_1, stuff_volume_2, stuff_value, backpack_volume_1, backpack_volume_2):
        memo = np.zeros((backpack_volume_1 + 1, backpack_volume_2 + 1))
        for stuff_idx in range(len(stuff_value)):
            current_stuff_memo = np.zeros((backpack_volume_1 + 1, backpack_volume_2 + 1))
            for vol1 in range(stuff_volume_1[stuff_idx], backpack_volume_1 + 1, +1):
                for vol2 in range(stuff_volume_2[stuff_idx], backpack_volume_2 + 1, +1):
                    collect = stuff_value[stuff_idx] + memo[vol1 - stuff_volume_1[stuff_idx], vol2 - stuff_volume_2[stuff_idx]]
                    uncollect = memo[vol1, vol2]
                    current_stuff_memo[vol1, vol2] = max(collect, uncollect)
            memo = current_stuff_memo
        print(memo)
        print(memo[-1, -1])


    @staticmethod
    def backpack_group():
        pass
    
    def backpack_dependency():
        pass
"""
test_cases
"""
stuff_volume_1 = [1, 4, 3, 2]
stuff_volume_2 = [2, 3, 4, 1]
stuff_value = [3, 5, 10,9]
stuff_multiple = [2, 3, 2, 2]
backpack_volume_1 = 6
backpack_volume_2 = 5
BKPK.backpack_2d(stuff_volume_1, stuff_volume_2, stuff_value, backpack_volume_1, backpack_volume_2)
