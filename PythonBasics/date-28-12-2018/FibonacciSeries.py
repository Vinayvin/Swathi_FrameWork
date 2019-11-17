def fibo(n):
    f,s=0,1
    for i in range(n):
        print(f)
        res=f+s
        f=s
        s=res
fibo(10)
