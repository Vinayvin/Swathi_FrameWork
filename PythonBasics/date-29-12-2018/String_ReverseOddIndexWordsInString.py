string="Python is an object oriented programming language"
words=string.split()
oddindex = []
for j in range(len(words)):
    if j%2 == 1:
        s=words[j]
        oddindex.append(s[::-1])
    else:
        oddindex.append(words[j])
print(oddindex)


