"""Имена собственные всегда начинаются с заглавной буквы,
за которой следуют строчные буквы.
Исправьте данное имя собственное так,
чтобы оно соответствовало этому утверждению.
"pARiS" >> "Paris"

"""

WRONG_NAME = "pARiS"
print(f"Исходное имя: '{WRONG_NAME}'")

OK_NAME = WRONG_NAME.title()
WRONG_NAME = OK_NAME
print(f"Корректно написанное имя: '{WRONG_NAME}'")
