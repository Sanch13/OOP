# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=

# __eq__ - EQual to - равно
# __ne__ - Not Equal to - не равно
# __gt__ - Greater Than - больше, чем
# __ge__ - Greater than or Equal to - больше или равно
# __lt__ - Less Than - меньше, чем
# __le__ - Less than or Equal to - меньше или равно


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60  # секунды
        m = (self.seconds // 60) % 60  # минуты
        h = (self.seconds // 3600) % 24  # часы
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc

    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc


c1 = Clock(1000)
c2 = Clock(1000)
print(c1 == c2)  # False потому что объекты сравниваются по их id (адресу в памяти)

# чтобы сравнивались секунды в каждом из объектов c1 и c2.
# Для этого переопределим магический метод __eq__().

print(c1 != c2)  # если Python не находит определение метода ==, то он пытается выполнить
# противоположное сравнение с последующей инверсией результата. not (a == b).

print(c1 < c2)  # Подмена происходит только в случае отсутствия соответствующего магического
# метода. c2 < c1 здесь меняется порядок операндов


print(c1 <= c2)  # Подмена происходит только в случае отсутствия соответствующего магического
# метода. c2 <= c1 здесь меняется порядок операндов



