class Library:
    x = ["harry", "garry", "python", "c++"]
    y = len(x)

    def all_books(self):
        for i, j in enumerate(self.x):
            print(f"Book no. {i+1} is {j}")
        self.y = len(self.x)

    def add_book(self):
        book = input("Enter a book name = ")
        self.x.append(book)
        self.all_books()
        self.y = len(self.x)

    def avail_books(self):
        print("Number of books available =", self.y)


a = Library()
print("Below is book list")
a.all_books()
print("Lets add a book inside list below:")
a.add_book()
print("Below is number of books available:")
a.avail_books()
print("Hence Library is used, all books are deleted as you can see below:")
print("No. of books available =", a.x.clear())
