class Main:
    def __init__(self, name):
        print("init Main")
        self.name = name
        super().__init__()


class A:
    ID = 0

    def __init__(self):
        print("init A")
        A.ID += 1
        self.id = A.ID
        super().__init__()

    def get_info(self):
        return f"id: {self.id} name: {self.name}"


class B:
    phrase = "Hello"

    def __init__(self):
        print("init B")
        self.full_phrase = B.phrase + " " + self.name

    def get_phrase(self):
        return f"{self.full_phrase} . You are welcome !!!"


class SubClass(Main, A, B):
    pass


c = SubClass("Alex")  # SubClass -> init Main -> init A -> init B
print(c.get_info())  # id: 1 name: Alex
print(c.get_phrase())   # Hello Alex . You are welcome !!!
print(SubClass.__mro__)
# (<class '__main__.SubClass'>, <class '__main__.Main'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
