"""
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
        nonlocal start  # Говорим использ. вышестоящую лок. перем. start для добавления в лок. обл.
        start += 1
        return start

    return step


c_1 = counter(10)      # передаем начало отсчета от 10
c_2 = counter()        # Начало по умолчанию start=0
print(c_1(), c_2())    # 11 1
print(c_1(), c_2())    # 12 2
print(c_1(), c_2())    # 13 3
###################################################################################################





