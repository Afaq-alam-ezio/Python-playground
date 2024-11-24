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
search = int(input("Enter number to search:"))
begin = 0
end = size-1
middle = (begin+end)//2
while(begin <= end):
    if a[middle] < search:
        begin = middle + 1
    elif a[middle] > search:
        end = middle - 1
    elif a[middle] == search:
        print("Number found in array")
        break
        middle = (begin + end) // 2
    else:
        print("Number not in array")