import time


def forloop():
    for i in range(5000):
        i += 1
        print(i)


x = time.time()
forloop()
y = time.time() - x
print(f"Time taken to complete the above instruction is = {y}")

time.sleep(3)
# print(f"This statement is printed after 3 seconds")

d = time.localtime()
e = time.strftime("%d-%m-%y %H-%M-%S", d)
print(e)
