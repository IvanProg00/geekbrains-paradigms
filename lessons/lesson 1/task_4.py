def sum_square_imperative(numbers):
    result = 0

    for num in numbers:
        if num % 2 == 0:
            result += num**2

    return result


def sum_square_declarative(numbers):
    return sum([x**2 for x in numbers if x % 2 == 0])


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_square_imperative(numbers))
print(sum_square_declarative(numbers))
