# Подвиг 8. Вы несколько раз уже делали стек-подобную структуру, когда объекты последовательно
# связаны между собой:
# Доведем ее функционал до конца. Для этого, по прежнему, нужно объявить классы:
# Stack - для представления стека в целом;
# StackObj - для представления отдельных объектов стека.
# В классе Stack должны быть методы:
# push_back(obj) - для добавления нового объекта obj в конец стека;
# push_front(obj) - для добавления нового объекта obj в начало стека.
# В каждом объекте класса Stack должен быть публичный атрибут:
# top - ссылка на первый объект стека (при пустом стеке top = None).
# Объекты класса StackObj создаются командой:
# obj = StackObj(data)
# где data - данные, хранящиеся в объекте стека (строка).
# Также в каждом объекте класса StackObj должны быть публичные атрибуты:
# data - ссылка на данные объекта;
# next - ссылка на следующий объект стека (если его нет, то next = None).
# Наконец, с объектами класса Stack должны выполняться следующие команды:
# st = Stack()
# st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет
# начинается с нуля
# data = st[indx]  # получение данных из объекта стека по индексу
# n = len(st) # получение общего числа объектов стека
# for obj in st: # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль
# При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до
# N-1, где N - число объектов в стеке. Иначе, генерировать исключение командой:
# raise IndexError('неверный индекс')
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


def check_index(func):
    def wrapper(instance, index):
        if isinstance(index, int) and 0 <= index < len(instance):
            return func(instance, index)
        raise IndexError('неверный индекс')

    return wrapper


class StackObj:
    def __init__(self, data: str):
        self.data = data
        self.next = None


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

    def push_front(self, obj):
        if self.top is None:
            self.top = obj
        else:
            obj.next = self.top
            self.top = obj

    @check_index
    def get_obj_by_index(self, index):
        pointer = self.top
        for _ in range(index):
            pointer = pointer.next
        return pointer

    def __getitem__(self, index):
        return self.get_obj_by_index(index).data

    def __setitem__(self, index, value):
        self.get_obj_by_index(index).data = value

    def __len__(self):
        return sum(1 for _ in self)

    def __iter__(self):
        pointer = self.top
        while pointer:
            yield pointer
            pointer = pointer.next


# st = Stack()
# st.push_back(StackObj("1"))
# st.push_front(StackObj("2"))
# st.push_back(StackObj("3"))
# st.push_back(StackObj("4"))
# print(len(st))
# for obj in st:
#     print(obj.data)

st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"