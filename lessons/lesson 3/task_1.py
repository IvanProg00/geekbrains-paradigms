class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} yers.old.")


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.greet()
person2.greet()
