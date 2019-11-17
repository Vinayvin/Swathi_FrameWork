import functools
def mulElements():
    lst = [1,3,5,2]
    op=functools.reduce(lambda a,b:a*b,lst)
    print(op)

mulElements()

