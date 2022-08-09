import sys


class StreamData:   # здесь объявляется класс StreamData
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):  # Если кол-во элементов fields и lst_values не равны то return False и
            return False                    # локальные свойства не создадутся
        else:
            self.__dict__ = dict(zip(fields, lst_values))  # локальные свойства экз-ра класса будут создоваться
                                                           # из эл-тов fields и lst_values и устан. в  self.__dict__
            return True  # возвращает True


# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()   # создается экземпляр sd класса StreamData и он ссылается на локальные сво-ва self.__dict__
#         res = sd.create(self.FIELDS, lst_in)    # переменная res ссылается на True либо False
#         return sd, res   # создается кортедж. tuple(sd, res). Возвращает tuple[0] = sd который ссылается
#                          # на локальные сво-ва self.__dict__ экземпляра sd класса StreamData,
#                          # Возвращает tuple[1] = True либо False
#
# sr = StreamReader()   # создается экземпляр sr класса StreamReader
# data, result = sr.readlines()   # Из sr.readlines() вернеться ссылка на кортеж. data будет ссылаться на tuple[0]
#                                 # result будет ссылаться на tuple[1]
#########################################################################################
# import sys
#
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for el in data:
#             self.lst_data.append(dict(zip(self.FIELDS, el.split())))
#
#     def select(self, a, b):
#         return self.lst_data[a:b + 1]
#
#
# db = DataBase()
# db.insert(lst_in)
# print(db.select(0, 2))
#########################################################################################
class Translator:
    def __init__(self):  # Инициализация экземпляра класса Translator
        self.lst = {}  # Инициализация словаря lst экземпляра класса Translator

    def add(self, eng, rus):
        self.lst.setdefault(eng, []).append(rus)  # добавление eng(key) - rus(value). "tree" - "дерево"

    def remove(self, eng):
        del self.lst[eng]  # удаление по ключу eng(key) из лок сво-ва lst[eng] экземпляра класса Translator

    def translate(self, eng):  # возвращение по ключу eng(key) из лок сво-ва lst[eng] экземпляра класса Translator
        return self.lst[eng]


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
# print(*tr.translate('go'))
#########################################################################################
import random
class Figure:
    def __init__(self, a, b, c, d):  # Инициализация экземпляра класса Figure
        self.sp = a, b
        self.ep = c, d

class Line(Figure):  # Класс Line наследует класс Figure
    pass
class Rect(Figure):  # Класс Rect наследует класс Figure
    pass
class Ellipse(Figure):  # Класс Ellipse наследует класс Figure
    pass

def rnd_num():  # Функц. rnd_num возвращает случайное число в пределах 0 - 9
    return random.randint(0, 9)

obj_cls = [Line, Rect, Ellipse]  # Переменная obj_cls ссылается на список экзепляров классов
elements = [random.choice(obj_cls)(rnd_num(), rnd_num(), rnd_num(), rnd_num()) for _ in range(217)]  # создается список
                            # elements из 217 случайных объектов с слуйчайными числами
for obj in elements:
    if isinstance(obj, Line):       # Проверяются все экземляры класса Line
        setattr(obj, 'sp', (0, 0))   # устан. лок. св-ва sp и ep в нули экзмп. класса Line
        setattr(obj, 'ep', (0, 0))




