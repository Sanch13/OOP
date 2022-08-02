class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.__check_value(x) else 0
        self.__y = y if self.__check_value(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_value(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_value(y):
            self.__y = y

    @classmethod
    def __check_value(cls, value):
        if not isinstance(value, (int, float)):
            return False

        return cls.MIN_COORD <= value <= cls.MAX_COORD

    @staticmethod
    def norm2(vector):
        return vector.x ** 2 + vector.y ** 2


r1 = RadiusVector2D()
print(r1.x, r1.y)
r2 = RadiusVector2D(-1001)
print(r2.x, r2.y)
r3 = RadiusVector2D(4, 5)
res = RadiusVector2D.norm2(r3)
print(res)
res2 = RadiusVector2D.norm2(r1)
print(res2)

