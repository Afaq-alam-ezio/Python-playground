class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name is {self.name}")
        print(f"Species is {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Bull")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"The breed is {self.breed}")


class Gold(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, "Pitbull")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"The color is {self.color}")


o = Gold("Modi", "Black")
o.show()
