""" Task 3: validate """


def validate(code):

    """ Function return the existance of numeric! card """

    while True:
        if str(code).isdigit() and len(str(code)) == 16:
            code = list(str(code))
            length = len(code)
            sum_odd = 0
            sum_even = 0
            digit = 0
            for i in range(length):
                digit = int(code[i])
                if i % 2 != 0:
                    sum_odd += digit
                else:
                    doubled = digit * 2
                    if doubled > 9:
                        sum_even += doubled - 9
                    else:
                        sum_even += doubled
            return (sum_even + sum_odd) % 10 == 0
        break
    return None


print(validate("4g"))
print(validate(""))
print(validate(4561261212345464))
print(validate(4561261212345467))
