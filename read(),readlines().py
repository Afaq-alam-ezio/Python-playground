# f = open("data\hello.txt", 'r')
# while True:
#     line = f.readline()  # must always be inside loop
#     if not line:
#         break
#     print(line)
# f.close()

with open("data\hello.txt", 'w') as f:
    lines = [" hello", " girl"]
    f.writelines(lines)
    f.close()

f = open("data\hello.txt", 'r')
while True:
    line = f.readline()  # must always be inside loop
    if not line:
        break
    print(line)
f.close()
