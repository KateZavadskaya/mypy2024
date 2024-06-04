""" Task 1: clean # """


def line_with_symbol(line):

    """ Function cleans symbols '#' and the symbol before """

    new_line = line[:]
    a = list(new_line)
    volue = new_line.count("#")
    if volue == 0:
        return new_line
    while "#" in a:
        if a[0] == "#":
            del a[0]
            new_line = "".join(a)
        elif new_line.index("#") >= 0:
            del a[a.index("#") - 1:a.index("#") + 1]
            new_line = "".join(a)
    return "".join(a)


print(line_with_symbol("abc#d##c78#"))

assert line_with_symbol("a#bc#d") == "bd", "Function return wrong result"
assert line_with_symbol("abc#d##c") == "ac", "Function return wrong result"
assert line_with_symbol("abc##d######") == "", "Function return wrong result"
assert line_with_symbol("#######") == "", "Function return wrong result"
assert line_with_symbol("1q") == "1q", "Incorrect processing without '#'"
assert line_with_symbol("") == "", "Incorrect empty string processing"
