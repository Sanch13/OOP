"""
Если в классе задан атрибут как объект-свойство, то в первую очередь выбирается оно, 
даже если в экземпляре класса есть локальное свойство с таким же именем.
Приоритет такой (если локальное свойство с таким же именем): 
1) Объект-свойство.
2) Локальное свойство в экземпляре класса.
3) Обращается в класс Person
"""


#######################################################################################################################
class Car:
    MIN = 1  # атрибут класса. миним. критерий
    MAX = 101  # атрибут класса. макс. критерий

    def __init__(self, model=None):  # Инициал. лок. св-в экз. класса Car
        self.__model = model  # Инициал. приватной лок. св-в экз. класса

    @property  # объект св-во
    def model(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__model

    @model.setter
    def model(self, value):  # через сеттер model устанавливаем приватное лок. св-ва self.__model экз. класса
        if self.__check_model(
                value):  # Вернет True если value строка и длина строки value входит в диапазон [2; 100]
            self.__model = value  # устанавливаем приватное лок. св-ва self.__model экз. класса

    @classmethod
    def __check_model(cls, value):  # Вернет True если value строка и длина строки value входит в диапазон [2; 100]
        """Метод проверят, что модель автомобиля - это строка; длина строки модели должна быть в диапазоне [2; 100]"""
        return isinstance(value, str) and cls.MIN < len(value) < cls.MAX


#######################################################################################################################
class WindowDlg:
    MIN = -1  # атрибут класса. миним. критерий
    MAX = 10_001  # атрибут класса. макс. критерий

    def __init__(self, title, width, height):  # Инициал. лок. св-в экз. класса WindowDlg
        self.__title = title  # Инициал. приват. лок. св-ва экз. класса
        if self.__check_size_side(width):  # метод вернет True если value явл. целым числом в диапазоне [0; 10000]
            self.__width = width  # Инициал. приват. лок. св-ва экз. класса
        if self.__check_size_side(height):  # метод вернет True если value явл. целым числом в диапазоне [0; 10000]
            self.__height = height  # Инициал. приват. лок. св-ва экз. класса

    @property  # объект св-во
    def width(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__width

    @width.setter
    def width(self, value):  # через сеттер width устанавливаем приватное лок. св-ва self.__width экз. класса
        if self.__width != value:  # Если предыдущ. знач. равно value то False и ничего не делаем, если предыдущ. знач.
            if self.__check_size_side(value):  # не равно value то провер. value методом __check_size_side
                self.__width = value  # Инициал. приват. лок. св-ва экз. класса
                self.show()  # отображаем на экране строку с измененными данными

    @property  # объект св-во
    def height(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__height

    @height.setter
    def height(self, value):  # через сеттер height устанавливаем приватное лок. св-ва self.__height экз. класса
        if self.__height != value:  # Если предыдущ. знач. равно value то False и ничего не делаем, если предыдущ. знач.
            if self.__check_size_side(value):  # не равно value то провер. value методом __check_size_side
                self.__height = value  # Инициал. приват. лок. св-ва экз. класса
                self.show()  # отображаем на экране строку с измененными данными

    @classmethod
    def __check_size_side(cls, value):  # метод вернет True если value явл. целым числом в диапазоне [0; 10000]
        return isinstance(value, int) and cls.MIN < value < cls.MAX  # иначе False

    def show(self):  # отображает на экране строку в формате "Окно : 100, 50"
        return f"{self.__title}: {self.width}, {self.height}"


#######################################################################################################################
class StackObj:

    def __init__(self, data, next=None):  # Инициал. лок. св-в экз. класса StackObj
        self.__data = data  # Инициал. приватной лок. св-в экз. класса
        self.__next = next  # Инициал. приватной лок. св-в экз. класса

    @property  # объект св-во
    def data(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__data

    @data.setter  # через сеттер data устанавливаем приватное лок. св-ва self.__data экз. класса
    def data(self, value):
        self.__data = value

    @property  # объект св-во
    def next(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__next

    @next.setter  # через сеттер next устанавливаем приватное лок. св-ва self.__next экз. класса
    def next(self, obj):  # Проверка. Если новый obj ссылается на None или явл. объектом класса StackObj то
        if obj is None or isinstance(obj, StackObj):  # изменяем лок. св-во иначе ничего не делаем
            self.__next = obj


class Stack:

    def __init__(self):  # Инициал. лок. св-в экз. класса StackObj
        self.top = None

    def push(self, obj):
        """Добавление объекта класса StackObj в конец односвязного списка"""
        pointer = self.top  # Переменная pointer ссылается на лок. св-во self.top класса Stack
        if pointer is None:  # Если переменная pointer==None то нет первого объекта связн. списка и
            self.top = obj  # лок. св-во self.top будет ссылаться на первый созданный объект StackObj
            return  # Констр. с if pointer is None: отработает всего лишь один раз, когда в связ. списке нет объектов
            # StackObj , а далее self.top будет (ВСЕГДА) ссылается на первый объект StackObj связ. списка
        while pointer.next:  # смотрим куда ссылается лок. св-во self.__next pointer. Если None выходим из цикла.
            pointer = pointer.next  # если на объект то True и вх. в while. Двигаем текущий указатель pointer
            # по связ. списку. Снова заходим в конструкцию while. И так до послед. объекта.
        pointer.next = obj  # присваиваем лок. св-ву pointer self.__next ссылку на следующий объект obj

    def get_data(self):  # Вывод всех данных связанного списка
        """Получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта
         в порядке их добавления, или пустой список, если объектов нет)"""
        out_data = []  # создаем список out_data для добавления туда объектов связ. списка.
        pointer = self.top  # Переменная pointer ссылается на лок. св-во self.top, а это ВСЕГДА ссылка на первый
        # объект связ. списка. Устанавливаем pointer в начало списка
        while pointer:  # Проверяем текущ. объект связ. списка. Если != None то добавляем данные в список out_data
            out_data.append(pointer.data)  # добавляем данные текущ. объкта в out_data
            pointer = pointer.next  # Переопределяем ссылку с текущего обекта на следующий объект связ. списка

        return out_data  # вывод данных связ. списка в списке out_data

    def pop(self):
        """Извлечение последнего объекта с его удалением из односвязного списка"""
        pointer = self.top  # текущ. указатель pointer. Указывает на первый объект связ. списка
        if pointer.next is None:  # если лок. св-во self.__next pointer вернет None то в связ. списке 1 объект
            self.top = None  # лок. св-во self.top ссылаем на None. связ. списк полностью пуст
            return pointer  # Возвращаем первый (единственный) объект связн. списка
        while pointer.next.next:  # смотрим на что указывает (указатель self.__next) следующего объекта
            pointer = pointer.next  # Если None то мы текущ. указателю устан. знач. None. Если True то двиг. pointer
        last_obj = pointer.next  # создаем ссылку на последний объект связ. списка, чтобы потом вернуть
        pointer.next = None  # Мы предпослед. объекту связ. списка лок. св-ву self.__next указыв. ссылку на None

        return last_obj  # Возвращаем последний объект связ. списка


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()


# res = st.get_data()    # ['obj1', 'obj2']
#######################################################################################################################
class RadiusVector2D:
    MIN_COORD = -101  # атрибут класса. миним. критерий
    MAX_COORD = 1025  # атрибут класса. маским. критерий

    def __init__(self, x=0, y=0):  # Инициал. лок. св-в экз. класса RadiusVector2D
        self.__x = x if self.__check_value(x) else 0  # проверка переданного знач. и инициал. его либо 0
        self.__y = y if self.__check_value(y) else 0  # проверка переданного знач. и инициал. его либо 0

    @property  # объект св-во
    def x(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__x

    @x.setter  # через сеттер x устанавливаем приватное лок. св-во self.__x экз. класса
    def x(self, value):
        if self.__check_value(value):  # проверка переданного знач. и установка его либо оставляем прежнее знач.
            self.__x = value

    @property  # объект св-во
    def y(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__y

    @y.setter  # через сеттер y устанавливаем приватное лок. св-во self.__y = value экз. класса
    def y(self, value):
        if self.__check_value(value):  # проверка переданного знач. и установка его либо оставляем прежнее знач.
            self.__y = value

    @classmethod
    def __check_value(cls, num):  # Вернет True если условие истина иначе False
        """Значение должно быть числом (целым или вещественным) в диапазоне [MIN_COORD; MAX_COORD]"""
        return type(num) in (int, float) and cls.MIN_COORD < num < cls.MAX_COORD

    @staticmethod
    def norm2(vector):  # Вернет значение квадратической нормы вектора
        """метод вычисляет квадратическую норму (квадратическая норма вектора: x*x + y*y)."""
        return vector.x ** 2 + vector.y ** 2


#####################################################################################################################
class TreeObj:

    def __init__(self, indx, value=None):  # Инициал. лок. св-в экз. класса TreeObj
        self.indx = indx  # Инициал. лок. св-в экз. класса TreeObj
        self.value = value  # Инициал. лок. св-в экз. класса TreeObj
        self.left = self.right = None  # Инициал. лок. св-в экз. класса TreeObj. По умолчанию None

    @property
    def left(self):  # объект св-во
        return self.__left  # Геттер. Возвращает приват. лок. св-во экз. класса

    @left.setter
    def left(self, obj):  # Через сеттер left уст. приват. лок. Св-во self.__left = obj экз. класса
        self.__left = obj

    @property
    def right(self):  # объект св-во
        return self.__right  # Геттер. Возвращает приват. лок. св-во экз. класса

    @right.setter
    def right(self, obj):  # через сеттер right уст. приват. лок. св-во self.__right = obj экз. класса
        self.__right = obj


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        """Метод проходит по решающему дереву для вектора x из корневого узла дерева root и возвращает конеч. знач."""
        pointer = root  # pointer ссылается на первый узел дерева (вершина)
        while pointer.left or pointer.right:  # в цикле while смотрим на что указ. лок. св-ва pointer. None или объект.
            pointer = pointer.left if x[
                pointer.indx] else pointer.right  # ссылаем pointer на new obj. (left or right)

        return pointer.value  # Возвращаем значение объекта на что указывает pointer

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        """Метод добавляет объект в решающее дерево и возвращает добавленную вершину - объект класса TreeObj"""
        if node:  # Если node==None, то вернет объект иначе, будут пров. следующ. условие.
            setattr(node, 'left' if left else 'right', obj)  # Если left==True, то к переданному объекту node через
            # объект св-во left указ. ссылку на новый obj иначе через объект св-во right
        return obj  # возвращаем добавленную вершину - объект класса TreeObj


# root = DecisionTree.add_obj(TreeObj(0))  # Добавление вершины решающего дерева
# v_11 = DecisionTree.add_obj(TreeObj(1), root)  # Добавление левого элемента к вершине решающего дерева
# v_12 = DecisionTree.add_obj(TreeObj(2), root, False)  # Добавление правого элемента к вершине решающего дерева
# DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)  # Добавление левого листового элем. к v_11
# DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)  # Добавление правого листового элем. к v_11
# DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)  # Добавление левого листового элем. к v_12
# DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)  # Добавление правого листового элем. к v_12
#
# x = [1, 1, 0]   # вектор х с бинарными значениями
# res = DecisionTree.predict(root,  x)  # вернет значение - будет программистом
# print(res)  # выведет в консоль будет программистом
#####################################################################################################################
class LineTo:

    def __init__(self, x=0, y=0):  # Инициал. лок. св-в экз. класса LineTo
        self.x = x             # Инициал. лок. св-в экз. класса LineTo
        self.y = y             # Инициал. лок. св-в экз. класса LineTo


class PathLines:

    def __init__(self, *line_obj):  # Инициал. лок. св-в экз. класса PathLines
        self.objects = list((LineTo(), ) + line_obj)  # Инициал. лок. св-ва (списка objects). Перв. эл. (0, 0)

    def get_path(self):
        """Возвращает список из объектов класса LineTo (если объектов нет, то пустой список);"""
        return self.objects[1:]  # Возвращает срез лок. св-ва (списка objects). А это объекты класса LineTo

    def add_line(self, line):
        """Добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута."""
        self.objects.append(line)   # Добавляет объект класса LineTo в конец списка

    def get_length(self):
        """Возвращает суммарную длину пути (сумма длин всех линейных сегментов)"""
        return sum(map(self.distance, self.objects, self.get_path()))

    @staticmethod
    def distance(p_0: LineTo, p_1: LineTo):
        """Возвращает расстояние между двумя точками"""
        return ((p_1.x - p_0.x) ** 2 + (p_1.y - p_0.y) ** 2) ** 0.5


# p = PathLines(LineTo(1, 2))
# print(p.get_length())  # 2.23606797749979
# p.add_line(LineTo(10, 20))
# p.add_line(LineTo(5, 17))
# print(p.get_length())  # 28.191631669843197
# m = p.get_path()
# print(all(isinstance(i, LineTo) for i in m) and len(m) == 3)  # True
#
# h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
# print(h.get_length())  # 71.8992593599813
#
# k = PathLines()
# print(k.get_length())  # 0
# print(k.get_path())  #[]
#####################################################################################################################
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def add(num_1, num_2):
    return num_1 + num_2


def pprint():
    out = list(map(add, a, b))  # map(func, iter, iter) выполняется по наименьшему iter
    print(out)

# pprint()  # [11, 22, 33, 44, 55]
#####################################################################################################################
class PhoneNumber:
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя "
    CHARS = alphabet + alphabet.upper()

    def __init__(self, number, fio):  # Инициал. лок. св-в экз. класса PhoneNumber
        if self.__check_number(number) and self.__check_fio(fio):   # Проверка, что number число, а fio строка
            self.number = number
            self.fio = fio
        else:
            raise TypeError('Введены некорректные данные')

    @staticmethod
    def __check_number(x):
        """Возвращает True если х число и длина его равна 11"""
        return type(x) is int and len(str(x)) == 11

    @classmethod
    def __check_fio(cls, fio):
        """Вернет True если fio из рус. алфавита"""
        return set(fio) <= set(cls.CHARS)


class PhoneBook:

    def __init__(self):
        self.list_phone = []

    def add_phone(self, phone):
        """Добавляет объект класса PhoneNumber в лок. св-во self.list_phone класса PhoneBook"""
        self.list_phone.append(phone)

    def remove_phone(self, indx):
        """Удаляет объект класса PhoneNumber по индексу из лок. св-во self.list_phone класса PhoneBook"""
        del self.list_phone[indx]

    def get_phone_list(self):
        """Возвращает номера объектов класса PhoneNumber из лок. св-во self.list_phone класса PhoneBook"""
        return [obj.number for obj in self.list_phone]


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
#####################################################################################################################


