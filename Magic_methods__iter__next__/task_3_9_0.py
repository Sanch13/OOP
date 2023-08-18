# Подвиг 5. Объявите в программе класс Person, объекты которого создаются командой:
# p = Person(fio, job, old, salary, year_job)
# где fio - ФИО сотрудника (строка); job - наименование должности (строка);
# old - возраст (целое число);
# salary - зарплата (число: целое или вещественное);
# year_job - непрерывный стаж на указанном месте работы (целое число).
# В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с
# такими же именами: fio, job, old, salary, year_job и соответствующими значениями.
# Также с объектами класса Person должны поддерживаться следующие команды:
# data = p[indx] # получение данных по порядковому номеру (indx) атрибута
# (порядок: fio, job, old, salary, year_job и начинается с нуля)
# p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
# for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
#     print(v)
# При работе с индексами, проверить корректность значения indx. Оно должно быть целым
# числом в диапазоне [0; 4]. Иначе, генерировать исключение командой:
# raise IndexError('неверный индекс')
# Пример использования класса (эти строчки в программе не писать):
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError
# P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно

def check_index(func):
    def wrapper(obj, indx, *args, **kwargs):
        if indx in [0, 1, 2, 3, 4]:
            return func(obj, indx, *args, **kwargs)
        raise IndexError('неверный индекс')

    return wrapper


class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.person = [self.fio, self.job, self.old, self.salary, self.year_job]

    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        if self.indx < len(self.person) - 1:
            self.indx += 1
            return self.person[self.indx]
        else:
            raise StopIteration

    @check_index
    def __getitem__(self, indx):
        return self.person[indx]

    @check_index
    def __setitem__(self, indx, value):
        self.person[indx] = value

    def __str__(self):
        return " ".join(map(str, self.person))


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# for el in pers:
#     print(el)
print(pers.__dict__[tuple(pers.__dict__)[0]])
