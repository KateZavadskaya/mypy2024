""" Task 3: function arguments are positive numbers """


def typed(*arg_types):

    """ Function takes arguments _any """

    def decorator(func):

        """ Function takes arguments func """

        def wrapper(*args):

            """ Function takes arguments in any value """

            converted_args = []
            for arg, arg_type in zip(args, arg_types):
                converted_arg = arg_type(arg)
                converted_args.append(converted_arg)
            return func(*converted_args)
        return wrapper
    return decorator


@typed(str, str, str)
def add(*args):

    """ Function work with str and int """

    result = ""
    for x in args:
        result += str(x)
    return result


assert add("9", 9, 8) == "998", "Error processing (str, int, int)"
assert add("9", "9", 8) == "998", "Error processing (str, str, int)"
assert add("9", "9", "8") == "998", "Error processing (str, str, str)"
assert add(9, 9, 8) == "998", "Error processing (str, int)"
assert add(9, 9) == "99", "Error processing (str, int)"
assert add("9", "9") == "99", "Error processing (str, int)"
#
# @typed(int, int)
# def concatenate(a, b):
#
#     """ Function work with int """
#
#     return str(a) + str(b)
#
#
# assert concatenate(5, 5) == "55", "Error processing (int, int)"

# @typed(float, float)
# def my_func(a, b):
#
#     """ Function add floats """
#
#     return a + b
#
#
# assert my_func(0.1, 0.2) == 0.30000000000000004, "Error - not (float,float)"
