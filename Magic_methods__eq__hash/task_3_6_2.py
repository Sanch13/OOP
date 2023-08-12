# Подвиг 7. Объявите класс с именем DataBase (база данных - БД),
# объекты которого создаются командой:
# db = DataBase(path)
# где path - путь к файлу с данными БД (строка).
# Также в классе DataBase нужно объявить следующие методы:
# write(self, record) - для добавления новой записи в БД, представленной объектом record;
# read(self, pk) - чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору
# pk (уникальное целое положительное число); запись ищется в значениях словаря (см. ниже)
# Каждая запись БД должна описываться классом Record, а объекты этого класса создаваться командой:
# record = Record(fio, descr, old)
# где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка);
# old - возраст человека (целое число).
# В каждом объекте класса Record должны формироваться следующие локальные атрибуты:
# pk - уникальный идентификатор записи (число: целое, положительное); формируется
# автоматически при создании каждого нового объекта;
# fio - ФИО человека (строка);
# descr - характеристика человека (строка);
# old - возраст человека (целое число).
# Реализовать для объектов класса Record вычисление хэша по атрибутам: fio и old
# (без учета регистра). Если они одинаковы для разных записей, то и хэши должны получаться равными.
# Также для объектов класса Record  с одинаковыми хэшами оператор == должен выдавать значение
# True, а с разными хэшами - False.
# Хранить записи в БД следует в виде словаря dict_db (атрибут объекта db класса DataBase),
# ключами которого являются объекты класса Record, а значениями список из объектов с равными хэшами:
# dict_db[rec1] = [rec1, rec2, ..., recN]
# где rec1, rec2, ..., recN - объекты класса Record с одинаковыми хэшами.
# Для наполнения БД прочитайте строки из входного потока с помощью команды:
# lst_in = list(map(str.strip, sys.stdin.readlines()))
# где каждая строка представлена в формате:
# "ФИО; характеристика; возраст"
# Например:
# Балакирев С.М.; программист; 33
# Кузнецов А.В.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 37
# Каждая строка должна быть представлена объектом класса Record и записана в БД db
# (в словарь db.dict_db).
# P.S. На экран ничего выводить не нужно.
# Sample Input:
# Балакирев С.М.; программист; 33
# Кузнецов Н.И.; разведчик-нелегал; 35
# Суворов А.В.; полководец; 42
# Иванов И.И.; фигурант всех подобных списков; 26
# Балакирев С.М.; преподаватель; 33
# Sample Output:

class Record:
    PK = 0

    def __new__(cls, *args, **kwargs):
        cls.PK += 1
        return super().__new__(cls)

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old
        self.pk = self.__class__.PK

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)


class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        list_rec_obj = list(self.dict_db.values())
        while list_rec_obj:
            rec_obj = list_rec_obj.pop(0)
            if isinstance(rec_obj, list):
                list_rec_obj.extend(rec_obj)
            elif rec_obj.pk == pk:
                return rec_obj

    def read_all_objects(self):
        lst_rec_obj = list(self.dict_db.values())
        lst_out = []
        for obj in lst_rec_obj:
            if isinstance(obj, list):
                lst_rec_obj.extend(obj)
            else:
                lst_out.append(obj)
        return lst_out


lst_in = ['Балакирев С.М.; программист; 33',
          'Кузнецов Н.И.; разведчик-нелегал; 35',
          'Суворов А.В.; полководец; 42',
          'Иванов И.И.; фигурант всех подобных списков; 26',
          'балакирев С.М.; преподаватель; 33'
          ]


db = DataBase("path")

for obj in lst_in:
    fio, descr, old = obj.split("; ")
    rec_obj = Record(fio, descr, int(old))
    db.write(rec_obj)


# print(db.dict_db)
# print([(i.pk, i.descr) for i in db.read_all_objects()])
# print(db.read(5).fio)
# r1 = Record('Балакирев С.М.', 'программист', 33)
# r2 = Record('балакирев С.М.', 'преподаватель', 33)
# print(r1 == r2, hash(r1), hash(r2), id(r1), id(r2))

# db22345 = DataBase('123')
# r1 = Record('fio', 'descr', 10)
# r2 = Record('fio', 'descr', 10)
# assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"
#
# db22345.write(r2)
# r22 = db22345.read(r2.pk)
# assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"
#
# assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"
#
# fio = lst_in[0].split(';')[0].strip()
# v = list(db.dict_db.values())
# if fio == "Балакирев С.М.":
#     assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
#         v[3]) == 1, "неверно сформирован словарь dict_db"
#
# if fio == "Гейтс Б.":
#     assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
#         v[3]) == 1, "неверно сформирован словарь dict_db"
