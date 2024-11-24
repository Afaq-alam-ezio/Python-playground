x = False

# print(x = True)  This will give error
# print(x := True)  This will not give error

foods = []
while (food := input("Enter the food = ")) != "quit":
    foods.append(food)

for i in foods:
    print(i)
