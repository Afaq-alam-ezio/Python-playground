# a = "$"
# match a:
#     case 1:
#         print("not found")
#     case 0:
#         print("match found")
#     case _:
#         print("number not in a")
a = int(input("Enter a number between 1 to 5 = "))
match a:
    case 1:
            print("match found =", a)
    case 2:
            print("match found", a)
    case 3:
            print("match found", a)
    case 4:
            print("match found", a)
    case 5:
            print("match found", a)
    case _:
        print("number beyond limit")