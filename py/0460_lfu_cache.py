
import heapq
"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.

For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class CacheNode(object):
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


"""
WA!! this is LRU!
"""


# class LFUCache:
class LRUCache(object):

    def __init__(self, capacity: int):
        self.head = CacheNode("key", "val")
        self.head.prev = self.head
        self.head.next = self.head
        self.cache_dict = {}
        self.capacity = capacity
        self.length = 0

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        node_get = self.cache_dict[key]
        node_get_prev, node_get_next = node_get.prev, node_get.next
        node_get_prev.next = node_get_next
        node_get_next.prev = node_get_prev
        node_last = self.head.prev
        node_last.next = node_get
        node_get.prev = node_last
        node_get.next = self.head
        self.head.prev = node_get
        return node_get.val

    def put(self, key: int, value: int) -> int:
        if key in self.cache_dict:
            node_put = self.cache_dict[key]
            node_put.val = value
            node_put_prev, node_put_next = node_put.prev, node_put.next
            node_put_prev.next = node_put_next
            node_put_next.prev = node_put_prev
            node_last = self.head.prev
            node_last.next = node_put
            node_put.prev = node_last
            node_put.next = self.head
            self.head.prev = node_put
        else:
            node_put = CacheNode(key, value)
            node_last = self.head.prev
            node_last.next = node_put
            node_put.prev = node_last
            node_put.next = self.head
            self.head.prev = node_put
            self.cache_dict[key] = node_put
            self.length += 1
            if self.length > self.capacity:
                node_delete = self.head.next
                node_delete_prev, node_delete_next = node_delete.prev, node_delete.next
                node_delete_prev.next = node_delete_next
                node_delete_next.prev = node_delete_prev
                del self.cache_dict[node_delete.key]
                self.length -= 1

    def display(self):
        if not self.head:
            print("empty linked list")
            return
        curr = self.head
        while curr:
            print("{}: {}".format(curr.key, curr.val), "-> " if curr.next else "", end="")
            curr = curr.next
            if curr == self.head:
                break
        print("")
        print(["{}: {}".format(x, y.val) for x, y in self.cache_dict.items()])


class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq_dict = {}
        self.cache_dict = {}
        self.length = 0

    def get(self, key):
        if key not in self.cache_dict:
            return -1
        node_get, node_freq = self.cache_dict[key]
        node_freq += 1
        

    def put(self, key, value):
        pass

        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)


if __name__ == "__main__":
    op_seq = ["LFUCache", "put", "put", "get", "get", "get", "put", "put", "get", "get", "get", "get"]

    pa_seq = [[3], [2, 2], [1, 1], [2], [1], [2], [3, 3], [4, 4], [3], [2], [1], [4]]
    for op, pa in zip(op_seq, pa_seq):
        if op == "LFUCache":
            # print("-", op, pa)
            obj = LFUCache(*pa)
            obj.display()
        elif op == "put":
            # print("-", op, pa)
            obj.put(*pa)
            obj.display()
        elif op == "get":
            ans = obj.get(*pa)
            obj.display()
            print("--", op, *pa, ans)
