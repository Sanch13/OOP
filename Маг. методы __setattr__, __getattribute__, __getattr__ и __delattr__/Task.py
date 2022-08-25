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


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
##################################################################################################
