queue = []
maxq = int(input("Enter Maximum size of queue:"))
def enqueue(x):
    if len(queue) < maxq:
        queue.append(x)
        print("Queue after enqueue operation:",queue)
    else:
        print("Queue Overflow")
def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        queue.pop(0)
        print("Queue after dequeue operation:",queue)
def display():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Queue elements are:")
for i in queue:
    print(i)

print("Insert 10 in queue:")
enqueue(10)
print("Insert 20 in queue:")
enqueue(20)
print("Insert 30 in queue:")
enqueue(30)
print("Delete an element from queue:")
dequeue()
print("Insert 40 in queue:")
enqueue(40)
print("Insert 50 in queue:")
enqueue(50)
print("Insert 60 in queue:")
enqueue(60)
print("Insert 70 in queue:")
enqueue(70)
print("Display elements of queue:")
display()