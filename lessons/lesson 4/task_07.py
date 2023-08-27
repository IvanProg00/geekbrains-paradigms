def custom_sort(numbers, comparison_func):
    return sorted(numbers, key=comparison_func)


def descending_order(x):
    return -x


numbers = [5, 2, 8, 1, 9, 3]
print(custom_sort(numbers, descending_order))
