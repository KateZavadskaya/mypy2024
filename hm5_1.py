# Заменить символ “#” на символ “/” в строке:
# Строка 'www.my_site.com#about'

# Способ 1 - смена символа с присвоением нового id

txt_1 = "www.my_site.com#about"

txt_2 = txt_1.replace("#", "/")  # замена символов
txt_1 = txt_2                    # присвоение нового id первоначальной переменной txt_1

print(txt_1)

print(id(txt_1))
print(id(txt_2))


# Способ 2 - смена символа через список

txt_1 = "www.my_site.com#about"

lst = list(txt_1)           # преобразуем строку txt_1 в список и даём списку переменную lst
x = lst.index("#")          # узнаём индекс у конкретного символа и кладём номер в переменную
lst[x] = "/"                # меняем на необходимый символ
txt_1 = "".join(lst)        # преобразуем список lst в строку и кладём в txt_1

print(txt_1)                # выводим txt_1


# Способ 3 - в одну строку

txt_1 = ("www.my_site.com#about".replace("#", "/"))

print(txt_1)
