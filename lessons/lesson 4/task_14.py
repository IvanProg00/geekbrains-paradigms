class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        if self.value is None:
            return self
        return func(self.value)


def safe_divide(x):
    if x == 0:
        return Maybe(None)
    return Maybe(10 / x)


result = Maybe(5).bind(safe_divide)
print(result.value)

result = Maybe(0).bind(safe_divide)
print(result.value)
