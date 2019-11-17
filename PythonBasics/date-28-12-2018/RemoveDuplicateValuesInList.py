#Method1
def removeDuplicates(MainList):
    newList=[]
    for i in MainList:
        if i not in newList:
            newList.append(i)
    return newList

print(removeDuplicates([2,3,5,2,6,8,1,4,3]))

#Method2
L=[1,2,2,3,1,5,8,10,3]
print((set(L)))


