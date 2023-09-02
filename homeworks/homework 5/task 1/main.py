def get_primes(start, end):
    res = []
    for i in range(start, end + 1):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            res.append(i)

    return res


print(get_primes(2, 100))
