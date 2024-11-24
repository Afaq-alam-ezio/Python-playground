class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iatb(self, data):
        if self.head is None:
            x1 = Node(data)
            self.head = x1
        else:
            print("Linked List is not empty!")

    def iate(self, data):
        e1 = Node(data)
        if self.head is None:
            self.head = e1
        else:
            ptr = self.head
            while ptr.link is not None:
                ptr = ptr.link
            ptr.link = e1

    def iatp(self, p, data):
        if p < 1:
            print("Invalid position!")
            return
        p1 = Node(data)
        if p == 1:
            p1.link = self.head
            self.head = p1
        else:
            ptr = self.head
            for i in range(1, p - 1):
                if ptr is None:
                    print("Invalid position!")
                    return
                ptr = ptr.link
            p1.link = ptr.link
            ptr.link = p1

    def datb(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            self.head = self.head.link

    def date(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            prev = None
            ptr = self.head
            while ptr.link is not None:
                prev = ptr
                ptr = ptr.link
            if prev is not None:
                prev.link = None
            else:
                # If there is only one element in the list
                self.head = None

    def datp(self, p):
        if p < 1:
            print("Invalid position!")
            return
        if p == 1:
            self.head = self.head.link
        else:
            prev = self.head
            ptr = self.head.link
            for i in range(1, p - 1):
                if ptr is None:
                    print("Invalid position!")
                    return
                prev = prev.link
                ptr = ptr.link
            if ptr is not None:
                prev.link = ptr.link
            else:
                print("Invalid position!")

    def trv(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, end=" ")
                ptr = ptr.link
            print()

# Example usage
ll = LinkedList()
print("Insert element 10 at beginning:")
ll.iatb(10)
print("Linked List:")
ll.trv()
print("Insert element 20 at end:")
ll.iate(20)
print("Linked List:")
ll.trv()
print("Insert element 30 at end:")
ll.iate(30)
print("Linked List:")
ll.trv()
print("Insert element 25 at 3rd position:")
ll.iatp(3, 25)
print("Linked List:")
ll.trv()
print("Insert element 15 at 2nd position:")
ll.iatp(2, 15)
print("Linked List:")
ll.trv()
print("Delete element from beginning:")
ll.datb()
print("Linked List:")
ll.trv()
print("Delete element from end:")
ll.date()
print("Linked List:")
ll.trv()
print("Delete element from 2nd position:")
ll.datp(2)
print("Linked List:")
ll.trv()
