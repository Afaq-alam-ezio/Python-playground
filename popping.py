number = [1, 2, 3, 4, 5, 6]
odd = []
even = []
for i in number[-1:-len(number)-1:-1]:
    n = number.pop()
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

if len(number) == 0:
    print("Main number list is empty.")
else:
    for i in number:
        print(i, end=" ")

print("\nBelow is the Odd list :")
odd.sort()
print(odd)

print("\nBelow is the Even list : ")
even.sort()
print(even)
