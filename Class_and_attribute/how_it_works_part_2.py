import sys


class StreamData:   # здесь объявляется класс StreamData
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):  # Если кол-во элементов fields и lst_values не равны то return False и
            return False                    # локальные свойства не создадутся
        else:
            self.__dict__ = dict(zip(fields, lst_values))  # локальные свойства экз-ра класса будут создоваться
                                                           # из эл-тов fields и lst_values и устан. в  self.__dict__
            return True  # возвращает True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    # def readlines(self):
    #     lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
    #     sd = StreamData()   # создается экземпляр sd класса StreamData и он ссылается на локальные сво-ва self.__dict__
    #     res = sd.create(self.FIELDS, lst_in)    # переменная res ссылается на True либо False
    #     return sd, res   # создается кортедж. tuple(sd, res). Возвращает tuple[0] = sd который ссылается
                         # на локальные сво-ва self.__dict__ экземпляра sd класса StreamData,
                         # Возвращает tuple[1] = True либо False

# sr = StreamReader()   # создается экземпляр sr класса StreamReader
# data, result = sr.readlines()   # Из sr.readlines() вернеться ссылка на кортеж. data будет ссылаться на tuple[0]
#                                 # result будет ссылаться на tuple[1]
#########################################################################################
import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for el in data:
            self.lst_data.append(dict(zip(self.FIELDS, el.split())))

    def select(self, a, b):
        return self.lst_data[a:b + 1]


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
                            # elements из 217 случайных объектов Line, Rect, Ellipse с слуйчайными числами
for obj in elements:
    if isinstance(obj, Line):       # Проверяются все экземляры класса Line
        setattr(obj, 'sp', (0, 0))   # устан. лок. св-ва sp и ep в нули экзмп. класса Line
        setattr(obj, 'ep', (0, 0))
#########################################################################################
class TriangleChecker:  # здесь объявите класс TriangleChecker

    def __init__(self, a, b, c):  # Инициализация экземпляра класса TriangleChecker
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __check_int_float(cls, x):  # Проверка явл. ли х int or float и x >= 0.
        return type(x) in (int, float) and x >= 0  # return True else False


    def is_triangle(self):
        a, b, c = self.a, self.b, self.c  # переопределение лок. св-в для удобства
        if not (self.__check_int_float(a) and self.__check_int_float(b) and self.__check_int_float(c)):
            return 1  # Если числа a, b, c НЕ int or float или x < 0 return 1

        if a + b > c and a + c > b and b + c > a:  # Условие проверки истинности треугольника
            return 3  # Если можно создать треугольник то return 3
        else:
            return 2  # Если не возможно создать треугольник то return 2


# a, b, c = map(int, input().split())  # эту строчку не менять
# tr = TriangleChecker(a, b, c)   # здесь создайте экземпляр tr класса TriangleChecker
# print(tr.is_triangle()) # вызовите метод is_triangle() с выводом информации на экран
# tr1 = TriangleChecker("5", 4, 3)
# print(tr1.__dict__)
# print(tr1.is_triangle())
# tr2 = TriangleChecker(0.8, 4, 3)
# print(tr2.__dict__)
# print(tr2.is_triangle())
#########################################################################################
class Graph:
    def __init__(self, data, is_show=True):  # Инициализация экземпляра класса Graph
        self.data = data.copy()  # Инициализация data экземпляра класса Graph c копированием.
        self.is_show = is_show   # Т.е. экз. класса будет ссылаться на свой индивидуальный data

    def set_data(self, data):   # установка нового списка данных
        self.data = data

    def show_table(self):   # отображения данных в виде строки из списка чисел
        if not self.is_show:
            print(f'Отображение данных закрыто')
        else:
            return ' '.join(str(i) for i in self.data)

    def show_graph(self):   # отображения данных в виде графика. метод выводит в консоль сообщение
        if not self.is_show:
            print(f'Отображение данных закрыто')
        else:
            print(f'Графическое отображение данных: {self.show_table()}')

    def show_bar(self):  # отображения данных в виде столбчатой диаграммы. метод выводит в консоль сообщение
        if not self.is_show:
            print(f'Отображение данных закрыто')
        else:
            print(f'Столбчатая диаграмма: {self.show_table()}')

    def set_show(self, fl_show):  # метод для изменения локального свойства is_show на переданное значение fl_show
        self.is_show = fl_show

# data_graph = list(map(int, input().split()))    # 8 11 10 -32 0 7 18
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show = False)
# gr.show_table()
# data = [1, 2, 3, 4]
# gr2 = Graph(data)
# gr3 = Graph(data)
# gr3.data.append(5)
# print(gr2.__dict__, gr3.__dict__, id(gr2) == id(gr3))
#########################################################################################
class CPU:
    def __init__(self, name, fr):  # Инициализация экземпляра класса CPU
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):  # Инициализация экземпляра класса Memory
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *memory):  # Инициализация экземпляра класса MotherBoard
        self.name = name                     # *memory принимает кортеж объектов класса Memory
        self.cpu = cpu  # здесь будет ссылка на объект класса CPU
        self.total_mem_slots = 4
        self.mem_slots = memory[:self.total_mem_slots]  # в лок. св-ве self.mem_slots устанавливаем ограничение
    # в передаваемом кортеже *memory (объекты класса Memory) срезом по конечному индексу self.total_mem_slots

    def get_config(self):   # Возвращает конфигурацию PC
        return [f'Материнская плата: {self.name}',  # Выводит имя материнской платы
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',   # обращаемся по ссылке cpu к лок.
                                                                # св-ву name и fr класса CPU
                f'Слотов памяти: {self.total_mem_slots}', # вывод лок. св-ва self.total_mem_slots  кол-во
                                                        # слотов памяти MotherBoard
                'Память: ' + '; '.join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))]  # перебираем кортеж
    # self.mem_slots (объекты класса Memory) и через аноним. функц. lambda выводим соответствующим образом
    # лок. знач. name и volume объектов класса Memory

mb = MotherBoard("ASUS", CPU("Intel", 3500), Memory("King", 1600), Memory("Cruser", 3200))
#########################################################################################
class Cart:
    def __init__(self):  # Инициализация экземпляра класса Cart
        self.goods = []  # Каждому экземпляру класса Cart будет создан пустой список

    def add(self, gd):  # Добавление товара gd (объекта какого-ниб. класса) в список экземпляра класса Cart
        self.goods.append(gd)

    def remove(self, indx):  # Удаление товара (объекта) из списока
        del self.goods[indx]    #  экземпляра класса Cart по индексу indx

    def get_list(self):     # вывод лок. св-в объектов (товаров) из списка экземпляра класса Cart
        return [f'{obj.name}: {obj.price}' for obj in self.goods]

class Goods:
    def __init__(self, name, price):  # Общий инициализатор для какого-ниб. товара
        self.name = name
        self.price = price

class Table(Goods): pass    # класс Table наследуется у класса Goods. При создании объектов
                            # класса Table используеться инициализатор класса Goods
class TV(Goods): pass    # класс TV наследуется у класса Goods. При создании объектов
                            # класса TV используеться инициализатор класса Goods
class Notebook(Goods): pass    # класс Notebook наследуется у класса Goods. При создании объектов
                            # класса Notebook используеться инициализатор класса Goods
class Cup(Goods): pass    # класс Cup наследуется у класса Goods. При создании объектов
                            # класса Cup используеться инициализатор класса Goods

cart = Cart()   # Создание объекта cart. Init empty list
cart.add(TV('LG', 500))   # Создание объекта TV и добавление его в список объекта cart
cart.add(TV('Samsung', 1000))   # Создание объекта TV и добавление его в список объекта cart
cart.add(Table('table', 200))   # Создание объекта Table и добавление его в список объекта cart
cart.add(Notebook('Lenovo', 1500))   # Создание объекта Notebook и добавление его в список объекта cart
cart.add(Notebook('Dell', 2500))   # Создание объекта Notebook и добавление его в список объекта cart
cart.add(Cup('Tea', 30))   # Создание объекта Cup и добавление его в список объекта cart
#########################################################################################



