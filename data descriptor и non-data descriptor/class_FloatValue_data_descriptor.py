class FloatValue:  # data descriptor
    @classmethod
    def verify_num(cls, num):  # проверяем чтобы num было float числом
        if type(num) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = "_" + name  # В этом методе мы формируем локальное свойство с именем атрибута, добавляя
        # перед ним одно нижнее подчеркивание (так принято делать при определении дескрипторов)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)  # Так будет правильнее, с точки зрения Python, чем обращение напрямую к
        # специальной коллекции __dict__.

    def __set__(self, instance, value):
        self.verify_num(value)  # проверяем чтобы value было float числом
        setattr(instance, self.name, value)  # Так будет правильнее, с точки зрения Python, чем обращение напрямую к
        # специальной коллекции __dict__.


class Cell:
    value = FloatValue()  # создаем атрибут 'value' как объект класса FloatValue

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]


table = TableSheet(5, 3)
count = 1
for i in range(table.N):
    for j in range(table.M):
        table.cells[i][j] = Cell(float(count))
        count += 1
