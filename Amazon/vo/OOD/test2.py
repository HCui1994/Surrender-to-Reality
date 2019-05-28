class A(object):
    def __init__(self, *args, **kwargs):
        self.a = 100
        return super().__init__(*args, **kwargs)

class B(A):
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)


print(B().a)