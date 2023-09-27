# Подвиг 6. Объявите класс DateString для представления дат, объекты которого создаются командой:
# date = DateString(date_string)
# где date_string - строка с датой в формате:
# "DD.MM.YYYY"
# здесь DD - день (целое число от 1 до 31); MM - месяц (целое число от 1 до 12);
# YYYY - год (целое число от 1 до 3000).
# Например:
# date = DateString("26.05.2022")
# или
# date = DateString("26.5.2022") # незначащий ноль может отсутствовать
# Если указанная дата в строке записана неверно (не по формату), то генерировать
# исключение с помощью собственного класса:
# DateError - класс-исключения, унаследованный от класса Exception.
# В самом классе DateString переопределить магический метод __str__() для формирования
# строки даты в формате:
# "DD.MM.YYYY"
# (здесь должны фигурировать незначащие нули, например, для аргумента "26.5.2022" должна
# формироваться строка "26.05.2022").
# Далее, в программе выполняется считывание строки из входного потока командой:
# date_string = input()
# Ваша задача создать объект класса DateString с аргументом date_string и
# вывести объект на экран командой:
# print(date) # date - объект класса DateString
# Если же произошло исключение, то вывести сообщение (без кавычек):
# "Неверный формат даты"
# Sample Input:
# 1.2.1812
# Sample Output:
# 01.02.1812


class DateString:
    def __init__(self, date_string):
        self.date_string = self.check_date(date_string)

    @classmethod
    def check_date(cls, date_string) -> True:
        try:
            d, m, y = map(int, date_string.split("."))
            if d not in range(1, 32) or m not in range(1, 13) or y not in range(1, 3001):
                raise DateError
        except ValueError:
            return f"Неверный формат даты"
        else:
            return f"{d:02}.{m:02}.{y:04}"

    def __str__(self):
        return f"{self.date_string}"


class DateError(Exception):
    pass


try:
    print(DateString(input()))
except DateError:
    print("Неверный формат даты")
