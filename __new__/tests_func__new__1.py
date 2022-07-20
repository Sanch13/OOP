class AbstractClass:
    __instance = None
    __obj = "Ошибка: нельзя создавать объекты абстрактного класса"

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            return cls.__obj

# class AbstractClass:
#     def __new__(cls, *args, **kwargs):
#         return "Ошибка: нельзя создавать объекты абстрактного класса"


obj = AbstractClass()
