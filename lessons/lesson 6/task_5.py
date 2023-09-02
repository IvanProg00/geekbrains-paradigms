def find_num(data, num: int | float) -> bool:
    return num in data


print(find_num([5, 3, 2, 8, 4], 2))
print(find_num([5, 3, 2, 8, 4], 6))
