def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_func = counter()
print(counter_func())
print(counter_func())
print(counter_func())
print(counter_func())
