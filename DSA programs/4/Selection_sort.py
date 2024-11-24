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
for i in range(size):
    small = i
    for j in range(i,size):
        if a[small] > a[j]:
            small = j
        a[i], a[small] = a[small], a[i]
print("Sorted Array:")
for i in a:
    print(i,end = " ")