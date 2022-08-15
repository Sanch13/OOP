class PointI:
    def __new__(cls, *args, **kwargs):  # __new__ Вызывается непосредственно перед созданием объекта класса
        # магический метод __new__ должен возвращать адрес нового созданного объекта. этот метод всегда вызывается при
        # создании нового объекта. При необходимости, мы можем его переопределять, добавляя новую логику его работы.
        # И то же самое относится ко всем магическим методам. Они всегда существуют у всех классов. Но переопределяем
        # мы лишь те, что необходимо, а остальные работают по умолчанию. В этом сила базового класса object. В нем уже
        # существует программный код, общий для всех классов языка Python. Иначе, нам пришлось бы его каждый раз прописывать заново.
        print('вызов __new__ для ' + str(cls))  # вывод сообщения и переменной cls
        return super().__new__(cls)  # функция super() возвращает ссылку на базовый класс и через нее мы вызываем
                                    # метод __new__ с одним первым аргументом.

    def __init__(self, x=0, y=0):   #  метод __init__ вызывается после создания объекта
        print('вызов __init__ для ' + str(self))
        self.x = x
        self.y = y

# pt = PointI(1, 2)
# print(pt)
################################################################################################################
class DataBase: # Пример паттерна Singleton
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('закрытие соединения с БД')

    def read(self):
        return 'данные из БД'

    def write(self,data):
        print(f'запись в БД {data}')


# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)
# print(id(db), id(db2))
# db.connect()
# db2.connect()
################################################################################################################
class AbstractClass:
    def __new__(cls, *args, **kwargs):    # Переопределение метода __new__. Запрещает создавать экз. класса.
                                          # Возвращает строку текста
        return f'Ошибка: нельзя создавать объекты абстрактного класса'
################################################################################################################
class SingletonFive:
    __count = 0    # атрибут класса. счетчик инициализируем 0
    __link = None  # атрибут класса. Будем использовать для ссылки на объект

    def __new__(cls, *args, **kwargs):  # Переопределение метода __new__. После 5 создан. объекта будет постоянно
                                        # ссылаться на 5 объект класса
        if cls.__count < 5:     # если атриб. класса cls.__count < 5 то True
            cls.__link = super().__new__(cls)   # создаем объект и атриб. класса cls.__link ссылается на созданный
            cls.__count += 1    # объект. Увеличиваем атр. класса cls.__count на +1. Когда cls.__count == 5
                                # то условие If больше не выполняется и cls.__count будет всегда равен 5. А арт.
                                # класса cls.__link будет ссылаться на пятый созданный объект класса
        return cls.__link       # Возврат атр. класса который ссылается на созданный объект

    def __init__(self, name):   # инициализируем объект класса
        self.name = name        # в каждом объекте класса SingletonFive будет свое лок. св-во self.name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
# for k, v in enumerate(objs):
#     print(f'{v} --> {k + 1}', v.__dict__)
################################################################################################################
TYPE_OS = 1  # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):  # Изменяем логику метода __new__. Метод будет возвращать экз. других классов
        if TYPE_OS != 1:    # Если TYPE_OS != 1 создаем экзепляр класса DialogLinux
            obj = super().__new__(DialogLinux)  # переменная obj ссылается на экзепляр класса DialogLinux
            obj.name = args[0]  # в экзепляре класса DialogLinux создаем лок. св-во name и ссылаем его на переданное
                                # значение в *args. Берем первый элем. кортежа args[0]
            return obj          # Возвращаем экзепляр класса DialogLinux
        obj = super().__new__(DialogWindows)  # переменная obj ссылается на экзепляр класса DialogWindows
        obj.name = args[0]  # в экзепляре класса DialogWindows создаем лок. св-во name и ссылаем его на переданное
                            # значение в *args. Берем первый элем. кортежа args[0]

        return obj          # Возвращаем экзепляр класса DialogWindows

# dlg = Dialog('123')
# print(dlg.__dict__, dlg.name_class, isinstance(dlg, DialogWindows))  # {'name': '123'} DialogWindows True
# TYPE_OS = 2
# dlg2 = Dialog('456')
# print(dlg2.__dict__, dlg2.name_class, isinstance(dlg2, DialogLinux))  # {'name': '456'} DialogLinux True
################################################################################################################
class Point:
    def __init__(self, x, y):   # Инициализируем экз. класса Point
        self.__x = x            # У каждого экз. класса будут свои лок. св-ва self.__x, self.__y
        self.__y = y

    def clone(self):
        return Point(self.__x, self.__y)    # создаем новый экз. класса и передаем ему в качестве параметров
                                # лок. св-ва предыдущего созданного экз. класса Point. В наш. случаи (pt = Point(3, 5))

    # def clone(self):
    #     new_clone = super().__new__(type(self))
    #     new_clone.__dict__.update(self.__dict__)
    #     return new_clone


pt = Point(3, 5)        # создаем экз. класса Point с пар-ми (3, 5)
pt_clone = pt.clone()   # Через метод clone создаем нов. экз. класса и обратимся к лок. св-вам объекта pt
# print(id(pt), id(pt_clone))  # 2444358680976 2444358680880 Разные объекты
# print(pt.__dict__, pt_clone.__dict__)   # {'_Point__x': 3, '_Point__y': 5} {'_Point__x': 3, '_Point__y': 5}
################################################################################################################
class Factory:
    def build_sequence(self):   # метод возвращает пустой список
        return []

    def build_number(self, string):   # метод возвращает данные в тип float
        return float(string)

class Loader:
    def parse_format(self, string, factory):   # метод возвращает список определенного выходного формата
                    # (парсер - обработчик строки). string - строка данных. factory - ссылка на объект класса Factory
        seq = factory.build_sequence()  # через ссылку на объект обратимся к методу build_sequence() класса Factory.
                                # переменная seq будет ссылаться на пустой список [] который вернет build_sequence()
        for sub in string.split(","):   # стоку данных string разбиваем на последовательность и проходим по очереди
            item = factory.build_number(sub)    # переменная item будет ссылаться на вернувшиеся float значение
                                            # функции build_number() короую вызвали через ссылку factory
            seq.append(item)    # добавление item в список seq

        return seq  # Возврат списка


ld = Loader()   # создание экземпляра класса Loader
s = input()     # ввод данных
res = ld.parse_format(s, Factory())  # в переменную res вернется список из метода parse_format объекта ld класса Loader
print(res)

