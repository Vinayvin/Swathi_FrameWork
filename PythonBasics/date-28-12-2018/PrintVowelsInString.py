#method2
str="Welcome To Bangalore"
str1=str.lower()
vowel=['a','e','i','o','u']
print([x for x in str1 if x in vowel])


#method 1
[print(x,end=" ") for x in str.lower() if x in vowel]


#method2
def printvowel(c):
    return c.lower() in "aeiou"

L1=[x for x in filter(printvowel,str)]
print(L1)