class IntegerReplacement(object):
    def num_of_replacement(self, n):
        if n == 0 or n == 2:
            return 1
        if n == 1:
            return 0
        if n & 1:
            return 1 + min(self.num_of_replacement(n + 1), self.num_of_replacement(n - 1))
        else:
            return 1 + self.num_of_replacement(n // 2)


res = IntegerReplacement().num_of_replacement(65535)
print(res)