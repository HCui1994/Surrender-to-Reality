class KHeap(object):
    def __init__(self, l=[], k=int(2)):
        self.list = l
        self.size - len(self.list)
        self.order = k
        self.build(self.list)
    
    def build(self):
        

    def move_up(self, i):
        """
        如果第 i 个节点小于其父节点，交换
        Params: 
            i: index of child node
        Return:
            None
        """
        child_idx = i
        while child_idx >= 0:
            parent_idx = (child_idx - 1) // self.order
            if self.list[child_idx] < self.list[parent_idx]:
                self.list[child_idx], self.list[parent_idx] = self.list[parent_idx], self.list[child_idx]
            child_idx = parent_idx
    
    