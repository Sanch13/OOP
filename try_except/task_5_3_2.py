# Подвиг 5. Вы начинаете разрабатывать свой сервис по тестированию. Для этого вам поручается
# разработать базовый класс Test для всех видов тестов, объекты которого создаются командой:
# test = Test(descr)
# где descr - формулировка теста (строка). Если длина строки descr меньше 10 или больше
# 10 000 символов, то генерировать исключение командой:
# raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
# В самом классе Test должен быть объявлен абстрактный метод:
# def run(self): ...
# который должен быть переопределен в дочернем классе. Если это не так, то должно
# генерироваться исключение командой:
# raise NotImplementedError
# Далее, объявите дочерний класс с именем TestAnsDigit для тестирования правильного
# введенного числового ответа на вопрос теста. Объекты класса TestAnsDigit должны
# создаваться командой:
# test_d = TestAnsDigit(descr, ans_digit, max_error_digit)
# где ans_digit - верный числовой ответ на тест; max_error_digit - максимальная погрешность
# в указании числового ответа (необходимо для проверки корректности вещественных чисел,
# по умолчанию принимает значение 0.01).
# Если аргумент ans_digit или max_error_digit не число (также проверить, что max_error_digit
# больше или равно нулю), то генерировать исключение командой:
# raise ValueError('недопустимые значения аргументов теста')
# В классе TestAnsDigit переопределите метод:
# def run(self): ...
# который должен читать строку из входного потока (ответ пользователя) командой:
# ans = float(input()) # именно такой командой, ее прописывайте в методе run()
# и возвращать булево значение True, если введенный числовой ответ ans принадлежит диапазону
# [ans_digit-max_error_digit; ans_digit+max_error_digit]. Иначе возвращается булево значение False.
# Теперь нужно воспользоваться классом TestAnsDigit. Для этого в программе вначале читается
# сам тест с помощью команд:
# descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при
# вычислении 2+2? | 4
# ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в
# преобразовании быть не может
# Далее, вам необходимо создать объект класса TestAnsDigit с аргументами descr, ans, а
# аргумент max_error_digit должен принимать значение по умолчанию 0.01.
# Запустите тест командой run() и выведите на экран результат его работы (значение True или False).
# Если в процессе создания объекта класса TestAnsDigit или в процессе работы метода run() возникли
# исключения, то они должны быть обработаны и на экран выведено сообщение, содержащееся
# в исключении.
# Sample Input:
# Какое значение получим, при выполнении команды int(5.7)? | 5
# 6
# Sample Output:
# False


class Test:
    MIN = 10
    MAX = 10_000

    def __init__(self, descr):
        self.check_size_text(descr)
        self.descr = descr

    @classmethod
    def check_size_text(cls, descr):
        size = len(descr)
        if size < cls.MIN or cls.MAX < size:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key == "ans_digit" and type(value) not in (int, float):
            raise ValueError('недопустимые значения аргументов теста')

        if key == "max_error_digit" and type(value) != int and value < 0:
            raise ValueError('недопустимые значения аргументов теста')

        object.__setattr__(self, key, value)

    def run(self):
        ans = float(input())
        min_value = self.ans_digit - self.max_error_digit
        max_value = self.ans_digit + self.max_error_digit
        return min_value < ans < max_value


descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

try:
    ts = TestAnsDigit(descr=descr, ans_digit=ans, max_error_digit=0.01)
    print(ts.run())
except Exception as e:
    print(e)

try:
    test = Test('descr')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

try:
    test = Test('descr ghgfhgjg ghjghjg')
    test.run()
except NotImplementedError:
    assert True
else:
    assert False

assert issubclass(TestAnsDigit, Test)

t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

try:
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
except ValueError:
    assert True
else:
    assert False


try:
    t = TestAnsDigit('ff', 1, -0.5)
except ValueError:
    assert True
else:
    assert False
