# Подвиг 7. Объявите класс Ellipse (эллипс), объекты которого создаются командами:
# el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
# el2 = Ellipse(x1, y1, x2, y2)
# где x1, y1 - координаты (числа) левого верхнего угла; x2, y2 - координаты (числа) нижнего
# правого угла. Первая команда создает объект класса Ellipse без локальных атрибутов x1, y1, x2, y2.
# Вторая команда создает объект с локальными атрибутами x1, y1, x2, y2 и соответствующими
# переданными значениями.
# В классе Ellipse объявите магический метод __bool__(), который бы возвращал True, если все
# локальные атрибуты x1, y1, x2, y2 существуют и False - в противном случае.
# Также в классе Ellipse нужно реализовать метод:
# get_coords() - для получения кортежа текущих координат объекта.
# Если координаты отсутствуют (нет локальных атрибутов x1, y1, x2, y2), то метод get_coords()
# должен генерировать исключение командой:
# raise AttributeError('нет координат для извлечения')
# Сформируйте в программе список с именем lst_geom, содержащий четыре объекта класса Ellipse.
# Два объекта должны быть созданы командой
# Ellipse()
# и еще два - командой:
# Ellipse(x1, y1, x2, y2)
# Переберите список в цикле и вызовите метод get_coords() только для объектов, имеющих
# координаты x1, y1, x2, y2. (Помните, что для этого был определен магический метод __bool__()).
# P.S. На экран ничего выводить не нужно.

class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1, self.y1, self.x2, self.y2 = args

    def __len__(self):
        return len(self.__dict__)

    def __bool__(self):
        return len(self) == 4

    def get_coords(self):
        if not len(self):
            raise AttributeError('нет координат для извлечения')
        return tuple(self.__dict__.values())


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
[obj.get_coords() for obj in lst_geom if obj]
# print(*[obj.get_coords() for obj in lst_geom if bool(obj)], sep="\n")
el1 = Ellipse()  # без создания локальных атрибутов x1, y1, x2, y2
el2 = Ellipse(1, 2, 3, 4)
print(el1, el1.__dict__, len(el1), bool(el1))
print(el2, el2.__dict__, len(el2), bool(el1))
# # print(el1.get_coords())
# print(el2.get_coords())

