area = lambda x: x*x
#  no need to use a return above like :- return x*x


def cube(fx, value):
    return 6 + fx(value)


print(area(5))
print(cube(area, 5))
