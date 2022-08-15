class Factory:

    @staticmethod
    def build_sequence():   # метод возвращает пустой список
        return []

    @staticmethod
    def build_number(string):   # метод возвращает данные в тип int
        return int(string)

class Loader:
    @staticmethod
    def parse_format(string, factory):   # метод возвращает список определенного выходного формата
                    # (парсер - обработчик строки). string - строка данных. factory - ссылка на объект класса Factory
        seq = factory.build_sequence()  # через ссылку на объект обратимся к методу build_sequence() класса Factory.
                                # переменная seq будет ссылаться на пустой список [] который вернет build_sequence()
        for sub in string.split(","):   # строку данных string разбиваем на последовательность и проходим по очереди
            item = factory.build_number(sub)    # переменная item будет ссылаться на вернувшиеся int значение
                                            # функции build_number() короую вызвали через ссылку factory
            seq.append(item)    # добавление item в список seq

        return seq  # Возврат списка

res = Loader.parse_format("1, 2, 3, -5, 10", Factory)  # в переменную res вернется список из метода parse_format класса Loader
print(res)
########################################################################################################################






















# print(bool(re.fullmatch('кот', 'кот-обормот')))  # Возвращает None если строки не равны. Завернуть в bool(None) return False
# print(bool(re.fullmatch('кот', 'кот')))  # Return object <_sre.SRE_Match object; span=(0, 3), match='кот'>. Завернуть в bool(True) return True

# print(bool(None))   # False
# print(bool(True))   # True