class Emp:
    company = "Apple"

    def show(self):
        print(f"The name = {self.name} and company = {self.company}")

    @classmethod
    def change(cls, comp):  # any var_name can be used at cls
        cls.company = comp


x = Emp()
x.name = "Afaq"
Emp.show(x)
x.change("tesla")
x.show()
print(Emp.company)
