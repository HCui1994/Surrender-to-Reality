class DoubleListNode(object):
    def __init__(self, x, *args, **kwargs):
        self.val = x
        self.prev = self.next = None
        return super().__init__(*args, **kwargs)


class SpecialStack(object):
    def __init__(self, *args, **kwargs):
        self.dummy = DoubleListNode("dummy")
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.mid = None
        self.mid_idx = None
        self.stack_size = 0
        return super().__init__(*args, **kwargs)

    def push(self, x):
        tail = self.dummy.prev
        newnode = DoubleListNode(x)
        tail.next = newnode
        newnode.prev = tail
        newnode.next = self.dummy
        self.dummy.prev = newnode
        if self.stack_size == 0:
            self.stack_size += 1
            self.mid_idx = 0
            self.mid = newnode
        else:
            self.stack_size += 1
            new_mid_idx = self.stack_size // 2
            if new_mid_idx > self.mid_idx:
                self.mid_idx = new_mid_idx
                self.mid = self.mid.next

    def pop(self):
        if self.stack_size == 0:
            return None
        tail = self.dummy.left
        tail_prev = tail.prev
        tail_prev.next = self.dummy
        self.dummy.prev = tail_prev
        self.stack_size -= 1
        if self.stack_size == 0:
            self.mid = self.mid_idx = None
        else:
            new_mid_idx = self.stack_size // 2
            if new_mid_idx < self.mid_idx:
                self.mid_idx = new_mid_idx
                self.mid = self.mid.prev
        return tail.val

    def get_middle(self):
        if not self.mid:
            return None
        return self.mid.val

    def pop_middle(self):
        if not self.mid:
            return None
        pop_mid = self.mid
        pop_mid.prev.next = pop_mid.next
        pop_mid.next.prev = pop_mid.prev
        self.stack_size -= 1
        if self.stack_size == 0:
            self.mid = self.mid_idx = None
        else:
            new_mid_idx = self.stack_size // 2
            if self.mid_idx == new_mid_idx:
                self.mid = pop_mid.next
            else:
                self.mid = pop_mid.prev
                self.mid_idx -= 1
        return pop_mid.val

    def _display(self):
        node = self.dummy.next
        res = []
        while node != self.dummy:
            res.append(node.val)
            node = node.next
        return res

    def __str__(self):
        return str(self._display())


# a better implementation
class SpecialStackOpt(object):
    def __init__(self, values, *args, **kwargs):
        self.dummy = DoubleListNode("dummy")
        self.dummy.next, self.dummy.prev = self.dummy, self.dummy
        self.stack_size = 0
        self.mid = self.dummy
        self.mid_idx = -1
        for val in values:
            self.push(val)
        return super().__init__(*args, **kwargs)

    def push(self, val):
        tail = self.dummy.prev
        newnode = DoubleListNode(val)
        tail.next, newnode.next = newnode, self.dummy
        newnode.prev, self.dummy.prev = tail, newnode
        self.stack_size += 1
        new_mid_idx = (self.stack_size - 1) // 2
        if new_mid_idx > self.mid_idx:
            self.mid = self.mid.next
            self.mid_idx = new_mid_idx

    def pop(self):
        if self.stack_size == 0:
            return None
        popnode = self.dummy.prev
        popnode.prev.next = popnode.next
        popnode.next.prev = popnode.prev
        self.stack_size -= 1
        new_mid_idx = (self.stack_size - 1) // 2
        if new_mid_idx < self.mid_idx:
            self.mid = self.mid.prev
            self.mid_idx = new_mid_idx
        return popnode.val

    def get_middle(self):
        if self.mid == self.dummy:
            return None
        return self.mid.val

    def pop_middle(self):
        if self.stack_size == 0:
            return None
        popnode = self.mid
        popnode.prev.next = popnode.next
        popnode.next.prev = popnode.prev
        self.stack_size -= 1
        new_mid_idx = (self.stack_size - 1) // 2
        if new_mid_idx < self.mid_idx:
            self.mid = popnode.prev
            self.mid_idx = new_mid_idx
        else:
            self.mid = popnode.next
        return popnode.val

    def __str__(self):
        display = []
        node = self.dummy.next
        while node != self.dummy:
            display.append(node.val)
            node = node.next
        return str(display)


special_stack = SpecialStackOpt([1, 2, 3, 4, 5])
print(special_stack)

for _ in range(5):
    print(special_stack.pop_middle())
    print(special_stack)
