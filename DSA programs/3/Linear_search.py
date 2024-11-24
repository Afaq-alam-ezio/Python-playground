from array import *
a = array("i",[])
print("Inserting array elements:")
for i in range(5):
    e = int(input("Enter element for array:"))
    a.append(e)
print("Array elements are:")
for i in a:
    print(i,end = " ")
print()
n = int(input("Enter number to search:"))
for i in a:
    if i == n:
        print("Number found in array.")
    break
else:
    print("Number not found.")