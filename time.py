# WAP to greet with gm, ga, ge, gn as per time defined by user
time = int(input("Enter the selection \n1. 1 for 6-12\n2. 2 12 >= - 16\n3. 3 16 - 18\n4. 4 for over 18 \nenter = "))
# if 6 < time < 12:
#     print("Good morning")
# elif 12 <= time < 16:
#     print("Good afternoon")
# elif 16 < time < 18:
#     print("Good evening")
# else:
#     print("Good night")

match time:
    case 1:
        if 6 < time < 12:
            print("gm")
    case 2:
        if 12 <= time < 16:
            print("ga")
    case 3:
        if 16 < time < 18:
            print("ge")
    case _:
        print("gn")

