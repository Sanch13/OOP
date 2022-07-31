class LinkedList:
    """объявите класс LinkedList, который будет представлять связный список в целом
    и иметь набор следующих методов:
    И локальные публичные атрибуты:
    head - ссылка на первый объект связного списка (если список пустой, то head = None);
    tail - ссылка на последний объект связного списка (если список пустой, то tail = None).
    """
    def __init__(self):
        self.head = None
        self.tail = None


    def add_obj(self, obj):
        """добавление нового объекта obj класса ObjList в конец связного списка;
        """
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        """удаление последнего объекта из связного списка;
        """
        if self.tail is None:
            return

        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)

        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        """получение списка из строк локального свойства __data всех объектов связного списка.
        """
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s


class ObjList:
    """Объекты класса ObjList должны иметь следующий набор приватных локальных свойств:
    __next - ссылка на следующий объект связного списка (если следующего объекта нет, то __next = None);
    __prev - ссылка на предыдущий объект связного списка (если предыдущего объекта нет, то __prev = None);
    __data - строка с данными.
    Также в классе ObjList должны быть реализованы следующие сеттеры и геттеры:
    """
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        """изменение приватного свойства __next на значение obj"""
        self.__next = obj

    def set_prev(self, obj):
        """изменение приватного свойства __prev на значение obj"""
        self.__prev = obj

    def get_next(self):
        """получение значения приватного свойства __next"""
        return self.__next

    def get_prev(self):
        """получение значения приватного свойства __prev"""
        return self.__prev

    def set_data(self, data):
        """изменение приватного свойства __data на значение data"""
        self.__data = data

    def get_data(self):
        """получение значения приватного свойства __data."""
        return self.__data


ob = ObjList("данные 1")
