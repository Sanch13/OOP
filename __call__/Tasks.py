from random import randint, choice  # функции для генерации целых случ. знач.


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):  # Инициал. лок. св-тв экз. класса
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):    # изм. поведение для функторов экз. класса
        """При вызове экз. класса с () будет случ. образом генер. последов. из psw_chars в
        диапазоне [min_length:max_length]"""
        number = randint(self.min_length, self.max_length)  # выбираем случ. число из диапазона
        return ''.join(choice(self.psw_chars) for _ in range(number))  # возвр. сгенер. пароль


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)  # созд. объект класса

lst_pass = [rnd() for _ in range(3)]    # созд. список из функтров=(пароли) экз. rnd
# print(lst_pass)
###################################################################################################


