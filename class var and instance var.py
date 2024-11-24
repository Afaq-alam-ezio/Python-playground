class Student:
    # below 2 are class variables
    company = "Halal food org"
    salary = 2000

    # below variables such as:- name and age are instance variables
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"The name is {self.name}\nThe age is {self.age}\n"
              f"The company is {self.company}\n"
              f"The salary is = {self.salary}")


# 2 methods below to call class member functions
x = Student("Harry", 20)
x.age = 32
# below are 2 ways to call show()
'''1.'''
# x.show()
'''2 .'''
Student.show(x)
# To entirely change the class variables use:- '''class_name.data_member = value'''
x.company = "google"
Student.company = "Helen"  # value "helen" will not be used for object X, as X instance variable already exists having a value for this object

Student.salary = 50000  # value 50000 will not be used for object Y, as Y instance variable below has a value 6500
y = Student("Gomez", 25)
y.salary = 6500
y.show()
