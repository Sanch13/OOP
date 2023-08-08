# Подвиг 8. В программе необходимо объявить классы для работы с кошельками в разных валютах:
# MoneyR - для рублевых кошельков
# MoneyD - для долларовых кошельков
# MoneyE - для евро-кошельков
# Объекты этих классов могут создаваться командами:
# rub = MoneyR()   # с нулевым балансом
# dl = MoneyD(1501.25) # с балансом в 1501.25 долларов
# euro = MoneyE(100)  # с балансом в 100 евро
# В каждом объекте этих классов должны формироваться локальные атрибуты:
# __cb - ссылка на класс CentralBank (центральный банк, изначально None);
# __volume - объем денежных средств в кошельке (если не указано, то 0).
# Также в классах MoneyR, MoneyD и MoneyE должны быть объекты-свойства (property) для работы
# с локальными атрибутами:
# cb - для изменения и считывания данных из переменной __cb;
# volume - для изменения и считывания данных из переменной __volume.
# Объекты классов должны поддерживать следующие операторы сравнения:
# rub < dl
# dl >= euro
# rub == euro  # значения сравниваются по текущему курсу центрального банка с погрешностью
# 0.1 (плюс-минус)
# euro > rub
# При реализации операторов сравнения считываются соответствующие значения __volume из
# сравниваемых объектов и приводятся к рублевому эквиваленту в соответствии с курсом валют
# центрального банка.
# Чтобы каждый объект классов MoneyR, MoneyD и MoneyE "знал" текущие котировки, необходимо в
# программе объявить еще один класс CentralBank. Объекты класса CentralBank создаваться не
# должны (запретить), при выполнении команды:
# cb = CentralBank()
# должно просто возвращаться значение None. А в самом классе должен присутствовать атрибут:
# rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
# Здесь числа (в значениях словаря) - курс валюты по отношению к доллару.
# Также в CentralBank должен быть метод уровня класса:
# register(cls, money) - для регистрации объектов классов MoneyR, MoneyD и MoneyE.
# При регистрации значение __cb объекта money должно ссылаться на класс CentralBank.
# Через эту переменную объект имеет возможность обращаться к атрибуту rates класса
# CentralBank и брать нужные котировки.
# Если кошелек не зарегистрирован, то при операциях сравнения должно генерироваться исключение:
# raise ValueError("Неизвестен курс валют.")
# Пример использования классов (эти строчки в программе писать не нужно):
# CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
# r = MoneyR(45000)
# d = MoneyD(500)
# CentralBank.register(r)
# CentralBank.register(d)
# if r > d:
#     print("неплохо")
# else:
#     print("нужно поднажать")
# P.S. В программе на экран ничего выводить не нужно, только объявить классы.


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money):
        money.cb = cls


class Money:
    def __init__(self, volume: int or float = 0):
        self.__volume = volume
        self.__cb = None

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value):
        self.__cb = value

    def get_value(self):
        """Returns the value (self.__cb) of the class instance"""
        return self.__volume

    @staticmethod
    def is_register_wallets(wallet_1, wallet_2):
        if not (wallet_1.cb and wallet_2.cb):
            raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other):
        self.is_register_wallets(wallet_1=self, wallet_2=other)
        return abs(self.get_value() - other.get_value()) < 0.1

    def __gt__(self, other):
        self.is_register_wallets(wallet_1=self, wallet_2=other)
        return self.get_value() > other.get_value()

    def __ge__(self, other):
        self.is_register_wallets(wallet_1=self, wallet_2=other)
        return self.get_value() >= other.get_value()


class MoneyR(Money):
    pass


class MoneyD(Money):
    def get_value(self):
        return super().get_value() * self.cb.rates.get("rub")


class MoneyE(Money):
    def get_value(self):
        return super().get_value() * self.cb.rates.get("rub") * self.cb.rates.get("euro")


rub = MoneyR()  # с нулевым балансом
dl = MoneyD(1501.25)  # с балансом в 1501.25 долларов
euro = MoneyE(100)  # с балансом в 100 евро
print(rub.__dict__, dl.__dict__, euro.__dict__, sep=" | ")
rub.volume = 1230
dl.volume = 34.5
euro.volume = 30
print(rub.__dict__, dl.__dict__, euro.__dict__, sep=" | ")
CentralBank.register(rub)
CentralBank.register(dl)
CentralBank.register(euro)
# print(rub.__dict__, dl.__dict__)
# print(rub.get_value())
# print(dl.get_value())
# print(euro.get_value())
# print(dl == euro)
# print(dl > euro)
# print(dl >= euro)
# print(dl < euro)
# print(dl <= euro)
# print(dl != euro)





# class MoneyR(Money):
#     def __init__(self, volume: int or float = 0, cb=None):
#         super().__init__(volume, cb)
#
#
# class MoneyD(Money):
#     def __init__(self, volume: int or float = 0, cb=None):
#         super().__init__(volume, cb)
#
#
# class MoneyE(Money):
#     def __init__(self, volume: int or float = 0, cb=None):
#         super().__init__(volume, cb)






