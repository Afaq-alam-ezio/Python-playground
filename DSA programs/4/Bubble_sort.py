from array import *
size = int(input("Enter size of array:"))
a = array("i",[])
print("Inserting array elements:")
for i in range(size):
    e = int(input("Enter element for array:"))
    a.append(e)
print("Array elements are:")
for i in a:
    print(i,end = " ")
print()
for i in range(0, size-1):
    for j in range(0, size-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Sorted Array:")
for i in a:
    print(i,end = " ")
print()