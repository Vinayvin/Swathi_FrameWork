str1="hello Welcome to bangalore"
vowels=set("aeiouAEIOU")
count=0
for char in str1:
    if char in vowels:
        count+=1
print("Count of vowels",count)