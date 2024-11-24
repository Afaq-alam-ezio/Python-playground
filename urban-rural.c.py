# Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
#
# if employee is a male and age is in between 20 to 40 then he may work in anywhere
#
# if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#
# And any other input of age should print "ERROR".

print("Good time sir, please enter below details :")
age = int(input("Please enter your age sir : "))
if 20 < age:
    sex = input("Please enter your gender sir (m = male / f = female): ")
    mstatus = input("Please tell marital status (y = Yes / n = No) : ")
    if 20 < age :
        match sex:
            case 'f':
                print("Your work is assigned in \'urban areas\' only")
            case 'm':
                if 20 < age < 40:
                    print("You can work any where either urban or rural")
            case 'm':
                if 40 < age < 60:
                    print("You can only work in urban areas")
            case _:
                print("sorry sir time to retire, you can't work now")
else:
    print("Incorrect age input sir.")
