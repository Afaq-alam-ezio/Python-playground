def gen():
    for i in range(10):
        yield i


geni = gen()
# any print statement below will not give 0-4 but only one digit at time.That's why called a generator
print(next(geni))
print(next(geni))
print(next(geni))
for j in geni:  # this will print from 3 as 0, 1 and 2 are printed using above statements
    print(j)
            