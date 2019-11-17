str1=input("Enter the first string:")
str2=input("Enter the Second string:")
commset=set(set(str1)&set(str2))
if len(commset)>0:
    print("Common letters present in two input strings")
print(commset)