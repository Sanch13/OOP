# Подвиг 9 (на повторение). Объявите в программе класс Vector, объекты которого создаются командой:
# v = Vector(x1, x2, x3,..., xN)
# где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).
# С каждым объектом класса Vector должны выполняться операторы:
# v1 + v2 # суммирование соответствующих координат векторов
# v1 - v2 # вычитание соответствующих координат векторов
# v1 * v2 # умножение соответствующих координат векторов
# v1 += 10 # прибавление ко всем координатам вектора числа 10
# v1 -= 10 # вычитание из всех координат вектора числа 10
# v1 += v2
# v2 -= v1
# v1 == v2 # True, если соответствующие координаты векторов равны
# v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает
# При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с
# новыми (вычисленными) координатами. При реализации операторов +=, -= координаты меняются в т
# екущем объекте, не создавая новый.
# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, *
# должно генерироваться исключение командой:
# raise ArithmeticError('размерности векторов не совпадают')
# P.S. В программе на экран выводить ничего не нужно, только объявить класс.


def check_len_objects(func):
    def wrapper(obj_1, obj_2):
        if len(obj_1) != len(obj_2):
            raise ArithmeticError('размерности векторов не совпадают')
        return func(obj_1, obj_2)

    return wrapper


class Vector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    @check_len_objects
    def __add__(self, other):
        return Vector(*(el1 + el2 for el1, el2 in zip(self.coords, other.coords)))

    def __iadd__(self, other):
        if isinstance(other, int):
            self.coords = tuple(el1 + other for el1 in self.coords)
        else:
            self.coords = tuple(el1 + el2 for el1, el2 in zip(self.coords, other.coords))
        return self

    @check_len_objects
    def __sub__(self, other):
        return Vector(*(el1 - el2 for el1, el2 in zip(self.coords, other.coords)))

    def __isub__(self, other):
        if isinstance(other, int):
            self.coords = tuple(el1 - other for el1 in self.coords)
        else:
            self.coords = tuple(el1 - el2 for el1, el2 in zip(self.coords, other.coords))
        return self

    @check_len_objects
    def __mul__(self, other):
        return Vector(*(el1 * el2 for el1, el2 in zip(self.coords, other.coords)))

    @check_len_objects
    def __eq__(self, other):
        return self.coords == other.coords


# v1 = Vector(3, 5)
# # print(v1.coords)
# v2 = Vector(3, 5)
# print(v1 == v2)
# print(v1.coords)
# v1 = Vector(3, 5)
# print(v1.coords)
# v1 += 10
# print(v1.coords)
# v2 = Vector(10, 20)
# print(v2.coords)
# v2 -= 5
# print(v2.coords)
# v3 = v1 + v2
# print(v3.coords)
# v4 = v1 - v2
# print(v4.coords)
# v5 = v1 * v2
# print(v5.coords)
