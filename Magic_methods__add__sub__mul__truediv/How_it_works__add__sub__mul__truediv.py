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

	def __sub__(self, other):
		return Clock(self.seconds - other)


c1 = Clock(3000)
print(c1.seconds)
c2 = Clock(1000)

c3 = c1 - 2500
print(c3.get_time())