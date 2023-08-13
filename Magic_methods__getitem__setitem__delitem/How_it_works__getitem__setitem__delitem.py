# __getitem__(self, key) – получение значения по ключу key;
# __setitem__(self, key, value) – запись значения value по ключу key;
# __delitem__(self, key) – удаление элемента по ключу key.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        if 0 <= key < len(self.marks):
            return self.marks[key]
        else:
            raise IndexError(f"Неверный индекс {key}")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым неотрицательным числом")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend([None] * off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым числом")

        if 0 <= key < len(self.marks):
            del self.marks[key]
        else:
            raise IndexError(f"Неверный индекс {key}")


s1 = Student('Сергей', [5, 5, 3, 2, 5])
print(s1.marks)
print(s1[2])
# print(s1[20])
# print(s1['abc'])
s1[6] = 4
print(s1.marks)
del s1[5]
print(s1.marks)


# object.__getitem__(self, key)
# Вызывается для реализации оценки self[key]. Для типов последовательностей допустимыми ключами
# должны быть целые числа и объекты-срезы. Обратите внимание, что специальная интерпретация
# отрицательных индексов (если класс хочет эмулировать тип последовательности) зависит от
# метода __getitem__(). Если ключ имеет неподходящий тип, может возникнуть ошибка TypeError;
# если значение вне набора индексов для последовательности (после какой-либо специальной
# интерпретации отрицательных значений), IndexError должен быть поднят. Для типов сопоставления,
# если ключ отсутствует (не в контейнере), должен быть поднят KeyError.
#
# object.__setitem__(self, key, value)
# Вызывается для реализации присваивания self[key]. То же примечание, что и для __getitem__().
# Это должно быть реализовано только для отображений, если объекты поддерживают изменения значений
# ключей, или если можно добавить новые ключи, или для последовательностей, если элементы
# можно заменить. Для неправильных значений ключа следует вызывать те же исключения,
# что и для метода __getitem__().
#
# object.__delitem__(self, key)
# Вызывается для удаления self[key]. То же примечание, что и для __getitem__().
# Это должно быть реализовано только для отображений, если объекты поддерживают удаление ключей,
# или для последовательностей, если элементы могут быть удалены из последовательности.
# Для неправильных значений ключа следует вызывать те же исключения, что и для метода __getitem__().
