# Подвиг 9 (релакс). Необходимо объявить класс Body (тело), объекты которого создаются командой:
# body = Body(name, ro, volume)
# где name - название тела (строка); ro - плотность тела (число: вещественное или целочисленное);
# volume - объем тела  (число: вещественное или целочисленное).
# Для объектов класса Body должны быть реализованы операторы сравнения:
# body1 > body2  # True, если масса тела body1 больше массы тела body2
# body1 == body2 # True, если масса тела body1 равна массе тела body2
# body1 < 10     # True, если масса тела body1 меньше 10
# body2 == 5     # True, если масса тела body2 равна 5
# Масса тела вычисляется по формуле:
# m = ro * volume
# P.S. В программе только объявить класс, выводить на экран ничего не нужно.

def check_value(func):
    def wrapper(self, other):
        val = other.m if isinstance(other, Body) else other
        return func(self, val)

    return wrapper


class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.m = self.ro * self.volume

    @check_value
    def __eq__(self, other):
        return self.m == other

    @check_value
    def __lt__(self, other):
        return self.m < other

    @check_value
    def __le__(self, other):
        return self.m <= other


body1 = Body("af", 15, 12)
body2 = Body("afacf", 12, 12)

print(body1 == body2)  # True, если масса тела body1 равна массе тела body2
print(body2 == 5)  # True, если масса тела body2 равна 5
print(3 == body1)  # True, если масса тела body2 равна 5
print(10 > body1)  # True, если масса тела body1 меньше 10
print(body1 < 10)  # True, если масса тела body1 меньше 10
print(body1 > body2)  # True, если масса тела body1 меньше 10
print(body1 >= body2)  # True, если масса тела body1 больше массы тела body2
