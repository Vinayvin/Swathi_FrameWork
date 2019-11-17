#WAP to generate random numbers from 1 to 20 and append them to a list
import random
randnum=[]
for i in range(6):
    randnum.append(random.randint(1,20))
print(randnum)