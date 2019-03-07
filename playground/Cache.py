import tokenize
import collections


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

    def get(self, key):
        return self[key]

    def put(self, key, value):
        self[key] = value


class LFUCache(object):
    def __init__(self, capacity, *args, **kwargs):
        self.capacity = capacity
        self.size = 0
        self.least_freq = 1  # 最小访问频率
        # key 对应 frequency
        self.freq_dict = collections.Counter()
        # frequency 对应一组 key: value 键值对
        self.od_dict = collections.defaultdict(collections.OrderedDict)

    def get(self, key):
        if key not in self.freq_dict:
            # key 没有相应的 freq，cache中没有对应的键值对
            return -1
        freq = self.freq_dict[key]
        # 从键值对所在的序列中取
        value = self.od_dict[freq].pop(key)
        if not self.od_dict[freq] and freq == self.least_freq:
            # 如果当前 freq 组没有键值对，且当前 freq 组为最小 freq
            self.least_freq += 1
        freq += 1
        # 将键值对放入新的 freq 组中
        self.freq_dict[key] = freq
        self.od_dict[freq][key] = value
        return value

    def put(self, key, value):
        if key not in self.freq_dict:
            # 如果 key 没有相应的键值对，需要插入新的键值对
            if self.size == self.capacity:
                # 检查 capacity，若达到上限，需要先腾出空间
                # 弹出最低访问频率组，最久未被访问的键值对
                del_key, del_value = self.od_dict[self.least_freq].popitem(last=False)  
                # 删除对应的 key freq 对
                del self.freq_dict[del_key]
                if not self.od_dict[self.least_freq]:
                    # 若此时最小组没有键值对
                    del self.od_dict[self.least_freq]  # 删除最小组
            self.least_freq = 1  # 由于键值对未出现过，访问频率必为 1
            self.freq_dict[key] = self.least_freq
            self.od_dict[self.least_freq][key] = value
        else:
            # 如果 key 已存在于 cache 中，需要用新的 value 覆盖，且增加访问频率
            freq = self.freq_dict[key]
            cover_value = self.od_dict[freq].pop(key)
            if not self.od_dict[freq] and freq == self.least_freq:
                self.least_freq += 1
            freq += 1
            self.freq_dict[key] = freq
            self.od_dict[freq][key] = value





if __name__ == "__main__":
    operation = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]

    parameter = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    for operation, parameter in zip(operation, parameter):
        if operation == "LRUCache":
            cache = LRUCache(*parameter)
        elif operation == "LFUCache":
            cache = LFUCache(*parameter)
        elif operation == "put":
            cache.put(*parameter)
            print(operation, *parameter)
        elif operation == "get":
            res = cache.get(*parameter)
            print(operation, *parameter, "\t", res)
