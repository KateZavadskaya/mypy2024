""" Task 1: oder """


def solution(array):

    """ Function show the possibility of increase in array:

    array - array where check should be

    """

    count_i = 0
    count_j = 0
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            count_i = count_i + 1
    for j in range(len(array) - 2):
        if array[j] >= array[j + 2]:
            count_j = count_j + 1
    return (count_i <= 1) and (count_j <= 1)


print(f"1 {solution([1, 3, 2])}")
print(f"2 {solution([1, 3, 2, 1])}")
print(f"3 {solution([1, 2, 1, 2])}")
print(f"4 {solution([1, 3, 2, 1])}")
print(f"5 {solution([1, 2, 3, 4, 5, 3, 5, 6])}")
print(f"6 {solution([40, 50, 60, 10, 20, 30])}")
