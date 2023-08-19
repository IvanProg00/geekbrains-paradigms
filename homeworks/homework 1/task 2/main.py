def find_min_number(numbers):
    if len(numbers) == 0:
        return None

    min_num = numbers[0]

    for num in numbers[1:]:
        if num < min_num:
            min_num = num

    return min_num


numbers = [5, 2, 4, 8, 3, 7]
print(find_min_number(numbers))
