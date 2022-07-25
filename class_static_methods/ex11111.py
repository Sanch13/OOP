from string import ascii_lowercase, digits
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


CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits

name = 'Aksjadhgaj1`2'

if not 2 < len(name) < 51:
    raise ValueError("некорректное поле name")

for el in name:
    if el not in CHARS_CORRECT:
        raise ValueError("некорректное поле name")