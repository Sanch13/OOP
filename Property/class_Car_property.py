class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__is_str(model) and self.__is_str_len(model):
            self.__model = model

    @staticmethod
    def __is_str(model):
        return type(model) == str

    @staticmethod
    def __is_str_len(model):
        return 2 <= len(model) <= 100


car = Car()
print(car.model, car.__dict__)
car.model = 'Toyota'
print(car.model, car.__dict__)
cr = Car()
print(cr.model, cr.__dict__)
cr.model = "BMV"
print(cr.model, cr.__dict__)
