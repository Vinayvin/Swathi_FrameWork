with open("file2.txt", 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if i.isdigit():
                print(i)
            else:
                for letter in i:
                    if letter.isdigit():
                        print(letter,end=" ")




