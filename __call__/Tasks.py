from random import randint, choice  # функции для генерации целых случ. знач.


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):  # Инициал. лок. св-тв экз. класса
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
        """При вызове экз. класса с () будет случ. образом генер. последов. из psw_chars в
        диапазоне [min_length:max_length]"""
        number = randint(self.min_length, self.max_length)  # выбираем случ. число из диапазона
        return ''.join(choice(self.psw_chars) for _ in range(number))  # возвр. сгенер. пароль


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)  # созд. объект класса

lst_pass = [rnd() for _ in range(3)]    # созд. список из функтров=(пароли) экз. rnd
# print(lst_pass)
###################################################################################################


class ImageFileAcceptor:
    def __init__(self, extensions):     # Инициал. лок. св-тв экз. класса
        self.__extensions = extensions  # Инициал. лок. св-тв экз. класса

    def __call__(self, file, *args, **kwargs):    # изм. поведение для функторов экз. класса
        return file.split('.')[-1] in self.__extensions  # Вернет True если переданный пар-тр
        # на вход функтура (например acceptor("boat.jpg")) после точки входит в перечень
        # допустимых расширений self.__extensions


# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg",
#              "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]  # Спис. для фильтра
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))    # Создаем в объекте лок. св-во с
# # разрешенными расширениями.
#
# image_filenames = filter(acceptor, filenames)   # Записываем в переменную истинные значения.
# # Используем станд. функцию filter. Вызывая функтор acceptor() и поочередно передавая значения
# # последовательности filenames. Отфильтрует корректные значения.
#
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"
###################################################################################################


