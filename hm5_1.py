""" Task 1: Заменить символ “#” на символ “/” в строке:

Строка 'www.my_site.com#about'

"""

# variant 1.

print("www.my_site.com#about".replace("#", "/"))


# Variant 2.

TXT_11 = "www.my_site.com#about"

LST = list(TXT_11)
X = LST.index("#")
LST[X] = "/"

print("".join(LST))



