""" Task 1: function arguments are positive numbers """


def decorator(_any):

    """ Function takes arguments _any """

    def wrapper(*args):

        """ Function takes arguments in any value """

        for i, y in enumerate(args, start=1):
            if isinstance(y, int):
                if y > 0:
                    print(f"{i}. {y} Число больше 0")
                elif y == 0:
                    raise ValueError(f"{i}. {y} Число равно 0")
                elif y < 0:
                    raise ValueError(f"{i}. {y} Число меньше 0")
            else:
                raise ValueError(f"{i}. {y} Невозможно сравнить")
    return wrapper


@decorator
def my_func(*args):

    """ Function prints arguments in any value """

    print(args)


my_func(1, 6, 2)
