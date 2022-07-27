class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, a, b, c=None, d=None):
        self.__sp = self.__ep = None

        if isinstance(a, Point) and isinstance(b, Point):
            self.__sp = a
            self.__ep = b
        elif all(map(lambda x: type(x) in (int, float), (a, b, c, d))):
            self.__sp = Point(a, b)
            self.__ep = Point(c, d)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


rect = Rectangle(Point(0, 0), Point(20, 34))
# rect = Rectangle(0, 0, 20, 34)
rect.draw()

# class Line:
#     def __init__(self,x1=0,y1=0,x2=0,y2=0):
#         self.__x1=x1
#         self.__y1=y1
#         self.__x2=x2
#         self.__y2=y2
#     def set_coords(self,*args):
#         self.__dict__=dict(zip(self.__dict__.keys(),args))
#     def get_coords(self):
#         return tuple(self.__dict__.values())
#     def draw(self):
#         print(*self.__dict__.values())
