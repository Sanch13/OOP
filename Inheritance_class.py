from random import randint


class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Figure):
    pass


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


def rnd_int():
    return randint(0, 9)


elements = [(Line, Rect, Ellipse)[randint(0, 2)](rnd_int(), rnd_int(), rnd_int(), rnd_int()) for _ in range(217)]

for obj in elements:
    if isinstance(obj, Line):
        obj.ep = obj.sp = 0, 0
