str="PYTHON is Good"
count=0

for char in str:
    if (char.islower()):
        count=count+1
print("The Count of lowercase characters",count)