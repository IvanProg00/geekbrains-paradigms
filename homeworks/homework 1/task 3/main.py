from functools import reduce


def calc_factorila(numbers):
    return reduce(lambda a, b: a * b, numbers)


numbers = [1, 2, 3, 4, 5]  # 120
print(calc_factorila(numbers))
