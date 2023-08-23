def sum_even_numbers(numbers):
    result = 0

    for num in numbers:
        if num % 2 == 0:
            result += num

    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_even_numbers(numbers))
