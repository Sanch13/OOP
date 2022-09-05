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
class WordString:
    def __init__(self, string=''):
        self.string = string

    def __call__(self, indx):
        return self.words(indx)

    def __len__(self):
        """Позволяет применять функцию len() к экземплярам класса"""
        return len(self.__list)

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value
        self.__list = value.split()

    def words(self, indx):
        """должно возвращаться слово по его индексу
        (indx - порядковый номер слова в строке, начиная с 0)."""
        return self.__list[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")






