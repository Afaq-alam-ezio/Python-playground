# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

a = int(input("Enter you years of work experience = "))
if a >= 5:
    print("Wow,working for a long time\nTime to give you a surprise...\nFill current salary below")
    b = int(input("kindly enter current salary sir = "))
    c = 5/100*b
    print("Dear employee,hence you are working with us for a long time \nWe would like to give your salary a boost of 5 % that is now =", int(b + c))
    print("THANKS FOR WORKING WITH US!!!")
else:
    print("Work experience does\'nt fit the criteria of 5 years or more\nStill,Thanks for working with us!!")
