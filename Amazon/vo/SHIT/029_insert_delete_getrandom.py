import random
import collections


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.data = []
        self.dict = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.data.append(val)
        self.dict[val].add(len(self.data) - 1)

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            return False
        rmi = next(iter(self.data[val]))
        self.data[val].remove(rmi)
        if not self.data[val]:
            del self.data[val]
        self.data[rmi], self.data[-1] = self.data[-1], self.data[rmi]
        self.data.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data)
