from array import *
a = array("i",[])
print("Inserting array elements:")
for i in range(5):
    e = int(input("Enter element for array:"))
    a.append(e)
print("Traversing and Displaying array elements:")
for i in a:
    print(i)
