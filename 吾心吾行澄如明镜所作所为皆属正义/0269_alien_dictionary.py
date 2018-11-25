class Solution:
    """ BFS Solution, AC """
    def alienOrder(self, words):
        graph = {}
        indegree = {}
        self._initialize(words, graph, indegree)
        self._build_graph(words, graph, indegree)
        print(graph)
        print(indegree)
        return self._topological_sort(graph, indegree)


    def _initialize(self, words, graph, indegree):
        """
        Args: 
            words: [string1, string2, ...]
            graph: {precursor1: set(successor11, successor12, ...), ...}
            indegree: {successor1: indegree2, ...}
        """
        for word in words:
            for letter in word:
                if not letter in graph.keys():
                    graph[letter] = set([])
                if not letter in indegree.keys():
                    indegree[letter] = 0

    def _build_graph(self, words, graph, indegree):
        edges = set([])
        for word_idx in range(len(words) - 1):
            word_smaller = words[word_idx]
            word_greater = words[word_idx + 1]
            for letter_idx in range(min(len(word_greater), len(word_smaller))):
                if word_smaller[letter_idx] == word_greater[letter_idx]:
                    continue
                if not (word_smaller[letter_idx], word_greater[letter_idx]) in edges:
                    edges.add((word_smaller[letter_idx], word_greater[letter_idx]))
                    graph[word_smaller[letter_idx]].add(word_greater[letter_idx])
                    indegree[word_greater[letter_idx]] += 1
                    break
                else:
                    break

    def _topological_sort(self, graph, indegree):
        order = ""
        queue = []
        for key in indegree.keys():
            if indegree[key] == 0:
                queue.append(key)
        while queue:
            prec = queue.pop(0)
            order += prec
            succ_set = graph[prec]
            if succ_set: # 如果有后继节点
                for succ in succ_set:
                    indegree[succ] -= 1
                    if indegree[succ] == 0: # 如果有环，在进入搜索时，进入环的节点，入读不可能减到 0
                                            # 将会导致没有完成搜索，队列就已经为空
                        queue.append(succ)
        if len(order) == len(graph):        # 所以 order 中字符的数量将少于dict字符数量
            return order                    
        else:
            return ""


# words = ["wrt","wrf","er","ett","rftt","te"]
# solution = Solution()
# print(solution.alienOrder(words))




""" graph data structrure """
class AlienCharacter:
    def __init__(self, char):
        self.char = char
        self.indegree = 0
        self.succ = set([])

class AlienOrder2:
    def alien_order(self , words):
        init_graph = self._initialize(words)
        graph = self._build_graph(words, init_graph)
        for key in graph.keys():
            node = graph[key]
            print(node.char, node.indegree, node.succ)
        order = self._topology_bfs(graph)
        print(order)
        
    def _initialize(self, words):
        init_graph = {}
        for word in words:
            for letter in word:
                if not letter in init_graph.keys():
                    init_graph[letter] = AlienCharacter(letter)
        return init_graph
    
    def _build_graph(self, words, init_graph):
        for word_idx in range(len(words) - 1):
            edges = set([])
            word_smaller = words[word_idx]
            word_greater = words[word_idx + 1]
            for letter_idx in range(min(len(word_greater), len(word_smaller))):
                # find the first pair of different letters within two adjacent words
                if word_smaller[letter_idx] == word_greater[letter_idx]:
                    continue
                prec = word_smaller[letter_idx]
                succ = word_greater[letter_idx]
                if not (prec, succ) in edges:
                    init_graph[prec].succ.add(init_graph[succ])
                    init_graph[succ].indegree += 1
                    edges.add((prec, succ))
                    break
                else:
                    break
                
        return init_graph

    def _topology_bfs(self, graph):
        queue = []
        order = ""
        for key in graph.keys():
            if graph[key].indegree == 0:
                queue.append(key)
        while queue:
            curr = queue.pop(0)
            order += curr
            if graph[curr].succ:
                for succ in graph[curr].succ:
                    succ.indegree -= 1
                    if succ.indegree == 0:
                        queue.append(succ.char)
        return order

words = ["wrt","wrf","er","ett","rftt","te"]
alien_order_2 = AlienOrder2()
alien_order_2.alien_order(words)
