# Подвиг 7. Теперь, вам необходимо разработать итератор, который бы перебирал указанные
# столбцы двумерного списка. Список представляет собой двумерную таблицу из данных:
# lst = [[x11, x12, ..., x1N],
#        [x21, x22, ..., x2N],
#        ...
#        [xM1, xM2, ..., xMN]
#       ]
# Для этого в программе необходимо объявить класс с именем IterColumn, объекты которого
# создаются командой:
# it = IterColumn(lst, column)
# где lst - ссылка на двумерный список; column - индекс перебираемого столбца (отсчитывается от 0).
# Затем, с объектами класса IterColumn должны быть доступны следующие операции:
# it = IterColumn(lst, 1)
# for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
#     print(x)
# it_iter = iter(it)
# x = next(it_iter)
# P.S. В программе нужно объявить только класс итератора. Выводить на экран ничего не нужно.


class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column
        self.dist = len(self.lst) - 1

    def __iter__(self):
        self.row = -1
        return self

    def __next__(self):
        while self.row != self.dist:
            self.row += 1
            return self.lst[self.row][self.column]
        raise StopIteration


lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

it = IterColumn(lst, 1)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
# print(x)
