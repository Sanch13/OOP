class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())

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

line = Line(1, 2, 3, 4)
line.draw()