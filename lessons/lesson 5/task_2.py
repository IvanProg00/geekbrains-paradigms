grades = {
    "Alice": [9, 8, 7, 9, 9],
    "Bob": [6, 7, 6, 5, 7],
    "Eve": [8, 9, 7, 8, 9],
    "Mike": [5, 6, 4, 3, 5],
}


def excellent_student(student):
    return sum(grades[student]) / len(grades[student]) > 8


def struggling_student(student):
    return sum(grades[student]) / len(grades[student]) < 5


students = ["Alice", "Bob", "Eve", "Mike"]

for student in students:
    if excellent_student(student):
        print(f"{student} - smart")
    elif struggling_student(student):
        print(f"{student} - needs in academic help")
    else:
        print(f"{student} - middle student")
