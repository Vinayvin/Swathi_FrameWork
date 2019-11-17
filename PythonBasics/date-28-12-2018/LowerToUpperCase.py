str="manGO"
#L=[i.upper() for i in str ]
#print(L)

L1=[i.upper() if i.islower() else i for i in str]
print(L1)

str1=""
for i in str:
    if i.islower():
        str1+=i.upper()
    else:
        str1+=i
print(str1)


#L2=[j.upper() if j.islower() else j.lower() for j in str]
#print(L2)

