class Point:
    color = "Red"
    circle = 2


a = Point()
b = Point()
# print(id(a.color) == id(b.color), a.color, b.color)  # True Red Red. Ссылаються на атрибут color класса Point
# Point.color = 'Grey'  # Изменяем атрибут color класса Point
#
# print(id(a.color) == id(b.color), a.color, b.color)  # True Grey Grey. Атрибут color класса Point изменен на Grey
# b.color = 'Green'  # Изменяем локальное свойство color экземпляра b класса Point
#
# print(Point.__dict__)  # {'color': 'Grey', 'circle': 2 and other param}
# print(id(a.color) == id(b.color), a.color, b.color)  # False Grey Green. a ссылается на на атрибут color класса Point
#                                                      # b ссылается на локальное свойство color экземпляра b класса Point
#########################################################################################
class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024
# setattr(Goods, "price", 2048)
# Goods.price = 2048
# setattr(Goods, "inflation", 100)
# Goods.inflation = 100
# print(Goods.__dict__)
#########################################################################################
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

# print(getattr(Notes, "author"))
#########################################################################################
class TravelBlog:
    total_blogs = 0


tb1 = TravelBlog()
tb1.name = "Франция"
tb1.days = 6
TravelBlog.total_blogs += 1
tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5
TravelBlog.total_blogs += 1
#########################################################################################
class Figure:
    type_fig = 'ellipse'
    color = 'red'


fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
delattr(fig1, 'color')

# for key in fig1.__dict__:
#     print(key, end=' ')
#########################################################################################
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
# print(True if p1.__dict__.get("job") else False)
# print('job' in p1.__dict__)
#########################################################################################
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
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Line(Figure):
    pass
class Rect(Figure):
    pass
class Ellipse(Figure):
    pass
def rnd_num():
    return random.randint(0, 9)


obj_cls = [Line, Rect, Ellipse]
elements = [random.choice(obj_cls)(rnd_num(), rnd_num(), rnd_num(), rnd_num()) for _ in range(217)]
for obj in elements:
    if isinstance(obj, Line):
        setattr(obj, 'sp', (0, 0))
        setattr(obj, 'ep', (0, 0))




