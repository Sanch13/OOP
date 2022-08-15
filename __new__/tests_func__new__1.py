class AbstractClass:
    __instance = None
    __obj = "Ошибка: нельзя создавать объекты абстрактного класса"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return cls.__obj

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"


obj = AbstractClass()
##########################################################################################################
class SingletonFive:
    __count = 0
    __link = None

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__count += 1
            cls.__link = super().__new__(cls)
        return cls.__link

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for k, v in enumerate(objs):
    print(k + 1, v)
##########################################################################################################
TYPE_OS = 2  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:  # здесь объявляйте класс Dialog
    def __new__(cls, *args, **kwargs):
        __link = None
        if TYPE_OS == 1:
            __link = super().__new__(DialogWindows)

        else:
            __link = super().__new__(DialogLinux)

        __link.name = args[0]
        return __link


dg = Dialog('1212')
print(dg.name_class)