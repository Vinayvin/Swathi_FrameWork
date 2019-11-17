f=open("file1.txt","r")
line_num=1
for line in f:
    if "the" in line:
        print(line_num)
    line_num += 1