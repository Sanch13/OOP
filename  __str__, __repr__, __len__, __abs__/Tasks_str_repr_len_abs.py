# import sys
#
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f'Книга: {self.title}; {self.author}; {self.pages}'
#
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# book = Book(*lst_in)
# print(book)
###################################################################################################
# class Model:
#     def __init__(self):
#         self.id = self.fio = self.old = None
#
#     def query(self, id, fio, old):
#         self.id = id
#         self.fio = fio
#         self.old = old
#
#     def __str__(self):
#         if self.id is None:
#             return f"Model"
#         return f'Model: id = {self.id}, fio = {self.fio}, old = {self.old}'
#
#
# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)
# model_1= Model()
# print(model_1)
###################################################################################################
# class Model:
#     def query(self, **kwargs):
#         self.__dict__ = kwargs
#
#     def __str__(self):
#         if len(self.__dict__) == 0:
#             return f"Model"
#         return f'Model: ' + ', '.join(f'{k} = {v}' for k, v in self.__dict__.items())
#
#
# model = Model()
# model.query(id=1, fio='Sergey', old=33)
# print(model)
# model_1 = Model()
# print(model_1)
###################################################################################################
# class WordString:
#     def __init__(self, string=''):
#         self.string = string
#
#     def __call__(self, indx):
#         return self.words(indx)
#
#     def __len__(self):
#         """Позволяет применять функцию len() к экземплярам класса"""
#         return len(self.__list)
#
#     @property
#     def string(self):
#         return self.__string
#
#     @string.setter
#     def string(self, value):
#         self.__string = value
#         self.__list = value.split()
#
#     def words(self, indx):
#         """должно возвращаться слово по его индексу
#         (indx - порядковый номер слова в строке, начиная с 0)."""
#         return self.__list[indx]
#
#
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
###################################################################################################
# class ObjList:
#     def __init__(self, data: str):
#         self.data = data
#         self.prev = self.next = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, value):
#         self.__data = value
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, value):
#         self.__prev = value
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, value):
#         self.__next = value
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None
#
#     def __call__(self, indx, *args, **kwargs):
#         return self.get_data_for_index(indx)
#
#     def add_obj(self, obj):
#         """Добавляет новый объект obj в конец связного списка"""
#         if self.head is None:                   # Если self.head ссылается на None то
#             self.head = self.tail = obj         # связ. список пустой. Указ. ссылки на obj и
#             return                              # выходим из метода.
#         self.tail.next = obj                    # Во всех других случаях: Указ. tail.next на нов.
#         obj.prev = self.tail                    # obj. obj.prev указвыаем на self.tail. И
#         self.tail = obj                         # двигаем self.tail на последний obj
#
#     def remove_obj(self, indx):
#         """Удаляет объект из связного списка по его порядковому номеру (индексу)"""
#         pointer = self.head                     # Устан. указ. pointer на начало связн. списка
#         if indx == 0:                           # Если удаляемый индекс равен 0 то
#             if pointer is None:                 # Если pointer указ. на None то связ. список пуст
#                 return                          # Выходим из метода.
#             if pointer.next is None:            # Если pointer.next указ. на None то в связ. сп.
#                 self.head = self.tail = None    # только 1 obj. Указ. ссылки на None
#                 return                          # Выходим из метода.
#             pointer.next.prev = None            # Иначе 2 obj лок. св-ву prev указ. ссылку на None
#             self.head = pointer.next            # self.head указываем на 2 obj связ. списка
#             return                              # Выходим из метода.
#         count = 0
#         while pointer:
#             if count == indx:                   # если count == удал. индексу то:
#                 if pointer.next is None:        # след. obj ссылается на None (явл. ли послед.)
#                     self.tail = pointer.prev    # self.tail указ. на предпосл. obj
#                     self.tail.next = None       # предпосл. obj лок. св-ву next указ ссылку на None
#                 else:
#                     pointer.prev.next = pointer.next    # пересвязываем ссылки связ. спсика
#                     pointer.next.prev = pointer.prev    # пересвязываем ссылки связ. спсика
#             pointer = pointer.next              # двигаемся по связ. списку
#             count += 1                          # увелич. счетчик
#
#     def __len__(self):
#         """Возвращает кол-во объектов связанного списка"""
#         pointer = self.head
#         count = 0
#         while pointer:
#             count += 1
#             pointer = pointer.next
#         return count
#
#     def get_data_for_index(self, indx):
#         """Возвращает данные из объекта связанного списка по его индексу"""
#         pointer = self.head
#         while indx != 0:
#             if pointer.next is None:
#                 return None
#             pointer = pointer.next
#             indx -= 1
#         return pointer.data
#
#     def show_data(self):
#         out_data = []
#         pointer = self.head
#         while pointer:
#             out_data.append(pointer.data)
#             pointer = pointer.next
#         return out_data
#
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# print(linked_lst.show_data())           # ['Sergey', 'Balakirev']
# linked_lst.remove_obj(0)                # del Sergey
# print(linked_lst.show_data())           # ['Balakirev']
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.add_obj(ObjList("Java"))
# linked_lst.add_obj(ObjList("GoLang"))
# print(linked_lst.show_data())           # ['Balakirev', 'Python', 'Java', 'GoLang']
# linked_lst.remove_obj(1)                # del Python
# print(linked_lst.show_data())           # ['Balakirev', 'Java', 'GoLang']
# linked_lst.add_obj(ObjList("C++"))
# linked_lst.add_obj(ObjList("JavaScript"))
# print(linked_lst.show_data())           # ['Balakirev', 'Java', 'GoLang', 'C++', 'JavaScript']
# linked_lst.remove_obj(2)                # del GoLang
# print(linked_lst.show_data())           # ['Balakirev', 'Java', 'C++', 'JavaScript']
# n = len(linked_lst)                     # n = 4
# s = linked_lst(3)
# print(s)
#
# ln = LinkedList()
# ln.add_obj(ObjList("Сергей"))
# ln.add_obj(ObjList("Балакирев"))
# ln.add_obj(ObjList("Python ООП"))
# ln.remove_obj(2)
# print(len(ln))
# print(ln.show_data())
# assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
# ln.add_obj(ObjList("Python"))
# assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
###################################################################################################
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#
#     @property
#     def real(self):
#         return self.__real
#
#     @real.setter
#     def real(self, value):
#         self.__check_value(value)
#         self.__real = value
#
#     @property
#     def img(self):
#         return self.__img
#
#     @img.setter
#     def img(self, value):
#         self.__check_value(value)
#         self.__img = value
#
#     @staticmethod
#     def __check_value(value):
#         if not isinstance(value, (int, float)):
#             raise ValueError("Неверный тип данных.")
#
#     def __abs__(self):
#         return (self.real ** 2 + self.img ** 2) ** 0.5
#
#
# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)
# print(c_abs)
###################################################################################################


