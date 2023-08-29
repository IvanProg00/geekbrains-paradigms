from functools import reduce


def reduce_multiply1(initial, nums):
    for n in nums:
        initial *= n

    return initial


def reduce_multiply2(initial, nums):
    return reduce(lambda acc, x: acc * x, nums, initial)


print(reduce_multiply1(2, [3, 5, 4, 7]))
print(reduce_multiply2(2, [3, 5, 4, 7]))
