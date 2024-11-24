# below are two solutions :
# ---------------------------------------
# 1st one below
try:
    sal = input("Enter the salary = ")
    if sal == "quit":
        print("error ignored")
    else:
        if int(sal) < 1000:
            raise ValueError("Low income inside try")
        else:
            print("Woow")
except:
    if sal != "quit":
        raise ValueError("error not ignored")

# -------------------------------------------------------
# 2nd one below:

a = input("Enter a number = ")
if a == "quit":
    print("error was about to occur")
else:
    try:
        if int(a) < 2000:
            raise ValueError("Not acceptable")
        else:
            print("Keep working")
    except ValueError:
        raise ValueError("Error not ignored")

    finally:
        pass
