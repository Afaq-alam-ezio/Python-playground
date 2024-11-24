class Emp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):    # for rectangle
        return self.x * self.y


class Stu(Emp):
    def __init__(self, x):
        super().__init__(x, x)

    def area(self):     # for circle
        return 3.14 * super().area()  # self.r * self.r


e1 = Emp(10, 5)
print(e1.area())

e2 = Stu(5)
print(e2.area())
