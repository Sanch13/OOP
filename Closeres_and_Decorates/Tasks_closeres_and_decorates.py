"""
Используя замыкания функций, определите вложенную функцию, которая бы увеличивала значение
переданного параметра на 5 и возвращала бы вычисленный результат.
При этом внешняя функция должна иметь следующую сигнатуру:
def counter_add(): ...
Вызовите функцию counter_add и результат ее работы присвойте переменной с именем cnt.
 Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
k = int(input())
Выведите результат на экран.
Sample Input:
7
Sample Output:
12
"""
# k = int(input())
#
#
# def counter_add():
#     def wrapper(step):
#         return step + 5
#
#     return wrapper
#
#
# cnt = counter_add()
# print(cnt(k))
###################################################################################################
"""
Используя замыкания функций, объявите внутреннюю функцию, которая увеличивает значение 
своего аргумента на некоторую величину n - параметр внешней функции с сигнатурой:
def counter_add(n): ...
Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте 
переменной cnt. Вызовите внутреннюю функцию через переменную cnt со значением k,
введенным с клавиатуры:
k = int(input())
Выведите результат на экран.
Sample Input:
5
Sample Output:
7
"""
# k = int(input())
#
#
# def counter_add(n):
#     def wrapper(step):
#         nonlocal n
#         return step + n
#
#     return wrapper
#
#
# cnt = counter_add(2)
# print(cnt(k))
###################################################################################################
"""
Используя замыкания функций, объявите внутреннюю функцию, которая заключает в тег h1 строку s 
(s - строка, параметр внутренней функции). Далее, на вход программы поступает строка и ее 
нужно поместить в тег h1 с помощью реализованного замыкания. Результат выведите на экран.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
Sample Input:
Balakirev
Sample Output:
<h1>Balakirev</h1>
"""
# s = input()
#
#
# def add_string(s):
#     def tag_h1():
#         nonlocal s
#         return f'<h1>{s}</h1>'
#
#     return tag_h1
#
#
# h1 = add_string(s)
# print(h1())
###################################################################################################
"""
Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s 
(s - строка, параметр внутренней функции) в произвольный тег, содержащийся в переменной 
tag - параметре внешней функции. 
Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым 
содержимым. Вторую строку нужно поместить в тег из первой строки с помощью реализованного 
замыкания. Результат выведите на экран.
P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
Sample Input:
div
Сергей Балакирев
Sample Output:
<div>Сергей Балакирев</div>
"""
# tag = input()
# name = input()
#
#
# def add_tag(tag):
#     def add_string(string):
#         nonlocal tag
#         return f'<{tag}>{string}</{tag}>'
#
#     return add_string
#
#
# tag = add_tag(tag)
# print(tag(name))
###################################################################################################
"""
Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из 
списка целых чисел, записанных через пробел, либо в список, либо в кортеж. Тип коллекции 
определяется параметром tp внешней функции. Если tp = 'list', то используется список, иначе 
(при другом значении) - кортеж.
Далее, на вход программы поступают две строки: первая - это значение для параметра tp; 
вторая - список целых чисел, записанных через пробел. С помощью реализованного замыкания 
преобразовать эти данные в соответствующую коллекцию. Результат вывести на экран командой 
(lst - ссылка на коллекцию):
print(lst)
Sample Input:
list
-5 6 8 11 0 111 -456 3
Sample Output:
[-5, 6, 8, 11, 0, 111, -456, 3]
"""
# tp = input()
# sequence_num = map(int, input().split())
#
#
# def add_type(tp):
#     def print_sequence(sequence):
#         nonlocal tp
#         return tuple(sequence) if tp != 'list' else list(sequence)
#
#     return print_sequence
#
#
# lst = add_type(tp)(sequence_num)
# print(lst)
###################################################################################################
"\nDECORATES  DECORATES  DECORATES   DECORATES  DECORATES  DECORATES   DECORATES\n"

###################################################################################################
"""
Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам:
 width и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на 
 экран не выводит). То есть, функция имеет сигнатуру:
def get_sq(width, height): ...
Определите декоратор func_show для этой функции, который ОТОБРАЖАЕТ результат на экране в 
виде строки (без кавычек):
"Площадь прямоугольника: <значение>"
Вызывать функцию и декоратор не нужно, только объявить. ПРИМЕНЯТЬ декоратор к функции также 
не нужно.
Sample Input:
8 11
Sample Output:
Площадь прямоугольника: 88
"""
# def func_show(func, *args, **kwargs):
#     def wrapper(*args, **kwargs):
#         print(f'Площадь прямоугольника: {func(*args)}')
#
#     return wrapper
#
#
# def get_sq(width, height):
#     return width * height
#
# x, y = map(int, input().split())
# get_sq = func_show(get_sq)(x, y)
###################################################################################################
"""
На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку 
через пробел. Необходимо задать функцию с именем get_menu, которая преобразует эту строку 
в список из слов и возвращает этот список. Сигнатура функции, следующая:
def get_menu(s): ...
Определите декоратор для этой функции с именем show_menu, который отображает 
список на экран в формате:
1. Пункт_1
2. Пункт_1
...
N. Пункт_N
Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в 
программе делать не нужно. Сами функции не вызывать.
Sample Input:
Главная Добавить Удалить Выйти
Sample Output:
1. Главная
2. Добавить
3. Удалить
4. Выйти
"""
# s = input()
#
#
# def show_menu(func, *args, **kwargs):
#     def wrapper(lst, *args, **kwargs):
#         # for cnt, el in enumerate(func(lst), start=1):
#         #     print(f'{cnt}. {el}')
#         return [print(f'{cnt}. {el}') for cnt, el in enumerate(func(lst), start=1)]
#
#     return wrapper
#
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
#
# get_menu(s)
###################################################################################################
"""
На вход программы поступает строка из целых чисел, записанных через пробел. Напишите функцию 
get_list, которая преобразовывает эту строку в список из целых чисел и возвращает его. 
Определите декоратор для этой функции, который сортирует список чисел по возрастанию. 
Результат сортировки должен возвращаться при вызове декоратора.
Вызовите декорированную функцию get_list и отобразите полученный отсортированный список 
lst командой:
print(*lst)
Sample Input:
8 11 -5 4 3 10
Sample Output:
-5 3 4 8 10 11
"""
# s = input()
#
#
# def show_numders(func, *args, **kwargs):
#     def wrapper(lst, *args, **kwargs):
#         return sorted(func(lst))
#
#     return wrapper
#
#
# @show_numders
# def get_list(s):
#     return [int(i) for i in s.split()]
#
#
# lst = get_list(s)
# print(*lst)
###################################################################################################
"""
Вводятся две строки из слов (слова записаны через пробел). Объявите функцию, которая 
преобразовывает эти две строки в два списка слов и возвращает эти списки.
Определите декоратор для этой функции, который из двух списков формирует словарь, в котором 
ключами являются слова из первого списка, а значениями - соответствующие элементы из 
второго списка. Полученный словарь должен возвращаться при вызове декоратора.
Примените декоратор к первой функции и вызовите ее для введенных строк. Результат 
(словарь d) отобразите на экране командой:
print(*sorted(d.items()))
Sample Input:
house river tree car
дом река дерево машина
Sample Output:
('car', 'машина') ('house', 'дом') ('river', 'река') ('tree', 'дерево')
"""
# lst_1 = input()
# lst_2 = input()
#
#
# def decor_dict(func, *args, **kwargs):
#     def wrapper(*args, **kwargs):
#         return dict(zip(*func(*args)))
#
#     return wrapper
#
#
# @decor_dict
# def convert_lst(*args):
#     return [el.split() for el in args]
#
#
# d = convert_lst(lst_1, lst_2)
# print(*sorted(d.items()))
###################################################################################################
"""
Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу, 
используя следующий словарь для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
Функция должна возвращать преобразованную строку. Замены делать без учета регистра (исходную 
строку перевести в нижний регистр - малые буквы). Все небуквенные символы ": ;.,_" превращать 
в символ '-' (дефиса).
Определите декоратор для этой функции, который несколько подряд идущих дефисов, превращает 
в один дефис. Полученная строка должна возвращаться при вызове декоратора. (Сам декоратор 
на экран ничего выводить не должен).
Примените декоратор к первой функции и вызовите ее для введенной строки s на кириллице:
s = input()
Результат работы декорированной функции отобразите на экране.
Sample Input:
Python - это круто!
Sample Output:
python-eto-kruto!
"""
# s = input()
# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#      'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#      'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
#
# def decorate_str(func, *args, **kwargs):
#     def wrapper(*args, **kwargs):
#         return '-'.join(func(*args).split())
#
#     return wrapper
#
#
# @decorate_str
# def translate(string):
#     return ''.join([t.get(el, el) for el in string.lower() if el not in ':;.,_-'])
#
#
# res = translate(s)
# print(res)
# ###################################################################################################







