"""
CLOSURE    CLOSURE    CLOSURE    CLOSURE    CLOSURE    CLOSURE    CLOSURE    CLOSURE    CLOSURE
Замыкание (closure) — функция, которая находится внутри другой функции и ссылается
на переменные объявленные в теле внешней функции (свободные переменные).
Внутренняя функция создается каждый раз во время выполнения внешней.

При вызове функции say_name() и передачей ей параметра (имя 'Sanch') произойдут следующ. действия:
1) Вызовется фун. say_name() в качестве пар-ра name передастся знач. 'Sanch'. Лок. пар-тр name
будет находится только в видимости фун. say_name(). Далее в теле фун. say_name() расположена
другая фун. print_your_name().
2) Далее осущ. вызов фун. print_your_name(). И мы заходим в ее тело выполняем print и по
завершению выходим из фун. print_your_name(). Далее управление возвращается в фун. say_name() и
так как далее нет ни каких операций осущ. выход из тела фун. say_name().
"""


def say_name(name):

    def print_your_name():
        print(f'My name is : ' + name)

    print_your_name()


say_name('Sanch')  # My name is : Sanch
###################################################################################################
"""
При вызове функции say_name() и передачей ей параметра (имя 'Alex') произойдут следующ. действия:
1) Вызовется фун. say_name() в качестве пар-ра name передастся знач. 'Alex'. Лок. пар-тр name
будет находится только в видимости фун. say_name(). Далее в теле фун. say_name() расположена
другая фун. print_your_name().
2) Обратите внимание, что у фун. say_name() есть ключ. слово return. И фун. возвращает 
print_your_name. Еще раз обратите внимание, print_your_name без (). () - в общем случае – это 
оператор вызова. Так как его нет, то и нет вызова. Соответственно print_your_name без () - это 
ссылка на функцию print_your_name(). Поэтому фун. print_your_name() ни разу не будет вызвана 
соответственно и не отработает print(f'My name is : ' + name). Строчка return print_your_name 
завершит работу тела фун. def say_name(name) и вернет ссылку на фун. print_your_name(). 
Но мы можем какой-нибудь переменной присвоить возвращаемую ссылку из фун. say_name(). А затем 
у этой переменной с помощью оператора вызова () вызвать внутреннюю фун. print_your_name(). И она 
распечатает строку print(f'My name is : ' + name).
f = say_name('Alex'). Обратите внимание на эту строчку.
Глобальная f ссылается --> print_your_name ссылается --> лок. окруж. say_name ссылается --> 
глобальное окружение и соотвт. на f. Получился круговой эффект ссылок. Такой эффект называется в 
Python ЗАМЫКАНИЕМ.
При каждом новом вызове будет создаваться свое замыкание.
f = say_name('Alex') ---> My name is : Alex
f1 = say_name('John') ---> My name is : John
Создаем одну реализацию замыкания. Но у каждого объекта при передаче своего параметра будет свое 
замыкание.
"""


def say_name(name):

    def print_your_name():
        print(f'My name is : ' + name)

    return print_your_name


say_name('Alex')         # Ничего не выведет на печать в консоль.
print(say_name('Alex'))  # фун. def say_name(name) и вернет ссылку на фун. print_your_name()
# В консоль выведет  <function say_name.<locals>.print_your_name at 0x0000028ECB330160>
f = say_name('Alex')     # переменной f присваиваем возвращ. ссылку из фун. say_name(). Она-ссылка
# указывает на внутреннюю функцию print_your_name().
f()  # f - это ссылка. Вызываем внутр. фун. print_your_name() с помощью оператора вызова (). В
# консоль выведет My name is : Alex
###################################################################################################
"""
Одна реализация функции-замыкания по удалению символов strip_chars вначале и в конце строки.
К многим объектам мы можем использовать самые различные комбинации удаления символов 
передав через пар-тр strip_chars
"""


def strip_string(strip_chars=' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip


str_1 = strip_string()      # Передаем пар-ры которые будем удалять из строки. По умолчанию пробел
str_2 = strip_string('!,. ')                # Передаем пар-ры которые будем удалять из строки
print(str_1('   Hello Everybody!!!.. '))    # В внутр. фун. передаем строку которую будем
# редактировать. Выведет в консоль Hello Everybody!!!..
print(str_2('   Hello Everybody!!!.. '))    # В внутр. фун. передаем строку которую будем
# редактировать.  Выведет в консоль Hello Everybody
###################################################################################################
"""
Одна реализация функции-замыкания счетчика. Функции-замыкания счетчика можно применить 
к многим объектам. И у каждого объекта будут свои собственные счетчики.
"""


def counter(start=0):   # Начало по умолчанию start=0
    def step():
        nonlocal start  # Говорим использ. вышестоящую лок. перем. start для вычисления в лок. обл.
        start += 1
        return start

    return step


c_1 = counter(10)      # передаем начало отсчета от 10
c_2 = counter()        # Начало по умолчанию start=0
print(c_1(), c_2())    # 11 1
print(c_1(), c_2())    # 12 2
print(c_1(), c_2())    # 13 3
print("\nDECORATES  DECORATES  DECORATES   DECORATES  DECORATES  DECORATES   DECORATES\n")

###################################################################################################
"""DECORATES   DECORATES  DECORATES  DECORATES   DECORATES  DECORATES  DECORATES   DECORATES"""
"""Декоратор — это паттерн проектирования (design pattern) в Python, а также функция 
второго уровня, то есть принимающая другие функции в качестве переменных и возвращающая их. 
И в сам декоратор, и в функцию-обёртку можно передать и позиционные, и 
именованные аргументы — args и kwargs соответственно."""
###################################################################################################


def func_decorator(func):   # func - это ссылка на декорируемую функцию
    def wrapper():          # wrapper() - это внут. фун. делает операции до и после дек. фун.
        print()
        print('----- что-то делаем перед вызовом декорируемой функции -----')
        func()              # вызываем декорируемую функцию
        print('----- что-то делаем после вызовом декорируемой функции -----')

    return wrapper          # Возвращаем ссылку на внут. фун.


def print_title():          # Простая фун. которая выводит на печать
    print('Вызвана функция ---> print_title')


print_title()               # При вызове, выведет на печать (Вызвана функция ---> print_title)
"""А теперь воспользуемся декоратором. Для этого сделаем переменную q и присвоим ей ссылку на 
внутреннюю функцию wrapper, а для этого вызовем фун. func_decorator(func) и вместо func положим 
нашу функцию которую мы собрались декорировать. q() вызовет внутр. фун. wrapper() и передаст 
туда декор. фун. мы можем внутри wrapper() сделать какую-нибудь логику до вызова и после.
"""
q = func_decorator(print_title)     # q присв. возвращ. ссылку из фун. func_decorator(print_title).
# print_title - это декор. фун. q - это ссылка указ. на внутр. фун. wrapper().
q()  # q - это ссылка. Вызываем внутр. фун. wrapper() с помощью оператора вызова () через ссылку q.
# q(). В консоли увидем
    # ----- что-то делаем перед вызовом декорируемой функции -----
    # Вызвана функция ---> print_title
    # ----- что-то делаем после вызовом декорируемой функции -----
"""На практике, чтобы не создавать множество переменных используют ссылку на тоже самое имя 
декор. фун. В итоге фун. print_title() как бы меняет свою работу благодаря замыканию (
декоратору)."""
print_title = func_decorator(print_title)   # Так делают на практике. И при вызове print_title()
print_title()                               # произойдет все тоже самое.
print()
"""Создадим такой же Декоратор, но с параметрами. Он будет УНИВЕРСАЛЬНЫЙ так как будет 
принимать позиционные, и именованные аргументы — args и kwargs соответственно. Если даже 
не будет ни одного аргумента то все равно не будет ошибок"""


def func_decorator_with_args(func, *args, **kwargs):   # func - это ссылка на декорируемую функцию
    def wrapper_with_args(*args, **kwargs):  # wrapper() - это внут. фун. делает операции до и
        # после дек. фун.
        print()
        print('----- что-то делаем перед вызовом декорируемой функции -----')
        r = func(*args, **kwargs)              # вызываем декорируемую функцию
        print('----- что-то делаем после вызовом декорируемой функции -----')
        return r

    return wrapper_with_args          # Возвращаем ссылку на внут. фун.


def print_with_args(arg_1, arg_2):    # Простая фун. кот. выводит на печать с 2 пар-рами
    print(f'Вызвана функция ---> print_with_args с параметрами {arg_1} и {arg_2}')
    # return f'Вызвана функция ---> print_with_args с параметрами {arg_1} и {arg_2}'


print_with_args('I am first', 'I am second')  # При вызове, выведет на печать (Вызвана
# функция ---> print_title_with_args с параметрами {arg_1} и {arg_2})

"""Теперь можно задекорировать нашу простую фун. и  вызвать вот так с передачей 2 аргументов"""
# print_with_args = func_decorator_with_args(print_with_args)('Передаю 1 арг.', 'Передаю 2 арг.')

"""Или вот так с передачей 2 аргументов"""
print_with_args = func_decorator_with_args(print_with_args)  # ссылка на внут. фун. декоратора
print_with_args('Передаю 1 арг.', 'Передаю 2 арг.')          # перед. 2 арг. в внут. фун. декорат.
# Если в декор. фун. нет return то по умол. вернется None. Поэтому результаты
# выполнения внут. фун. возвращаем через return

"""ВНИМАНИЕ. НА ПРАКТИКЕ ЧАЩЕ ИСПОЛЬЗУЮТ ДЕКОРИРОВАНИЕ ЧЕРЕЗ СПЕЦ. ЗНАК @. Смотрите ниже"""

@func_decorator_with_args
def print_with_args_2(arg_1, arg_2):    # Простая фун. кот. выводит на печать с 2 пар-рами
    print(f'Вызвана функция ---> print_with_args_2 с параметрами {arg_1} и {arg_2}')
    # return f'Вызвана функция ---> print_with_args с параметрами 1 - {arg_1} и 2 - {arg_2}'

print_with_args_2('1 пар-тр вызов через @', '2 пар-тр вызов через @')
# Вызываем через @func_decorator_with_args. Так проще.

###################################################################################################

"""Создадим декоратор, который будет замерять время выполнения функций"""


def test_time(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        import time         # Так лучше не делать.
        st = time.time()    # Запоминаем начальное время перед запуском функции
        res = func(*args, **kwargs)     # выполняется функция
        et = time.time()    # Запоминаем конечное время когда функция окончила работу
        dt = et - st        # Находим время работы функции
        return f'\nНаибольший делитель : {res}. Время работы {dt} сек'

    return wrapper


"""Измерим время выполнения функции (медленный и быстрый метод для поиска наибол. общего 
делителя для 2 натуральных чисел. Метод Евклида)"""

@test_time
def get_nod(x, y):  # медленный метод Евклида
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

@test_time
def get_fast_nod(x, y):  # быстрый метод Евклида
    if x < y:
        x, y = y, x

    while y:
        x, y = y, x % y

    return x


res_1 = get_nod(2, 10_000_000)        # Передаем 2 числа в фун. для поиска наибол. общего делителя
res_2 = get_fast_nod(2, 10_000_000)   # Передаем 2 числа в фун. для поиска наибол. общего делителя
print(res_1, res_2)     # Наибольший делитель : 2. Время работы 0.2343904972076416 сек
                        # Наибольший делитель : 2. Время работы 0.0 сек
