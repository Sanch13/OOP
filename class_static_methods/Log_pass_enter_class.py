from string import ascii_lowercase, digits


class Data:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    @classmethod
    def check_name(cls, name):
        if not 2 < len(name) < 51 or type(name) != str:
            raise ValueError("некорректное поле name")

        for el in name:
            if el not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")


class TextInput(Data):

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(Data):

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


# здесь объявляйте классы TextInput и PasswordInput


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("ahgar"), PasswordInput("zbsrt4572345"))
html = login.render_template()
print(html)