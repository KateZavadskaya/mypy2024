""" Task 5: Создайте список из 10 элементов,

5.1 вставьте на 3-ю позицию новое значение,

5.2 удалите элемент из списка под индексом 6

"""

# Создайте список из 10 элементов
LST = list(range(0, 10))
print(LST)

# 5.1 вставьте на 3-ю позицию новое значение
LST.insert(2, 777)
print(LST)

# 5.2 удалите элемент из списка под индексом 6
del LST[6]
print(LST)
