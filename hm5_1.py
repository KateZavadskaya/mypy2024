""" Заменить символ “#” на символ “/” в строке:

Строка 'www.my_site.com#about'

"""

# Способ 1.

TXT_1 = "www.my_site.com#about"

TXT_2 = TXT_1.replace("#", "/")

print(TXT_2 )

# Способ 2.

TXT_11 = "www.my_site.com#about"

LST = list(TXT_11)
X = LST.index("#")
LST[X] = "/"
TXT_12 = "".join(LST)

print(TXT_12)


# Способ 3.

print("www.my_site.com#about".replace("#", "/"))
