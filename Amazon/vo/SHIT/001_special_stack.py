class DoubleListNode(object):
    def __init__(self, x, *args, **kwargs):
        self.val = x
        self.prev = self.next = None
        return super().__init__(*args, **kwargs)


class SpecialStack(object):
    def __init__(self, *args, **kwargs):
        self.dummy = DoubleListNode("dummy")
        self.dummy.prev = self.dummy.next = self.dummy
        self.size = 0
        self.mid_idx = (self.size - 1) // 2
        self.mid_ele = self.dummy
    
    def stackpush(self, val):
        pushnode = DoubleListNode(val)
        # top pointer inc
        self.size += 1
        # put the node at stack top
        tail = self.dummy.prev
        tail.next, pushnode.next = pushnode, self.dummy
        pushnode.prev, self.dummy.prev = tail, pushnode
        # re-calc mid index
        new_mid_idx = (self.size - 1) // 2
        if new_mid_idx > self.mid_idx:
            self.mid_ele = self.mid_ele.next
            self.mid_idx = new_mid_idx
    
    def stackpop(self):
        if self.size == 0:
            return None
        popnode = self.dummy.prev
        # pick the popnode out
        popnode.prev.next = popnode.next
        popnode.next.prev = popnode.prev
        # dec stack top pointer
        self.size -= 1
        # recalc mid index
        new_mid_idx = (self.size - 1) // 2

        # 1 2 3 4 5   mid = 2
        #     ^
        # 1 2 3 4     mid = 1
        #   ^
        # 1 2 3       mid = 1
        #   ^
        if new_mid_idx < self.mid_idx:
            self.mid_ele = self.mid_ele.prev
            self.mid_idx = new_mid_idx
        return popnode.val
        
    def stackpopmid(self):
        if self.mid_idx == -1:
            return None
        # pick popnode out
        popnode = self.mid_ele
        popnode.prev.next = popnode.next
        popnode.next.prev = popnode.prev
        # dec stack top
        self.size -= 1
        # recalc mid idx

        # 1 2 3 4 5     mid = 2
        #     ^
        # 1 2 4 5       mid = 1
        #   ^
        new_mid_idx = (self.size - 1) // 2
        if new_mid_idx < self.mid_idx:
            self.mid_ele = self.mid_ele.prev
            self.mid_idx = new_mid_idx
        else:
            self.mid_ele = self.mid_ele.next
        return popnode.val

    def __str__(self):
        res = []
        node = self.dummy.next
        while node != self.dummy:
            res.append(node.val)
            node = node.next
        return str(res)



if __name__ == "__main__":
    specia_stack = SpecialStack()
    for i in range(1, 6):
        specia_stack.stackpush(i)
        print(specia_stack)
    for _ in range(5):
        print(specia_stack.stackpopmid(), specia_stack)