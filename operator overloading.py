class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i} i + {self.j} j + {self.k} k"

    def __add__(self, x):  # Overloading is done here
        # return f"{self.i + x.i} i + {self.j} j + {self.k} k"  # returns a string as its a f string
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)  # returns a Vector to the __str__()


e1 = Vector(3, 4, 5)
print(e1)

e2 = Vector(4, 5, 6)
print(e2)
print(e1 + e2)
print(type(e1 + e2))
