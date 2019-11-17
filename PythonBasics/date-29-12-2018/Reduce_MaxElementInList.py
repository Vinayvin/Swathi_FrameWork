import functools
def maxElementInList():
    l = [10, 50, 40, 89,300,23]
    num=functools.reduce(lambda a,b:a if a>b else b,l)
    print(num)

maxElementInList()
