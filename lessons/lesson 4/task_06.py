def apply_function(func, numbers):
    return [func(x) for x in numbers]


def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
print(apply_function(square, numbers))
