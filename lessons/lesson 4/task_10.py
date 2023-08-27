def make_multiplier(factor):
    def multiplier(number):
        return number * factor

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))
