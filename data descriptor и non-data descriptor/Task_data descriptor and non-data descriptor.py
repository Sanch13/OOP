# class FloatValue:
#
#     @staticmethod
#     def __check_value(value):
#         """Если число не вещественное, то сгенерируется исключение"""
#         if not isinstance(value, float):
#             raise TypeError("Присваивать можно только вещественный тип данных.")
#
#     def __set_name__(self, owner, name):  # В этом методе мы формируем лок. св-во с именем атрибута.
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):  # метод возвращ. знач. лок. св-ва из экз. класса
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.__check_value(value)  # Проверяем чтобы value было веществ. числом.
#         setattr(instance, self.name, value)  # Обращ. к экз. класса и его лок. св-ву уст. знач. value
#
#
# class Cell:
#     value = FloatValue()  # Cоздаем атрибут 'value' как объект класса FloatValue
#
#     def __init__(self, value=0.0):  # Инициал. лок. св-в экз. класса Cell. По умолч. value=0.0
#         self.value = value  # Инициал. лок. св-в экз. класса Cell
#
#
# class TableSheet:
#
#     def __init__(self, N, M):  # Инициал. лок. св-в экз. класса TableSheet.
#         self.N = N  # Инициал. лок. св-в (строка) экз. класса TableSheet.
#         self.M = M  # Инициал. лок. св-в экз. (столбец) класса TableSheet.
#         self.cells = [[Cell() for _ in range(M)] for _ in range(N)]  # Инициал. лок. св-в cells (список сост.
#         # из объектов Cell. По умолчанию список заполняется Cell(value=0.0)).
#
#
# table = TableSheet(5, 3)  # Созд. объект кл. TableSheet. В нем есть лок. св-во cells со списком 5 на 3.
# count = 1  # Уст. счетчик на 1
# for i in range(table.N):  # Проходим по внеш. списку (строка)
#     for j in range(table.M):  # Проходим по внут. списку внеш. списка (столбец)
#         table.cells[i][j] = Cell(float(count))  # Уст. в яч. table.cells объекты Cells с знач. float(count)
#         count += 1  # Увеличиваем счетчик на 1


############################################################################################################


# class ValidateString:
#
#     def __init__(self, min_length=3, max_length=100):  # Инициал. лок. св-в экз. класса по умолч.
#         self.min_length = min_length                   # Инициал. лок. св-в экз. класса ValidateString
#         self.max_length = max_length                   # Инициал. лок. св-в экз. класса ValidateString
#
#     def validate(self, string):
#         """Возвр. True, если string явл. стр. (тип str) и длина стр. в пределах [min_length; max_length]"""
#         return isinstance(string, str) and self.min_length <= len(string) <= self.max_length
#

# class StringValue:
#
#     def __init__(self, validator=ValidateString()):  # Инициал. лок. св-в экз. класса StringValue
#         self.validator = validator  # лок. св-в экз. класса - это ссылка на объект класса ValidateString
#
#     def __set_name__(self, owner, name):    # В этом методе мы формируем лок. св-во с именем атрибута.
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):     # метод возвращ. знач. лок. св-ва из экз. класса
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):     # метод уст. знач. value лок. св-ву экз. класса
#         if self.validator.validate(value):  # Провер. чтобы пар-тр value явл. тип str и был в диапазоне.
#             setattr(instance, self.name, value)  # Обращ. к экз. класса и его лок. св-ву и уст. знач. value.
#
# class RegisterForm:
#     login = StringValue()     # Cозд. атр. 'login' как объект класса StringValue
#     password = StringValue()  # Cозд. атр. 'password' как объект класса StringValue
#     email = StringValue()     # Cозд. атр. 'email' как объект класса StringValue
#
#     def __init__(self, login, password, email):  # Инициал. лок. св-в экз. класса RegisterForm
#         self.login = login        # Инициал. лок. св-в экз. класса RegisterForm
#         self.password = password  # Инициал. лок. св-в экз. класса RegisterForm
#         self.email = email        # Инициал. лок. св-в экз. класса RegisterForm
#
#     def get_fields(self):
#         """Возвращает список из значений полей в порядке [login, password, email]"""
#         return [self.login, self.password, self.email]
#
#     def show(self):
#         """Выводит в консоль многострочную строку в формате"""
#         print('<form>', \
#               f"Логин: {self.login}", \
#               f"Пароль: {self.password}", \
#               f"Email: {self.email}", \
#               '</form>', sep='\n')


# r = RegisterForm('11111', '1111111', '11111111')
# r.show()
# print(r.get_fields())
# frm = RegisterForm("123", "2345", "sc_lib@list.ru")
# print(frm.get_fields())
############################################################################################################


class Value:

    def __set_name__(self, owner, name):  # В этом методе мы формируем лок. св-во с именем атрибута.
        self.name = '_' + name

    def __get__(self, instance, owner):  # метод возвращ. знач. лок. св-ва из экз. класса
        return getattr(instance, self.name)


class StringValue(Value):  # Наследуемся у класса Value

    def __init__(self, min_length=1, max_length=51):  # Инит. по умолчанию
        self.min_length = min_length
        self.max_length = max_length

    def __check_value(self, value):
        """Вернет True если value тип str с длиной строки в диапазоне [2; 50]"""
        return isinstance(value, str) and self.min_length < len(value) < self.max_length

    def __set__(self, instance, value):  # метод уст. знач. value лок. св-ву экз. класса
        if not self.__check_value(
                value):  # Провер. чтобы пар-тр value явл. тип str и был в диапазоне.
            return  # Выйдем из метода если value не удолетв. условию.
        setattr(instance, self.name,
                value)  # Обращ. к экз. класса и его лок. св-ву и уст. знач. value.


class PriceValue(Value):  # Наследуемся у класса Value

    def __init__(self, max_value=10_000):  # Инит. по умолчанию
        self.max_value = max_value

    def __check_value(self, value):
        """Вернет True если value тип int или float и находится в диапазоне [0; 10_000]"""
        return isinstance(value, (float, int)) and 0 <= value <= self.max_value

    def __set__(self, instance, value):  # метод уст. знач. value лок. св-ву экз. класса
        if not self.__check_value(
                value):  # Провер. чтобы пар-тр value явл. тип str и был в диапазоне.
            return  # Выйдем из метода если value не удолетв. условию.
        setattr(instance, self.name,
                value)  # Обращ. к экз. класса и его лок. св-ву и уст. знач. value.


class Product:
    name = StringValue()  # Cозд. атр. 'name' как объект класса Product
    price = PriceValue()  # Cозд. атр. 'price' как объект класса Product

    def __init__(self, name, price):  # Инициал. лок. св-в экз. класса Product
        self.name = name
        self.price = price


class SuperShop:

    def __init__(self, name):  # Инициал. лок. св-в экз. класса SuperShop
        self.name = name
        self.goods = []

    def add_product(self, product):
        """Добавление товара product в магазин (в конец списка goods)"""
        return self.goods.append(product)

    def remove_product(self, product):
        """Удаление товара из магазина (из списка goods)"""
        if product in self.goods:
            self.goods.remove(product)


# shop = SuperShop("У Балакирева")
# shop.add_product(Product("Mark", 100))
# shop.add_product(Product("name", 10_000))
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")
############################################################################################################


class Bag:

    def __init__(self, max_weight):  # Инициал. лок. св-в экз. класса Bag
        self.max_weight = max_weight
        self.__things = []

    @property  # объект св-во
    def things(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__things

    def add_thing(self, thing):
        """Добавление нового предмета в рюкзак"""
        if thing.weight + self.get_total_weight() <= self.max_weight:  # Если общ. масса вещей не превыш.
            self.__things.append(thing)  # макс. знач. то доб. вещь в список

    def remove_thing(self, indx):
        """Удаление предмета по индексу списка"""
        if indx <= len(
                self.things):  # если indx (число) не больше или равно кол-ву объектов списка то
            self.__things.remove(indx)  # удаляем объект из списка по указанному indx

    def get_total_weight(self):
        """Возвращает суммарный вес предметов в рюкзаке"""
        return sum(
            obj.weight for obj in self.things)  # прох. по списку вещей и возвр. общую массу вещей


class Thing:

    def __init__(self, name, weight):  # Инициал. лок. св-в экз. класса Bag
        if not self.__check_value_str(name):  # Проверка, что name строка
            raise ValueError("некорректное значение name")  # Если name не строка просто выходим
        self.name = name  # Инициал. лок. св-в экз. класса
        if not self.__check_value(weight):  # Пров., что weight явл. (int, float)). Если
            raise ValueError(
                "некорректное значение weight")  # weight не явл. (int, float)) просто выходим
        self.weight = weight  # Инициал. лок. св-в экз. класса

    @staticmethod
    def __check_value_str(value):
        """Вернет True если value тип str"""
        return isinstance(value, str)

    @staticmethod
    def __check_value(value):
        """Вернет True если value тип int или float"""
        return isinstance(value, (int, float))


# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# bag.add_thing(Thing("Палатка", 280))
# w = bag.get_total_weight()
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")
###################################################################################################


class TVProgram:

    def __init__(self, name):  # Инициал. лок. св-в экз. класса TVProgram
        self.name = name
        self.items = []

    def add_telecast(self, tl):
        """Добавление новой телепередачи в список self.items"""
        self.items.append(tl)

    def remove_telecast(self, indx):
        """ удаление телепередачи по ее порядковому номеру (атрибуту __id)"""
        for obj in self.items:   # Проходим по списку self.items (это объекты класса Telecast)
            if obj.uid == indx:  # У кажд. obj выз. объект св-во uid и сравн. с передан. знач. indx
                self.items.remove(obj)  # Если obj.uid == indx удаляем obj из self.items
                break

class Telecast:

    def __init__(self, uid, name, duration):  # Инициал. лок. св-в экз. класса Telecast
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property  # объект св-во
    def uid(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__id

    @uid.setter
    def uid(self, value):  # сеттер. Уст. приватное лок. св-во экз. класса
        self.__id = value

    @property  # объект св-во
    def name(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__name

    @name.setter
    def name(self, value):  # сеттер. Уст. приватное лок. св-во экз. класса
        self.__name = value

    @property  # объект св-во
    def duration(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__duration

    @duration.setter
    def duration(self, value):  # сеттер. Уст. приватное лок. св-во экз. класса
        self.__duration = value


pr = TVProgram("Первый канал")
pr.add_telecast(Telecast(1, "Доброе утро", 10000))
pr.add_telecast(Telecast(2, "Новости", 2000))
pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
pr.remove_telecast(3)
# for t in pr.items:
#     print(f"{t.name}: {t.duration}")
###################################################################################################
# self.items.remove(list(filter(lambda obj: obj.uid == indx, self.items))[0])


numbers = [1, 2, 4, 5, 7, 8, 10, 11]  # список чисел


def filter_odd_num(in_num):  # метод вернет True если число in_num четное
    return in_num % 2 == 0


out_filter = filter(filter_odd_num, numbers)  # Применяем фильтр. Первый пар-тр польз. функц.
                                              # второй пар-тр последовательность numbers

# print("Тип объекта out_filter: ", type(out_filter))  # Тип объекта out_filter:  <class 'filter'>
# print("Отфильтрованный список: ", list(out_filter))  # Отфильтрованный список:  [2, 4, 8, 10]
###################################################################################################
