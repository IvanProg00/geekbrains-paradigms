class Parent:
    def speak(self):
        print("Hello from Parent")


class Child(Parent):
    def speak(self):
        print("Hello from Child")


parent = Parent()
child = Child()

parent.speak()
child.speak()
