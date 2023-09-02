class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f"{self.name} - {self.price}$ ({self.count})"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        for prod in self.products:
            print(prod)

    def calculate(self):
        total = 0

        for prod in self.products:
            total += prod.count * prod.price

        return total


prod1 = Product("prod 1", 10, 5)
prod2 = Product("prod 2", 8, 4)

store = Store()

store.add_product(prod1)
store.add_product(prod2)

store.print_products()
print(store.calculate())
