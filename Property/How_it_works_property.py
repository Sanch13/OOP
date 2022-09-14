class Person:
    # old = 4  # атрибут класса Person

    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    # def get_old(self):
    #     return self.__old
    #
    # def set_old(self, old):
    #     self.__old = old
    #
    # def del_old(self):
    #     del self.__old
    #
    # old = property()
    # old = old.setter(set_old)
    # old = old.getter(get_old)
    # old = old.deleter(del_old)

    @property
    def old(self):         # объект-свойство old. Возвращает значение приватной переменной
        return self.__old  # __old: p.old экземпляра р класса Person

    @old.setter           # объект-свойство old. Устанавливает значение приватной переменной
    def old(self, old):   # __old: p.old = 10 через присваевание объект-свойства экземпляра р
        self.__old = old  # класса Person

    @old.deleter    # метод делитер, который вызывается при удалении свойства:
    def old(self):  # del p.old удаляет old из экземпляра p класса Person
        del self.__old

"""
Если в классе задан атрибут как объект-свойство, то в первую очередь выбирается оно, 
даже если в экземпляре класса есть локальное свойство с таким же именем.
Приоритет такой (если локальное свойство с таким же именем): 
1) Объект-свойство.
2) Локальное свойство в экземпляре класса.
3) Обращается в класс Person
"""

p = Person('Aliaksander', 37)  # создаем экземпляр p класса Person с данными name, old
print(p.__dict__, '---1')   # {'_Person__name': 'Aliaksander', '_Person__old': 37} ---1
p.__dict__['old'] = 'old in obj p'  # создаем локальную переменную 'old' в экземпляре p класса Person
print(p.old, p.__dict__, '---2')  # 37 {'_Person__name': 'Aliaksander', '_Person__old': 37, 'old': 'old in obj p'} ---2
p.old = 33  # изменяем p.old = 37 через присваевание объект-свойства old на p.old = 33
print(p.old, p.__dict__, '---3')  # 33 {'_Person__name': 'Aliaksander', '_Person__old': 33, 'old': 'old in obj p'} ---3
del p.old   # удаляем свойство old из экземпляра p класса Person
print(p.__dict__['old'], p.__dict__, '---4')  # old in obj p {'_Person__name': 'Aliaksander', 'old': 'old in obj p'} ---4
p.old = 10  # Устанавливает значение приватной переменной __old: через присваевание объект-свойства p.old = 10
print(p.old, p.__dict__, '---5')  # 10 {'_Person__name': 'Aliaksander', 'old': 'old in obj p', '_Person__old': 10} ---5

