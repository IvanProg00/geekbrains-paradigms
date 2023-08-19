def fast_pow(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 1:
        return fast_pow(base, exponent - 1) * base
    else:
        half_pow = fast_pow(base, exponent // 2)
        return half_pow * half_pow


base = 2
exponent = 10
print(fast_pow(base, exponent))
