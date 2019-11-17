L=[10,20,30,40]
L1=['Apple','Bat','Cat']

d1={x:y for x,y in zip(map(int,L),map(str,L1))}
print(d1)