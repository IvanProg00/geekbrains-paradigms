class Circle:
    def print(self):
        print("Circle")


class Squre:
    def print(self):
        print("Squre")


class Rectangle:
    def print(self):
        print("Rectangle")


class ShapeFactory:
    def create_shape(self, name: str):
        if name == "circle":
            return Circle()
        elif name == "square":
            return Squre()
        elif name == "rectangle":
            return Rectangle()


shape_factory = ShapeFactory()
shape_factory.create_shape("circle").print()
shape_factory.create_shape("square").print()
shape_factory.create_shape("rectangle").print()
