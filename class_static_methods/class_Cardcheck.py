from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        """проверяет строку с номером карты и возвращает булево значение True,
               если номер в верном формате и False - в противном случае. Формат номера,
               следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)."""
        if number.count('-') == 3:
            return all(map(lambda x: len(x) == 4 and x.isdigit(), number.split('-')))
        else:
            return False

    @classmethod
    def check_name(cls, name):
        """проверяет строку name с именем пользователя карты.
                Возвращает булево значение True, если имя записано верно
                и False - в противном случае.
                Формат имени: два слова (имя и фамилия) через пробел,
                записанные заглавными латинскими символами и цифрами.
                Например, SERGEI BALAKIREV."""
        if name.count(' ') == 1:
            return all(map(lambda x: set(x) < set(ascii_lowercase.upper()), name.split()))
        else:
            return False


'''     Через регулярку  '''
# import re
#
#
# class CardCheck:
#     @staticmethod
#     def check_card_number(number):
#         return bool(re.fullmatch(r"\d{4}(?:-\d{4}){3}", number))
#
#     @staticmethod
#     def check_name(name):
#         return bool(re.fullmatch(r"[A-Z\d]+ [A-Z\d]+", name))


# print(bool(re.fullmatch('кот', 'кот-обормот')))  # Возвращает None если строки не равны. Завернуть в bool(None) return False
# print(bool(re.fullmatch('кот', 'кот')))  # Return object <_sre.SRE_Match object; span=(0, 3), match='кот'>. Завернуть в bool(True) return True
#
# print(bool(None))   # False
# print(bool(True))   # True
