def printOddNum():
    l = [1,2,3,4,5,6,7,8,9]
    f=filter(lambda l:l%2!=0,l)
    print(list(f))


printOddNum()
