class A:
    def __init__(self, name, old):
        super().__init__()
        self.name = name
        self.old = old


class B:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class C(B, A):
    # программа будет успешно выполняться вне зависимости от порядка наследования
    # классов A и B в дочернем классе C
    def __init__(self, name, old, weight, height):
        super().__init__(name, old)
        self.weight = weight
        self.height = height


person = C("Balakirev", 33, 80, 185)
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
print(person.__dict__)  # {'name': 'Balakirev', 'old': 33, 'weight': 80, 'height': 185}
