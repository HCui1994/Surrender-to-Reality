import collections


class DoubleLinkedListNode(object):
    def __init__(self, val, key, *args, **kwargs):
        self.val = val
        self.key = key
        self.prev = self.next = None
        return super().__init__(*args, **kwargs)


class LRUCache(object):
    def __init__(self, capacity, *args, **kwargs):
        self.dummy = DoubleLinkedListNode("val", "key")
        self.dummy.prev = self.dummy.next = self.dummy
        self.dict = {}  # key-to-ref
        self.capacity = capacity
        self.size = 0
        return super().__init__(*args, **kwargs)

    def get(self, key):
        if key not in self.dict:
            return None  # not found
        getnode = self.dict[key]
        # pick out the visited node
        getnode.prev.next = getnode.next
        getnode.next.prev = getnode.prev
        # put the visited node at tail
        tail = self.dummy.prev
        tail.next, getnode.next = getnode, self.dummy
        getnode.prev, self.dummy.prev = tail, getnode
        return getnode.val

    def put(self, key, val):
        if key in self.dict:
            putnode = self.dict[key]
            # assign new value
            putnode.val = val
            # pickout, put to tail
            putnode.prev.next = putnode.next
            putnode.next.prev = putnode.prev
            tail = self.dummy.prev
            tail.next, putnode.next = putnode, self.dummy
            putnode.prev, self.dummy.prev = tail, putnode
        else:
            if self.size == self.capacity:
                # delete lru node
                deletenode = self.dummy.next
                # pick delete node out
                deletenode.prev.next = deletenode.next
                deletenode.next.prev = deletenode.prev
                del self.dict[deletenode.key]
                self.size -= 1
            # NEW new node, set reference
            putnode = DoubleLinkedListNode(val, key)
            self.dict[key] = putnode
            # put new node to tail
            tail = self.dummy.prev
            tail.next, putnode.next = putnode, self.dummy
            putnode.prev, self.dummy.prev = tail, putnode
            self.size += 1


class LRUCache2(collections.OrderedDict):
    def __init__(self, capacity, *args, **kwargs):
        self.capacity = capacity
        return super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key in self:
            value = super().__getitem__(key)
            self.move_to_end(key)
            return value
        return -1

    def __setitem__(self, key, val):
        if key in self:
            super().__setitem__(key, val)
            self.move_to_end(key)
        else:
            if len(self) == self.capacity:
                del_key = next(iter(self))
                del self[del_key]
                self.capacity -= 1
            super().__setitem__(key, val)

    def get(self, key):
        return self[key]

    def put(self, key, val):
        self[key] = val
