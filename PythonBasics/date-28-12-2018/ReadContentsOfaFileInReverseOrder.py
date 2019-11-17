from file_read_backwards import FileReadBackwards
with FileReadBackwards("file1.txt",encoding="utf-8") as f:
    for line in f :
        print(line)

