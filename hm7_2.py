""" Task 2: *** """

STEPS = 10
VALUE_STAR = 1
SPACE = STEPS - VALUE_STAR
for i in range(STEPS):
    print(' ' * SPACE + '*' * VALUE_STAR)
    VALUE_STAR += 2
    SPACE -= 1
