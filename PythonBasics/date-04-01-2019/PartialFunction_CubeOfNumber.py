from functools import partial

#function for multiplication
def find_power(a,b):
    return a**b

#finding cube of a number
print(find_power(2,3))
#finding square of a number
print(find_power(4,2))

#creating partial function to find cube of a number
cube_num=partial(find_power,b=3)
print(cube_num(3))

square=partial(find_power,b=2)
print(square(6))