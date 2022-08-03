class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args):
        self.coords = list((LineTo(0, 0),) + args)

    def get_path(self):
        return self.coords[1:]

    def get_length(self):
        g = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
        return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))

    def add_line(self, line):
        self.coords.append(line)


# class LineTo:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def length(self, x1, y2):
#         return ((self.x - x1) ** 2 + (self.y - y2) ** 2) ** 0.5
#
#
# class PathLines:
#
#     def __init__(self, *points):
#         self.__points = list(points)
#
#     def add_line(self, point):
#         self.__points.append(point)
#
#     def get_path(self):
#         return self.__points
#
#     def get_length(self):
#         x = y = length = 0
#         for point in self.__points:
#             length += point.length(x, y)
#             x, y = point.x, point.y
#         return length



p = PathLines(LineTo(1, 2))
print(p.get_length())  # 2.23606797749979
p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
print(p.get_length())  # 28.191631669843197
m = p.get_path()
print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
print(h.get_length())  # 71.8992593599813

k = PathLines()
print(k.get_length())  # 0
print(k.get_path())  # []
