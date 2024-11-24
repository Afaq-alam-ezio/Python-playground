import random
# 1 = snake  2 = water 3 = gun
comp = random.randint(1, 3)
user = int(input("Welcome to snake water gun game\n1. Snake = 1\n2. Water = 2\n3. Gun   = 3\nChoose option = "))
print("computer chose =", comp)
if comp == user:
    print("match draw")
else:
    if comp == 1 and user == 2:
        print("Computer wins, you lose")
    else:
        if comp == 2 and user == 3:
            print("Computer wins, you lose")
        else:
            if comp == 2 and user == 1:
                print("you win, Computer lose")
            else:
                if comp == 3 and user == 1:
                    print("computer wins, you lose")
                else:
                    if comp == 1 and user == 3:
                        print("you win, computer lose")
if user > 3:
    print("invalid user input")
    