# __iter__(self) – получение итератора для перебора объекта;
# __next__(self) – переход к следующему значению и его считывание.

# a = iter(range(5))  # [0, 1, 2, 3, 4]
# next(a)  # 0
# next(a)  # 1
# В конце генерируется исключение StopIteration.

# мы можем создать подобный объект (экземпляр класса),
# используя магические методы __iter__ и __next__

class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        # начальное значение прогрессии, конечное и шаг изменения
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        print("__iter__FRange__iter")
        self.value = self.start - self.step
        return self

    def __next__(self):
        # увеличиваем значение value на шаг step и возвращаем до тех пор,
        # пока не достигли значения stop (не включая его)
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration
        # При достижении конца генерируем исключение StopIteration
        # благодаря определению магического метода __next__ в классе FRange,
        # мы можем применять функцию next() для перебора значений его объектов


# fr = FRange(0, 2, 0.5)
# print(next(fr))  # next(fr) == fr.__next__()
# print(next(fr))  # next(fr) == fr.__next__()
# print(next(fr))  # next(fr) == fr.__next__()
# print(next(fr))  # next(fr) == fr.__next__()
# Здесь функция next() вызывает метод __next__ и возвращенное им значение, возвращается
# функцией next(). При этом, в качестве аргумента мы ей передаем экземпляр самого класса.
# То есть, объект класса выступает в роли итератора. В нашем случае так и задумывалось.
# Однако, перебрать объект fr с помощью цикла for не получится:
# for x in fr:  # TypeError: 'FRange' object is not iterable
#     print(x)
# Необходимо еще, чтобы объект возвращал итератор при вызове функции iter. Для этого в классе
# нужно прописать еще один магический метод __iter__. После объявленного метода __iter__, он неявно
# вызывается внутри класса метод __iter__. Устанавливается начальное значение объекта и
# возвращается сам объект self. После отрабатывает встроенная функция next() которая перебирает
# последовательность уже итерируемого объекта до конца последовательности.


class FRange2D:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        # в инициализаторе создается одномерный объект FRange, который будет
        # формировать строки таблицы. Параметр rows – число строк.
        self.fr = FRange(start, stop, step)
        self.rows = rows

    def __iter__(self):
        print("__iter__2D__iter")
        self.value_row = 0
        return self

    def __next__(self):
        if self.value_row < self.rows:
            self.value_row += 1
            return iter(self.fr)
        # Обратите внимание, что метод __next__ возвращает не конкретное значение,
        # а итератор на объект класса FRange.
        else:
            raise StopIteration


fr = FRange2D(0, 2, 0.5, 4)
# Первый цикл перебирает первый итератор – объект класса FRange2D и на каждой итерации
# возвращает итератор объекта класса FRange. Именно поэтому мы в методе __next__ класса
# FRange2D возвращаем иетратор, иначе бы не смогли перебирать объект row во вложенном цикле for.
for row in fr:
    for x in row:
        print(x, end=" ")
    print()
