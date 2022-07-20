class SingletonFive:
    __count = 0
    __link = None

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__count += 1
            cls.__link = super().__new__(cls)
        return cls.__link

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for k, v in enumerate(objs):
    print(k + 1, v)
