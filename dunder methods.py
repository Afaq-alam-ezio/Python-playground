class Emp:
    name = "harry"

    def __len__(self):
        i = 0
        for x in self.name:
            i = i + 1
        return i


e1 = Emp()
print(len(e1))  # len method called using a dunder method
