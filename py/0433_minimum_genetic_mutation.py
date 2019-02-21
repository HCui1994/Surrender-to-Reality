"""
A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.

Note:
1.  Starting point is assumed to be valid, so it might not be included in the bank.
2.  If multiple mutations are needed, all mutations during in the sequence must be valid.
3.  You may assume start and end string is not the same.
 
Example 1:
start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]
return: 1
 
Example 2:
start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
return: 2
"""

class Solution:
    def min_mutation_brutal(self, start, end, bank):
        """
        same as 0127 word ladder
        """
        bank = set(bank)
        gene_visited = {start : 0}
        queue = [start]
        while queue:
            current_gene = queue.pop(0)
            for idx in range(8):
                next_gene_list = list(current_gene)
                for base in ['A', 'T', 'C', 'G']:
                    next_gene_list[idx] = base
                    next_gene = "".join(next_gene_list)
                    if next_gene not in bank:
                        # 如果下一基因不在基因库中，直接跳过
                        continue
                    if next_gene == end:
                        # 找到目标基因，返回突变次数
                        return gene_visited[current_gene] + 1
                    if next_gene not in gene_visited.keys():
                        # 如果下一基因没有被访问过，记录其与初始基因的突变距离，加入 bfs 队列等待
                        gene_visited[next_gene] = gene_visited[current_gene] + 1
                        queue.append(next_gene)
        # 如果便利所有情况没有发现目标基因，则无法通过基因库达成目标基因突变
        return 0
                    
    def test(self):
        start = "AACCGGTT"
        end = "AAACGGTA"
        bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
        print(self.min_mutation_brutal(start, end, bank))


Solution().test()