import os
# x = os.mkdir("data")

# f = open("data\hello.txt", 'r')
# print(f.read())
# f.close()

# f = open("data\hello.txt", 'w')
# f.write("hii bro")
# f.close()

# f = open("data\hello.txt", 'r')
# print(f.read())
# f.close()

with open("data\hello.txt", 'r') as f:
    print(f.read())
