class BelowZeroException(Exception):
    pass
class GetInput():
    n=int(input("enter a number"))
    if n<0:
        raise BelowZeroException