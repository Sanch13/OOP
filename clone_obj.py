class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def clone(self):
        return Point(self.__x, self.__y)



pt = Point(1, 2)
pt_clone = Point.clone(pt)  # clone obj pt
print(pt.__dict__, pt_clone.__dict__)