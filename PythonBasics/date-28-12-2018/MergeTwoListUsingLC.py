#merge two lists and sort the result list using list comprehension
import itertools
lst1=[1,2,5]
lst2=[1,3,4,7]


L=sorted([x for x in itertools.chain(lst1,lst2)])
print(L)






