class TriangleChecker:
    """
    1 - на входе есть отрицательное, или равное нулю число
    2 - из таких значений сторон треугольник не получится (все значения больше нуля)
    3 - с такими получается треугольник
    Если что, треугольник получится тогда, когда сумма длин любых двух сторон, больше длины третьей.
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.lst = [a, b, c]    # __second way__

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if not all(map(lambda x: type(x) in (int, float), [a, b, c])):
            return 1
        elif not all(map(lambda x: x > 0, [a, b, c])):
            return 1


        if a >= b + c or b >= a + c or c >= a + b:
            return 2
        return 3

    # def is_triangle(self):     __second way__
    #     for num in self.lst:
    #         if not isinstance(num, int) or num <= 0:
    #             return 1
    #     if max(self.lst) >= sum(self.lst) - max(self.lst):
    #         return 2
    #     return 3

    # def is_triangle(self):
    #     sides = self.__dict__.values()
    #     for side in sides:
    #         if not isinstance(side, (int, float)) or side < 0:
    #             return 1
    #     x, y, z = sorted(sides)
    #     if z < x + y:
    #         return 3
    #     return 2

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)

print(tr.is_triangle())


