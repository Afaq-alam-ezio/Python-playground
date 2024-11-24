class Person:
    def __init__(self, a, n):
        self.age = a
        self.name = n

    def show(self):
        print(self.age, self.name)


class Student(Person):
    def __init__(self, a, n, rno, b):
        super().__init__(a, n)
        self.rollno = rno
        self.branch = b

    def show(self):
        super().show()
        print(self.rollno, self.branch)


s1 = Student(18, "Alan", 101, "CSE")
s1.show()
