""" Task 2: number against """


def opposite(n, first_number):

    """ Function return the number againts

    n - volume of numbers

    first_number - function return the number against first_number

    """

    while True:
        if first_number <= n:
            middle = n / 2
            result = False
            if first_number < middle:
                result = middle + first_number
            elif first_number > middle:
                result = abs(middle - first_number)
            elif first_number == middle:
                result = 0
            return int(result)
        break
    return "Wrong number is input"


print(opposite(10, 9))
