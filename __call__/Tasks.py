# from random import randint, choice  # функции для генерации целых случ. знач.
#
#
# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):  # Инициал. лок. св-тв экз. класса
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
#         """При вызове экз. класса с () будет случ. образом генер. последов. из psw_chars в
#         диапазоне [min_length:max_length]"""
#         number = randint(self.min_length, self.max_length)  # выбираем случ. число из диапазона
#         return ''.join(choice(self.psw_chars) for _ in range(number))  # возвр. сгенер. пароль
#
#
# rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)  # созд. объект класса

# lst_pass = [rnd() for _ in range(3)]    # созд. список из функтров=(пароли) экз. rnd
# print(lst_pass)
###################################################################################################


# class ImageFileAcceptor:
#     def __init__(self, extensions):     # Инициал. лок. св-тв экз. класса
#         self.__extensions = extensions  # Инициал. лок. св-тв экз. класса
#
#     def __call__(self, file, *args, **kwargs):    # изм. поведение для функторов экз. класса
#         return file.split('.')[-1] in self.__extensions  # Вернет True если переданный пар-тр
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

# from string import ascii_lowercase, digits
#
# class LoginForm:
#     def __init__(self, name, validators=None):
#         self.name = name
#         self.validators = validators
#         self.login = ""
#         self.password = ""
#
#     def post(self, request):
#         self.login = request.get('login', "")
#         self.password = request.get('password', "")
#
#     def is_validate(self):
#         if not self.validators:
#             return True
#
#         for v in self.validators:
#             if not v(self.login) or not v(self.password):
#                 return False
#
#         return True
#
#
# class LengthValidator:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
#         return self.min_length <= len(args[0]) <= self.max_length
#
#
# class CharsValidator:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
#         return set(args[0]) <= set(self.chars)
###################################################################################################


# class DigitRetrieve:
#     def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
#         try:
#             return int(args[0])
#         except ValueError:
#             return None


# dg = DigitRetrieve()
# st = ["123", "abc", "-56.4", "0", "-5"]
# digits_1 = list(map(dg, st))  # [123, None, None, 0, -5]
# print(digits_1)
###################################################################################################


# class RenderList:
#     def __init__(self, tag):
#         self.tag = tag if tag in ('ul', 'ol') else 'ul'
#
#     def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
#         res = ''.join(f'<li>{el}</li>\n' for el in args[0])  # Сформир. список из вход. аргум.
#         return f'<{self.tag}>\n{res}</{self.tag}>'  # Вернем сформир. строку html


# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3", "Пункт меню 4", "Пункт меню 5"]
# render = RenderList("ol")
# html = render(lst)
# print(html)
###################################################################################################


# class HandlerGET:
#     def __init__(self,  func):
#         self.__fn = func            # Здесь в иниц. сохр. ссылку на функцию, которую декорируем
#
#     def __call__(self, *args, **kwargs):
#         return self.get(self.__fn, args[0])         # Возвращ. возвращаемое значение фун. get.
#
#     def get(self, func, request, *args, **kwargs):  # Возвращает "GET: <данные из декор. фун.>"
#         if request.get("method") in ("GET", None):  # func - ссылка на декор. фун.
#             return f'GET: {func(request)}'          # Если в словаре request ключ {"method": 'GET'}
#                                                     # или вовсе нет ключа возвращаем строку
#         return None                                 # иначе возвращаем None
#
# @HandlerGET
# def contact(request):
#     return "Сергей Балакирев"
#
#
# res = contact({"method": 'GET', "url": "contact.html"})
# print(res)

###################################################################################################


# class Handler:
#     def __init__(self, methods=('GET',)):   # передаем арг. декоратору класса. По умолч. 'GET'
#         self.methods = methods              # передаем арг. декоратору класса
#
#     def __call__(self, func, *args, **kwargs):  # метод __call__ исп. как декоратор общего
#         # назначения (декоратор без аргументов). func - это ссылка на декор. фун.
#         def wrapper(request, *args, **kwargs):      # внут. фун. кот. прин. послед. request
#             method = request.get('method', 'GET')   # по ключу method вызыв. знач. или по умол.
#             if method in self.methods:  # если знач. method есть в арг. декор. класса то
#                 return self.__getattribute__(method.lower())(func, request) # вызыв. соотвт.
#                 # метод класса и передаем ссылку (то же будет арг.) на декор. фун. и арг. request
#         return wrapper
#
#     def get(self, func, request, *args, **kwargs):  # вернет строку и обратится по ссылке func
#         return f"GET: {func(request)}"    # кот. вернет строку. также обяз. перед. 1 арг. request
#
#     def post(self, func, request, *args, **kwargs):  # вернет строку и обратится по ссылке func
#         return f"POST: {func(request)}"   # кот. вернет строку. также обяз. перед. 1 арг. request
#
#
# @Handler(methods=('GET', 'POST'))   # передаем арг. декоратору класса Handler
# def contact(request):               # декор. фун.
#     return "Сергей Балакирев"       # вернет строку
#
#
# res = contact({"method": "POST", "url": "contact.html"})
# print(res)
###################################################################################################


# class InputDigits:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return list(map(int, self.func().split()))
#
#
# @InputDigits
# def input_dg():
#     return input()
#
#
# res = input_dg()
# print(res)
###################################################################################################


# class InputValues:
#     def __init__(self, render):     # render - ссылка на функцию или объект для преобразования
#         self.render = render        # здесь строчки программы
#
#     def __call__(self, func):       # func - ссылка на декорируемую функцию
#         def wrapper(*args, **kwargs):
#             return list(map(self.render, func().split()))
#         return wrapper
#
#
# class RenderDigit:
#     def __call__(self, s, *args, **kwargs):
#         if s.isdigit() or s[0] == '-' and s[1:].isdigit():
#             return int(s)
#
#
# render = RenderDigit()
# input_dg = InputValues(render)(input)
# res = input_dg()
# print(res)
###################################################################################################
