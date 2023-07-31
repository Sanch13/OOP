# __add__() – для операции сложения;
# __sub__() – для операции вычитания;
# __mul__() – для операции умножения;
# __truediv__() – для операции деления.
# __radd__()  Он автоматически вызывается, если не может быть вызван метод __add__()
# __iadd__() Она вызывается для команды: c1 += 100

# Оператор Метод оператора         Оператор Метод оператора
# x + y    __add__(self, other)     x += y   __iadd__(self, other)
# x - y    __sub__(self, other)     x -= y   __isub__(self, other)
# x * y    __mul__(self, other)     x *= y   __imul__(self, other)
# x / y    __truediv__(self, other) x /= y   __itruediv__(self, other)
# x // y   __floordiv__(self, other)x //= y  __ifloordiv__(self, other)
# x % y    __mod__(self, other)     x %= y   __imod__(self, other)

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
        return f"{h:02}:{m:02}:{s:02}"

    def __add__(self, other):
        """Складывает лок. атриб. экз. класса Clock и созд. новый экз. с суммой"""
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        # Теперь, в программе можно складывать и отдельные целые числа и объекты классов Clock
        sc = other if isinstance(other, int) else other.seconds
        return Clock(self.seconds + sc)

    def __radd__(self, other):
        """сложения текущего объекта класса Clock с параметром other, который может быть или
        числом или тоже объектом класса Clock. В свою очередь будет вызван метод __add__,
        но с правильным порядком типов данных, поэтому сложение пройдет без ошибок"""
        return self + other

    def __iadd__(self, other):
        """не создаем нового объекта, а меняем число секунд в текущем объекте."""
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть типом int или объектом Clock")

        sc = other if isinstance(other, int) else other.seconds
        self.seconds += sc

        return self

# c1 = Clock(1000)
# c1.seconds = c1.seconds + 100
# c1 = c1 + 100
# с1 = c1.__add__(100)  Этот объект возвращается методом __add__ и переменная c1
# начинает ссылаться на этот новый экземпляр класса. 1000 + 100 = 1100, с1 = 1100
# c1 = Clock(1000)
# c2 = Clock(2000)
# c3 = Clock(3000)
# c4 = c1 + c2 + c3
# метод __add__ возвращает каждый раз новый экземпляр класса Clock.
# c1 = 100 + c1 # 100.__add__(c1) # __radd__()
# c1 += 100 # в методе __add__ создается новый объект класса Clock,
# тогда как при операции += этого делать не обязательно. __iadd__ не создаем нового объекта,
# а меняет число секунд в текущем
