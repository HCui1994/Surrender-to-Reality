import collections


class DoubleListNode(object):
    def __init__(self, key, val, *args, **kwargs):
        self.key, self.val = key, val
        self.prev = self.next = None
        return super().__init__(*args, **kwargs)


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dummy = DoubleListNode("key", "val")
        self.dummy.prev = self.dummy.next = self.dummy
        self.dict = {}

    def get(self, key):
        if key not in self.dict:
            return -1
        getnode = self.dict[key]
        # pick the getnode out
        getnode.prev.next = getnode.next
        getnode.next.prev = getnode.prev
        # put the getnode to tail
        tail = self.dummy.prev
        tail.next, getnode.next = getnode, self.dummy
        getnode.prev, self.dummy.prev = tail, getnode
        return getnode.val

    def put(self, key, val):
        if key in self.dict:
            # modify the put node
            self.dict[key].val = val
            # call get()
            self.get(key)
        else:
            # currently not in cache
            if self.size == self.capacity:
                # del lru
                delnode = self.dummy.next
                # pick the delnode out
                delnode.prev.next = delnode.next
                delnode.next.prev = delnode.prev
                # del from dict
                del self.dict[delnode.key]
                self.size -= 1
            putnode = DoubleListNode(key, val)
            # link the putnode to tail
            tail = self.dummy.prev
            tail.next, putnode.next = putnode, self.dummy
            putnode.prev, self.dummy.prev = tail, putnode
            self.size += 1
            self.dict[key] = putnode


class LRUCache2(collections.OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        return super().__init__()

    def __getitem__(self, key):
        if key not in self:
            return -1
        ret = super().__getitem__(key)
        self.move_to_end(key)
        return ret
    
    def __setitem__(self, key, val):
        if key in self:
            super().__setitem__(key, val)
            self.move_to_end(key)
            return
        if len(self) == self.capacity:
            delete = next(iter(self))
            del self[delete]
        super().__setitem__(key, val)
    
    def get(self, key):
        return self[key]

    def put(self, key, val):
        self[key] = val



