class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__check_value(x)    # check value then init it
        self.__y = self.__check_value(y)    # check value then init it

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
        '''return the number if the condition is correct otherwise return 0'''
        return value if isinstance(value, (int, float)) and cls.MIN_COORD <= value <= cls.MAX_COORD else 0

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

