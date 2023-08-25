# Подвиг 3. Создается проект, в котором предполагается использовать списки из целых чисел.
# Для этого вам ставится задача создать класс с именем ListInteger с базовым классом list
# и переопределить три метода:
# __init__()
# __setitem__()
# append()
# так, чтобы список ListInteger содержал только целые числа. При попытке присвоить любой
# другой тип данных, генерировать исключение командой:
# raise TypeError('можно передавать только целочисленные значения')
# Пример использования класса ListInteger (эти строчки в программе не писать):
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# print(s)
# s[0] = 10.5 # TypeError
# P.S. В программе нужно объявить только класс. На экран выводить ничего не нужно.


class ListInteger(list):
    def __init__(self, nums):
        super().__init__([self.check_int_value(x) for x in nums])

    @staticmethod
    def check_int_value(item):
        if isinstance(item, int):
            return item
        raise TypeError('можно передавать только целочисленные значения')

    def __setitem__(self, key, value):
        super().__setitem__(key, self.check_int_value(value))

    def append(self, item):
        super().append(self.check_int_value(item))


s = ListInteger((11, 2, 3))
print(s.__dict__)
print(s[0])
s[1] = 10
s.append(11)
print(s.__dict__)
# assert s[0] == -10, "список вернул неверное значение, возможно, некорректно работает присваивание по индексу нового значения"
# s[0] = 10.5
# print(s.__dict__)

# def __getitem__(self, item):
#     if 0 <= item < len(self.lst):
#         return self.lst[item]