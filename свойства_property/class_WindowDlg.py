class WindowDlg:
    MIN = 0
    MAX = 10000

    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.__resize_window(width):
            if self.__width:
                self.show()
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__resize_window(height):
            if self.__height:
                self.show()
            self.__height = height

    @classmethod
    def __resize_window(cls, side):
        return type(side) == int and cls.MIN <= side <= cls.MAX
