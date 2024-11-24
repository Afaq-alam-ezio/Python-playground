x = [1, 2, 3, 4, 5, 7, 9, 10]

n = int(input("Enter the number to search = "))
begin = 0
end = len(x)-1
while begin <= end:
    middle = (begin+end)//2
    if n == x[middle]:
        print(f"Number found at location {middle+1} and the index is {middle}")
        break
    elif n > x[middle]:
        begin = middle+1
    else:
        end = middle-1

if begin > end:
    print("Number not found in list")
