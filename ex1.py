# import sys
#
# # программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#
#
# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self, data):
#         for i in data:
#             self.lst_data.append(dict(zip(self.FIELDS, i.split())))
#
#     def select(self, a, b):
#         return self.lst_data[a:b + 1]
#
#
# db = DataBase()
# db.insert(lst_in)
# db.select(0, 1)
from string import ascii_letters, digits


# items = ascii_letters + digits + '@._'
# print(len(items))
# for k, v in enumerate(items):
#     print(k, v)
#
#
# email = 'Sanch13@gmail.com'
# print(set(email) <= set(items))
# if set(email) <= set(items):
#     print('YOOOOOOOOOOOO')
#
# if email.count('..') == 0:
#     print(True)
# else:
#     print(False)


# parts = email.split('@')
# print(parts)
# if not len(parts[0]) <= 100 and not len(parts[1]) <= 50:
#     print(False)
# else:
#     print(True)

# part = email.split('@')
# for k, v in enumerate(email):
#     print(k, v)
# print(len(email))
# print(f'{part[0]= }', len(part[0]))
# print(f'{part[1]= }', len(part[1]))
from random import randint

EMAIL_CHARS = ascii_letters + digits + '@._'
EMAIL_RAND_CHARS = ascii_letters + digits + '_'

n = randint(1, 20)
print(n)
length = len(EMAIL_RAND_CHARS) - 1
p = ''.join(EMAIL_RAND_CHARS[randint(0, length)] for _ in range(n)) + '@gmail.com'
print(p)