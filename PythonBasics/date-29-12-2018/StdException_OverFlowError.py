# i=1
# f = 3.0**i
# for i in range(100):
#     print (i, f)
#     f = f ** 2

#Above code throws overflow error

try:
    i=1
    f=3.0**i
    for i in range(50):
        print(i)
        f=f**2
except Exception as e:
    print(type(e))