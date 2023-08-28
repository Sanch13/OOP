# Подвиг 10 (на повторение). Объявите базовый класс с именем ItemAttrs, который бы позволял
# обращаться к локальным атрибутам объектов дочерних классов по индексу. Для этого в классе
# ItemAttrs нужно переопределить следующие методы:
# __getitem__() - для получения значения атрибута по индексу;
# __setitem__() - для изменения значения атрибута по индексу.
# Объявите дочерний класс Point для представления координаты точки на плоскости.
# Объекты этого класса должны создаваться командой:
# pt = Point(x, y)
# где x, y - целые или вещественные числа.
# Пример использования классов (эти строчки в программе не писать):
# pt = Point(1, 2.5)
# x = pt[0]   # 1
# y = pt[1]   # 2.5
# pt[0] = 10
# P.S. В программе нужно объявить только классы. На экран выводить ничего не нужно.


class ItemAttrs:
    def __getitem__(self, index):
        return list(self.__dict__.values())[index]
        # for i, value in enumerate(self.__dict__.values()):
        #     if index == i:
        #         return value

    def __setitem__(self, index, value):
        self.__dict__[list(self.__dict__)[index]] = value
        # for i, key in enumerate(self.__dict__):
        #     if index == i:
        #         self.__dict__[key] = value
        #         return ''


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]   # 1
print(x, pt.__dict__)
y = pt[1]
print(y, pt.__dict__)
pt[0] = 10
print(x, pt.__dict__)

