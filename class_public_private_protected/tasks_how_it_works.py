class Clock:
    MIN_TIME = 0  # атрибут класса
    MAX_TIME = 100_000  # атрибут класса

    def __init__(self, time):  # Инициал. лок. св-ва экз. класса
        self.set_time(time)  # через сеттер set_time устанавливаем лок. св-ва экз. класса

    def set_time(self, tm):  # сеттер set_time. устанавливает лок. св-ва экз. класса
        if self.__check_time(tm):  # обращение к приватному методу для проверки корректности ввода данных
            self.__time = tm  # Если метод вернет True то устанавливаем приватное лок. св-ва экз. класса

    def get_time(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__time

    @classmethod
    def __check_time(cls, tm):  # метод проверяет корректность ввода данных
        return type(tm) == int and cls.MIN_TIME <= tm < cls.MAX_TIME  # Если целое число и от 0 до 100_000 вернет True


clock = Clock(4530)


#######################################################################################################################
class Money:

    def __init__(self, money):  # Инициал. лок. св-ва экз. класса
        self.set_money(money)  # через сеттер set_money устанавливаем лок. св-ва экз. класса

    def set_money(self, money):  # сеттер set_money. устанавливает лок. св-ва экз. класса
        if self.__check_money(money):  # обращение к приватному методу для проверки корректности ввода данных
            self.__money = money  # Если метод вернет True то устанавливаем приватное лок. св-ва экз. класса

    def get_money(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__money

    def add_money(self, mn):  # метод добавляет к текущему лок. св-ву экз. класса средства от объекта mn.__money
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money):  # метод проверяет корректность ввода данных
        return type(money) == int and money >= 0  # Если целое число и money больше либо равно 0 то вернет True


# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()  # 100
# m2 = mn_2.get_money()  # 120
# print(m1, m2)
#######################################################################################################################
class Book:
    def __init__(self, author, title, price):  # Инициал. лок. св-ва экз. класса
        self.set_author(author)  # через сеттер set_author устанавливаем лок. св-ва экз. класса
        self.set_title(title)    # через сеттер set_title устанавливаем лок. св-ва экз. класса
        self.set_price(price)    # через сеттер set_price устанавливаем лок. св-ва экз. класса

    def set_author(self, author):    # через сеттер set_author устанавливаем лок. св-ва экз. класса
        self.__author = author

    def set_title(self, title):  # через сеттер set_title устанавливаем лок. св-ва экз. класса
        self.__title = title

    def set_price(self, price):    # через сеттер set_price устанавливаем лок. св-ва экз. класса
        self.__price = price

    def get_author(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__author

    def get_title(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__title

    def get_price(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__price
#######################################################################################################################
class Line:

    def __init__(self, x1, y1, x2, y2):  # Инициал. лок. св-ва экз. класса
        self.set_coords(x1, y1, x2, y2)  # через сеттер set_coords устанавливаем лок. св-ва экз. класса

    def set_coords(self, x1, y1, x2, y2):    # через сеттер set_coords устанавливаем приватные лок. св-ва экз. класса
        self.__x1 = x1  # устанавливаем приватные лок. св-ва экз. класса
        self.__y1 = y1  # устанавливаем приватные лок. св-ва экз. класса
        self.__x2 = x2  # устанавливаем приватные лок. св-ва экз. класса
        self.__y2 = y2  # устанавливаем приватные лок. св-ва экз. класса

    def get_coords(self):  # геттер. Возвращает приватное лок. св-во экз. класса в виде кортежа
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):  # метод выводит на печать лок. св-ва экз. класса в виде кортежа
        print(*self.get_coords())
#######################################################################################################################
class Point:

    def __init__(self, x, y):  # Инициал. лок. св-ва экз. класса
        self.set_coord(x, y)  # через сеттер set_coords устанавливаем лок. св-ва экз. класса

    def set_coord(self, x, y):    # через сеттер set_coords устанавливаем приватные лок. св-ва экз. класса
        if self.__check_int_float(x) and self.__check_int_float(y):
            self.__x = x
            self.__y = y

    @staticmethod
    def __check_int_float(x):  # метод проверяет корректность ввода данных
        return type(x) in (int, float)  # Если  число целое или вещественное то вернет True

    def get_coords(self):  # геттер. Возвращает приватное лок. св-во экз. класса в виде кортежа
        return self.__x, self.__y

class Rectangle:

    def __init__(self, x1, y1, x2=None, y2=None):  # Инициал. лок. св-ва экз. класса
        self.__sp = self.__ep = None  # Инициал. приватных лок. св-ва экз. класса. По умолчанию None
        self.set_coords(x1, y1, x2, y2)  # через сеттер set_coords устанавливаем лок. св-ва экз. класса

    def set_coords(self, x1, y1, x2=None, y2=None):    # через сеттер устанавливаем приватные лок. св-ва экз. класса
        if isinstance(x1, Point) and isinstance(y1, Point):  # проверяем если первые 2 аргумента объекты Point то
            self.__sp = x1                                  # инициал. приватные лок. св-ва экз. класса
            self.__ep = y1                                  # инициал. приватные лок. св-ва экз. класса
        else:                   # иначе инициал. приватные лок. св-ва экз. класса создавая объекты Point
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)

    def get_coords(self):  # геттер. Возвращает приватное лок. св-во экз. класса в виде кортежа
        return self.__sp, self.__ep

    def draw(self):  # метод выводит на печать лок. св-ва экз. класса в виде кортежа
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


rect = Rectangle(Point(0, 0), Point(20, 34))
# rect.draw()
#######################################################################################################################
class LinkedList:

    def __init__(self, head=None, tail=None):  # Инициал. лок. св-в экз. класса LinkedList
        self.head = head        # Инициал. лок. св-в экз. класса. По умолчанию None
        self.tail = tail

    def add_obj(self, obj):   # Добавление объекта в связанный список
        """Метод добавляет объект (obj) в связанный список LinkedList"""
        if self.head is None:    # Если лок. св-во self.head == None то нет первого объекта связн. списка и
            self.head = self.tail = obj  # лок. св-во self.head и self.tail будет ссылаться на первый созданный объект
            return  # Конструкция с if self.head is None: отработает всего лишь один раз, когда в связанном списке
                    # нет объектов, а далее self.head будет постоянно ссылается на первый объект связанного списка
        self.tail.set_next(obj)  # self.tail ссылается на послед. объект св. списка. Мы его лок. св-ву self.__next
                                 # установим ссылку на новый объект obj.
        obj.set_prev(self.tail)  # установим новому объекту obj его лок. св-во self.__prev. ссылка на предыдущ. obj
        self.tail = obj          # self.tail установим ссылку на новый obj. Он теперь последний объект связн. списка

    def remove_last_obj(self):  # удаление последнего объекта связ. списка
        """Удаляет последний объект связанного списка"""
        if self.head.get_next() is None:  # смотрим куда ссылается первый объект связн. списка. Если на None то в связн.
            self.head = self.tail = None  # списке только 1 объект. лок. св-вам делаем ссылку на None. Таким образом
            return                        # на 1 объект нет ни одной ссылки. Выходим из метода return
        self.tail = self.tail.get_prev()  # лок. св-ву self.tail указываем ссылку на предыдущий объект связн. списка.
        self.tail.set_next(None)          # теперь self.tail ссылается на предыдущий объект связ. списка.
                                    # предыдущему объекту связн. списка лок. св-ву self.__next устан. ссылку на None
                                    # на посл. объект связ. списка нет ни одной ссылки и он удалится сборщ. мусора

    def get_data(self):    # Вывод всех данных связанного списка
        """Возвращает все данные связанного списка """
        cur_obj = self.head   # Так как у нас уже создан связанный список то лок. св-во self.head  ВСЕГДА ссылается
                            # на первый объект связ. списка. Если связ. список пуст то self.head = None и
                            # метод show_data(self) ничего не выведет. Текущ. указат. cur_obj указыв. на первый объект
        out_data = []       # создаем пустой список out_data для добавления туда данных объектов связ. списка.
        while cur_obj:     # Проверяем текущ. объект связ. списка. Если != None то добавляем данные в список out_data
            out_data.append(cur_obj.get_data())    # добавляем данные текущ. объкта в out_data через метод get_data()
            cur_obj = cur_obj.get_next()  # Переопределяем ссылку с текущего обекта на следующий объект связ. списка
        return out_data                 # возвращает данные связ. списка в списке out_data

class ObjList:
    def __init__(self, data):  # Инициал. лок. св-в экз. класса ObjList
        self.__next = self.__prev = None        # Инициал. лок. св-в экз. класса. По умолчанию None
        self.set_data(data)        # Инициал. лок. св-ва экз. класса.

    def set_next(self, obj):    # через сеттер set_next устанавливаем приватные лок. св-ва экз. класса
        self.__next = obj

    def set_prev(self, obj):    # через сеттер set_prev устанавливаем приватные лок. св-ва экз. класса
        self.__prev = obj

    def set_data(self, data):    # через сеттер set_data устанавливаем приватные лок. св-ва экз. класса
        self.__data = data

    def get_next(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__next

    def get_prev(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__prev

    def get_data(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__data

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.remove_last_obj()
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)