import collections


class DoubleListNode(object):
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None


class LRUCache(object):

    def __init__(self, capacity, *args, **kwargs):
        self.dummy = DoubleListNode("dummy")
        self.dummy.prev, self.dummy.next = self.dummy, self.dummy
        self.dict = {}
        self.size = 0
        self.capacity = capacity
        return super().__init__(*args, **kwargs)

    def put(self, key, value):
        if key not in self.dict:
            if self.size == self.capacity:
                head = self.dummy.next
                head.prev.next = head.next
                head.next.prev = head.prev
                del_key = head.key
                del self.dict[del_key]
                self.size -= 1
            new_node = DoubleListNode(key, value)
            tail = self.dummy.prev
            tail.next, new_node.next = new_node, self.dummy
            new_node.prev, self.dummy.prev = tail, new_node
            self.dict[key] = new_node
            self.size += 1
        else:
            visit_node = self.dict[key]
            visit_node.val = value
            visit_node.prev.next = visit_node.next
            visit_node.next.prev = visit_node.prev
            tail = self.dummy.prev
            tail.next, visit_node.next = visit_node, self.dummy
            visit_node.prev, self.dummy.prev = tail, visit_node

    def get(self, key):
        if key not in self.dict:
            return None
        visit_node = self.dict[key]
        visit_node.prev.next = visit_node.next
        visit_node.next.prev = visit_node.prev
        tail = self.dummy.prev
        tail.next, visit_node.next = visit_node, self.dummy
        visit_node.prev, self.dummy.prev = tail, visit_node
        return visit_node.val


#  extend from Ordereddict


class LRUCache2(collections.OrderedDict):
    def __init__(self, capacity, *args, **kwargs):
        self.capacity = capacity
        return super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key not in self:
            return -1
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            super().__setitem__(key, value)
            self.move_to_end(key)
        else:
            if len(self) == self.capacity:
                oldest = next(iter(self))
                del self[oldest]
            super().__setitem__(key, value)
            
