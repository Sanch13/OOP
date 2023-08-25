# Подвиг 10 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, ..., xN)
# где x1, x2, ..., xN - координаты радиус-вектора (числа: целые или вещественные).
# С объектами этого класса должны выполняться команды:
# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2 # формируется новый вектор (объект класса Vector) с соответствующими координатами
# Если размерности векторов v1 и v2 не совпадают, то генерировать исключение:
# raise TypeError('размерности векторов не совпадают')
# В самом классе Vector объявите метод с именем get_coords, который возвращает кортеж из текущих
# координат вектора.
# На основе класса Vector объявите дочерний класс VectorInt для работы с целочисленными
# координатами:
# v = VectorInt(1, 2, 3, 4)
# v = VectorInt(1, 0.2, 3, 4) # ошибка: генерируется исключение raise ValueError('координаты
# должны быть целыми числами')
# При операциях сложения и вычитания с объектом класса VectorInt:
# v = v1 + v2  # v1 - объект класса VectorInt
# v = v1 - v2  # v1 - объект класса VectorInt
# должен формироваться объект v как объект класса Vector, если хотя бы одна координата является
# вещественной. Иначе, v должен быть объектом класса VectorInt.
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


def check_size_matrix(func):
    def wrapper(m1, m2):
        if len(m1.coords) != len(m2.coords):
            raise TypeError('размерности векторов не совпадают')
        return func(m1, m2)

    return wrapper


def check_int_value(func):
    def wrapper(instance, *args):
        if not all(isinstance(x, int) for x in args):
            raise ValueError('координаты должны быть целыми числами')
        return func(instance, *args)

    return wrapper


class Vector:
    def __init__(self, *args):
        self.coords = args

    @check_size_matrix
    def __add__(self, other):
        return Vector(*[el1 + el2 for el1, el2 in zip(self.coords, other.coords)])

    @check_size_matrix
    def __sub__(self, other):
        return Vector(*[el1 - el2 for el1, el2 in zip(self.coords, other.coords)])

    def get_coords(self):
        return self.coords


class VectorInt(Vector):
    @check_int_value
    def __init__(self, *args):
        super().__init__(*args)

    @check_size_matrix
    def __add__(self, other):
        if isinstance(self, VectorInt) and isinstance(other, VectorInt):
            return VectorInt(*[el1 + el2 for el1, el2 in zip(self.coords, other.coords)])

        return Vector.__add__(self, other)

    @check_size_matrix
    def __sub__(self, other):
        if isinstance(self, VectorInt) and isinstance(other, VectorInt):
            return Vector(*[el1 - el2 for el1, el2 in zip(self.coords, other.coords)])

        return Vector.__sub__(self, other)

# v1 = Vector(1, 2, 3)
# v2 = Vector(3, 4, 5)
# print(v1.get_coords(), v2.get_coords())
# print(v1.__dict__, v2.__dict__)
# print(len(v1) == len(v2))
# v = v1 + v2
# print(v.__dict__)
# v = v1 - v2
# print(v.__dict__)
# v3 = VectorInt(1, 3, 4)
# print(v3.__dict__, v3.__class__, v1.__dict__, v1.__class__)
# v = v3 + v1
# print(v.__dict__, v.__class__)


v1 = Vector(1, 2, 3)
v2 = Vector(3, 4, 5)

assert (v1 + v2).get_coords() == (4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
assert (v1 - v2).get_coords() == (-2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

v = VectorInt(1, 2, 3, 4)
assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

try:
    v = VectorInt(1, 2, 3.4, 4)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

v1 = VectorInt(1, 2, 3, 4)
v2 = VectorInt(4, 2, 3, 4)
v3 = Vector(1.0, 2, 3, 4)

v = v1 + v2
assert type(v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
v = v1 + v3
print(v.__class__)
assert type(v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
