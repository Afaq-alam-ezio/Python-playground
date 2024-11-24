# A student will not be allowed to sit in exam if his/her attendance is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
avg = int(0.75*365)
print("TOTAL NO. OF WORKING DAYS = 365, HENCE TO SIT FOR EXAM YOUR ATTENDANCE MUST BE 75% THAT IS =", avg)
attendance = int(input("Enter no. of days attended = "))
if attendance >= avg:
    print("Eligible for Exam")
else:
    print("Not eligible for exam")
