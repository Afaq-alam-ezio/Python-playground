from functools import reduce

# BELOW IS MAP
y = lambda a: a*a
n = [1, 2, 3, 4, 5]
x = list(map(y, n))
print(x)

# BELOW IS FILTER
def z(a):
    return a > 2


c = list(filter(z, n)) # always use filter when returning a boolean value
print(c)

# BELOW IS REDUCE
def red(a, b):
    return a + b


d = reduce(red, n)
print(d)  # output will be 15 as (1+2+3+4+5 = 15)
