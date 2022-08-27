class Book:
    def __init__(self, title='', author='', pages=0, year=0):  # Инициал. лок. св-в экз. кл. Book
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):  # Автомат. вызыв. при присваивании атрибуту нового знач.
        if key in ('title', 'author') and not isinstance(value, str):   # проверяем условие
            raise TypeError("Неверный тип присваиваемых данных.")   # вывод в консоль исключ.

        if key in ('pages', 'year') and not isinstance(value, int):   # проверяем условие
            raise TypeError("Неверный тип присваиваемых данных.")   # вывод в консоль исключ.

        super().__setattr__(key, value)    # вызов базового класса с передачей параметров


# book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
##################################################################################################


class Shop:
    def __init__(self, name):   # Инициал. лок. св-в экз. кл. Shop
        self.name = name        # Инициал. лок. св-в экз. кл. Shop.
        self. goods = []        # У кажд. экз. кл..будет свой список

    def add_product(self, product):
        """Добавление нового товара в магазин (в конец списка goods)"""
        self.goods.append(product)

    def remove_product(self, product):
        """Удаление товара product из магазина (из списка goods)"""
        if product in self.goods:
            self.goods.remove(product)


class Product:
    count_id = 0  # Атрибут кл. Product. Будем его использовать для счета экз. класса

    def __new__(cls, *args, **kwargs):   # Переопр. маг. метод чтобы созд. уник. id экз. класса
        instance = super().__new__(cls)  # Созд. ссылку на нов. экз. класса
        cls.count_id += 1                # Увел. атр. клс. на 1
        instance.id = cls.count_id       # Через ссылку в экз. класса созд. атр. id и уст. знач.

        return instance                  # Вернем ссылку на базовый класс

    def __init__(self, name: str, weight: int, price: int):  # Инициал. лок. св-в экз. кл. Product
        self.name = name                                     # Инициал. лок. св-в экз. кл. Product
        self.weight = weight                                 # Инициал. лок. св-в экз. кл. Product
        self.price = price                                   # Инициал. лок. св-в экз. кл. Product

    def __setattr__(self, key, value):  # Автомат. вызыв. при присваивании атрибуту нового знач.
        if key == 'name' and not isinstance(value, str):   # проверяем условие
            raise TypeError("Неверный тип присваиваемых данных.")   # вывод в консоль исключ.

        if key in ('weight', 'price'):  # проверяем условие, что key явл. одним из знач.
            if isinstance(value, (int, float)) and value <= 0:  # проверяем условие
                raise TypeError("Неверный тип присваиваемых данных.")   # вывод в консоль исключ.

        super().__setattr__(key, value)    # вызов базового класса с передачей параметров

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


class Picture:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    def __init__(self, name, author, descr):
        self.name = name
        self.author = author
        self.descr = descr


class Papyri:
    def __init__(self, name, date, descr):
        self.name = name
        self.date = date
        self.descr = descr


class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор", "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради", "Древняя Россия", "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
print(mus.__dict__)
for x in mus.exhibits:
    print(x.descr)
##################################################################################################


