""" Task 1: bulls and cows """

while True:
    x = input("Введите неповторяющееся четырёхзначное число: ")
    if x.isdigit() and len(set(x)) == len(x) and len(x) == 4:
        while True:
            y = input("Что было загадано?: ")
            if y.isdigit() and len(set(y)) == len(y) and len(y) == 4:
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
        break
