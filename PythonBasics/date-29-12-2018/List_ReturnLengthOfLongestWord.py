#WAP to read a list of words and return the length of longest one
n=int(input("Enter the no.of words"))
words=[]
wordslength=[]
for i in range(n):
    w=input("Enter the word")
    words.append(w)
    wordslength.append(len(w))

print(words)
print("Length of longest word:",max(wordslength))
