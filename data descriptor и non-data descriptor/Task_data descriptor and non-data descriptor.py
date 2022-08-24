class FloatValue:

    @staticmethod
    def __check_value(value):
        """Если число не вещественное, то сгенерируется исключение"""
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):  # В этом методе мы формируем лок. св-во с именем атрибута.
        self.name = '_' + name

    def __get__(self, instance, owner):  # метод возвращ. знач. лок. св-ва из экз. класса
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__check_value(value)  # Проверяем чтобы value было веществ. числом.
        setattr(instance, self.name, value)  # Обращ. к экз. класса и его лок. св-ву уст. знач. value


class Cell:
    value = FloatValue()  # Cоздаем атрибут 'value' как объект класса FloatValue

    def __init__(self, value=0.0):  # Инициал. лок. св-в экз. класса Cell. По умолч. value=0.0
        self.value = value  # Инициал. лок. св-в экз. класса Cell


class TableSheet:

    def __init__(self, N, M):  # Инициал. лок. св-в экз. класса TableSheet.
        self.N = N  # Инициал. лок. св-в (строка) экз. класса TableSheet.
        self.M = M  # Инициал. лок. св-в экз. (столбец) класса TableSheet.
        self.cells = [[Cell() for _ in range(M)] for _ in range(N)]  # Инициал. лок. св-в cells (список сост.
        # из объектов Cell. По умолчанию список заполняется Cell(value=0.0)).


table = TableSheet(5, 3)  # Созд. объект кл. TableSheet. В нем есть лок. св-во cells со списком 5 на 3.
count = 1  # Уст. счетчик на 1
for i in range(table.N):  # Проходим по внеш. списку (строка)
    for j in range(table.M):  # Проходим по внут. списку внеш. списка (столбец)
        table.cells[i][j] = Cell(float(count))  # Уст. в яч. table.cells объекты Cells с знач. float(count)
        count += 1  # Увеличиваем счетчик на 1


############################################################################################################


class ValidateString:

    def __init__(self, min_length=3, max_length=100):  # Инициал. лок. св-в экз. класса по умолч.
        self.min_length = min_length                   # Инициал. лок. св-в экз. класса ValidateString
        self.max_length = max_length                   # Инициал. лок. св-в экз. класса ValidateString

    def validate(self, string):
        """Возвр. True, если string явл. стр. (тип str) и длина стр. в пределах [min_length; max_length]"""
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class StringValue:

    def __init__(self, validator=ValidateString()):  # Инициал. лок. св-в экз. класса StringValue
        self.validator = validator  # лок. св-в экз. класса - это ссылка на объект класса ValidateString

    def __set_name__(self, owner, name):    # В этом методе мы формируем лок. св-во с именем атрибута.
        self.name = '_' + name

    def __get__(self, instance, owner):     # метод возвращ. знач. лок. св-ва из экз. класса
        return getattr(instance, self.name)

    def __set__(self, instance, value):     # метод уст. знач. value лок. св-ву экз. класса
        if self.validator.validate(value):  # Провер. чтобы пар-тр value явл. тип str и был в диапазоне.
            setattr(instance, self.name, value)  # Обращ. к экз. класса и его лок. св-ву и уст. знач. value.

class RegisterForm:
    login = StringValue()     # Cозд. атр. 'login' как объект класса StringValue
    password = StringValue()  # Cозд. атр. 'password' как объект класса StringValue
    email = StringValue()     # Cозд. атр. 'email' как объект класса StringValue

    def __init__(self, login, password, email):  # Инициал. лок. св-в экз. класса RegisterForm
        self.login = login        # Инициал. лок. св-в экз. класса RegisterForm
        self.password = password  # Инициал. лок. св-в экз. класса RegisterForm
        self.email = email        # Инициал. лок. св-в экз. класса RegisterForm

    def get_fields(self):
        """Возвращает список из значений полей в порядке [login, password, email]"""
        return [self.login, self.password, self.email]

    def show(self):
        """Выводит в консоль многострочную строку в формате"""
        print('<form>', \
              f"Логин: {self.login}", \
              f"Пароль: {self.password}", \
              f"Email: {self.email}", \
              '</form>', sep='\n')


# r = RegisterForm('11111', '1111111', '11111111')
# r.show()
# print(r.get_fields())
# frm = RegisterForm("123", "2345", "sc_lib@list.ru")
# print(frm.get_fields())
############################################################################################################


