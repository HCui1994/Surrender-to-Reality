class LRUCache(collections.OrderedDict):
    def __init__(self, capacity, *args, **kwargs):
        self.capacity = capacity
        super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        if key not in self:
            return -1
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self) > self.capacity:
            oldest = next(iter(self))
            del self[oldest]
