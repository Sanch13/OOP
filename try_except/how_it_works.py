# исключения можно разбить на две группы:
# - исключения в момент исполнения; # возникает в момент исполнения программы (уже скомпилированный файл интерпритируется)
# - исключения при компиляции (до исполнения кода). # возникает в момент компиляции текста программы (синтаксическая ошибка в коде)

#                               иерархия  исключений
#                               BaseException
#                                    ^
#   _________________________________|____________________________________
#   ^                   ^                       ^                        ^
#   |                   |                       |                        |
# Exception        SystemExit             GeneratorExit       KeyboardInterrupt
#   ^
#   |
#   ----------------------------------------------------------------------
#   ^           ^         ^       ^        ^         ^         ^         ^
#   |           |         |       |        |         |         |         |
# Attribute  Arithmetic   EOF    Name    Lookup      OS       Type     Value
#  Error       Error     Error   Error    Error     Error     Error    Error
#               ^                          ^          ^
#               | - ZeroDivision           | - Index  | - FileNotFound
#               |    Error                 |   Error  |      Error
#               |                          |          |
#               | - FloatingPoint          | - Key    | - Interrupted
#               |      Error               |  Error   |      Error
#               |                                     |
#               | - Overflow Error                    | - Permission
#                                                     |      Error
#                                                     |
#                                                     | - TimeOut Error

#  блоков except может быть сколько угодно
#  Сначала прописываются блоки со специализированными классами исключений, а затем с более общими (базовыми).
# try поддерживает необязательный блоки else, finally.

try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as z:  # ZeroDivisionError будет отлавливать свой тип исключения
    print(z)
except ValueError as z:  # ValueError будет отлавливать свой тип исключения
    print(z)
except Exception as e:  # Exception будет отлавливать все исключения, возникающие в блоке try.
    print(e)
else:  # выполняется при штатном выполнении кода внутри блока try, то есть, когда не произошло никаких ошибок.
    print("Исключений не произошло")
finally:  # выполняется всегда после блока try, вне зависимости произошла ошибка или нет
    print("Блок finally выполняется всегда")

#  блоки try / except можно вкладывать один в другой
try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except ZeroDivisionError:
        print("Деление на ноль")
except ValueError as z:
    print("Ошибка ValueError")

# можно внутренний блок try вынести в функцию
def div(a, b):
    try:
        return x / y
    except ZeroDivisionError:
        return "Деление на ноль"


try:
    x, y = map(int, input().split())
    res = div(x, y)
except ValueError as z:
    print("Ошибка ValueError")

print(res)

