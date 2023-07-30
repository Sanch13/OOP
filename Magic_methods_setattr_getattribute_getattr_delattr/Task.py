class Book:
    def __init__(self, title='', author='', pages=0, year=0):  # Инициал. лок. св-в экз. кл. Book
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):  # Автомат. вызыв. при присваивании атрибуту нового знач.
        if key in ('title', 'author') and not isinstance(value, str):  # проверяем условие
            raise TypeError("Неверный тип присваиваемых данных.")  # вывод в консоль исключ.

        if key in ('pages', 'year') and not isinstance(value, int):  # проверяем условие
            raise TypeError("Неверный тип присваиваемых данных.")  # вывод в консоль исключ.

        super().__setattr__(key, value)  # вызов базового класса с передачей параметров


# book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
##################################################################################################


class Shop:
    def __init__(self, name):  # Инициал. лок. св-в экз. кл. Shop
        self.name = name  # Инициал. лок. св-в экз. кл. Shop.
        self.goods = []  # У кажд. экз. кл..будет свой список

    def add_product(self, product):
        """Добавление нового товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """Удаление товара product из магазина (из списка goods)"""
        if product in self.goods:
            self.goods.remove(product)


class Product:
    count_id = 0  # Атрибут кл. Product. Будем его использовать для счета экз. класса

    def __new__(cls, *args, **kwargs):  # Переопр. маг. метод чтобы созд. уник. id экз. класса
        instance = super().__new__(cls)  # Созд. ссылку на нов. экз. класса
        cls.count_id += 1  # Увел. атр. клс. на 1
        instance.id = cls.count_id  # Через ссылку в экз. класса созд. атр. id и уст. знач.

        return instance  # Вернем ссылку на базовый класс

    def __init__(self, name: str, weight: int, price: int):  # Инициал. лок. св-в экз. кл. Product
        self.name = name  # Инициал. лок. св-в экз. кл. Product
        self.weight = weight  # Инициал. лок. св-в экз. кл. Product
        self.price = price  # Инициал. лок. св-в экз. кл. Product

    def __setattr__(self, key, value):  # Автомат. вызыв. при присваивании атрибуту нового знач.
        if key == 'name' and not isinstance(value, str):  # проверяем условие
            raise TypeError("Неверный тип присваиваемых данных.")  # вывод в консоль исключ.

        if key in ('weight', 'price'):  # проверяем условие, что key явл. одним из знач.
            if isinstance(value, (int, float)) and value <= 0:  # проверяем условие
                raise TypeError("Неверный тип присваиваемых данных.")  # вывод в консоль исключ.

        super().__setattr__(key, value)  # вызов базового класса с передачей параметров

    def __delattr__(self, item):  # Автомат. вызыв. при удалении атрибута item
        """Метод __delattr__ вызывается в момент удаления какого-либо атрибута из экземпляра
        класса"""
        if item == 'id':  # Если удаляемый атр. item == 'id' то выводим исключ.
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)  # вызов баз. класса с передачей пар-ров для удал. его
        # из коллекции


# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 1, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")
# for p in shop.goods:
#     print(p.__dict__)
##################################################################################################


class LessonItem:
    attr = {'title': str, 'practices': int, 'duration': int}

    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    @classmethod
    def check_key_value(cls, key, value) -> bool:
        if cls.attr[key] is not type(value):
            return True
        elif isinstance(value, int) and value < 0:
            return True
        return False

    def __setattr__(self, key, value):  # Автомат. вызыв. при присваивании атрибуту нового знач.
        if self.check_key_value(key, value):
            raise TypeError("Неверный тип присваиваемых данных.")
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.attr.keys():
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        object.__delattr__(self, item)


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if indx <= len(self.lessons):
            del self.lessons[indx - 1]


class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        if indx <= len(self.modules):
            del self.modules[indx - 1]


# course = Course("Python ООП")
# module_1 = Module("Часть первая")
# module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
# module_1.add_lesson(LessonItem("Урок 3", 5, 800))
# print(module_1.__dict__)
# course.add_module(module_1)
# module_2 = Module("Часть вторая")
# module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
# module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
# course.add_module(module_2)
# module_1.remove_lesson(1)
# print(module_1.__dict__)
##################################################################################################
#
#
# class Picture:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#
# class Mummies:
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#
# class Papyri:
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr
#
#
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
#
#
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
# mus.add_exhibit(p)
# print(mus.__dict__)
# for x in mus.exhibits:
#     print(x.descr)
##################################################################################################


class SmartPhone:

    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        if type(app) not in map(type, self.apps):
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory: int):
        self.name = "YouTube"
        self.memory_max = memory


class AppPhone:
    def __init__(self, phone_list: dict):
        self.name = "Phone"
        self.phone_list = phone_list


# app_1 = AppYouTube(1024)
# app_2 = AppYouTube(1024)
# sm = SmartPhone("Honor 1.0")
# sm.add_app(app_1)
# sm.add_app(app_2)  # второй раз добавляться не должно
# sm.add_app(AppVK())
# sm.add_app(AppVK())
# print(len(sm.apps))
# for a in sm.apps:
#     print(a.name)
##################################################################################################


class Circle:
    def __init__(self, x, y, radius):  # Инициал. лок. св-в экз. кл. Circle
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):  # проверяем value явл. (int, float) и больше 0
        if isinstance(value, (int, float)) and value > 0:
            super().__setattr__(key, value)  # вызов базового класса с передачей параметров
        elif isinstance(value, str):  # проверяем value явл. (str). Вызыв. исключение
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):  # Если в лок. коллекции экз. класса нет item вернем False
        return False


# circle = Circle(10.5, 7, 22)
# print(circle.__dict__)
# circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# print(circle.__dict__)
# x, y = circle.x, circle.y
# res = circle.name # False, т.к. атрибут name не существует
# print(res)
##################################################################################################


class Dimensions:
    MIN_DIMENSION = 9
    MAX_DIMENSION = 1001

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value

    @classmethod
    def check_value(cls, value):
        return cls.MIN_DIMENSION < value < cls.MAX_DIMENSION

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if self.check_value(value):
            super().__setattr__(key, value)


# d = Dimensions(10.5, 20.1, 30)
# print(d.__dict__)
# d.a = 8
# d.b = 15
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(d.__dict__)
# d.MAX_DIMENSION = 10  # исключение AttributeError
##################################################################################################


import time  # Импортируем модуль time для взятия кол-ва числа секунд от начала эпохи


class Filter:                            # Общий (базовый) класс для Mechanical, Aragon, Calcium
    def __init__(self, date: float):     # Общий инициал. для Mechanical, Aragon, Calcium
        self.date = date

    def __setattr__(self, key, value):   # Общий __setattr__. для Mechanical, Aragon, Calcium
        if key not in self.__dict__:
            self.__dict__[key] = value


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MIN_DATE_FILTER = 0      # атрибут класса GeyserClassic. Мин. критерий
    MAX_DATE_FILTER = 100    # атрибут класса GeyserClassic. Мах. критерий
    attr = {1: Mechanical, 2: Aragon, 3: Calcium}    # атрибут класса GeyserClassic.

    def __init__(self):      # Инициал. лок. св-ва экз. класса GeyserClassic
        self.slots = {1: None, 2: None, 3: None}

    @classmethod
    def check_service_life(cls, obj) -> bool:      # Метод вернет True если усл. в диапазоне
        return cls.MIN_DATE_FILTER <= time.time() - obj.date <= cls.MAX_DATE_FILTER

    def add_filter(self, slot_num, filter):  # Метод добавит объект если его нет и он соотв.
        if isinstance(filter, self.attr.get(slot_num)) and not self.slots.get(slot_num):
            self.slots[slot_num] = filter

    def remove_filter(self, slot_num):  # Метод удал. объект по индексу
        self.slots[slot_num] = None

    def get_filters(self):  # Метод возващ. кортеж объектов фильтра
        return tuple(self.slots.values())

    def water_on(self) -> bool:  # Вернет True если условия True))
        if None in self.slots.values():  # Если есть хотя бы один None return False
            return False
        return len(list(filter(self.check_service_life, self.get_filters()))) == 3
        # Проходим по кортежу объектов. Каждый объект попадет в check_service_life. Она вернет
        # True если объект в нужном диапазоне.Если кол-во True == 3, то возвращаем True

my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
print(my_water.slots)
w = my_water.water_on() # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
print(my_water.slots)
w = my_water.water_on() # True
print(w)
my_water.remove_filter(1)
print(my_water.slots)
my_water.add_filter(1, Mechanical(time.time() - 99))
print(my_water.slots)
w = my_water.water_on() # False
print(w)
##################################################################################################
# import time
#
#
# class Filter:
#     def __init__(self, date):
#         self.date = date
#
#     def __setattr__(self, key, value):
#         if self.__dict__.get("date", False):
#             return
#         object.__setattr__(self, key, value)
#
#
# class Mechanical(Filter):
#     pass
#
#
# class Aragon(Filter):
#     pass
#
#
# class Calcium(Filter):
#     pass
#
#
# class GeyserClassic:
#     MAX_DATE_FILTER = 100
#     MIN_DATE_FILTER = 0
#     FILTER = {"Mechanical": 1, "Aragon": 2, "Calcium": 3}
#
#     def __init__(self):
#         self.slots = {1: None, 2: None, 3: None}
#
#     @classmethod
#     def check_filter(cls, slot_num, filter):
#         return slot_num == cls.FILTER.get(filter.__class__.__name__)
#
#     def add_filter(self, slot_num, filter):
#         if self.slots.get(slot_num) is None and self.check_filter(slot_num, filter):
#             self.slots[slot_num] = filter
#
#     def remove_filter(self, slot_num):
#         if self.slots.get(slot_num):
#             self.slots[slot_num] = None
#
#     def get_filters(self):
#         return tuple(self.slots.values())
#
#     def water_on(self):
#         return all(self.slots.values()) and \
#                all(map(self.check_time_value_filter, self.get_value_filter()))
#
#     @classmethod
#     def check_time_value_filter(cls, filter):
#         return cls.MIN_DATE_FILTER <= filter <= cls.MAX_DATE_FILTER
#
#     def get_value_filter(self):
#         return [time.time() - obj.date for obj in self.slots.values()]
