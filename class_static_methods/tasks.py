


print(bool(re.fullmatch('кот', 'кот-обормот')))  # Возвращает None если строки не равны. Завернуть в bool(None) return False
print(bool(re.fullmatch('кот', 'кот')))  # Return object <_sre.SRE_Match object; span=(0, 3), match='кот'>. Завернуть в bool(True) return True

print(bool(None))   # False
print(bool(True))   # True