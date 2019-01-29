"""
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").
 

Example 1:

Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:   
TimeMap kv;   
kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
kv.get("foo", 1);  // output "bar"   
kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
kv.set("foo", "bar2", 4);   
kv.get("foo", 4); // output "bar2"   
kv.get("foo", 5); //output "bar2"   

Example 2:

Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output: [null,null,null,"","high","high","low","low"]
 

Note:

All key/value strings are lowercase.
All key/value strings have length in the range [1, 100]
The timestamps for all TimeMap.set operations are strictly increasing.
1 <= timestamp <= 10^7
TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.dict = collections.defaultdict(list)

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.dict[key].append((timestamp, value))

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.dict or timestamp < self.dict[key][0][0]:
            return ""
        if timestamp >= self.dict[key][-1][0]:
            return self.dict[key][-1][1]
        low, high = 0, len(self.dict[key])
        while low < high:
            print(low, high, mid)
            mid = (low + high) // 2
            low_time = self.dict[key][low][0]
            high_time = self.dict[key][low][0]
            mid_time = self.dict[key][mid][0]
            if low_time == timestamp:
                return self.dict[key][low][1]
            if high_time == timestamp:
                return self.dict[key][high][1]
            if mid_time == timestamp:
                return self.dict[key][mid][1]
            if mid_time > timestamp:
                if self.dict[key][mid - 1][0] < timestamp:
                    return self.dict[key][mid - 1][1]
                else:
                    high = mid - 1
            else:
                if self.dict[key][mid + 1][0] > timestamp:
                    return self.dict[key][mid + 1][1]
                else:
                    low = mid + 1
        # for idx in range(len(self.dict[key])):
        #     if timestamp == self.dict[key][idx][0]:
        #         return self.dict[key][idx][1]
        #     if timestamp < self.dict[key][idx][0]:
        #         break
        # return self.dict[key][idx - 1][1]
