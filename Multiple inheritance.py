class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class Dance:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class DancerEmp(Employee, Dance):  # from above, here comes 2 show() but Employee's show() will work as it is mentioned first
        def __init__(self, name, dance):
            self.name = name
            self.dance = dance


a = DancerEmp("Modi", "breakdance")
# Dance.show(a)
a.show()
print(DancerEmp.mro())  # will always search all functions like show() in itself, then Employee class and lastly Dance class because inheritance was in this order
