def filter_even_imperative(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


def filter_even_declarative(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(filter_even_imperative(numbers))
print(filter_even_declarative(numbers))
