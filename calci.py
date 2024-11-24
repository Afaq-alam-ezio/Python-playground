from array import *
a = array("i", [10, 20, 30, 40, 50, 0, 0])
size = len(a)
item = 25
p = 2  # position to enter the element
n = 5  # total number of elements
i = n-1
while i >= p:
    a[i+1] = a[i]
a[p] = item
n = n+1
for i in a:
    print(i, end=" ")