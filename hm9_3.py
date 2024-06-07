""" Task 3: "cccbba" == "c3b2a" """


def count_chars(s):

    """ Function count letters and show result except 1 """

    count = 0
    result = ''
    first_char = s[0]
    for char in s:
        if first_char == char:
            count += 1
        else:
            if count > 1:
                result += f"{first_char}{count}"
            else:
                result += first_char
            first_char = char
            count = 1
    if count > 1:
        result += f"{first_char}{count}"
    else:
        result += first_char

    return result


assert count_chars("cccbba") == "c3b2a", "Incorrect count"
assert count_chars("abeehhhhhccced") == "abe2h5c3ed", "Incorrect count"
assert count_chars("aaabbceedd") == "a3b2ce2d2", "Incorrect count"
assert count_chars("abcde") == "abcde", "Incorrect count"
assert count_chars("aaabbdefffff") == "a3b2def5", "Incorrect count"
