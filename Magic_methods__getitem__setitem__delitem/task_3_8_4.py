# Подвиг 6. Ранее вы уже создавали стек-подобную структуру, когда один объект ссылается на
# следующий и так по цепочке до последнего:
# Для этого в программе объявлялись два класса:
# StackObj - для описания объектов стека;
# Stack - для управления стек-подобной структурой.
# И, далее, объекты класса StackObj следовало создавать командой:
# obj = StackObj(data)
# где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса
# StackObj должен иметь следующие локальные атрибуты:
# data - ссылка на строку с данными, указанными при создании объекта;
# next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).
# Класс Stack предполагается использовать следующим образом:
# st = Stack() # создание объекта стек-подобной структуры
# В каждом объекте класса Stack должен быть локальный публичный атрибут:
# top - ссылка на первый объект стека (если стек пуст, то top = None).
# А в самом классе Stack следующие методы:
# push(self, obj) - добавление объекта класса StackObj в конец стека;
# pop(self) - извлечение последнего объекта с его удалением из стека;
# Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по
# его индексу, например:
# obj_top = st[0] # получение первого объекта
# obj = st[4] # получение 5-го объекта стека
# st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый
# Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно
# генерироваться исключение командой:
# raise IndexError('неверный индекс')
# Пример использования классов Stack и StackObj (эти строчки в программе не писать):
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
# res = st[3] # исключение IndexError
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


def check_index(func):
    def wrapper(obj, indx, *args, **kwargs):
        if isinstance(indx, int) and 0 <= indx < len(obj):
            return func(obj, indx, *args, **kwargs)
        raise IndexError('неверный индекс')

    return wrapper


class StackObj:
    def __init__(self, data: str):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        """Adds the object in the end of the linked list"""
        if self.top is None:
            self.top = obj
        else:
            pointer = self.top
            while pointer.next:
                pointer = pointer.next
            pointer.next = obj

    def pop(self):
        """Deletes the latest object from linked list"""
        if self.top.next is None:
            last, self.top = self.top, None
        else:
            pointer = self.top
            while pointer.next.next:
                pointer = pointer.next
            last = pointer.next
            pointer.next = None
        return last

    @check_index
    def get_obj_by_indx(self, indx):
        """Returns an object by index of the linked list"""
        pointer = self.top
        while indx:
            pointer = pointer.next
            indx -= 1
        return pointer

    def __getitem__(self, key):
        return self.get_obj_by_indx(key)

    def __setitem__(self, key, obj):
        if key:
            prev_obj = self.get_obj_by_indx(key - 1)
            obj.next = prev_obj.next.next
            prev_obj.next = obj
        else:
            obj.next = self.top.next
            self.top = obj

    def __len__(self):
        pointer = self.top
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next
        return count


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
print(st[2].data)  # obj13
print(st[1].data)  # obj2-new
# res = st[3] # исключение IndexError


assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
print(obj.data)
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

