father_of = {
    ("John", "Alice"),
    ("John", "Bob"),
    ("Michael", "John"),
    ("Michael", "Sara"),
}


def uncle(x, y):
    return any(
        (father, y) in father_of and (father, x) in father_of
        for father in father_of
        if (x, y) != father
    )


person_x = "Alice"
person_y = "Sara"

if uncle(person_x, person_y):
    print(f"{person_x}, is uncle of {person_y}")
else:
    print(f"{person_x}, is not uncle of {person_y}")
