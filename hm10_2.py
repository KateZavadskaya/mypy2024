""" Task 2: return number """


def decorator(_any):

    """ Function takes arguments _r """

    def wrapper(*args):

        """ Function takes arguments in any value """

        for x in args:
            if not isinstance(x, (int, float)):
                print("Result is not numeric")
                break
        return False
    return wrapper


@decorator
def my_func(*args):

    """ Function shows sum of arguments """

    a = sum(args)
    return a


my_func(1, 3, "k")
