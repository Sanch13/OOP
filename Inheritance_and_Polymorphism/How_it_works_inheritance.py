# когда один класс определяется на основе другого, называется наследованием

class Geom:  # родительский или базовый или суперкласс
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f"инициализатор Geom для {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.draw()

    def draw(self):
        print("Рисование примитива")


# Geom расширяет класс Line. все, что доступно в классе Geom автоматически становится доступным и
# в классе Line
class Line(Geom):  # подкласс родительского или дочерний класс
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)  # обращение к переопределенным методам базового класса
        # с помощью функции super() называется делегированием. То есть, мы делегировали вызов
        # инициализатора класса Geom, чтобы он создал в нашем объекте локальные свойства с
        # координатами углов прямоугольника. Причем, вызов метода __init__() базового класса
        # лучше делать в первой же строчке, чтобы он случайно не переопределял какие-либо
        # локальные свойство в дочернем классе.
        print("инициализатор Rect")
        self.fill = fill

    def draw(self):
        print("Рисование линии")


# Geom расширяет класс Rect. все, что доступно в классе Geom автоматически становится
# доступным и в классе Rect
class Rect(Geom):  # подкласс родительского или дочерний класс
    def draw(self):
        print("Рисование прямоугольника")

# При реализации методов в классах следует придерживаться одного простого правила:
# внутри них обращаться только к разрешенным атрибутам либо внутри текущего класса,
# либо базовых классов. Но не дочерних.
# если указанное свойство не находится в соответствующем дочернем классе, то поиск продолжается
# в базовых. Однако, если свойство name прописать непосредственно в дочернем классе, например,
# Line то для объектов-линий оно будет взято непосредственно из класса Line.
# когда мы определяем какой-либо существующий атрибут в дочернем классе – это
# называется переопределением.
# Если draw() вызвать из дочерних объектов то будут вызваны соответствующие методы дочерних классов.
# А если мы вызываем draw() из базового класса то будет вызван метод базового класса. Разумеется,
# если в каком-либо дочернем классе убрать метод draw(), например, в прямоугольнике,
# то для него будет вызван метод уже базового класса.


l = Line(1, 2, 3, 4)
r = Rect(0, 5, 6, 7)
l.set_coords(1, 1, 2, 2)  # Во-первых, когда происходит его вызов, например,
# через объект класса Line то метод с таким названием сначала ищется в классе Line и если не
# находится, то поиск продолжается в базовых классах. В данном случае – это класс Geom.
# В нем этот метод обнаруживается и запускается. Во-вторых, при вызове метода set_coords() из
# базового класса его параметр self будет ссылаться на объект, через который этот метод был вызван.
# То есть, на объект класса Line. Вот это очень важный момент! Параметр self в базовых классах
# может ссылаться не только на объекты этого же класса, но и на объекты производных (дочерних)
# от него классов, как в нашем случае – на объект класса Line.
r.set_coords(1, 1, 2, 2)
