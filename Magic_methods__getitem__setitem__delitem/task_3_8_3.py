# Большой подвиг 5. Вам необходимо написать программу для удобного обращения с таблицами однотипных
# данных (чисел, строк, булевых значений и т.п.), то есть, все ячейки таблицы должны представлять
# какой-то один указанный тип.
# Для этого в программе необходимо объявить три класса:
# TableValues - для работы с таблицей в целом;
# CellInteger - для операций с целыми числами;
# IntegerValue - дескриптор данных для работы с целыми числами.
# Начнем с дескриптора IntegerValue. Это должен быть дескриптор данных (то есть, и для записи и
# считывания значений). Если присваиваемое значение не является целым числом, должно генерироваться
# исключение командой:
# raise ValueError('возможны только целочисленные значения')
# Следующий класс CellInteger описывает одну ячейку таблицы для работы с целыми числами. В этом
# классе должен быть публичный атрибут (атрибут класса):
# value - объект дескриптора, класса IntegerValue.
# А объекты класса CellInteger должны создаваться командой:
# cell = CellInteger(start_value)
# где start_value - начальное значение ячейки (по умолчанию равно 0 и сохраняется в ячейке через
# дескриптор value).
# Наконец, объекты последнего класса TableValues создаются командой:
# table = TableValues(rows, cols, cell=CellInteger)
# где rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс, описывающий
# работу с отдельными ячейками таблицы. Если параметр cell не указан, то генерировать исключение
# командой:
# raise ValueError('параметр cell не указан')
# Иначе, в объекте table класса TableValues создается двумерный (вложенный) кортеж с именем cells
# размером rows x cols, состоящий из объектов указанного класса (в данном примере -
# класса CellInteger).
# Также в классе TableValues предусмотреть возможность обращения к отдельной ячейке по ее
# индексам, например:
# value = table[1, 2] # возвращает значение ячейки с индексом (1, 2)
# table[0, 0] = value # записывает новое значение в ячейку (0, 0)
# Обратите внимание, по индексам сразу должно возвращаться значение ячейки, а не объект класса
# CellInteger. И то же самое с присваиванием нового значения.
# Пример использования классов (эти строчки в программе не писать):
# table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
# table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError
# # вывод таблицы в консоль
# for row in table.cells:
#     for x in row:
#         print(x.value, end=' ')
#     print()
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
# P.P.S. В качестве домашнего задания создайте класс CellString для работы со строками и
# используйте тот же класс TableValues для этого нового типа данных.
# Последнее: дескрипторы здесь для повторения. В реальной разработке лучше использовать в
# таких задачах объекты-свойства (property).


class DescriptorValue:
    def __set_name__(self, owner, name):
        self.name = f"__{owner.__name__}_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        instance.check_type_value(value)
        setattr(instance, self.name, value)


class CellInteger:
    value = DescriptorValue()

    def __init__(self, value=0):
        self.value = value

    @staticmethod
    def check_type_value(value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')


class CellString:
    value = DescriptorValue()

    def __init__(self, value=""):
        self.value = value

    @staticmethod
    def check_type_value(value):
        if not isinstance(value, str):
            raise ValueError('возможны только строковые значения')


class TableValues:
    def __init__(self, rows, cols, cell):
        if cell is not cell:
            raise ValueError('параметр cell не указан')
        self.cells = [[cell() for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, key):
        row, col = key
        return self.cells[row][col].value

    def __setitem__(self, key, value):
        row, col = key
        self.cells[row][col].value = value

    def __repr__(self):
        return f"{[[obj.value for obj in row] for row in self.cells]}"


table = TableValues(2, 3, cell=CellInteger)
print(table)
table1 = TableValues(2, 3, cell=CellString)
print(table1)
table1[0, 2] = "asd"
print(table1)
# print(table[0, 1])
# table[0, 2] = 9999
# print(table)
