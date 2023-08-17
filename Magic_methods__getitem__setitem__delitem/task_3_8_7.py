# Подвиг 9 (релакс). Объявите в программе класс Bag (сумка), объекты которого создаются командой:
# bag = Bag(max_weight)
# где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.
# Каждый предмет описывается классом Thing и создается командой:
# t = Thing(name, weight)
# где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное
# значение). В объектах класса Thing должны автоматически формироваться локальные свойства с
# теми же именами: name и weight.
# В классе Bag должен быть реализован метод:
# add_thing(thing) - добавление нового объекта thing класса Thing в сумку.
# Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight.
# Иначе, генерируется исключение:
# raise ValueError('превышен суммарный вес предметов')
# Также с объектами класса Bag должны выполняться следующие команды:
# t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления
# вещей, начиная с 0)
# bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
# del bag[indx] # удаление вещи из сумки, расположенной по индексу indx
# Если индекс в этих командах указывается неверно, то должно генерироваться исключение:
# raise IndexError('неверный индекс')
# Пример использования классов (эти строчки в программе не писать):
# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name) # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name) # платок
# del bag[0]
# print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError
# P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

def check_index(func):
    def wrapper(obj, indx, *args, **kwargs):
        if isinstance(indx, int) and 0 <= indx < len(obj):
            return func(obj, indx, *args, **kwargs)
        raise IndexError('неверный индекс')

    return wrapper


class Bag:
    def __init__(self, max_weight):
        self.max_weight_bag = max_weight
        self.current_weight_bag = 0
        self.bag = []

    def add_thing(self, thing):
        self.current_weight_bag += thing.weight
        if self.current_weight_bag <= self.max_weight_bag:
            self.bag.append(thing)
        else:
            raise ValueError('превышен суммарный вес предметов')

    @check_index
    def __getitem__(self, key):
        return self.bag[key]

    def __setitem__(self, key, value):
        self.current_weight_bag -= self.bag[key].weight
        self.current_weight_bag += value.weight
        if self.current_weight_bag <= self.max_weight_bag:
            self.bag[key] = value
        else:
            raise ValueError('превышен суммарный вес предметов')

    def __delitem__(self, key):
        del self.bag[key]

    def __len__(self):
        return len(self.bag)


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# print(bag.current_weight)
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name)  # рубашка
# bag[1] = Thing('платок', 100)
# print(bag[1].name)  # платок
# print(bag)
# del bag[0]
# print(bag)
# print(bag[0].name)  # платок
# t = bag[4] # генерируется исключение IndexError





