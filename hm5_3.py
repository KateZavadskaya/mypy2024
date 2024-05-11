"""В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

"""

TXT = "Ivanou Ivan"

TXT_2 = TXT.split()

X = TXT_2[0]
TXT_2[0] = TXT_2[1]
TXT_2[1] = X

TXT = " ".join(TXT_2)

print(TXT)
