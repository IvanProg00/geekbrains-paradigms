def sum_imperative(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def sum_declarative(n):
    return sum(range(1, n + 1))


n = 5

result = sum_imperative(n)
print(result)

result = sum_declarative(n)
print(result)
