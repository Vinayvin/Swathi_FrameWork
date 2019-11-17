str="Hi come to mysore hi dont forget to come to mysore"

#without using dictionary comprehension
d=dict()
words=str.split()
for s in words:
    c=str.count(s)
    d.setdefault(s,c)
print(d)

#using dictionary comprehension
d1={k:str.count(k) for k in str.split()}
print(d1)