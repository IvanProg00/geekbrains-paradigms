def create_multiplier(factor):
    def multiplier(x):
        return x * factor

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

result1 = double(5)
result2 = triple(5)

print(result1)
print(result2)
