# Подвиг 2. Объявите класс Record (запись), который описывает одну произвольную запись из БД.
# Объекты этого класса создаются командой:
# r = Record(field_name1=value1,... , field_nameN=valueN)
# где field_nameX - наименование поля БД; valueX - значение поля из БД.
# В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты
# по именам полей (field_name1,... , field_nameN) с соответствующими значениями. Например:
# r = Record(pk=1, title='Python ООП', author='Балакирев')
# В объекте r появляются атрибуты:
# r.pk # 1
# r.title # Python ООП
# r.author # Балакирев
# Также необходимо обеспечить доступ к этим полям (чтение/запись) через индексы следующим образом:
# r[0] = 2 # доступ к полю pk
# r[1] = 'Супер курс по ООП' # доступ к полю title
# r[2] = 'Балакирев С.М.' # доступ к полю author
# print(r[1]) # Супер курс по ООП
# r[3] # генерируется исключение IndexError
# Если указывается неверный индекс (не целое число или некорректное целое число), то должно
# генерироваться исключение командой:
# raise IndexError('неверный индекс поля')
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
# P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record.


def check_index(func):
    def wrapper(obj, indx, *args, **kwargs):
        if isinstance(indx, int) and 0 <= indx < len(obj):
            return func(obj, indx, *args, **kwargs)
        raise IndexError('неверный индекс поля')

    return wrapper


class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def __len__(self):
        return len(self.__dict__)

    @check_index
    def __getitem__(self, item):
        return list(self.__dict__.values())[item]

    @check_index
    def __setitem__(self, key, value):
        self.__dict__[list(self.__dict__.keys())[key]] = value


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.__dict__)
print(r[2])
r[1] = 'Супер курс по ООП'
print(r.__dict__)
