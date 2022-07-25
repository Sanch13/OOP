from string import ascii_lowercase, digits
import re

#
# class TextInput:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         return
#
#
#
# class PasswordInput:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def get_html(self):
#         pass
#
#
# # здесь объявляйте классы TextInput и PasswordInput
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()


# CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
# CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
# name = 'Aksjadhgaj1`2'
#
# if not 2 < len(name) < 51:
#     raise ValueError("некорректное поле name")
#
# for el in name:
#     if el not in CHARS_CORRECT:
#         raise ValueError("некорректное поле name")

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        if number.count('-') == 3:
            return all(map(lambda x: len(x) == 4 and x.isdigit(), number.split('-')))
        else:
            return False

    @classmethod
    def check_name(cls, name):
        if name.count(' ') == 1:
            return all(map(lambda x: set(x) < set(ascii_lowercase.upper()), name.split()))
        else:
            return False


# print(CardCheck.check_card_number("1234-5678-9012-0080"))
# print(CardCheck.check_name("SERGEI BALAKIREV"))


print(bool(re.fullmatch('кот', 'кот-обормот')))  # Возвращает None если строки не равны. Завернуть в bool(None) return False
print(bool(re.fullmatch('кот', 'кот')))  # Return object <_sre.SRE_Match object; span=(0, 3), match='кот'>. Завернуть в bool(True) return True

print(bool(None))   # False
print(bool(True))   # True