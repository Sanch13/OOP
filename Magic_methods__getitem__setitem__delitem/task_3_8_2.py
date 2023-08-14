# Подвиг 4. Вам необходимо написать программу по работе с массивом однотипных данных
# (например, только числа или строки и т.п.). Для этого нужно объявить класс с именем Array,
# объекты которого создаются командой:
# ar = Array(max_length, cell)
# где max_length - максимальное количество элементов в массиве; cell - ссылка на класс,
# описывающий отдельный элемент этого массива (см. далее, класс Integer). Начальные значения в
# ячейках массива (в объектах класса Integer) должны быть равны 0.
# Для работы с целыми числами объявите в программе еще один класс с именем Integer, объекты
# которого создаются командой:
# cell = Integer(start_value)
# где start_value - начальное значение ячейки (в данном случае - целое число).
# В классе Integer должно быть следующее свойство (property):
# value - для изменения и считывания значения из ячейки (само значение хранится в локальной
# приватной переменной; имя придумайте сами).
# При попытке присвоить не целое число должно генерироваться исключение командой:
# raise ValueError('должно быть целое число')
# Для обращения к отдельным элементам массива в классе Array необходимо определить набор
# магических методов для следующих операций:
# value = ar[0] # получение значения из первого элемента (ячейки) массива ar
# ar[1] = value # запись нового значения во вторую ячейку массива ar
# Если индекс не целое число или число меньше нуля или больше либо равно max_length, то должно
# генерироваться исключение командой:
# raise IndexError('неверный индекс для доступа к элементам массива')
# Пример использования классов (эти строчки в программе не писать):
# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int) # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
# P.P.S. В качестве дополнительного домашнего задания: объявите еще один класс Float для работы
# с вещественными числами и создайте массив, используя тот же класс Array,
# с этим новым типом данных.

def check_index(func):
    def wrapper(obj, indx, *args, **kwargs):
        if isinstance(indx, int) and 0 <= indx < len(obj):
            return func(obj, indx, *args, **kwargs)
        raise IndexError('неверный индекс для доступа к элементам массива')

    return wrapper


class Integer:
    def __init__(self, start_value=0):
        self.__start = start_value

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, value):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.__start = value


class Array:
    def __init__(self, max_length, cell):
        self.max_length = max_length
        self.list_cells = [cell() for _ in range(self.max_length)]

    def __len__(self):
        return self.max_length

    @check_index
    def __getitem__(self, key):
        return self.list_cells[key].start

    def __setitem__(self, key, value):
        self.list_cells[key].start = value

    def __str__(self):
        return f"{' '.join(str(obj.start) for obj in self.list_cells)}"


ar_int = Array(10, cell=Integer)
print(ar_int.__dict__)
print(ar_int[1])
ar_int[1] = 10
ar_int[0] = 23
ar_int[9] = 1023
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10.5  # должно генерироваться исключение ValueError
# ar_int[10] = 1  # должно генерироваться исключение IndexError