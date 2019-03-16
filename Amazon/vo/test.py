class test(object):
    def __init__(self, *args, **kwargs):
        self.data = [1, 2, 3, 4, 5]
        return super().__init__(*args, **kwargs)

    def __getitem__(self, key):
        return self.data[key]


if __name__ == "__main__":
    t = test()
    t[2] = 999
    print(t[2])