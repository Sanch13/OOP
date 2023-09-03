# Подвиг 9 (на повторение). Необходимо объявить функцию-декоратор class_log для класса,
# которая бы создавала логирование вызовов методов класса. Например следующие строчки программы:
# vector_log = []
# @class_log(vector_log)
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
# декорируют класс Vector и в список vector_log добавляются имена методов, которые были вызваны
# при использовании этого класса. В частности, после выполнения команд:
# v = Vector(1, 2, 3)
# v[0] = 10
# в списке vector_log должны быть два метода:
# ['__init__', '__setitem__']
# Ваша задача реализовать декоратор с именем class_log.
# Напоминание. Ранее вы уже создавали функцию-декоратор для класса следующим образом:
# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#     return cls
# Используйте этот принцип для успешного прохождения подвига.
# P.S. В программе нужно объявить только класс и необходимые функции.
# На экран выводить ничего не нужно.

########################    the first way   ##############################################
# def record_func_name(func):  # Записывает имя вызываемой функции в список vector_log
#    def wrapper(*args, **kwargs):
#         vector_log.append(func.__name__)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def class_log(vector_log):
#     def wrapper(class_):
#         methods = {k: v for k, v in class_.__dict__.items() if callable(v)}
#         for k, v in methods.items():  # устанавливает декоратор к всем методам класса
#             setattr(class_, k, record_func_name(v))
#         return class_
#     return wrapper


########################    the second way   ##############################################
# def class_log(lst_methods):  # Записывает имя вызываемой функции в список vector_log
#     def wrapper(class_):
#         methods = {k: v for k, v in class_.__dict__.items() if callable(v)}
#         for k, v in methods.items():
#             setattr(class_, k, write_method(v))  # устанавливает декоратор к всем методам класса
#         return class_
#
#     def write_method(func):
#         def inner(*args, **kwargs):
#             lst_methods.append(func.__name__)
#             return func(*args, **kwargs)
#         return inner
#
#     return wrapper


########################    the third way   ##############################################
class class_log:
    def __init__(self, log_list):  # create local attribute (list) to add the function name
        self.log_list = log_list

    def write_method_on_list(self, name,  func):
        """Writes the function name to the list self.log_list"""
        def wrapper(*args, **kwargs):
            self.log_list.append(name)
            return func(*args, **kwargs)
        return wrapper

    def __call__(self, class_, *args, **kwargs):
        """Creates decorators for the called class methods """
        for k, v in class_.__dict__.items():
            if callable(v):
                setattr(class_, k, self.write_method_on_list(k, v))
        return class_


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(vector_log)
print(Vector.__dict__)
