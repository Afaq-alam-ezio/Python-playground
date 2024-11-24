# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
score = int(input("Enter your percentage = "))
if score >= 0 and score <= 100:
    if score < 25:
        print("Your grade is = F")
    elif score >= 25 and score <= 45:
        print("Your grade is = E")
    elif score > 45  and score < 50:
        print("Your grade is = D")
    elif score >= 50 and score < 60:
        print("Your grade is = C")
    elif score >= 60 and score < 80:
        print("Your grade is = B")
    elif score >= 80 and score <= 100:
        print("Your score is = A , Congrats !!!")
else:
    print("Wrong percentage entered!!")

