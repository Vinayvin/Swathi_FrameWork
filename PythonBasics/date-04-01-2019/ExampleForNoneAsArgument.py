def func(l=None):
    print(l)

func()

def add(a,b,c=None,d=None):
    if c==None and d==None:
        print(a+b)
    elif d==None:
        print(a+b+c)
    else:
        print(a+b+c+d)

add(1,2)
add(1,2,3)
add(2,5,6,7)
