# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

txt = "Ivanou Ivan"

txt_2 = txt.split()

x = txt_2[0]
txt_2[0] = txt_2[1]
txt_2[1] = x

txt = " ".join(txt_2)

print(txt)
