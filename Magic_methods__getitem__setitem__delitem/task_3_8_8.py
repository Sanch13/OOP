# Подвиг 10. Вам необходимо описывать в программе очень большие и разреженные таблицы данных
# (с большим числом пропусков). Для этого предлагается объявить класс SparseTable,
# объекты которого создаются командой:
# st = SparseTable()
# В каждом объекте этого класса должны создаваться локальные публичные атрибуты:
# rows - общее число строк таблицы (начальное значение 0);
# cols - общее число столбцов таблицы (начальное значение 0).
# В самом классе SparseTable должны быть объявлены методы:
# add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row,
# col (целые неотрицательные числа);
# remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).
# При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows,
# cols объекта класса SparseTable. Если происходит попытка удалить несуществующую ячейку,
# то должно генерироваться исключение:
# raise IndexError('ячейка с указанными индексами не существует')
# Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:
# data = Cell(value)
# где value - данные ячейки (любой тип).
# Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j,
# а значениями - объекты класса Cell.
# Также с объектами класса SparseTable должны выполняться команды:
# res = st[i, j] # получение данных из таблицы по индексам (i, j)
# st[i, j] = value # запись новых данных по индексам (i, j)
# Чтение данных возможно только для существующих ячеек. Если ячейки с указанными
# индексами нет, то генерировать исключение командой:
# raise ValueError('данные по указанным индексам отсутствуют')
# При записи новых значений их следует менять в существующей ячейке или добавлять новую,
# если ячейка с индексами (i, j) отсутствует в таблице. (Не забывайте при этом пересчитывать
# атрибуты rows и cols).
# Пример использования классов (эти строчки в программе не писать):
# st = SparseTable()
# st.add_data(2, 5, Cell("cell_25"))
# st.add_data(0, 0, Cell("cell_00"))
# st[2, 5] = 25 # изменение значения существующей ячейки
# st[11, 7] = 'cell_117' # создание новой ячейки
# print(st[0, 0]) # cell_00
# st.remove_data(2, 5)
# print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


def check_cells(func):
    def wrapper(obj, cell, *args, **kwargs):
        if (cell[0], cell[1]) in obj.data_table:
            return func(obj, cell, *args, **kwargs)
        raise ValueError('данные по указанным индексам отсутствуют')

    return wrapper


class Cell:
    def __init__(self, value=0):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = self.cols = 0
        self.data_table = {}

    def update_index(self):
        self.rows = max(key[0] for key in self.data_table) + 1
        self.cols = max(key[1] for key in self.data_table) + 1

    def add_data(self, row, col, data):
        self.data_table[(row, col)] = data
        self.update_index()

    def remove_data(self, row, col):
        try:
            del self.data_table[(row, col)]
            self.update_index()
        except KeyError:
            raise IndexError('ячейка с указанными индексами не существует')

    @check_cells
    def __getitem__(self, key):
        r, c = key
        return self.data_table[(r, c)].value

    def __setitem__(self, key, value):
        r, c = key
        self.data_table[(r, c)].value = value
        self.update_index()

    def __str__(self):
        return f"{self.data_table}"


st = SparseTable()
st.add_data(2, 5, Cell(25))
st.add_data(1, 1, Cell(11))
print(st[2, 5])
assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

try:
    v = st[3, 2]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

st[3, 2] = 100
assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

print(st)
st.remove_data(1, 1)
try:
    v = st[1, 1]
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    st.remove_data(1, 1)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

d = Cell('5')
assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"




