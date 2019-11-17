#WAP to find the largest number in a list
Lst=[45,67,34,90,23,200,56]
print("Largest Number in a list:",max(Lst))

#method2
max=Lst[0]
for i in Lst:
   if i>max:
       max=i
print(max)