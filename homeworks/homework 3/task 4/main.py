class Coffee:
    def cost(self):
        return 10


class Sugar:
    def __init__(self, item=None):
        self.item = item

    def cost(self):
        price = 0

        if self.item:
            price += self.item.cost()

        return price + 2


class Milk:
    def __init__(self, item=None):
        self.item = item

    def cost(self):
        price = 0

        if self.item:
            price += self.item.cost()

        return price + 3


coffee = Coffee()
print("coffee + sugar + milk =", Milk(Sugar(coffee)).cost())
print("coffee + milk =", Milk(coffee).cost())
print("coffee + sugar =", Sugar(coffee).cost())
