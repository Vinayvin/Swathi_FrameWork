from functools import partial

#function for multiplication
def multiply(a,b):
    return a*b


print(multiply(2,3))

#creating partial function
mul=partial(multiply,b=9)
print(mul(6))

