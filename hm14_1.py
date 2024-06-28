""" Task 1: students.txt """

try:
    with open("students.txt", "w", encoding="utf-8") as file_students:
        file_students.write("ст. Иванов ИИ, группа №1, оценки: 1, 2, 3, 4\n")
        file_students.write("ст. Петров ПП, группа №2, оценки: 5, 6, 7, 8\n")
    file_students.close()
except FileNotFoundError:
    print("Где файл, Лебовски?")

try:
    with open("students.txt", "r", encoding="utf-8") as file_students:
        for text in file_students:
            print(text, end="")
    file_students.close()
except FileNotFoundError:
    print("Где файл, Лебовски?")

with open("students.txt", "r", encoding="utf-8") as file_students:
    TOTAL_STUDENTS = 0
    GROUP_1 = 0
    GROUP_2 = 0
    for line in file_students:
        TOTAL_STUDENTS += 1
        if "группа №1" in line:
            GROUP_1 += 1
        elif "группа №2" in line:
            GROUP_2 += 1
    print(f"Итого студентов: {TOTAL_STUDENTS}, "
          f"Итого в группе 1: {GROUP_1} чел, "
          f"Итого в группе 2: {GROUP_2} чел")
file_students.close()

with open("students.txt", "r", encoding="utf-8") as file_students:
    for line in file_students:
        if "группа №1" in line:
            medium_1_str = line.split(":")[1].strip()
            medium_1 = [int(grade) for grade in medium_1_str.split(", ")]
            avagare_1 = sum(medium_1)/len(medium_1)
        elif "группа №2" in line:
            medium_2_str = line.split(":")[1].strip()
            medium_2 = [int(grade) for grade in medium_2_str.split(", ")]
            avagare_2 = sum(medium_2)/len(medium_2)
    print(f"Средний балл гр №1: {avagare_1},"
          f" Средний балл гр №2: {avagare_2}")
file_students.close()
