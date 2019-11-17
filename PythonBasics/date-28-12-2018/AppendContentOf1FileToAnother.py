with open("file1.txt") as f:
    with open("output.txt", "w") as f1:
        for line in f:
            f1.write(line)