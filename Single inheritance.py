class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        print(f"Sound made by {self.name} and species is {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        # super().__init__(name, species="Dog") here in super() no need to give self but below self is mandatory
        Animal.__init__(self, name, species="dog")
        self.breed = breed

    def sound(self):
        print(f"Sound made by {self.name} is of species {self.species} and breed is {self.breed}")


a = Animal("Animal", "Animal")
a.sound()

d = Dog("Dog", "Modi")
d.sound()
