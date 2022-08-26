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


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 1, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
for p in shop.goods:
    print(p.__dict__)
##################################################################################################


