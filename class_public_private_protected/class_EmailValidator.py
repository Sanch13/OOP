from random import randint
from string import ascii_letters, digits


class EmailValidator:
    EMAIL_CHARS = ascii_letters + digits + '@._'
    EMAIL_RAND_CHARS = ascii_letters + digits + '_'

    def __new__(cls, *args, **kwargs):  # prohibit the creation of class instances
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):  # check email. return True if email have type str else False
            return False

        if not set(email) < set(cls.EMAIL_CHARS): # if the set email is included in the set of allowed characters then True
            return False

        if not email.count('@') == 1:  # if quantity "@" != 1 then False else True
            return False

        parts = email.split('@')    # Split email for parts
        if len(parts[0]) > 100 and len(parts[1]) > 50:    # if first parts more than 100 then False
            return False                                  # if second parts more than 50 then False

        if not parts[1].count('.') >= 1:    # if quantity '.' more than or equal 1 then True else False
            return False

        if not email.count('..') == 0:    # if quantity '..' equal 0 then True else False
            return False

        return True

    @classmethod
    def get_random_email(cls):
        n = randint(1, 20)  # choice random number from 1 - 20
        length = len(cls.EMAIL_RAND_CHARS) - 1  # reduced the length of the string by -1 to keep the range
        return ''.join(cls.EMAIL_RAND_CHARS[randint(0, length)] for _ in range(n)) + '@gmail.com'   # create random email

    @staticmethod
    def __is_email_str(email):  # check email have type str
        return type(email) == str  # return True if email have type str


