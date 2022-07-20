class Translator:

    def add(self, eng, rus):
        if "DICT" not in self.__dict__:
            self.DICT = {}

        self.DICT.setdefault(eng, [])
        self.DICT[eng].append(rus)

    def remove(self, eng):
        self.DICT.pop(eng, False)

    def translate(self, eng):
        return self.DICT.get(eng)


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')
print(*tr.translate('go'))
