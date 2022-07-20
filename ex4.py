class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]

class Table:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV("samsung", 1111))
cart.add(TV("LG", 1234))
cart.add(Table("ikea", 2345))
cart.add(Notebook("msi", 5433))
cart.add(Notebook("apple", 542))
cart.add(Cup("keepcup", 43))

print(cart.get_list())
cart.remove(0)
print(cart.get_list())
