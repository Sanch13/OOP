class Data:
    __in = None

    def __new__(cls, *args, **kwargs):
        if cls.__in == None:  # то есть ЭК ещё ни разу не создавался !
            cls.__in = super().__new__(cls) # Наследование от базового класса Object,  super().__new__(cls)
        return cls.__in  # А если он уже был, тогда - просто возвращается прежнее super().__new__(cls)

    def __init__(self, name="Cary"):  # При создании ЭК ему передаётся один аргумент, или может не передаваться ничего
        self.name = name

    def get_name(self):  # Функция показывает значение атрибута name
        print(self.name, id(self.name))

    def get_in(self):
        print(self.__in)

    def set_in(self, inw):
        self.__in = inw


d = Data("Coca")  # Передаю имя Соса
d.get_name()  # Печатаю его
d2 = Data()  # Создаю ЭК, не передавая аргумента
d2.get_name()  # По умолчанию Cary
print(d.__dict__, id(d), d2.__dict__, id(d2))
Data.get_name(d)  # снова выводится Cary
d3 = Data("Gucha")  # Создаю ЭК, передаю имя Gucha
Data.get_name(d)  # Печатаю name ЭК -  d ( a не d3) = Gucha
# print(d.__dict__)  # Печатаю словарь d {'name': 'Gucha'} - там переопределяется атрибут name
# d.get_in()  # <__main__.Data object at 0x000001D3F01881F0>
# d.set_in("jjj")  # устанавливаю новое значение свойства __in
# d.get_in()  # Печатается jjj
# d2.get_in()  # Печатается jjj
# print(d.__dict__, d2.__dict__, d3.__dict__, sep="\n")
# {'name': 'Gucha', '_Data__in': 'jjj'}
# {'name': 'Gucha', '_Data__in': 'jjj'}
# {'name': 'Gucha', '_Data__in': 'jjj'}
print(id(d), id(d2), id(d3), sep="\n")
# 2009777865200
# 2009777865200
# 2009777865200
print(Data.__dict__)