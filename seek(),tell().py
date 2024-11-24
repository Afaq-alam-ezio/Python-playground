# with open("data\hello.txt", 'r') as f:
#     f.seek(4)
#     print(f.tell())
#     data = f.read()
#     print(data)
#     # print(f.tell())


with open("data\hello.txt", 'w') as f:
    f.write("hii bro")
    f.truncate(5)

with open("data\hello.txt", 'r') as f:
    print(f.read())
    