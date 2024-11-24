class Emp:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        # print("Method of parent class called")


class Sub(Emp):
    def __init__(self, name, roll, sec):
        super().__init__(name, roll)  # no need to pass self
        self.sec = sec

    def show(self):
        print(f"The name is {self.name}, roll is {self.roll} and section is {self.sec}")


e1 = Sub("Harry", 3, "A")
Sub.show(e1)
