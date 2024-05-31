""" Task 2: number against """


def opposite(n, first_number):

    """ Function return the number againts

    n - volume of numbers

    first_number - function return the number against it

    """

    while True:
        if first_number <= n:
            middle = n / 2
            if first_number < middle:
                result = middle + first_number
            elif first_number > middle:
                result = abs(middle - first_number)
            elif first_number == middle:
                result = 0
            return int(result)
        break
    return None


print(opposite(10, 9))
