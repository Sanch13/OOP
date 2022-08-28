class ObjList:
    def __init__(self, data):  # Инициал. лок. св-в экз. класса ObjList
        self.__next = self.__prev = None        # Инициал. лок. св-в экз. класса. По умолчанию None
        self.set_data(data)        # Инициал. лок. св-ва экз. класса.

    def set_next(self, obj):    # через сеттер set_next устанавливаем приватные лок. св-ва экз. класса
        self.__next = obj

    def set_prev(self, obj):    # через сеттер set_prev устанавливаем приватные лок. св-ва экз. класса
        self.__prev = obj

    def set_data(self, data):    # через сеттер set_data устанавливаем приватные лок. св-ва экз. класса
        self.__data = data

    def get_next(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__next

    def get_prev(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__prev

    def get_data(self):  # геттер. Возвращает приватное лок. св-во экз. класса
        return self.__data

class LinkedList:

    def __init__(self, head=None, tail=None):  # Инициал. лок. св-в экз. класса LinkedList
        self.head = head        # Инициал. лок. св-в экз. класса. По умолчанию None
        self.tail = tail

    def add_obj(self, obj):   # Добавление объекта в связанный список
        """Метод добавляет объект (obj) в связанный список LinkedList"""
        if self.head is None:    # Если лок. св-во self.head == None то нет первого объекта связн. списка и
            self.head = self.tail = obj  # лок. св-во self.head и self.tail будет ссылаться на первый созданный объект
            return  # Конструкция с if self.head is None: отработает всего лишь один раз, когда в связанном списке
                    # нет объектов, а далее self.head будет постоянно ссылается на первый объект связанного списка
        self.tail.set_next(obj)  # self.tail ссылается на послед. объект св. списка. Мы его лок. св-ву self.__next
                                 # установим ссылку на новый объект obj.
        obj.set_prev(self.tail)  # установим новому объекту obj его лок. св-во self.__prev. ссылка на предыдущ. obj
        self.tail = obj          # self.tail установим ссылку на новый obj. Он теперь последний объект связн. списка

    def remove_last_obj(self):  # удаление последнего объекта связ. списка
        """Удаляет последний объект связанного списка"""
        if self.head.get_next() is None:  # смотрим куда ссылается первый объект связн. списка. Если на None то в связн.
            self.head = self.tail = None  # списке только 1 объект. лок. св-вам делаем ссылку на None. Таким образом
            return                        # на 1 объект нет ни одной ссылки. Выходим из метода return
        self.tail = self.tail.get_prev()  # лок. св-ву self.tail указываем ссылку на предыдущий объект связн. списка.
        self.tail.set_next(None)          # теперь self.tail ссылается на предыдущий объект связ. списка.
                                    # предыдущему объекту связн. списка лок. св-ву self.__next устан. ссылку на None
                                    # на посл. объект связ. списка нет ни одной ссылки и он удалится сборщ. мусора

    def get_data(self):    # Вывод всех данных связанного списка
        """Возвращает все данные связанного списка """
        cur_obj = self.head   # Так как у нас уже создан связанный список то лок. св-во self.head  ВСЕГДА ссылается
                            # на первый объект связ. списка. Если связ. список пуст то self.head = None и
                            # метод show_data(self) ничего не выведет. Текущ. указат. cur_obj указыв. на первый объект
        out_data = []       # создаем пустой список out_data для добавления туда данных объектов связ. списка.
        while cur_obj:     # Проверяем текущ. объект связ. списка. Если != None то добавляем данные в список out_data
            out_data.append(cur_obj.get_data())    # добавляем данные текущ. объкта в out_data через метод get_data()
            cur_obj = cur_obj.get_next()  # Переопределяем ссылку с текущего обекта на следующий объект связ. списка
        return out_data                 # возвращает данные связ. списка в списке out_data



lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.remove_last_obj()
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)