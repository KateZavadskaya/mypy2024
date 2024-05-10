"""В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

"""

txt = "Ivanou Ivan"

txt2 = txt.split()

x = txt2[0]
txt2[0] = txt2[1]
txt2[1] = x

txt = " ".join(txt2)

print(txt)
