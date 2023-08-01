# Ранее, в одном из подвигов мы с вами создавали односвязный список с объектами
# класса StackObj (когда один объект ссылается на следующий и так далее):
# Давайте снова создадим такую структуру данных. Для этого объявим два класса:
# Stack - для управления односвязным списком в целом;
# StackObj - для представления отдельных объектов в односвязным списком.
# Объекты класса StackObj должны создаваться командой:
# obj = StackObj(data)
# где data - строка с некоторыми данными.
# Каждый объект класса StackObj должен иметь локальные приватные атрибуты:
# __data - ссылка на строку с переданными данными;
# __next - ссылка на следующий объект односвязного списка (если следующего нет, то __next = None).
# Объекты класса Stack создаются командой:
# st = Stack()
# и каждый из них должен содержать локальный атрибут:
# top - ссылка на первый объект односвязного списка (если объектов нет, то top = None).
# Также в классе Stack следует объявить следующие методы:
# push_back(self, obj) - добавление объекта класса StackObj в конец односвязного списка;
# pop_back(self) - удаление последнего объекта из односвязного списка.
# Дополнительно нужно реализовать следующий функционал (в этих операциях копии односвязного
# списка создавать не нужно):
# # добавление нового объекта класса StackObj в конец односвязного списка st
# st = st + obj
# st += obj
# # добавление нескольких объектов в конец односвязного списка
# st = st * ['data_1', 'data_2', ..., 'data_N']
# st *= ['data_1', 'data_2', ..., 'data_N']
# В последних двух строчках должны автоматически создаваться N объектов класса StackObj с
# данными, взятыми из списка (каждый элемент списка для очередного добавляемого объекта).
# P.S. В программе достаточно только объявить классы. На экран ничего выводить не нужно.


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        """Adds the object in the end of the linked list"""
        if self.top is None:
            self.top = obj
        else:
            pointer = self.top
            while pointer.next:
                pointer = pointer.next
            pointer.next = obj

    def pop_back(self):
        """Deletes the latest object from linked list"""
        if self.top.next is None:
            self.top = None
        else:
            pointer = self.top
            while pointer.next.next:
                pointer = pointer.next
            pointer.next = None

    def show(self):
        pointer = self.top
        lst = []
        while pointer:
            lst.append(pointer.data)
            pointer = pointer.next
        return lst

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other: list):
        for el in other:
            self.push_back(StackObj(el))
        return self

    def __imul__(self, other):
        for el in other:
            self.push_back(StackObj(el))
        return self


# st = Stack()
# data_1 = StackObj("data_1")
# data_2 = StackObj("data_2")
# data_3 = StackObj("data_3")
# st.push_back(data_1)
# st.push_back(data_2)
# st.push_back(data_3)
# print(st.show())
# obj_1 = StackObj("obj_1")
# st = st + obj_1
# print(st.show())
# obj_2 = StackObj("obj_2")
# st += obj_2
# print(st.show())
# st = st * ['__mul___1', '__mul___2', '__mul___N']
# print(st.show())
# st *= ['__imul___1', '__imul___2', '__imul___N']
# print(st.show())

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"






