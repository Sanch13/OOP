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
    MIN = 1     # атрибут класса. миним. критерий
    MAX = 101   # атрибут класса. макс. критерий

    def __init__(self, model=None):  # Инициал. лок. св-в экз. класса Car
        self.__model = model            # Инициал. приватной лок. св-в экз. класса

    @property           # объект св-во
    def model(self):    # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__model

    @model.setter
    def model(self, value):            # через сеттер model устанавливаем приватное лок. св-ва self.__model экз. класса
        if self.__check_model(value):  # Вернет True если value строка и длина строки value входит в диапазон [2; 100]
            self.__model = value       # устанавливаем приватное лок. св-ва self.__model экз. класса

    @classmethod
    def __check_model(cls, value):  # Вернет True если value строка и длина строки value входит в диапазон [2; 100]
        """Метод проверят, что модель автомобиля - это строка; длина строки модели должна быть в диапазоне [2; 100]"""
        return isinstance(value, str) and cls.MIN < len(value) < cls.MAX
#######################################################################################################################
class WindowDlg:
    MIN = -1        # атрибут класса. миним. критерий
    MAX = 10_001    # атрибут класса. макс. критерий

    def __init__(self, title, width, height):  # Инициал. лок. св-в экз. класса WindowDlg
        self.__title = title                   # Инициал. приват. лок. св-ва экз. класса
        if self.__check_size_side(width):      # метод вернет True если value явл. целым числом в диапазоне [0; 10000]
            self.__width = width               # Инициал. приват. лок. св-ва экз. класса
        if self.__check_size_side(height):     # метод вернет True если value явл. целым числом в диапазоне [0; 10000]
            self.__height = height             # Инициал. приват. лок. св-ва экз. класса

    @property           # объект св-во
    def width(self):    # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__width

    @width.setter
    def width(self, value):   # через сеттер width устанавливаем приватное лок. св-ва self.__width экз. класса
        if self.__width != value:   # Если предыдущ. знач. равно value то False и ничего не делаем, если предыдущ. знач.
            if self.__check_size_side(value):  # не равно value то провер. value методом __check_size_side
                self.__width = value           # Инициал. приват. лок. св-ва экз. класса
                self.show()                    # отображаем на экране строку с измененными данными

    @property            # объект св-во
    def height(self):    # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__height

    @height.setter
    def height(self, value):   # через сеттер height устанавливаем приватное лок. св-ва self.__height экз. класса
        if self.__height != value:  # Если предыдущ. знач. равно value то False и ничего не делаем, если предыдущ. знач.
            if self.__check_size_side(value):  # не равно value то провер. value методом __check_size_side
                self.__height = value           # Инициал. приват. лок. св-ва экз. класса
                self.show()                     # отображаем на экране строку с измененными данными

    @classmethod
    def __check_size_side(cls, value):  # метод вернет True если value явл. целым числом в диапазоне [0; 10000]
        return isinstance(value, int) and cls.MIN < value < cls.MAX  # иначе False

    def show(self):  # отображает на экране строку в формате "Окно : 100, 50"
        return f"{self.__title}: {self.width}, {self.height}"
#######################################################################################################################
class StackObj:

    def __init__(self, data, next=None):  # Инициал. лок. св-в экз. класса StackObj
        self.__data = data                # Инициал. приватной лок. св-в экз. класса
        self.__next = next                # Инициал. приватной лок. св-в экз. класса

    @property          # объект св-во
    def data(self):    # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__data

    @data.setter       # через сеттер data устанавливаем приватное лок. св-ва self.__data экз. класса
    def data(self, value):
        self.__data = value

    @property          # объект св-во
    def next(self):    # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__next

    @next.setter       # через сеттер next устанавливаем приватное лок. св-ва self.__next экз. класса
    def next(self, obj):    # Проверка. Если новый obj ссылается на None или явл. объектом класса StackObj то
        if obj is None or isinstance(obj, StackObj):    # изменяем лок. св-во иначе ничего не делаем
            self.__next = obj


class Stack:

    def __init__(self):  # Инициал. лок. св-в экз. класса StackObj
        self.top = None

    def push(self, obj):
        """Добавление объекта класса StackObj в конец односвязного списка"""
        pointer = self.top    # Переменная pointer ссылается на лок. св-во self.top класса Stack
        if pointer is None:    # Если переменная pointer==None то нет первого объекта связн. списка и
            self.top = obj  # лок. св-во self.top будет ссылаться на первый созданный объект StackObj
            return  # Констр. с if pointer is None: отработает всего лишь один раз, когда в связ. списке нет объектов
                    # StackObj , а далее self.top будет (ВСЕГДА) ссылается на первый объект StackObj связ. списка
        while pointer.next:  # смотрим куда ссылается лок. св-во self.__next pointer. Если None выходим из цикла.
            pointer = pointer.next  # если на объект то True и вх. в while. Двигаем текущий указатель pointer
                                    # по связ. списку. Снова заходим в конструкцию while. И так до послед. объекта.
        pointer.next = obj  # присваиваем лок. св-ву pointer self.__next ссылку на следующий объект obj

    def get_data(self):    # Вывод всех данных связанного списка
        """Получение списка из объектов односвязного списка (список из строк локального атрибута __data каждого объекта
         в порядке их добавления, или пустой список, если объектов нет)"""
        out_data = []         # создаем список out_data для добавления туда объектов связ. списка.
        pointer = self.top    # Переменная pointer ссылается на лок. св-во self.top, а это ВСЕГДА ссылка на первый
                              # объект связ. списка. Устанавливаем pointer в начало списка
        while pointer:        # Проверяем текущ. объект связ. списка. Если != None то добавляем данные в список out_data
            out_data.append(pointer.data)    # добавляем данные текущ. объкта в out_data
            pointer = pointer.next  # Переопределяем ссылку с текущего обекта на следующий объект связ. списка

        return out_data  # вывод данных связ. списка в списке out_data

    def pop(self):
        """Извлечение последнего объекта с его удалением из односвязного списка"""
        pointer = self.top          # текущ. указатель pointer. Указывает на первый объект связ. списка
        if pointer.next is None:    # если лок. св-во self.__next pointer вернет None то в связ. списке 1 объект
            self.top = None         # лок. св-во self.top ссылаем на None. связ. списк полностью пуст
            return pointer          # Возвращаем первый (единственный) объект связн. списка
        while pointer.next.next:    # смотрим на что указывает (указатель self.__next) следующего объекта
            pointer = pointer.next  # Если None то мы текущ. указателю устан. знач. None. Если True то двиг. pointer
        last_obj = pointer.next     # создаем ссылку на последний объект связ. списка, чтобы потом вернуть
        pointer.next = None         # Мы предпослед. объекту связ. списка лок. св-ву self.__next указыв. ссылку на None

        return last_obj             # Возвращаем последний объект связ. списка

st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']
#######################################################################################################################
