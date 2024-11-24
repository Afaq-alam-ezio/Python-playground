class Emp:
    def __init__(self, name, sal):
        self.name = name
        self.salary = sal

    def show(self):
        print(f"The name = {self.name} and salary = {self.salary}")

    @classmethod
    def fromstr(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))  # this is returned to constructor


e1 = Emp("harry", 20000)
e1.show()

string = "Afaq-10000"
e2 = Emp.fromstr(string)
e2.show()
