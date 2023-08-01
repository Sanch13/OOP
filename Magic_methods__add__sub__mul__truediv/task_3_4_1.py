# Подвиг 5. Объявите класс с именем ListMath, объекты которого можно создавать командами:
# lst1 = ListMath() # пустой список
# lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями
# В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и
# вещественные числа, остальные игнорировать (если указываются в списке). Например:
# lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
# В каждом объекте класса ListMath должен быть публичный атрибут:
# lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).
# Также с объектами класса ListMath должны работать следующие операторы:
# При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса
# ListMath с новыми списками, прежние списки не меняются.
# При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего
# объекта (новый объект не создается).
# P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно.

class ListMath:
    def __init__(self, lst: list = None):
        self.lst_math = self.get_correct_list(lst) if lst else []

    @classmethod
    def get_correct_list(cls, lst: list) -> list:
        """Returns the correct list ot the values"""
        return list(filter(cls.check_int_or_float, lst))

    @classmethod
    def check_int_or_float(cls, value) -> bool:
        """Returns True if a value is (int, float)"""
        return type(value) in (int, float)

    def __add__(self, other):
        if self.check_int_or_float(other):
            return ListMath([el + other for el in self.lst_math])

    def __iadd__(self, other):
        if self.check_int_or_float(other):
            self.lst_math = [el + other for el in self.lst_math]
            return self

    def __sub__(self, other):
        if self.check_int_or_float(other):
            return ListMath([el - other for el in self.lst_math])

    def __rsub__(self, other):
        if self.check_int_or_float(other):
            return ListMath([other - el for el in self.lst_math])

    def __mul__(self, other):
        if self.check_int_or_float(other):
            return ListMath([other * el for el in self.lst_math])

    def __rmul__(self, other):
        if self.check_int_or_float(other):
            return ListMath([other * el for el in self.lst_math])

    def __truediv__(self, other):
        if self.check_int_or_float(other):
            return ListMath([el / other for el in self.lst_math])

    def __itruediv__(self, other):
        if self.check_int_or_float(other):
            self.lst_math = [el / other for el in self.lst_math]
            return self


lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)

assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"

assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"

res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

lst = ListMath([0, 1, 2])
res3 = lst - 76
res4 = 7 - lst
assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"

lst -= 3
assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="

lst = ListMath([1, 2, 3])
res5 = lst * 5
res6 = 3 * lst
lst *= 4
assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"

lst = lst / 2
lst /= 13.0
