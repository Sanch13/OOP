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
class ObjList:
    def __init__(self, data: str):
        self.data = data
        self.prev = self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = self.tail = obj
            return
        self.tail.next = obj
        obj.prev = self.tail
        self.tail = obj

    def remove_obj(self, indx):
        pointer = self.head
        if indx == 0:
            if pointer is None:
                return
            if pointer.next is None:
                self.head = self.tail = None
                return
            pointer.next.prev = None
            self.head = pointer.next
            return
        count = 0
        # while pointer:
        #     if count == indx:
        #
        #     pointer = pointer.next
        #     count += 1




    def show_data(self):
        out_data = []
        pointer = self.head
        while pointer:
            out_data.append(pointer.data)
            pointer = pointer.next

        return out_data


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
print(linked_lst.show_data())
linked_lst.remove_obj(0)
linked_lst.add_obj(ObjList("Python"))
print(linked_lst.show_data())



