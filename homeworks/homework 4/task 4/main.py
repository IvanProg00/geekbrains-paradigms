def sum(a):
    def clousure(b):
        return a + b

    return clousure


n1 = sum(10)
print(n1(70))
print(n1(50))

n2 = sum(5)
print(n2(8))
print(n2(9))
