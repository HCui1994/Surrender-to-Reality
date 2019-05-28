class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)  
        return cls._instance


class Instance(Singleton):
    a = 100

a = Instance()

b = Instance()

print(a is b)