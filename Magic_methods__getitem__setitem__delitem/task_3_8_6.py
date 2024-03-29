# Подвиг 8. Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". Для этого
# требуется объявить класс TicTacToe (крестики-нолики), объекты которого создаются командой:
# game = TicTacToe()
# Каждый объект game должен иметь публичный атрибут:
# pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.
# Каждая клетка игрового поля представляется объектом класса Cell и создается командой:
# cell = Cell()
# Объекты класса Cell должны иметь следующие публичные локальные атрибуты:
# is_free - True, если клетка свободна; False в противном случае;
# value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).
# Также с каждым объектом класса Cell должна работать функция:
# bool(cell)
# которая возвращает True, если клетка свободна (cell.is_free=True) и False в противном случае.
# Класс TicTacToe должен иметь следующий метод:
# clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое
# состояние);
# А объекты этого класса должны иметь следующую функциональность (обращение по индексам):
# game[0, 0] = 1 # установка нового значения, если поле закрыто
# res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)
# Если указываются некорректные индексы, то должно генерироваться исключение командой:
# raise IndexError('неверный индекс клетки')
# Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:
# raise ValueError('клетка уже занята')
# Также должны быть реализованы следующие полные срезы при обращении к клеткам игрового поля:
# slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
# slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx
# Пример использования классов (эти строчки в программе не писать):
# game = TicTacToe()
# game.clear()
# game[0, 0] = 1
# game[1, 0] = 2
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
# if game[0, 0] == 0:
#     game[0, 0] = 2
# v1 = game[0, :]  # 1, 0, 0
# v2 = game[:, 0]  # 1, 2, 0
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
#
# P.P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса
# становится объектом класса slice. Его можно указывать непосредственно в квадратных скобках
# упорядоченных коллекций (списков, кортежей и т.п.).

class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))

    def clear(self):
        for obj in self.pole:
            for el in obj:
                el.is_free = True
                el.value = 0

    def __getitem__(self, item):
        self.check_indx(item)
        r, c = item
        if type(r) == slice:
            return tuple(self.pole[x][c].value for x in range(3))
        if type(c) == slice:
            return tuple(self.pole[r][x].value for x in range(3))

        return self.pole[r][c].value

    def __setitem__(self, key, value):
        self.check_indx(key)
        r, c = key
        if self.pole[r][c].is_free:
            self.pole[r][c].value = value
            self.pole[r][c].is_free = False
        else:
            raise ValueError('клетка уже занята')

    @staticmethod
    def check_indx(value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise IndexError('неверный индекс клетки')
        if any(not (0 <= x < 3) for x in value if not isinstance(x, slice)):
            raise IndexError('неверный индекс клетки')

    def __str__(self):
        return "\n".join([str([obj.value for obj in row]) for row in self.pole])


game = TicTacToe()
print(game)
res = game[1, 1]
print(res)
game[0, 0] = 1
print(game)
slice_1 = game[:, 0]
print(slice_1)


g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"
print(g)

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3
print(g)

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
# res = cell.is_free
# cell.is_free = True
# assert bool(cell), "функция bool вернула False для свободной клетки"
