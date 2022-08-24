class ReadIntX:  # non-data descriptor

    def __set_name__(self, owner, name):
        self.name = "_x"  # будет считывать локальный атрибут _x

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # def __set__(self, instance, value):  # станет data descriptor если раcкоментировать
    #     setattr(instance, self.name, value)


class Integer:  # data descriptor

    @classmethod
    def verify_coord(cls, coord):  # проверяем чтобы coord было целым числом
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name  # В этом методе мы формируем локальное свойство с именем атрибута, добавляя
        # перед ним одно нижнее подчеркивание (так принято делать при определении дескрипторов)

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]  Мы здесь через ссылку instance обращаемся к словарю __dict__ и считываем
        # значение нужного локального свойства, которое, затем, возвращается геттером. Это же значение автоматически
        # возвращается и самим дескриптором.
        return getattr(instance, self.name)  # Так будет правильнее, с точки зрения Python, чем обращение напрямую к
        # специальной коллекции __dict__.

    def __set__(self, instance, value):
        self.verify_coord(value)  # проверяем чтобы coord было целым числом
        # instance.__dict__[self.name] = value  Мы здесь через ссылку instance обращаемся к словарю __dict__ и
        # присваеваем локальному свойству с именем атрибута [self.name] значение value
        setattr(instance, self.name, value)  # Так будет правильнее, с точки зрения Python, чем обращение напрямую к
        # специальной коллекции __dict__.


class Point3D:
    x = Integer()  # создаем атрибут 'x' как объект класса Integer # create the 'x' attribute as an Integer object
    y = Integer()  # создаем атрибут 'y' как объект класса Integer # create the 'y' attribute as an Integer object
    z = Integer()  # создаем атрибут 'z' как объект класса Integer # create the 'z' attribute as an Integer object
    xr = ReadIntX()  # будет считывать локальное свойство _x согласно non-data descriptor ReadIntX

    """Эти атрибуты и есть дескрипторы данных, через которые будет проходить взаимодействие. Итак, когда мы создавали 
        экземпляры классов Integer, то автоматически вызывался магический метод __set_name__, в котором параметр self 
        являлся ссылкой на создаваемый экземпляр класса; owner – ссылка на класс Point3D; name – имя атрибута 
        (для первого объекта x, затем, y и z). В этом методе мы формируем локальное свойство с именем атрибута, добавляя 
        перед ним одно нижнее подчеркивание (так принято делать при определении дескрипторов). В итоге, в экземплярах 
        классов будут храниться имена _x, _y, _z."""

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
print(pt.__dict__)
"""Сработает инициализатор, а в нем идет обращение к дескрипторам x, y, z. В частности, мы им присваиваем переданные 
значения. В этом случае, в классе Integer срабатывает сеттер (магический метод __set__), параметр self – это ссылка на 
объект дескриптора; instance – ссылка на объект pt, из которого произошло обращение к дескриптору; 
value – присваиваемое значение.Следующей строчкой через ссылку instance, то есть, на экземпляр класса pt, формируем 
в нем локальное свойство с именем self.name и присваиваем значение value. В результате, в объекте pt появляются 
локальные свойства _x, _y, _z с соответствующими значениями."""


print(pt.xr)  # считывания локального атрибута _x = 1
print(pt.__dict__)
pt.xr = 8  # В экземпляре pt будет создано новое лок. свойство с именем xr и ссылаться он будет на заданное значение.
print(pt.xr, pt.__dict__)
# pt.__dict__['xr'] = 5
# print(pt.xr, pt.__dict__)
