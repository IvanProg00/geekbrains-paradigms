from functools import reduce


def sum_reducer(acc, value):
    return acc + value


numbers = [1, 2, 3, 4, 5]
result = reduce(sum_reducer, numbers, 0)
print(result)
