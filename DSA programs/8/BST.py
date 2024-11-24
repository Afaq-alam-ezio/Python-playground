class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traversal(root):
    if root:
        traversal(root.left)
        print(root.val, end=" ")
        traversal(root.right)

def search(root, x):
    if root is None:
        return False
    if root.val == x:
        return True
    if root.val < x:
        return search(root.right, x)
    return search(root.left, x)

root = Node(9)
root.left = Node(1)
root.right = Node(10)
root.left.left = Node(0)
root.left.right = Node(3)
root.left.right.right = Node(4)

print("The tree elements are: ")
traversal(root)

x = int(input("Enter element to search in binary search tree: "))
v = search(root, x)

if v:
    print("The element is present in the given BST.")
else:
    print("The element is not present in the given BST.")
