# функция bool()
# В стандартном поведении она возвращает True для непустых объектов и False – для пустых.
# print(bool(123), bool(-1), bool(0), bool("python"), bool(""), bool([]))
#         True      True    False         True        False    False

# __len__() – вызывается функцией bool(), если не определен магический метод __bool__();
# __bool__() – вызывается в приоритетном порядке функцией bool().


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return self.x * self.x + self.y * self.y

    def __bool__(self):
        # Теперь, объект будет считаться правдивым (истинным), если его координаты равны
        print("__bool__")
        return self.x == self.y
        # В реальности, мы можем в этом методе прописывать любую логику.
        # Единственное условие, чтобы данный метод возвращал булево значение True или False.
        # Указывать в операторе return другие типы данных запрещено.


p = Point(3, 4)
print(bool(p))  # True
p = Point(0, 0)
print(bool(p))  # True
# используется? Чаще всего в условных конструкциях
if p:
    print("объект p дает True")
else:
    print("объект p дает False")
