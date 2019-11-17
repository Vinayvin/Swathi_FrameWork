str="Python Scripting is easy "
w=str.split()
count=0
s=""
for i in w:
    s+=i.upper()+" "
    count+=1
    if count>1:
        break
for j in range(len(w)):
    if j >1:
        s+=w[j]+" "
print(s)
