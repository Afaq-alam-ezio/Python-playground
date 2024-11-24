try:
    a = int(input("Enter the number = "))
    x = [3, 4, 5]
    print(f"The list element at index {a} is", x[a])
except IndexError:
    print("index error has happened")
finally:
    print("hii")
