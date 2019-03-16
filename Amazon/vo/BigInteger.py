class BigInteger(object):
    def __init__(self, num, *args, **kwargs):
        if type(num) == int:
            num = str(num)
        if type(num) == float:
            num = str(num // 1)
        self.num = num
        return super().__init__(*args, **kwargs)

    def __add__(self, other):
        