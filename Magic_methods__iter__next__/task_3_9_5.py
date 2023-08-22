# Подвиг 10 (на повторение). Объявите класс Matrix (матрица) для операций с матрицами.
# Объекты этого класса должны создаваться командой:
# m1 = Matrix(rows, cols, fill_value)
# где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное
# значение элементов матрицы (должно быть число: целое или вещественное). Если в качестве
# аргументов передаются не числа, то генерировать исключение:
# raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
# Также объекты можно создавать командой:
# m2 = Matrix(list2D)
# где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных).
# Если список list2D не прямоугольный, или хотя бы один из его элементов не число, то
# генерировать исключение командой:
# raise TypeError('список должен быть прямоугольным, состоящим из чисел')
# Для объектов класса Matrix должны выполняться следующие команды:
# matrix = Matrix(4, 5, 0)
# res = matrix[0, 0] # возвращается первый элемент матрицы
# matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2)
# присваивается новое значение
# Если в результате присвоения тип данных не соответствует числу, то генерировать
# исключение командой:
# raise TypeError('значения матрицы должны быть числами')
# Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров
# матрицы), то генерировать исключение:
# raise IndexError('недопустимые значения индексов')
# Также с объектами класса Matrix должны выполняться операторы:
# matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
# matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
# Во всех этих операция должна формироваться новая матрица с соответствующими значениями.
# Если размеры матриц не совпадают (разные хотя бы по одной оси), то генерировать
# исключение командой:
# raise ValueError('операции возможны только с матрицами равных размеров')
# Пример для понимания использования индексов (эти строчки в программе писать не нужно):
# mt = Matrix([[1, 2], [3, 4]])
# res = mt[0, 0] # 1
# res = mt[0, 1] # 2
# res = mt[1, 0] # 3
# res = mt[1, 1] # 4
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
import numpy as np


class Matrix:
    def __init__(self, *args):
        if len(args) == 3:
            self.rows, self.cols, self.fill_value = self.check_args(*args)
            self.list2D = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.list2D = self.check_lst(*args)
            self.rows, self.cols = len(self.list2D), len(self.list2D[0])
        self.matrix = np.array(self.list2D)

    def __len__(self):
        return len(self.list2D)

    def __getitem__(self, item):
        self.check_index(item)
        row, col = item
        return self.list2D[row][col]

    def __setitem__(self, key, value):
        self.check_index(key)
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        row, col = key
        self.list2D[row][col] = value

    def check_index(self, index):
        row, col = index
        r = list(range(self.rows))
        c = list(range(self.cols))
        if row not in r or col not in c:
            raise IndexError('недопустимые значения индексов')

    @staticmethod
    def check_lst(*args):
        check_nums = all(1 if isinstance(el, (int, float)) else 0 for row in args[0] for el in row)
        for row in range(1, len(args[0])):
            if len(args[0][row - 1]) != len(args[0][row]) or not check_nums:
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
        return args[0]

    @staticmethod
    def check_args(*args):
        rows, cols, fill_value = args
        if isinstance(rows, int) and isinstance(cols, int) and isinstance(fill_value, (int, float)):
            return rows, cols, fill_value
        raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

    @staticmethod
    def check_equal_matrix(m1, m2):
        if not (m1.rows == m2.rows and m1.cols == m2.cols):
            raise ValueError('операции возможны только с матрицами равных размеров')

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Matrix((self.matrix + other).tolist())
        elif isinstance(other, Matrix):
            self.check_equal_matrix(self, other)
            return Matrix((self.matrix + other.matrix).tolist())

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix((self.matrix - other).tolist())
        elif isinstance(other, Matrix):
            self.check_equal_matrix(self, other)
            return Matrix((self.matrix - other.matrix).tolist())


# matrix = Matrix(4, 5, 0)
# print(matrix)
# res = matrix[0, 0]
# print(res)
# matrix[0, 0] = 235
# print(matrix)
# print(len(matrix))

list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

try:
    v = matrix['0', 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1], [1, 1]])

try:
    matrix = m1 + m2
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == 1, "некорректно отработал оператор -"
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"


# class Matrix:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.rows, self.cols, self.fill_value = self.check_args(*args)
#             self.list2D = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
#         else:
#             self.list2D = self.check_lst(*args)
#             self.rows, self.cols = len(self.list2D), len(self.list2D[0])
#
#     def __len__(self):
#         return len(self.list2D)
#
#     def __getitem__(self, item):
#         self.check_index(item)
#         row, col = item
#         return self.list2D[row][col]
#
#     def __setitem__(self, key, value):
#         self.check_index(key)
#         if not isinstance(value, (int, float)):
#             raise TypeError('значения матрицы должны быть числами')
#         row, col = key
#         self.list2D[row][col] = value
#
#     def check_index(self, index):
#         row, col = index
#         r = list(range(self.rows))
#         c = list(range(self.cols))
#         if row not in r or col not in c:
#             raise IndexError('недопустимые значения индексов')
#
#     @staticmethod
#     def check_lst(*args):
#         check_nums = all(1 if isinstance(el, (int, float)) else 0 for row in args[0] for el in row)
#         for row in range(1, len(args[0])):
#             if len(args[0][row - 1]) != len(args[0][row]) or not check_nums:
#                 raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#         return args[0]
#
#     @staticmethod
#     def check_args(*args):
#         rows, cols, fill_value = args
#         if isinstance(rows, int) and isinstance(cols, int) and isinstance(fill_value, (int, float)):
#             return rows, cols, fill_value
#         raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#
#     @staticmethod
#     def check_matrix(matrix1, matrix2):
#         if len(matrix1) != len(matrix2):
#             raise ValueError('операции возможны только с матрицами равных размеров')
#         for i in range(len(matrix1)):
#             if len(matrix1.list2D[i]) != len(matrix2.list2D[i]):
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#
#     def __add__(self, other):
#         if isinstance(other, (int, float)):
#             return Matrix([[el + other for el in row] for row in self.list2D])
#         elif isinstance(other, Matrix):
#             self.check_matrix(self, other)
#             res = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
#             for i in range(self.rows):
#                 for j in range(self.cols):
#                     res[i][j] = self.list2D[i][j] + other.list2D[i][j]
#             return Matrix(res)
#
#     def __sub__(self, other):
#         if isinstance(other, (int, float)):
#             return Matrix([[el - other for el in row] for row in self.list2D])
#         elif isinstance(other, Matrix):
#             self.check_matrix(self, other)
#             res = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
#             for i in range(self.rows):
#                 for j in range(self.cols):
#                     res[i][j] = self.list2D[i][j] - other.list2D[i][j]
#             return Matrix(res)