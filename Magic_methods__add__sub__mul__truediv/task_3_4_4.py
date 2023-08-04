# Подвиг 8. Вам необходимо создать простую программу по учету семейного бюджета. Для этого в
# программе объявите два класса с именами:
# Budget - для управления семейным бюджетом;
# Item - пункт расходов бюджета.
# Объекты класса Item должны создаваться командой:
# it = Item(name, money)
# где name - название статьи расхода; money - сумма расходов (вещественное или целое число).
# Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и
# money с переданными значениями.
# Также с объектами класса Item должны выполняться следующие операторы:
# s = it1 + it2 # сумма для двух статей расходов
# и в общем случае:
# s = it1 + it2 + ... + itN # сумма N статей расходов
# При суммировании оператор + должен возвращать число - вычисленную сумму по атрибутам
# money соответствующих объектов класса Item.
# Объекты класса Budget создаются командой:
# my_budget = Budget()
# А сам класс Budget должен иметь следующие методы:
# add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
# remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру
# indx (индексу: отсчитывается с нуля);
# get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).
# Пример использования классов (эти строчки в программе писать не нужно):
# my_budget = Budget()
# my_budget.add_item(Item("Курс по Python ООП", 2000))
# my_budget.add_item(Item("Курс по Django", 5000.01))
# my_budget.add_item(Item("Курс по NumPy", 0))
# my_budget.add_item(Item("Курс по C++", 1500.10))
# # вычисление общих расходов
# s = 0
# for x in my_budget.get_items():
#     s = s + x
# P.S. В программе требуется только объявить класс. На экран ничего выводить не нужно.

class Item:
    def __init__(self, name: str, money: int or float):
        self.name = name
        self.money = money

    def __add__(self, other) -> int:
        self.money += other if isinstance(other, (int, float)) else other.money
        return self.money

    def __radd__(self, other):
        return self + other


class Budget:
    def __init__(self):
        self.lst = []

    def add_item(self, it):
        """Adds Items object on a current list"""
        self.lst.append(it)

    def remove_item(self, indx):
        """Delete object from a current list"""
        if indx < len(self.lst):
            del self.lst[indx]

    def get_items(self):
        """Returns a current list of the Items objects"""
        return self.lst


it1 = Item("Курс по Python ООП", 2000)
it2 = Item("Курс по Django", 5000.01)
it3 = Item("Курс по C++", 1500.10)
it4 = Item("Курс по FastAPI", 10000.02)
s = it1 + it2 + it3 + it4
print(s)
assert Item('a', 150) + Item('b', 111.11) == 261.11
my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
print(my_budget.get_items())
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)

