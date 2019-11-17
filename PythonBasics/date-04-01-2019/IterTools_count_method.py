import itertools as iter

#count() starts with default 0
counter = iter.count()
print(list(next(counter) for i in range(5)))

#count() with start arg to start with 1 and step argument to define the interval between numbers
#even numbers using itertools count()
even_num = iter.count(start=0,step=2)
print(list(next(even_num) for j in range(5)))

#odd numbers using itertools count()
odd_num = iter.count(start=1,step=2)
print(list(next(odd_num) for k in range(5)))

#count() with float
count_with_floats = iter.count(start=0.5, step=0.75)
print(list(next(count_with_floats) for _ in range(5)))