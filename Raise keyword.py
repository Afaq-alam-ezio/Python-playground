sal = int(input("Enter the salary = "))
if (sal < 1000):
    raise ValueError("Your salary is too low")
else:
    print("Good, keep earning")
