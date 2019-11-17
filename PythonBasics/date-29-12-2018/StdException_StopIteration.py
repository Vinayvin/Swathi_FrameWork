# z = [5, 9, 7]
# i = iter(z)
# print (i)
# print (next(i))
# print (next(i))
# print (next(i))
# print (next(i))


#above code throws topiterationas we aretrying to access more than the index of the list

try:
    l = [15, 25, 35]
    i = iter(l)
    print (next(i))
    print (next(i))
    print (next(i))
    print (next(i))
except Exception as e:
    print (type(e))