top=0
stack = []
maxstack = int(input("Enter Maximum size of stack:"))
def push(x):
    global top
    if top < maxstack:
        stack.append(x)
        print("Stack after push operation:",stack)
        top = top + 1
    else:
        print("Stack Overflow")
def pop():
    global top
    if top == 0:
      print("Stack Underflow")
    else:
        stack.pop()
        print("Stack after pop operation:",stack)
        top = top - 1

    def display():
            global top, stack

            if top == 0:
                print("Stack Underflow")
            else:
                print("Stack elements are:")
                for i in stack:
                    print(i)
    print("Push 11 in stack:")
    push(11)
    print("Push 22 in stack:")
    push(22)
    print("Push 33 in stack:")
    push(33)
    print("Pop an element from stack:")
    pop()
    print("Push 33 in stack:")
    push(33)
    print("Push 44 in stack:")
    push(44)
    print("Push 55 in stack:")
    push(55)
    print("Push 66 in stack:")
    push(66)
    print("Display elements of stack:")
    display()