""" Заменить символ “#” на символ “/” в строке:

Строка 'www.my_site.com#about'

"""

# Способ 1.

txt1 = "www.my_site.com#about"

txt2 = txt1.replace("#", "/")
txt1 = txt2

print(txt1)

print(id(txt1))
print(id(txt2))


# Способ 2.

txt11 = "www.my_site.com#about"

lst = list(txt11)
x = lst.index("#")
lst[x] = "/"
txt11 = "".join(lst)

print(txt11)


# Способ 3.

print("www.my_site.com#about".replace("#", "/"))
