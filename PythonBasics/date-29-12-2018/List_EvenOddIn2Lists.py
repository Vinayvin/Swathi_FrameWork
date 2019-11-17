#WAP to put even and odd elements in a list into two different lists
Lst=[12,34,78,57,23,67]
even=[]
odd=[]
for i in Lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("Odd Numbers",odd)
