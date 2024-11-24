# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

print("EACH ITEM WORTH IS ₹ 100\nNOTE :- A CART VALUE OF 1000 OR MORE WILL RESULT IN 10 % DISCOUNT ON TOTAL CART VALUE")
item = int(input("Enter total number of items purchased = "))
cart_value = item * 100
if cart_value >= 1000:
    print("HURRAY!!, YOU ARE ELIGIBLE FOR DISCOUNT !!")
    print('PRICE BEFORE = ₹', cart_value)
    print('PRICE NOW = ₹', int(cart_value-0.10*cart_value))
    print("VISIT US AGAIN!!!")
else:
    print("Total price = ₹", cart_value)