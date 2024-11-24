from array import *
a = array("i", [10, 20, 30, 40, 0])
p = int(input("Enter element position to remove = "))
new = int(input("Enter element to insert = "))
size = len(a)
i = size - 1
while i >= p:
    a[i] = a[i - 1]
    i = i - 1
a[p] = new
print("new array = ")
for i in a:
    print(i, end=" ")
