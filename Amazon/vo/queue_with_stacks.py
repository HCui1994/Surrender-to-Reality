class QueueWithStacks(list):
    def __init__(self, *args, **kwargs):
        self.reverse_stack = []
        return super().__init__(*args, **kwargs)

    def enqueue(self, val):
        super().append(val)

    def dequeue(self):
        if not self:
            return None
        while self:
            self.reverse_stack.append(super().pop())
        deq_val = self.reverse_stack.pop()
        while self.reverse_stack:
            super().append(self.reverse_stack.pop())
        return deq_val


qws = QueueWithStacks()
for i in range(1, 6):
    qws.enqueue(i)
    print(qws)

while qws:
    print(qws.dequeue())