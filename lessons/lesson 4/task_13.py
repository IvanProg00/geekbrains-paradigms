from functools import reduce


def concat_reducer(acc, value):
    return acc + value


strs = ["Hello, ", "world", "!", " Welcome"]
result = reduce(concat_reducer, strs)
print(result)
