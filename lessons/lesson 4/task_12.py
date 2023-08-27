from functools import reduce


def max_reducer(acc, value):
    return max(acc, value)


numbers = [1, 2, 3, 4, 5]
result = reduce(max_reducer, numbers, 0)
print(result)
