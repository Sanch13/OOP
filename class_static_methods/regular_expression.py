import re

'''     Через регулярку  '''


class CardCheck:
    @staticmethod
    def check_card_number(number):
        """проверяет строку с номером карты и возвращает булево значение True,
                       если номер в верном формате и False - в противном случае. Формат номера,
                       следующий: XXXX-XXXX-XXXX-XXXX, где X - любая цифра (от 0 до 9)."""
        return bool(re.fullmatch(r"\d{4}(?:-\d{4}){3}", number))

    @staticmethod
    def check_name(name):
        """проверяет строку name с именем пользователя карты.
                        Возвращает булево значение True, если имя записано верно
                        и False - в противном случае.
                        Формат имени: два слова (имя и фамилия) через пробел,
                        записанные заглавными латинскими символами и цифрами.
                        Например, SERGEI BALAKIREV."""
        return bool(re.fullmatch(r"[A-Z\d]+ [A-Z\d]+", name))


print('CardCheck number=>', CardCheck.check_card_number("1234-5678-9012-0000"))
print('CardCheck name=>', CardCheck.check_name("SERGEI BALAKIREV"))


""" Определяет соответствие строки указанному шаблону.
    re.fullmatch(pattern, string, flags=0) -> объект Match/MatchObject, либо None
    pattern : Шаблон, соответствие которому следует определить

    string : Строка, которую требуется проверить на соответствие шаблону.

    flags=0 : Флаги управления интерпретацией регулярного выражения.
    
Возвращает объект соответствия, если строка, как целое, полностью соответствует шаблону, в противном случае возвращает None."""

print(bool(re.fullmatch('кот', 'кот-обормот')))  # Возвращает None если строки не равны. Завернуть в bool(None) return False
print(bool(re.fullmatch('кот', 'кот')))  # Return object <_sre.SRE_Match object; span=(0, 3), match='кот'>. Завернуть в bool(True) return True

print(bool(None))  # False
print(bool(True))  # True
