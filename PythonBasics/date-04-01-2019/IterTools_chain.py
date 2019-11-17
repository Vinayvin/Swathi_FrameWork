import itertools as iter


lst1 = ['a','c']
lst2 = ['b' ,'e' ,'f']

L = sorted([i for i in iter.chain(lst1, lst2)])
print(L)