# Подвиг 9. Объявите класс Box3D для представления прямоугольного параллелепипеда (бруска),
# объекты которого создаются командой:
# box = Box3D(width, height, depth)
# где width, height, depth - ширина, высота и глубина соответственно (числа: целые или вещественные)
# В каждом объекте класса Box3D должны создаваться публичные атрибуты:
# width, height, depth - ширина, высота и глубина соответственно.
# С объектами класса Box3D должны выполняться следующие операторы:
# box1 = Box3D(1, 2, 3)
# box2 = Box3D(2, 4, 6)
# box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
# box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# box = 3 * box2    # Box3D: width=6, height=12, depth=18
# box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно
# делятся на 2)
# box = box2 % 3    # Box3D: width=2, height=1, depth=0
# При каждой арифметической операции следует создавать новый объект класса Box3D с соответствующими
# значениями локальных атрибутов.
# P.S. В программе достаточно только объявить класс Box3D. На экран ничего выводить не нужно.

class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_attrs(self):
        return self.width, self.height, self.depth

    def __add__(self, other):
        return self.__class__(*map(sum, zip(self.get_attrs(), other.get_attrs())))

    def __mul__(self, other):
        return self.__class__(*[el * other for el in self.get_attrs()])

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self.__class__(*[el_1 - el_2 for el_1, el_2 in zip(self.get_attrs(), other.get_attrs())])

    def __floordiv__(self, other):
        return self.__class__(*[el // other for el in self.get_attrs()])

    def __mod__(self, other):
        return self.__class__(*[el % other for el in self.get_attrs()])


# box1 = Box3D(1, 2, 3)
# print("box1", box1.__dict__)
# box2 = Box3D(2, 4, 6)
# print("box2", box2.__dict__)
# box_ans1 = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности
# складываются)
# print("box_ans1", box_ans1.__dict__)
# box_ans2 = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
# print("box_ans2", box_ans2.__dict__)
# box_ans3 = 3 * box2    # Box3D: width=6, height=12, depth=18
# print("box_ans3", box_ans3.__dict__)
# box_ans4 = box2 - box1  # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
# print("box_ans4", box_ans4.__dict__)
# box_ans5 = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности
# целочисленно делятся на 2)
# print("box_ans5", box_ans5.__dict__)
# box_ans6 = box2 % 3    # Box3D: width=2, height=1, depth=0
# print("box_ans6", box_ans6.__dict__)
