class Factory:

    @staticmethod
    def build_sequence():   # метод возвращает пустой список
        return []

    @staticmethod
    def build_number(string):   # метод возвращает данные в тип int
        return int(string)

class Loader:
    @staticmethod
    def parse_format(string, factory):   # метод возвращает список определенного выходного формата
                    # (парсер - обработчик строки). string - строка данных. factory - ссылка на объект класса Factory
        seq = factory.build_sequence()  # через ссылку на объект обратимся к методу build_sequence() класса Factory.
                                # переменная seq будет ссылаться на пустой список [] который вернет build_sequence()
        for sub in string.split(","):   # строку данных string разбиваем на последовательность и проходим по очереди
            item = factory.build_number(sub)    # переменная item будет ссылаться на вернувшиеся int значение
                                            # функции build_number() короую вызвали через ссылку factory
            seq.append(item)    # добавление item в список seq

        return seq  # Возврат списка

res = Loader.parse_format("1, 2, 3, -5, 10", Factory)  # в переменную res вернется список из метода parse_format класса Loader
# print(res)
########################################################################################################################
from string import ascii_lowercase, digits  # из модуля string импортируем англ. алф. и цифры

class TextInput:    # класс для ввода login
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase  # формируем перем. CHARS рус. алф и анг. алф. + space
    CHARS_CORRECT = CHARS + CHARS.upper() + digits  # формируем перем. CHARS_CORRECT рус. алф и анг. алф. + заглавные
                                                    # буквы этих алфавитов + цифры

    def __init__(self, name, size=10):  # инициал. лок. св-тв объектов класса TextInput
        if self.check_name(name):   # проверка на коррект. ввода name
            self.name = name    # инициал. лок. св-тва self.name
            self.size = size    # инициал. лок. св-тва self.size

    def get_html(self):  # возвращает сформированную HTML-строку в определенном формате
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):   # проверка на коррект. ввода name
        if 2 < len(name) < 51:   # Длина name от 3 до 50 символом включительно то True
            if set(name) < set(cls.CHARS_CORRECT):   # name состоит из коректных символов то True
                return True   # Вернет True

        raise ValueError("некорректное поле name")  # Если хотя бы одно из условие if False то сгенерируется исключение

class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase  # формируем перем. CHARS рус. алф и анг. алф. + space
    CHARS_CORRECT = CHARS + CHARS.upper() + digits  # формируем перем. CHARS_CORRECT рус. алф и анг. алф. + заглавные
                                                    # буквы этих алфавитов + цифры

    def __init__(self, name, size=10):  # инициал. лок. св-тв объектов класса PasswordInput
        if self.check_name(name):   # проверка на коррект. ввода name
            self.name = name    # инициал. лок. св-тва self.name
            self.size = size    # инициал. лок. св-тва self.size

    def get_html(self):  # возвращает сформированную HTML-строку в определенном формате
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):   # проверка на коррект. ввода name
        if 2 < len(name) < 51:   # Длина name от 3 до 50 символом включительно то True
            if set(name) < set(cls.CHARS_CORRECT):   # name состоит из коректных символов то True
                return True   # Вернет True

        raise ValueError("некорректное поле name")  # Если хотя бы одно из условие if False то сгенерируется исключение

class FormLogin:
    def __init__(self, lgn, psw):  # инициал. лок. св-тв объектов класса FormLogin
        self.login = lgn   # инициал. лок. св-тва self.login. lgn ссылка на экз. класса TextInput
        self.password = psw   # инициал. лок. св-тва self.login. psw ссылка на экз. класса PasswordInput

    def render_template(self):  # возвращает сформированную HTML-строку в определенном формате
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])  # через
    # лок. св-во self.login (ссылка на экз. класса TextInput) обратимся с методу get_html() класса TextInput. Он же
    # в свою очередь обратится к лок. св-вам экз. класса TextInput и вернет их значения. Аналогично произойдет с
    # self.password.get_html().


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))  # Сначала создается экз. класса TextInput. Перед
    # созданеим лок. св-тв экз. класса идет проверка на коррект. ввода данных методом check_name(cls, name). Если метод
    # вернет True то экз. класса создастся с переданным значение name. Аналогично далее с экз. класса PasswordInput.
    # Далее создадуться лок. св-ва экз. класса FormLogin. Они будут ссылаться на объекты других классов. И так...
    # login будет ссылаться на свои лок. св-ва, а его лок. св-ва будут ссылаться на объекты других классов.
html = login.render_template()  # в переменную html будем возвращать html код с данными login и password. Для этого
    # через экз. класса login обратимся с методу render_template(self), который в свою очередь обратиться к лок. св-вам
    # self.login и self.login, а мы знаем что это ссылки на объекты других классов. Соответственно, он обратиться туда
    # к методам get_html(), а они вернут данные имени (self.name = Логина) и данные пароля (self.name = password).
    # Далее сформируется html код с данными. И они будут ссылать на переменную html. Всё!!!
# print(html)
########################################################################################################################
from string import ascii_lowercase, digits  # из модуля string импортируем прописные англ. алф. и цифры


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + ' ' + digits  # атрибут класса CardCheck вкл. загл. буквы алф. + цифры

    @staticmethod
    def check_card_number(number):  # статит. метод. Возвращает True если данные number корректны
        lst = number.split('-')  # разделяет строку на подстроки по разделителю '-'
        items = digits + '-'     # лок. атрб. стат. метода вкл. цифры и дефис
        if number.count('-') != 3:  # Возвращает кол-во '-' в number и сравнивает с 3. Если != 3 то метод вернет False
            return False

        if len(lst) != 4:  # Возвращает кол-во эл. lst и сравнивает с 4. Если != 4 то метод вернет False
            return False

        if not all(map(lambda x: len(x) == 4, lst)):  # Проверяет длину эл. lst и сравнивает с 4. Если не все эл. lst
            return False                              # длиной == 4 то метод вернет False

        return set(number) <= set(items)    # проверяем вхождение сета данных number с сетом разрешенных символов items
                                            # если входит или равен тогда вернет True иначе вернет False

    @classmethod
    def check_name(cls, name):      # метод класса. Возвращает True если данные name корректны
        if name.count(' ') != 1:    # Возвращает кол-во ' ' в name и сравнивает с 1. Если != 1 то метод вернет False
            return False

        if len(name.split()) != 2:  # Возвращает кол-во эл. name и сравнивает с 2. Если != 2 то метод вернет False
            return False

        return set(name) <= set(cls.CHARS_FOR_NAME)  # проверяем вхождение сета данных name с сетом разрешенных
                                                     # символов обращаясь к атрибуту класса CardCheck cls.CHARS_FOR_NAME
                                                     # если входит или равен тогда вернет True иначе вернет False
########################################################################################################################
class Video:

    def create(self, name):  # метод создает лок. св-во self.name экз. класса Video
        self.name = name

    def play(self):  # метод вопроизв. видео с названием self.name экз. класса Video
        print(f'воспроизведение видео {self.name}')

class YouTube:
    videos = []  # атрибут класса YouTube. Будут хранится экз. класса Video

    @classmethod
    def add_video(cls, video):  # метод добавляет в атрибут класса videos экз. класса Video
        cls.videos.append(video)

    @classmethod
    def play(cls, video_indx):  # метод обрщается к атрибуту класса videos по индексу video_indx.
        cls.videos[video_indx].play()  # Так как там экз. класса Video он обращается к методу play() класса Video
                                       # а он вопроизв. видео с названием self.name

v1 = Video()  # создаем экз. класса Video
v2 = Video()  # создаем экз. класса Video
v1.create('Python')  # экз. класса Video создаем лок. св-во Python
v2.create('Python ООП')  # экз. класса Video слздаем лок. св-во Python ООП
YouTube.add_video(v1)  # добавляем экз. v1 класса Video в атрибут класса videos
YouTube.add_video(v2)  # добавляем экз. v2 класса Video в атрибут класса videos
# YouTube.play(0)  # обрщаемся к атрибуту класса videos по индексу 0. экз. класса Video обращается к методу play()
# YouTube.play(1)  # обрщаемся к атрибуту класса videos по индексу 1. экз. класса Video обращается к методу play()
########################################################################################################################
class AppStore:
    def __init__(self):     # инициал. лок. св-тв объектов класса AppStore
        self.dict_app = {}  # у экз. класса будет лок. св-во пустой словарь

    def add_application(self, app):     # метод добавляет в лок. св-во экз. класса некий объект app
        self.dict_app[id(app)] = app    # в виде ключа будет id(app), а значение сам объект app

    def remove_application(self, app):  # метод удаляет объект app из в лок. св-во экз. класса
        if id(app) in self.dict_app:    # если ключ id(app) есть в в лок. св-во экз. класса то удаляем по ключу
            del self.dict_app[id(app)]

    def block_application(self, app):               # метод меняет лок. св-во объекта класса Application
        self.dict_app.get(id(app)).blocked = True   # по ключу id(app) обращаемся к объекту класса Application и
                                                    # лок. св-ву меняем значение на True

    def total_apps(self):  # метод возвращает кол-во объектов класса Application
        return len(self.dict_app)

class Application:
    def __init__(self, name, blocked=False):  # инициал. лок. св-тв объектов класса Application
        self.name = name
        self.blocked = blocked

# store = AppStore()
# app_youtube = Application("Youtube")
# app_twitch = Application("Twitch")
# store.add_application(app_youtube)
# store.add_application(app_twitch)
# print(store.total_apps())
# print(store.__dict__)
# store.remove_application(app_youtube)
# print(store.total_apps())
########################################################################################################################
class Viber:
    list_msg = []   # атрибут класса Viber

    @classmethod
    def add_message(cls, msg):    # метод добавляет некий объект msg
        cls.list_msg.append(msg)  # метод добавляет некий объект msg в атрибут list_msg класса Viber

    @classmethod
    def remove_message(cls, msg):     # метод удаляет некий объект msg
        if msg in cls.list_msg:       # если объект msg есть в атрибуте list_msg класса Viber
            cls.list_msg.remove(msg)  # то удаляем его из list_msg по значению msg

    @staticmethod
    def set_like(msg):       # метод меняет лок. св-во объекта msg
        msg.fl_like = False if msg.fl_like else True  # лок. св-ву fl_like объекта msg через терн. опер. уст. знач.

    @classmethod
    def show_last_message(cls, num):  # метод отображает послед. кол-во сообщ. из списка list_msg объектов msg
        print([obj.text for obj in cls.list_msg[-num:]])    # проходим по списку list_msg. у каждого объекта msg
                                                            # обращ. к лок. св-ву text (сообщение) и печатем его
    @classmethod
    def total_messages(cls):  # метод возвращает кол-во объектов msg из списка list_msg
        return len(cls.list_msg)

class Message:
    def __init__(self, text, fl_like=False):     # инициал. лок. св-тв объектов класса Message
        self.text = text
        self.fl_like = fl_like

# msg = Message("Всем привет!")
# Viber.add_message(msg)
# Viber.add_message(Message("Это курс по Python ООП."))
# Viber.add_message(Message("Что вы о нем думаете?"))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Viber.show_last_message(2)
########################################################################################################################

# print(bool(re.fullmatch('кот', 'кот-обормот')))  # Возвращает None если строки не равны. Завернуть в bool(None) return False
# print(bool(re.fullmatch('кот', 'кот')))  # Return object <_sre.SRE_Match object; span=(0, 3), match='кот'>. Завернуть в bool(True) return True

# print(bool(None))   # False
# print(bool(True))   # True