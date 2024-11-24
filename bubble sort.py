x = [5, 6, 4, 3, 1, 0]
# Running n-1 ; n = no. of elements
for i in range(0, len(x)):
    for j in range(0, len(x)-1):
        # We need to select till 2nd last element and last will be accessed by using +1
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
print(x)
