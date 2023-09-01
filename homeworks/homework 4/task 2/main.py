def fibonacci(n, prev=0, cur=1):
    if n <= 0:
        return prev
    elif n < 2:
        return cur

    return fibonacci(n - 1, cur, prev + cur)


print(fibonacci(5))
