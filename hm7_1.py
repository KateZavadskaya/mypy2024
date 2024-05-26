""" Task 1: bulls and cows """

x = input("Введите неповторяющееся четырёхзначное число: ")
while True:
    y = input("Что было загадано?: ")
    BULL = 0
    COW = 0
    for i in range(4):
        if x[i] == y[i]:
            BULL += 1
        elif y[i] in x:
            COW += 1
    print(f'bulls {BULL} and cows {COW}')
    if BULL == 4:
        print('Вы выиграли!')
        break
