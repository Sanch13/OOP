# Подвиг 7. С помощью наследования можно как бы "наполнять" дочерние классы нужными
# качествами (свойствами). Как пример, объявите в программе класс с именем:
# Singleton
# который бы позволял создавать только один экземпляр (все последующие экземпляры должны
# ссылаться на первый). Как это делать, вы должны уже знать из этого курса.
# Затем, объявите еще один класс с именем:
# Game
# который бы наследовался от класса Singleton. Объекты класса Game должны создаваться командой:
# game = Game(name)
# где name - название игры (строка). В каждом объекте класса Game должен создаваться атрибут
# name с соответствующим содержимым.
# Убедитесь, что атрибут name принимает значение первого созданного объекта (если это не так,
# то поправьте инициализатор дочернего класса, чтобы это условие выполнялось).
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.


class Singleton:
    __instance = None
    __instance_base = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton and cls.__instance_base is None:
            cls.__instance_base = super().__new__(cls)
            return cls.__instance_base

        cls.__instance = cls.__instance or super().__new__(cls)
        return cls.__instance


class Game(Singleton):
    def __init__(self, name):
        # if not hasattr(self, "name"): проверка на наличие "name" в self
        if "name" not in self.__dict__:
            self.name = name


s = Singleton()
c1 = Game("python")
c2 = Game("clock")
print(id(c1), id(c2), sep="\n")
print(c1.__dict__)
print(c2.__dict__)
