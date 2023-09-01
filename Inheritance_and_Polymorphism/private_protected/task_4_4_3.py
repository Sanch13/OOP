# Подвиг 8. Объявите базовый класс Aircraft (самолет), объекты которого создаются командой:
# air = Aircraft(model, mass, speed, top)
# где model - модель самолета (строка); mass - подъемная масса самолета (любое положительное число);
# speed - максимальная скорость (любое положительное число); top - максимальная высота полета
# (любое положительное число).
# В каждом объекте класса Aircraft должны создаваться локальные атрибуты с именами: _model, _mass,
# _speed, _top и соответствующими значениями. Если передаваемые аргументы не соответствуют
# указанным критериям (строка, любое положительное число), то генерируется исключение командой:
# raise TypeError('неверный тип аргумента')
# Далее, в программе объявите следующие дочерние классы:
# PassengerAircraft - пассажирский самолет;
# WarPlane - военный самолет.
# Объекты этих классов создаются командами:
# pa = PassengerAircraft(model, mass, speed, top, chairs)  # chairs - число пассажирских мест
# (целое положительное число)
# wp = WarPlane(model, mass, speed, top, weapons) # weapons - вооружение (словарь);
# ключи - название оружия, значение - количество
# В каждом объекте классов PassengerAircraft и WarPlane должны формироваться локальные атрибуты
# с именами _chairs и _weapons соответственно. Инициализация остальных атрибутов должна
# выполняться через инициализатор базового класса.
# В инициализаторах классов PassengerAircraft и WarPlane проверять корректность передаваемых
# аргументов chairs и weapons. Если тип данных не совпадает, то генерировать исключение командой:
# raise TypeError('неверный тип аргумента')
# Создайте в программе четыре объекта самолетов со следующими данными:
# PassengerAircraft: МС-21, 1250, 8000, 12000.5, 140
# PassengerAircraft: SuperJet, 1145, 8640, 11034, 80
# WarPlane: Миг-35, 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
# WarPlane: Су-35, 7034, 34000, 2400, {"ракета": 4, "бомба": 7}
# Все эти объекты представить в виде списка planes.
# P.S. В программе нужно объявить только классы и сформировать список
# На экран выводить ничего не нужно.


class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = self.is_valid_str(model)
        self._mass, self._speed, self._top = [self.is_valid_nums(el) for el in (mass, speed, top)]
        # [self.is_valid_nums(el) for el in (mass, speed, top)]
        # self._mass = mass
        # self._speed = speed
        # self._top = top

    @staticmethod
    def is_valid_str(value) -> str:
        if type(value) != str:
            raise TypeError('неверный тип аргумента')
        return value

    @staticmethod
    def is_valid_nums(value) -> int:
        if not (isinstance(value, (int, float)) and value > 0):
            raise TypeError('неверный тип аргумента')
        return value

    @staticmethod
    def is_positive_num(number):
        if type(number) != int or number < 0:
            raise TypeError('неверный тип аргумента')
        return number

    def __str__(self):
        return ", ".join(f"{k}: {v}" for k, v in self.__dict__.items())


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = self.is_positive_num(chairs)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons: dict):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = {self.is_valid_str(k): self.is_positive_num(v) for k, v in weapons.items()}


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

# p = PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140)
# print(p)
for obj in planes:
    print(obj)
