def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Bye")
    return mfx


# @greet
def add(x, y):
    print(f"Alen {x} {y}")


# you can use any two below to use decorator(greet)for 1st one write @greet above the func() and in 2nd just don't write
# add()
greet(add)("max", "payne")
